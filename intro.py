# Author: Shana Scogin
# Date: 1/5/2021
# Acknowledgements: My patience

######## Notes ###########
# currently on scikit-learn==0.23
# for scikit, watch: https://github.com/scikit-learn/scikit-learn/issues/19063
# for debug, check into: https://atom.io/packages/python-debugger
# R vs python: https://www.dataquest.io/blog/python-vs-r/
##########################

########## Running a simple regression #######
# from: https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9

## Import data
import statsmodels.api as sm
from sklearn import datasets as ds ## imports datasets from scikit-learn
data = ds.load_boston() ## loads Boston dataset from datasets library

## Load data as pandas
import pandas as pd
# define the data/predictors as the pre-set feature names
df = pd.DataFrame(data.data, columns=data.feature_names)
# Put the target (housing value -- MEDV) in another DataFrame
gouda = pd.DataFrame(data.target, columns=["MEDV"]) # this means DV apparently

## Run the model without a constant
import statsmodels.api as sm
X = df["RM"] # having the separate X and y does seem to help readability
y = gouda["MEDV"]
model_ = sm.OLS(y, X).fit()
predictions = model_.predict(X) # make the predictions by the model

## Print out the stats
print(model_.summary())
print(predictions)
