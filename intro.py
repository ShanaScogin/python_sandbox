# Author: Shana Scogin
# Date: 1/5/2021
# Acknowledgements: My patience

######## Notes ###########
# currently on scikit-learn==0.23
# for scikit, watch: https://github.com/scikit-learn/scikit-learn/issues/19063
# for debug, check into: https://atom.io/packages/python-debugger
# R vs python: https://www.dataquest.io/blog/python-vs-r/
##########################

## Implement simple print functions
print('hello')
print(10 + 60)

########## Running a simple regression
# from: https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9

## Import data
import statsmodels.api as sm
from sklearn import datasets as ds ## imports datasets from scikit-learn
data = ds.load_boston() ## loads Boston dataset from datasets library

## Load data as pandas
import numpy as np # I don't see this being used - where is this used
import pandas as pd
# define the data/predictors as the pre-set feature names
df = pd.DataFrame(data.data, columns=data.feature_names)
# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target, columns=["MEDV"]) # this means DV apparently
print(target) # checking to see if it prints

## Run the model without a constant
import statsmodels.api as sm
X = df["RM"]
y = target["MEDV"] # this just seems like an unnecessary step
cheese = sm.OLS(y, X).fit()
predictions = cheese.predict(X) # make the predictions by the model
print(X)

## Print out the stats
print(cheese.summary()) ## why is this not printing


## Print out df as test
print(df)
