#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np


# In[32]:


import pandas as pd


# In[33]:


stageAndstatus = pd.read_excel("Predictive Score Doc\Xlsx\stage&status.xlsx")


# In[34]:


QName = pd.read_excel("Predictive Score Doc\Xlsx\QName.xlsx")


# In[35]:


PGName = pd.read_excel("Predictive Score Doc\Xlsx\PGName.xlsx")


# In[36]:


PGSpec = pd.read_excel("Predictive Score Doc\Xlsx\PGSpec.xlsx")


# In[37]:


PGIns = pd.read_excel("Predictive Score Doc\Xlsx\PGIns.xlsx")


# In[38]:


PreviousEmp = pd.read_excel("Predictive Score Doc\Xlsx\PreviousEmp.xlsx")


# In[39]:


PreviousDesignation = pd.read_excel("Predictive Score Doc\Xlsx\PreviousDesignation.xlsx")


# In[40]:


Industry = pd.read_excel("Predictive Score Doc\Xlsx\Industry.xlsx")


# In[41]:


FunctionArea = pd.read_excel("Predictive Score Doc\Xlsx\FunctionArea.xlsx")


# In[42]:


IndentRequirment = pd.read_excel("Predictive Score Doc\Xlsx\IndentRequirment.xlsx")


# In[43]:


SourceName = pd.read_excel("Predictive Score Doc\Xlsx\SourceName.xlsx")


# In[65]:


Low_pop = pd.read_csv("Predictive Score Doc\Low_Pop\cat_map_tab_BM_DBM_model.csv")


# In[175]:


sample_data = pd.read_excel("Sample.xlsx")
allCandidate = []


# In[176]:


firstCandidate = sample_data.iloc[0]


# In[177]:


firstCandidate


# In[202]:


Qualification = QName[QName['QName1'] == firstCandidate.QName1]['QName1_Class'].item().encode("utf-8")
PostGraduateName = PGName[PGName['PGName2'] == firstCandidate.PGName]['PGName2_Class'].item().encode("utf-8")
PostSpec = PGSpec[PGSpec['PGSpec'] == firstCandidate.PGSpecification]['PGSpec_Class'].item().encode("utf-8")
University = PGIns[PGIns['PGIns2 / PGUni2'] == firstCandidate.PGIns]['PGIns_Class'].item().encode("utf-8")
PreiviousEmpDetail = PreviousEmp[PreviousEmp['Previous Employer'] == firstCandidate.PreviousEmployer]['Prev_Empl_Class'].item().encode("utf-8")
Designation = PreviousDesignation[PreviousDesignation['Previous Designation'] == firstCandidate.PreviousDesignation]['Prev_Desig_Class'].item().encode("utf-8")  
IndustryDetail = Industry[Industry['Industry'] == firstCandidate.Industry]['Industry_Class'].item().encode("utf-8")
functionA = FunctionArea[FunctionArea['Functional_Area'] ==  firstCandidate.FunctionalArea]['Function_Class'].item().encode("utf-8")
SourceNa = SourceName[SourceName['Source TAG'] == firstCandidate.SourceName]['Source Name'].item().encode("utf-8")
Requirement = IndentRequirment[IndentRequirment['Indent Title'] == firstCandidate.IndentTitle]['Title_Class'].item().encode("utf-8")


# In[207]:


sample_data.last_valid_index()


# In[211]:


for i in range(0,sample_data.last_valid_index()):
    rid = {}
    rid['RID'] = sample_data.iloc[i].RID
    firstCandidate = 


# In[ ]:




