# BMW-3-market_analysis_and_price_prediction
Considering buying a car, I wanted to know the market better. Especially how do diffrent factors impact the price. It is very important in order to pick a right offer - for car that is moderatly new, so it is cheaper, but the greatest price drop has already happened, so it will hold value better. Analyzing many factors can give us a great overview on the car market what is very interesting. Also building a regression model, trained on a great number of car offers can be very useful in order to fairly price the car for sale.
Consist of:
* Data collection via web scrapping
* Data cleaning
* Data analysis and visualisation
* Price prediction using machine learning

The project was run on a anaconda enviroment using Python 3.10.1 and Jupyter Notebook.

Key takeaways:
* There are more offers for cars marked as manufactured in Germany, than in Poland
* Amount of offers for cars aged over 20 years drop dirastically - this may be due to a car longevity
* Almost half of the offered cars have been in a accident
* There is very low variability in prices for cars aged between 15 and 30 years. This means that the condition, equipment and other variables might be not that important in these offers.
* Prices in newer cars (aged <6 years) vary dirastically
* There is a greater price drop with age than with mileage
* Mileage for offers in the first ~12 years has almost linear character, after it gets very hard to find relationship
* The greatest results for price prediction have been found for Random Forrest Regression model. Surprisingly it is based almost entirely on age
* Linear regression model takes into account many more features (is more balanced) but has a worse performance

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
![Feature importance in Linear Regression for BMW 3 Series price prediciton](https://github.com/WaznyKamo/BMW-3-market_analysis_and_price_prediction/assets/34655004/c9dfac65-eeec-4269-9a6c-66936e50c6f4)


Feature importance based on Random Forrest Regression model:
![obraz_2024-01-28_213146040](https://github.com/WaznyKamo/BMW-3-market_analysis_and_price_prediction/assets/34655004/7cfacd47-6f9a-4917-9169-ffb758d8945f)
