# -*- coding: utf-8 -*-  

from math import log 

#计算给定数据集的香农熵 
def calcShannonEnt(dataSet):  
    numEntries = len(dataSet)  
    
    #为所有的分类创建字典
    labelCounts = {}  
    for featVec in dataSet:  
        currentLabel = featVec[-1]  
        if currentLabel not in labelCounts.keys():  
            labelCounts[currentLabel] = 0  
        labelCounts[currentLabel] += 1  
        
    #计算香农熵 
    shannonEnt = 0.0  
    for key in labelCounts:  
        prob = float(labelCounts[key]) / numEntries  
        shannonEnt -= prob * log(prob, 2)  
    return shannonEnt

#根据dataSet元素的第axis个特征是否等于value进行划分
def splitDataSet(dataSet, axis, value):  

    retDataSet = []    
    for featVec in dataSet:  
        if featVec[axis] == value:  
            reducedFeatVec = featVec[:axis]  
            reducedFeatVec.extend(featVec[axis+1:])  
            retDataSet.append(reducedFeatVec)  
    return retDataSet  

#根据信息增益进行数据划分
def chooseBestFeatureToSplit(dataSet):  
    #特征数量
    numberFeatures = len(dataSet[0])-1  
    #原始农香熵
    baseEntropy = calcShannonEnt(dataSet)  
    #信息增益
    bestInfoGain = 0.0;  
    
    bestFeature = -1;  
    for i in range(numberFeatures):  
        #所有样本的第i个特征列表
        featList = [example[i] for example in dataSet] 
        #所有样本的第i个特征Set，Set中元素不重复
        uniqueVals = set(featList)  
       
        newEntropy =0.0  
        for value in uniqueVals:  
            #根据dataSet元素的第i个特征是否等于value进行划分
            subDataSet = splitDataSet(dataSet, i, value)  
            prob = len(subDataSet)/float(len(dataSet))  
            newEntropy += prob * calcShannonEnt(subDataSet) 
        #计算第i个特征的信息增益 
        infoGain = baseEntropy - newEntropy  
        #找出第i个特征的信息增益最大
        if(infoGain > bestInfoGain):  
            bestInfoGain = infoGain  
            bestFeature = i  
    return bestFeature  

#创建样本数据集  
def createDataSet():  
    dataSet = [[0, 0, 'yes'], [0, 0, 'yes'], [1, 0, 'no'], [1, 0, 'no'], [1, 0, 'no']]  
    return dataSet  

data = createDataSet()

split = chooseBestFeatureToSplit(data)

print('split:',split)


