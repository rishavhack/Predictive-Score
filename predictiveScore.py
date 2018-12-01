# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:29:31 2018

@author: Hirecraft
"""


    
    
def result():
    import numpy as np
    import pandas as pd
    import math
    stageAndstatus = pd.read_excel("Predictive Score Doc/Xlsx/stage&status.xlsx")
    QName = pd.read_excel("Predictive Score Doc/Xlsx/QName.xlsx")
    PGName = pd.read_excel("Predictive Score Doc/Xlsx/PGName.xlsx")
    PGSpec = pd.read_excel("Predictive Score Doc/Xlsx/PGSpec.xlsx")
    PGIns = pd.read_excel("Predictive Score Doc/Xlsx/PGIns.xlsx")
    PreviousEmp = pd.read_excel("Predictive Score Doc/Xlsx/PreviousEmp.xlsx")
    PreviousDesignation = pd.read_excel("Predictive Score Doc/Xlsx/PreviousDesignation.xlsx")
    Industry = pd.read_excel("Predictive Score Doc/Xlsx/Industry.xlsx")
    FunctionArea = pd.read_excel("Predictive Score Doc/Xlsx/FunctionArea.xlsx")
    IndentRequirment = pd.read_excel("Predictive Score Doc/Xlsx/IndentRequirment.xlsx")
    SourceName = pd.read_excel("Predictive Score Doc/Xlsx/SourceName.xlsx")
    Low_pop = pd.read_csv("Predictive Score Doc/Low_Pop/cat_map_tab_BM_DBM_model.csv")
    BM = pd.read_excel("Predictive Score Doc/pred_Score/BM.xlsx")
    DBM = pd.read_excel("Predictive Score Doc/pred_Score/DBM.xlsx")
    sample_data = pd.read_excel("sample - Copy.xlsx")
    allCandidate = []
    sample_data = sample_data.replace(np.nan, '', regex=True)
    
    for i in range(0,sample_data.last_valid_index()):
        rid = {};
        rid['RID'] = sample_data.iloc[i].RID
        rid['QName1_Class'] = QName[QName['QName1'].str.strip() == sample_data.iloc[i].QName1.strip()]['QName1_Class'].item().encode("utf-8") if len(QName[QName['QName1'].str.strip() == sample_data.iloc[i].QName1.strip()]['QName1_Class']) > 0 else "NO_INFO"
        rid['PGName2_Class'] = PGName[PGName['PGName2'].str.strip() == sample_data.iloc[i].PGName.strip()]['PGName2_Class'].item().encode("utf-8") if len(PGName[PGName['PGName2'].str.strip() == sample_data.iloc[i].PGName.strip()]['PGName2_Class']) > 0 else "NO_INFO"
        rid['PGSpec_Class'] = PGSpec[PGSpec['PGSpec'].str.strip() == sample_data.iloc[i].PGSpecification.strip()]['PGSpec_Class'].item().encode("utf-8") if len(PGSpec[PGSpec['PGSpec'].str.strip() == sample_data.iloc[i].PGSpecification.strip()]['PGSpec_Class']) > 0 else "NO_INFO"
        rid['PGIns_Class'] = PGIns[PGIns['PGIns2 / PGUni2'].str.strip() == sample_data.iloc[i].PGIns.strip()]['PGIns_Class'].item().encode("utf-8") if len(PGIns[PGIns['PGIns2 / PGUni2'].str.strip() == sample_data.iloc[i].PGIns.strip()]['PGIns_Class']) > 0  else "NO_INFO"
        rid['Prev_Empl_Class'] = PreviousEmp[PreviousEmp['Previous Employer'].str.strip() == sample_data.iloc[i].PreviousEmployer.strip()]['Prev_Empl_Class'].item().encode("utf-8") if len(PreviousEmp[PreviousEmp['Previous Employer'].str.strip() == sample_data.iloc[i].PreviousEmployer.strip()]['Prev_Empl_Class']) > 0  else "NO_INFO"
        rid['Prev_Desig_Class'] = PreviousDesignation[PreviousDesignation['Previous Designation'].str.strip() == sample_data.iloc[i].PreviousDesignation.strip()]['Prev_Desig_Class'].item().encode("utf-8") if len(PreviousDesignation[PreviousDesignation['Previous Designation'].str.strip() == sample_data.iloc[i].PreviousDesignation.strip()]['Prev_Desig_Class']) > 0 else "NO_INFO"
        rid['Industry_Class'] = Industry[Industry['Industry'].str.strip() == sample_data.iloc[i].Industry.strip()]['Industry_Class'].item().encode("utf-8") if len(Industry[Industry['Industry'].str.strip() == sample_data.iloc[i].Industry.strip()]['Industry_Class']) > 0 else "NO_INFO"
        rid['Function_Class'] = FunctionArea[FunctionArea['Functional_Area'].str.strip() ==  sample_data.iloc[i].FunctionalArea.strip()]['Function_Class'].item().encode("utf-8") if len(FunctionArea[FunctionArea['Functional_Area'].str.strip() ==  sample_data.iloc[i].FunctionalArea.strip()]['Function_Class']) > 0 else "UNKNOWN"
        rid['Source_Name'] = SourceName[SourceName['Source TAG'].str.strip() == sample_data.iloc[i].SourceName.strip()]['Source Name'].item().encode("utf-8") if  len(SourceName[SourceName['Source TAG'].str.strip() == sample_data.iloc[i].SourceName.strip()]['Source Name']) > 0 else "UNKNOWN"
        rid['Title_Class'] = IndentRequirment[IndentRequirment['Indent Title'].str.strip() == sample_data.iloc[i].IndentTitle.strip()]['Title_Class'].item().encode("utf-8") if len(IndentRequirment[IndentRequirment['Indent Title'].str.strip() == sample_data.iloc[i].IndentTitle.strip()]['Title_Class']) > 0 else "UNKNOWN"
        rid['Gender'] = sample_data.iloc[i].Gender.encode("utf-8")
        rid['Age'] = sample_data.iloc[i].Age
        rid['Marital_Status'] = sample_data.iloc[i].MartitalStatus.encode("utf-8")
        rid['QType1'] = sample_data.iloc[i].QType1.encode("utf-8")
        rid['QPer2'] = sample_data.iloc[i].Qpercentage
        rid['PGPer3'] = sample_data.iloc[i].PGPercentage
        rid['Present_CTC'] = sample_data.iloc[i].PresentCTC
        rid['Work_Ex'] = sample_data.iloc[i].WorkExperience
        allCandidate.append(rid)
        
    hack = [];
    for i in range(0,len(allCandidate)):
        pdScore = {}
        pdScore['RID'] = allCandidate[i]['RID']
        pdScore['QPer2'] = allCandidate[i]['QPer2']
        pdScore['PGPer3'] = allCandidate[i]['PGPer3']
        pdScore['Present_CTC'] = allCandidate[i]['Present_CTC']
        pdScore['Work_Ex'] = allCandidate[i]['Work_Ex']
        x = Low_pop[Low_pop['Variable_name'] == 'Gender']
        pdScore['Gender']= x[x['Category'] == allCandidate[i]['Gender']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'Marital_Status']
        pdScore['Marital_Status']= x[x['Category'] == allCandidate[i]['Marital_Status']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'QName1_Class']
        pdScore['QName1']= x[x['Category'] == allCandidate[i]['QName1_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'QType1']
        pdScore['QType1']= x[x['Category'] == allCandidate[i]['QType1']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'PGName2_Class']
        pdScore['PGName2']= x[x['Category'] == allCandidate[i]['PGName2_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'PGSpec_Class']
        pdScore['PGSpec']= x[x['Category'] == allCandidate[i]['PGSpec_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'PGIns_Class']
        pdScore['PGIns']= x[x['Category'] == allCandidate[i]['PGIns_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'Prev_Empl_Class']
        pdScore['Prev_Empl']= x[x['Category'] == allCandidate[i]['Prev_Empl_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'Prev_Desig_Class']
        pdScore['Prev_Desig']= x[x['Category'] == allCandidate[i]['Prev_Desig_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'Industry_Class']
        pdScore['Industry']= x[x['Category'] == allCandidate[i]['Industry_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'Function_Class']
        pdScore['Function']= x[x['Category'] == allCandidate[i]['Function_Class']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'Source_Name']
        pdScore['Source_Name']= x[x['Category'] == allCandidate[i]['Source_Name']]['New_category'].item()
        x = Low_pop[Low_pop['Variable_name'] == 'Title_Class']
        pdScore['Title']= x[x['Category'] == allCandidate[i]['Title_Class']]['New_category'].item()
        pdScore['Age'] = allCandidate[i]['Age']
        hack.append(pdScore)
    
    formula = []
    for i in range(0,len(hack)):
        if(hack[i]['Title'] == 'BM'):
            predScore = {}
            y = BM[BM['Variable'] == 'Function']
            predScore['Function'] = y[y['Class'] == hack[i]['Function']]['Estimate'].item()
            y = BM[BM['Variable'] == 'Gender']
            predScore['Gender'] = y[y['Class'] == hack[i]['Gender']]['Estimate'].item()
            y = BM[BM['Variable'] == 'Industry']
            predScore['Industry'] = y[y['Class'] == hack[i]['Industry']]['Estimate'].item()
            y = BM[BM['Variable'] == 'Marital_Status']
            predScore['Marital_Status'] = y[y['Class'] == hack[i]['Marital_Status']]['Estimate'].item()
            y = BM[BM['Variable'] == 'PGIns']
            predScore['PGIns'] = y[y['Class'] == hack[i]['PGIns']]['Estimate'].item()
            y = BM[BM['Variable'] == 'PGName2']
            predScore['PGName2'] = y[y['Class'] == hack[i]['PGName2']]['Estimate'].item()
            y = BM[BM['Variable'] == 'PGSpec']
            predScore['PGSpec'] = y[y['Class'] == hack[i]['PGSpec']]['Estimate'].item()
            y = BM[BM['Variable'] == 'Prev_Desig']
            predScore['Prev_Desig'] = y[y['Class'] == hack[i]['Prev_Desig']]['Estimate'].item()
            y = BM[BM['Variable'] == 'Prev_Empl']
            predScore['Prev_Empl'] = y[y['Class'] == hack[i]['Prev_Empl']]['Estimate'].item()
            y = BM[BM['Variable'] == 'QName1']
            predScore['QName1'] = y[y['Class'] == hack[i]['QName1']]['Estimate'].item()
            y = BM[BM['Variable'] == 'QType1']
            predScore['QType1'] = y[y['Class'] == hack[i]['QType1']]['Estimate'].item()
            y = BM[BM['Variable'] == 'Source_Name']
            predScore['Source_Name'] = y[y['Class'] == hack[i]['Source_Name']]['Estimate'].item()
            predScore['Age'] = hack[i]['Age'] * -0.04243;
            predScore['QPer2'] = hack[i]['QPer2'] * -0.01251;
            predScore['PGPer3'] = hack[i]['PGPer3'] * 0.01125;
            predScore['Present_CTC'] = hack[i]['Present_CTC'] * -0.000001902;
            predScore['Work_Ex'] = hack[i]['Work_Ex'] * -0.02372;
            predScore['Intercept'] = 4.021;
            predScore['RID'] = hack[i]['RID']
            predScore['SUM'] = predScore['Age'] + predScore['Function'] + predScore['Gender'] + predScore['Industry'] + predScore['Intercept'] + predScore['Marital_Status'] + predScore['PGIns'] + predScore['PGName2'] + predScore['PGPer3'] + predScore['PGSpec'] + predScore['Present_CTC'] + predScore['Prev_Desig'] + predScore['Prev_Empl'] + predScore['QName1'] + predScore['QPer2'] + predScore['QType1'] + predScore['Source_Name'] + predScore['Work_Ex']
            predScore['PredictedProbability'] = 1 / (1+(math.exp(predScore['SUM'] * -1)))
            predScore['Score'] = predScore['PredictedProbability'] * 100
            formula.append(predScore)
            
    result= [] 
    for i in range(0,len(formula)):
        obj = {}
        obj['rid'] = str(formula[i]['RID'])
        obj['PredictedProbability'] = str(formula[i]['PredictedProbability'])
        obj['Score'] = str(formula[i]['Score'])
        result.append(obj)
    return result

    
