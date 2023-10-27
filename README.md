# Streamlit-ML-app

#Black Friday Sales Prediction Using Regression Models
#Introduction
Black Friday Sales Prediction is a problem of predicting the amount of money spent by customers during the Black Friday sales event. This problem can be tackled using regression techniques. In this case, the data was provided as a CSV file, which was loaded into a pandas DataFrame.
In this report, we have analyzed the Black Friday sales data and built regression models to predict the sales based on the given features. The dataset consists of 537,577 rows and 12 columns, including both numerical and categorical variables.

#Data Preprocessing
We started by checking for missing values and found that the Product_Category_2 and Product_Category_3 features have a lot of missing values. We filled these missing values with -3, as we can assume that the customer did not purchase any product in those categories. We also dropped the User_ID and Product_ID columns as they were not useful for modeling.

#Exploratory Data Analysis
Exploratory Data Analysis (EDA) is a critical step in any data analysis project. It is the process of exploring and understanding the data in order to gain insights, identify patterns, and uncover potential issues with the data.
In the Black Friday Sales Prediction project, the EDA phase involved analyzing and visualizing the data to understand the characteristics of the data and identify any trends or patterns that might be useful in predicting the purchase amounts of customers.

#Feature Engineering
Feature engineering involves creating new features from the existing features to improve the performance of the machine learning models. In this project, we created a new feature called "Total_Products" which represented the total number of products purchased by a customer.

#Outlier Analysis
Outliers are extreme values that can affect the performance of machine learning models. We used boxplots and scatterplots to identify any outliers in the data. We found a few outliers in the "Purchase" variable, which we removed from the dataset.

#Data Normalization
Normalization is the process of scaling the data so that all features have the same scale. We normalized the data using the Z-score normalization method, which scales each feature to have a mean of 0 and a standard deviation of 1. Overall, the EDA phase helped us to better understand the data, identify potential issues, and create new features that could improve the performance of the machine learning models.

#Modelling
Several regression models were trained and evaluated, including linear regression, decision tree regression, and random forest regression. The linear regression model had the highest RMSE, indicating that it was not a good fit for the data. The decision tree and random forest regression models had lower RMSEs, indicating that they were better fits for the data.
The best performing model was the random forest regression model on the testing data. This model was then used to make predictions on a sample dataset containing new data.
In conclusion, the Black Friday Sales Prediction problem can be tackled using regression techniques. In this case, a random forest regression model was found to be the best fit for the data. Some of the recommendations for future work include exploring other regression models, performing feature selection to reduce the dimensionality of the dataset, and using hyperparameter tuning to optimize the model's performance.
Additionally, it is recommended to further explore the relationships between features and purchase amount, as well as to possibly engineer new features to improve the model's performance. Furthermore, considering the relatively low correlation between product categories 2 and 3 and the purchase amount, it may be beneficial to exclude these features from the model to simplify it and potentially improve its performance.
Finally, it is important to note that the dataset used for this analysis may not be representative of the entire population and may have biases or limitations, which should be taken into account when interpreting the results and making decisions based on them.
