# BMW-3-market_analysis_and_price_prediction
Project for Data Science and Data Engineering postgraduate studies. 
Consist of:
* Data collection via web scrapping
* Data cleaning
* Data analysis and visualisation
* Price prediction using machine learning

The project was run on a anaconda enviroment using Python 3.10.1 and Jupyter Notebook.

## Data collection
Data has been collected from otomoto.pl - Poland's greatest web car marketplace. The data was gathered on 08.01.2024 using requests and BeautifulSoup libraries. 

Dataset consist of every offer from the time, resulting in 50 features for 3500+ offers. It has been stored in a csv format.

## Data cleaning
Each feature has been evaluated on its usability, correctness and  occurence of missing values and acted upon accordingly.

This means:
* dropping unuseful columns
* fixing incorrect data
* treating missing values
* preparing values for further analysis (removing units from numeric types etc.)
* aggregating classes with low exposure

## Data analysis and visualisation
Basic market analysis - checking relationships between diffrent variables (age to price, mileage to price etc), visualisation of distribution of values or classes for each column and many more

## Price prediction using machine learning
The most important part of the project - price prediction.

In this order, there have been trained models based on:
* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest Regression

For models evaluation there have been used metrics of R Squared and cross validation score.
All models have performed well with Linear, Ridge and Lasso regressors having score of 0.86 for training and 0.85 for test data splits. Random Forest Regressor has achieved even greater scores of 0.97 and 0.95 accordingly.

Feature importance based on Linear Regression model:
![Feature importance in Linear Regression for BMW 3 Series price prediciton](https://github.com/WaznyKamo/BMW-3-market_analysis_and_price_prediction/assets/34655004/618356ec-c349-4087-8dd1-984fdae5d261)

Feature importance based on Random Forrest Regression model:
![obraz_2024-01-28_213146040](https://github.com/WaznyKamo/BMW-3-market_analysis_and_price_prediction/assets/34655004/7cfacd47-6f9a-4917-9169-ffb758d8945f)
