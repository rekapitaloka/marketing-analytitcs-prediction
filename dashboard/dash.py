from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

data = pd.read_csv('data_marketing.csv')

#halaman home
@app.route('/')
def home():
    return render_template('home.html')

#halaman dataset
@app.route('/dataset', methods=['GET'])
def dataset():
    rows = list(data.values)
    header = list(data.columns)
    return render_template('dataset.html', rows=rows, header=header)

# #halaman visualisasi
@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

def predictSegment(r,f,m):
    newDataId = 9876
    RFM_Segmentation = pd.read_csv('rfm_data.csv')
    newData = pd.DataFrame([[newDataId, int(r), int(f), int(m)]],columns=['ID','Recency','Frequency','Monetary'])
    RFM_Segmentation = RFM_Segmentation.append(newData, ignore_index=True)

    #kolom cluster recency
    kmeans = KMeans(n_clusters=2, random_state=0)
    kmeans.fit(RFM_Segmentation[['Recency']])
    RFM_Segmentation['RecencyCluster'] = kmeans.labels_
    RFM_Segmentation['RecencyCluster']=np.where(RFM_Segmentation['RecencyCluster']==1,0,1)

    #kolom cluster freq
    kmeans.fit(RFM_Segmentation[['Frequency']])
    RFM_Segmentation['FrequencyCluster'] = kmeans.labels_
    RFM_Segmentation['FrequencyCluster']=np.where(RFM_Segmentation['FrequencyCluster']==1,0,1)

    #kolom cluter monetary
    kmeans = KMeans(n_clusters=10)
    kmeans.fit(RFM_Segmentation[['Monetary']])
    RFM_Segmentation['MonetaryCluster'] = kmeans.labels_

    #kolom Score
    RFM_Segmentation['RF_Score'] = RFM_Segmentation['RecencyCluster'] + RFM_Segmentation['FrequencyCluster']
    #penamaan Clustering berdasar unique nilai RFM
    def rfm_label(df):
        if df['RF_Score'] == 2:
            return 'Priority'
        elif ((df['RF_Score'] == 1)):
            return 'Loyal'
        else:
            return 'Need Attention'

    

    saran = {'Priority':'Berikan Reward Dan Info Terbaru Tentang Product', 'Need Attention': 'Jaga Dan Dengarkan Saran Mereka', 'Loyal': 'Berikan Discount!'}

    RFM_Segmentation['RFM_Label'] = RFM_Segmentation.apply(rfm_label, axis=1)

    result = RFM_Segmentation.loc[RFM_Segmentation['ID'] == newDataId]['RFM_Label'].tolist()[0]

    return {'hasil':result, 'saran': saran[result]}
    

# #halaman input prediksi cust
@app.route('/segment-predict', methods = ['GET'])
def segmentPredict():
    return render_template('segment_prediction.html')

# #halaman hasil prediksi
@app.route('/segment-result', methods = ['POST', 'GET'])
def segmentResult():
    if request.method == 'POST':
        input = request.form

        segmen = predictSegment(input['Recency'], input['Frequency'], input['Monetary'])

        return render_template('segment_result.html',
            data=input, pred=segmen['hasil'], saran=segmen['saran'])


# #halaman input prediksi camp
@app.route('/campaign-predict', methods = ['GET'])
def campaignPredict():
    return render_template('campaign_prediction.html')

@app.route('/campaign-result', methods = ['POST', 'GET'])
def campaignResult():
    if request.method == 'POST':
        input = request.form

        df_predict=pd.DataFrame({
            'Education':[input['Education']],
            'Marital_Status':[input['Marital_Status']],
            'Income':[input['Income']],
            'Kidhome':[input['Kidhome']],
            'Teenhome':[input['Teenhome']],
            'Recency':[input['Recency']],
            'Country':[input['Country']],
            'Customer_Age':[input['Customer_Age']],
        })

        prediksi = model.predict_proba(df_predict)[0][1]

        if prediksi > 0.5:
            quality = "Respond"
        else:
            quality = "Not Respond"

        return render_template('campaign_result.html',
            data=input, pred=quality)

if __name__ == '__main__':
    # model = joblib.load('model_joblib')

    filename = 'Model Final.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)