# Author: Shana Scogin
# Date: 1/5/2021
# Acknowledgements: My patience

######## Notes ###########
# currently on scikit-learn==0.23
# for scikit, watch: https://github.com/scikit-learn/scikit-learn/issues/19063
# for debug, check into: https://atom.io/packages/python-debugger
##########################

## Implement simple print functions
print('hello')
print(10 + 60)

########## Running a simple regression
# from: https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9

## importing data
import statsmodels.api as sm
from sklearn import datasets ## imports datasets from scikit-learn
data = datasets.load_boston() ## loads Boston dataset from datasets library

## Load data as pandas
import numpy as np
import pandas as pd
# define the data/predictors as the pre-set feature names
df = pd.DataFrame(data.data, columns=data.feature_names)
# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target, columns=["MEDV"])

## Run the model without a constant
import statsmodels.api as sm
X = df["RM"]
y = target["MEDV"]
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

## Print out the stats
model.summary() ## why is this not printing

## Print out df as test
print(df)
