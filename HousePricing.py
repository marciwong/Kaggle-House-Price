#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:49:30 2017

@author: marcowong
"""
from sklearn.linear_model import ElasticNet
import pandas as pd
import numpy as np
import csv
from sklearn import preprocessing
from sklearn import cross_validation

data = pd.read_csv('/Users/marcowong/Desktop/train.csv')
test = pd.read_csv('/Users/marcowong/Desktop/test.csv')
new = [data,test]
new = pd.concat(new)

numberOfVar = len(new.columns)
isNullArray = new.notnull().sum()

newDF = pd.DataFrame()

for i in range(0,numberOfVar):
    if isNullArray[i] == 2919:
        pass
    else:
        newDF = pd.concat([newDF,new.iloc[:,i]],axis = 1)
        
PoolQC = []
PoolArea = []
for i in range(0,len(new)): 
    PoolArea.append(new['PoolArea'].iloc[i])
    PoolQC.append(new['PoolQC'].iloc[i])
          
PoolQCSum = new['PoolQC'].value_counts()
new['PoolArea'].iloc[2420] = 'Ex'
new['PoolArea'].iloc[2503] = 'Ex'
new['PoolArea'].iloc[2599] = 'Fa'

for i in range(0, len(new)):
    if PoolArea[i] > 0:
        pass
    else:
        new['PoolArea'].iloc[i] = 0
        print(i)
    if type(new['PoolQC'].iloc[i]) != str:
        new['PoolQC'].iloc[i] = 'None'

for i in range(0,len(new)):
    if type(PoolQC[i]) != str:
        new['PoolArea'].iloc[i] == 'None'
    if new['GarageYrBlt'].iloc[i] != float:
        new['GarageYrBlt'].iloc[i] == new['YearBuilt']
        
garage = pd.DataFrame()
garage = new['GarageArea']
garage = pd.concat([garage,new['GarageCars']],axis = 1)
garage = pd.concat([garage,new['GarageQual']],axis = 1)
garage = pd.concat([garage,new['GarageFinish']],axis = 1)
garage = pd.concat([garage,new['GarageCond']],axis = 1)
garage = pd.concat([garage,new['GarageType']],axis = 1)

new['GarageQual'].iloc[2126] = 'TA'
new['GarageFinish'].iloc[2126] = 'Unf'
new['GarageCond'].iloc[2126] = 'TA'

new['KitchenQual'].iloc[1555] = 'TA'
new['Electrical'].iloc[1379] = 'SBrkr'

Bsmt = new['BsmtQual']
Bsmt = pd.concat([Bsmt,new['BsmtCond']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtExposure']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtFinType1']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtFinSF1']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtFinType2']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtFinSF2']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtUnfSF']],axis = 1)
Bsmt = pd.concat([Bsmt,new['TotalBsmtSF']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtFullBath']],axis = 1)
Bsmt = pd.concat([Bsmt,new['BsmtHalfBath']],axis = 1)

new['BsmtExposure'].iloc[948] = 'No'
new['BsmtExposure'].iloc[1487] = 'No'
new['BsmtExposure'].iloc[2348] = 'No'

for i in range(0,len(new)):
    if type(new['Exterior1st'].iloc[i]) == str:
        pass
    else:
        print(i)
    if type(new['Exterior2nd'].iloc[i]) == str:
        pass
    else:
        print(i)

for i in range(0,len(new)):       
    if type(Bsmt.iloc[i,0]) == str:
        pass
    else:
        new['BsmtQual'].iloc[i] == 'Other'
    if type(Bsmt.iloc[i,1]) == str:
        pass
    else:
        new['BsmtCond'].iloc[i] == 'Other'
    if type(Bsmt.iloc[i,2]) == str:
        pass
    else:
        new['BsmtExposure'].iloc[i] == 'Other'
    if type(Bsmt.iloc[i,3]) == str:
        pass
    else:
        new['BsmtFinType1'].iloc[i] == 'Other'
    if Bsmt.iloc[i,4] > 0:
        pass
    else:
        new['BsmtFinSF1'].iloc[i] == 0
    if type(Bsmt.iloc[i,5]) == str:
        pass
    else:
        new['BsmtFinType2'].iloc[i] == 0
    if Bsmt.iloc[i,6] > 0:
        pass
    else:
        new['BsmtFinSF2'].iloc[i] == 0
    if Bsmt.iloc[i,7] > 0:
        pass
    else:
        new['BsmtUnfSF'].iloc[i] == 0
    if Bsmt.iloc[i,8] > 0:
        pass
    else:
        new['TotalBsmtSF'].iloc[i] == 0
    if Bsmt.iloc[i,9] > 0:
        pass
    else:
        new['BsmtFullBath'].iloc[i] == 0
    if Bsmt.iloc[i,10] > 0:
        pass
    else:
        new['BsmtHalfBath'].iloc[i] == 0
    
new['Exterior1st'].iloc[2151] = 'Other'
new['Exterior2nd'].iloc[2151] = 'Other'

for i in range(0,len(new)):
    if np.isnan(new['LotFrontage'].iloc[i]) == True:
        new['LotFrontage'].iloc[i] = 69


for i in range(0,len(new)):
    if type(new['Alley'].iloc[i]) == float:
        new['Alley'].iloc[i] = 'Other'
    if type(new['Fence'].iloc[i]) == float:
        new['Fence'].iloc[i] = 'Other'
    if type(new['FireplaceQu'].iloc[i]) == float:
        new['FireplaceQu'].iloc[i] = 'Other'
    if type(new['MiscFeature'].iloc[i]) == float:
        new['MiscFeature'].iloc[i] = 'Other'
    if new['YearBuilt'].iloc[i] != new['GarageYrBlt'].iloc[i]:
        new['GarageYrBlt'] = new['YearBuilt'].iloc[i]
    if type(new['GarageCond'].iloc[i]) == float:
        new['GarageCond'].iloc[i] = 'TA'
    if type(new['GarageQual'].iloc[i]) == float:
        new['GarageQual'].iloc[i] = 'TA'
    if type(new['GarageFinish'].iloc[i]) == float:
        new['GarageFinish'].iloc[i] = 'Unf'
    if type(new['GarageType'].iloc[i]) == float:
        new['GarageType'].iloc[i] = 'Detchd' 

meanMasVnrArea = np.mean(new['MasVnrArea'])
for i in range(0,len(new)):
        if np.isnan(new['MasVnrArea'].iloc[i]) == True:
            new['MasVnrArea'].iloc[i] = meanMasVnrArea
            
new.iloc[2120,4] = 0
new.iloc[2120,5] = 0
new.iloc[2120,6] = 0
new.iloc[2120,7] = 0
new.iloc[2120,8] = 0
new.iloc[2120,31] = np.mean(new['TotalBsmtSF'])
new.iloc[2188,6] = 0
new.iloc[2188,7] = 0
new.iloc[2576,12] = 0
new.iloc[2576,13] = 0

new = new.drop('SalePrice',axis =1 )
new = pd.get_dummies(new)

data = pd.read_csv('/Users/marcowong/Desktop/train.csv')
test = pd.read_csv('/Users/marcowong/Desktop/test.csv')

train = new.iloc[0:1460,:]
testX = new.iloc[1460:,:]

YTrain = data['SalePrice']
XTrain = train
XTrain = XTrain.loc[:, XTrain.columns != 'Id']
XTest = testX.iloc[:, testX.columns !='Id']
Id = test['Id']

XTest.iloc[660,5] = 0
XTest.iloc[660,6] = 0
XTest.iloc[660,7] = 0
XTest.iloc[660,8] = 0
XTest.iloc[660,30] = 0
XTest.iloc[728,6] = 0
XTest.iloc[728,7] = 0
XTest.iloc[1116,12] = 0
XTest.iloc[1116,13] = 0

XTest = preprocessing.scale(XTest)
XTrain = preprocessing.scale(XTrain)

enet = ElasticNet(alpha = 0.5, l1_ratio = 0.7)
yPredictEnet = enet.fit(XTrain, YTrain).predict(XTest)

for i in range(0,len(yPredictEnet)):
    yPredictEnet[i] = abs(yPredictEnet[i]) 
    

with open('Answer.csv', 'w')  as csvfile:
    fieldnames = ['Id','SalePrice']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    
    for i in range(0,len(yPredictEnet)):
        writer.writerow({'Id' : Id[i],'SalePrice' : yPredictEnet[i]})

