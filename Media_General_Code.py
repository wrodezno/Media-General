# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:41:27 2016

@author: wrodezno
"""


import pandas as pd
import seaborn as sns
import scipy as sp
import MySQLdb

#%%
result_file = 'result_table.csv'

#%%

try:
    db=MySQLdb.connect(passwd="M4382vwr",user = "root",db="MediaGeneral")
    query = 'select * from conversion_table'
    data_raw = pd.read_sql(query,db)
    db.close() 
except Exception as e:    
    db.close() 
    print 'Data did not load'    
    



data = data_raw.copy()
col = ['Flag1','Flag2','Flag3']
conv_prob = {'Flag1':.10, 'Flag2':.20, 'Flag3':.30}

for c in col:
    data[c] = conv_prob[c]*data[c]
    

data['FraudulentRate'] = data.loc[:,('Flag1','Flag2','Flag3')].sum(axis=1)
data['ExpectedTrueConversions'] = (1 - data['FraudulentRate'])*data['Conversions']
data = data.sort_values(['ExpectedTrueConversions'],ascending = False)
data['score'] = 100*data['ExpectedTrueConversions']/data['ExpectedTrueConversions'].max()
data['score'] = data['score'].round(1)





data.loc[:,('Website_ID','score')].to_csv(result_file,index = False)


#%%

#data_raw = data_raw.loc[data_raw.Website_ID!=5004,:]
g = sns.FacetGrid(data_raw, col="Flag1",size = 5,ylim=(0,7),xlim = (-.5,45))
g.map(sns.distplot, "Conversions",rug = True,bins = range(0,50,5),kde = False,rug_kws={"color": "r"})



test_stat_ks = sp.stats.ks_2samp(data_raw.loc[data_raw.Flag1==0,'Clicks'].values, data_raw.loc[data_raw.Flag1==1,'Clicks'].values)
listTestGroups = [data_raw.loc[data_raw.Flag1==0,'Clicks'].values, data_raw.loc[data_raw.Flag1==1,'Clicks'].values]
test_stat_ads = sp.stats.anderson_ksamp(listTestGroups)
sp.stats.ranksums(data_raw.loc[data_raw.Flag1==0,'Clicks'].values, data_raw.loc[data_raw.Flag1==1,'Clicks'].values)



















