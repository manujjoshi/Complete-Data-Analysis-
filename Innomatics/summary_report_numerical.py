#!/usr/bin/env python
# coding: utf-8

# In[1]:


def summary_report_num(data):   
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
    summary['mean'] = data.mean().values
    summary['std'] = data.std().values
    summary['min on boxplot'] = np.percentile(data,25,axis=0) - (np.percentile(data,75,axis=0) - np.percentile(data,25,axis=0))
    summary['q1'] = np.percentile(data,25,axis=0)
    summary['q2'] = np.percentile(data,50,axis=0)
    summary['q3'] = np.percentile(data,75,axis=0)
    summary['max on boxplot'] = np.percentile(data,75,axis=0) + (np.percentile(data,75,axis=0) - np.percentile(data,25,axis=0))
    summary['skewness'] = data.skew().values
    summary['kurtosis'] = data.kurt().values
    return summary

# In[ ]:




