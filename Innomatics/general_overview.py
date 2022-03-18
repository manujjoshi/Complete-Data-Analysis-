#!/usr/bin/env python
# coding: utf-8

# In[1]:

def summary_report_general(data):   
    import numpy as np
    import pandas as pd
    summary = pd.DataFrame(data.dtypes,columns = ['data_type'])
    summary = summary.reset_index()
    summary = summary.rename(columns={'index':'column_name'})
    ## Identifying the missing values
    summary['missing'] = data.isnull().sum().values
    summary['missing%'] = (data.isnull().sum()/len(data)*100).values
    summary['uniques'] = data.nunique().values
    summary['unique%'] = (data.nunique()/len(data)*100).values
    summary['count'] = (data.count()).values
    return summary