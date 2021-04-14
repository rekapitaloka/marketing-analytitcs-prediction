# Marketing Analysis Prediction

Final Project for Purwadhika Data Scientist Course

This Repository includes Jupyter Notebooks and Dashboard. The dataset that used in this project could be found [here](https://www.kaggle.com/jackdaoud/marketing-data).


This dataset has 11 features, the features are:
1. **Marital Status** : Customer's marital status. there are 3 choises (Single, Together and Other)
2. **Education** : Customer's education level from basic until Phd
3. **Total Income** : Customer's yearly household income.
4. **Number of Kidhome** : Number of children in customer's household
5. **Number of Teenhome** : Number of Teenager in customer's household
6. **Recency** : Number of days since customer's last purchase (-1 if customer never purchase before)
7. **Customer Age** : Number of Age Customer
8. **Country** : Customer location
9. **Recency** : Time since last order  
10. **Frequency** : Total number of Customer transactions
11. **Monetary** : Total transactions value

This project has 2 predictions that are :
1. **Campaign Prediction** Predict customer would respond to Campaign or not. (for New Customer)
2. **Customer Segment Prediction** Predict customer segment and show an advice what to do for that customer.(For Old Membership)

Steps that i took for this project are:
 - Exploratory data analysis
 - Preprocessing
 - Model selections
 - Segmentation
 - Deployment with flask

## Model Selection
Analysis:
In this modelling i use precisionn score for model evaluation. Because i wanna avoid False Positive (FP).
For Modelling I try Logistic Regression, KNN, Decision Tree, Boosting and Balancing Datase. Based on Model evaluation (precision score) the best model is Logistic Regression without balancing so i choose it. 

## Notebook
This project has 3 notebooks those are:
1. Exploratory Data Analysis for this dataset
2. Modeling for campaign prediction
3. Segmentation for customer segment prediction

## Dashboard
Dashboard are made using flask, it consist of 7 pages:
1. Home
![Home Page](/assets/home.png "Home Page")
2. Dataset
![Dataset](/assets/dataset.png "Dataset")
3. Visualization
![Visualization](/assets/visualization.png "Visualization")
4. Campaign Prediction
![Campaign Prediction](/assets/campaign_predict.png "Campaign Prediction")
5. Campaign Prediction Result
![Campaign Prediction Result](/assets/campaign_predict_result.png "Campaign Prediction Result")
6. Customer Segment Prediction
![Customer Segment Prediction](/assets/cust_seg_predict.png "Customer Segment Prediction")
7. Customer Segment Prediction Result
![Customer Segment Prediction Result](/assets/cust_seg_predict_result.png "Customer Segment Prediction Result")
