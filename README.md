# Marketing Analysis Prediction

Final Project for Purwadhika Data Scientist Course

This Repository includes Jupyter Notebooks and Dashboard. The dataset that used in this project could be found [here](https://www.kaggle.com/jackdaoud/marketing-data).

This dataset has 25 features, the features are:
1. **Marital** Customer's marital status.
2. **Kidhome** Number of small children in customer's household.
3. **Teenhome** Number of teenagers in customer's household.
4. **Education** Customer's level of education
5. **Income** Customer's yearly household income
6. **MntWines** Amount spent on wine products in last 2 years.
7. **MntFruits** Amount spent on fruit products in last 2 years.
8. **MntMeatProducts** Amount spent on meat products in last 2years.
9. **MntFishProducts** Amount spent on fish products in last 2 years.
10. **MntSweetProducts** Amount spent on sweet products in last 2 years.
11. **MntGoldProds** Amount spent on gold products in last 2 years.
12. **NumDealsPurchases** Number of purchases made with discount.
13. **NumCatalogPurchases** Number of purchases made using catalogue.
14. **NumStorePurchases** Number of purchases made directly in stores.
15. **NumWebPurchases** Number of purchases made through company's web site.
16. **NumWebVisitsMonth** Number of visits to company's website in the last month.
17. **Recency** number of days since the last purchase.
18. **AcceptedCmp1** 1 if costumer accepter the offer in the 1st campaign, 0 otherwise.
19. **AcceptedCmp2** 1 if costumer accepter the offer in the 2nd campaign, 0 otherwise.
20. **AcceptedCmp3** 1 if costumer accepter the offer in the 3rd campaign, 0 otherwise.
21. **AcceptedCmp4** 1 if costumer accepter the offer in the 4th campaign, 0 otherwise.
22. **AcceptedCmp5** 1 if costumer accepter the offer in the 5th campaign, 0 otherwise.
23. **Response** 1 if costumer accepter the offer in the last campaign, 0 otherwise.
24. **Complain** 1 if costumer complained in the last 2 years.
25. **DtCustomer** Date of customer's enrollment with the company.

This project has 2 predictions that are :
1. **Campaign Prediction** Predict customer would respond to last campaign or not.
2. **Customer Segment Prediction** Predict customer segment and show an advice what to do for that customer.

Steps that i took for this project are:
 - Exploratory data analysis
 - Preprocessing
 - Model selections
 - Segmentation
 - Deployment with flask

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
