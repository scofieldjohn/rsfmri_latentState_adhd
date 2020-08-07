# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:58:51 2019

@author: jscof
"""

import numpy as np
from sklearn.externals import joblib
np.random.seed(42)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
opath = 'C:/Users/jscof/OneDrive - University of Missouri/John PhD Mizzou/Research/EP/Resting-state functional connectivity sex differences/adhd/adhd200'

################################### load in overall HMM models
picklepath = '%s/hmm2_model_pickle_fa.pkl'%(opath)
fa_mod = joblib.load(picklepath)
fa_means = fa_mod.means_
fa_covars = fa_mod.covars_
np.diag(fa_mod.covars_[0])
fa_tpm = fa_mod.transmat_

picklepath = '%s/hmm2_model_pickle_fc.pkl'%(opath)
fc_mod = joblib.load(picklepath)
fc_means = fc_mod.means_
fc_covars = fc_mod.covars_
np.diag(fc_mod.covars_[0])
fc_tpm = fc_mod.transmat_

picklepath = '%s/hmm2_model_pickle_ma.pkl'%(opath)
ma_mod = joblib.load(picklepath)
ma_means = ma_mod.means_
ma_covars = ma_mod.covars_
np.diag(ma_mod.covars_[0])
ma_tpm = ma_mod.transmat_

picklepath = '%s/hmm2_model_pickle_mc.pkl'%(opath)
mc_mod = joblib.load(picklepath)
mc_means = mc_mod.means_
mc_covars = mc_mod.covars_
np.diag(mc_mod.covars_[0])
mc_tpm = mc_mod.transmat_


##read in states data
statepath = '%s/hmm2_states_fa.csv'%(opath)
lengthspath = '%s/concat_timeseries_fa_lengths.csv'%(opath)
fastates = pd.read_csv(statepath)
falengths = pd.read_csv(lengthspath)
del(falengths['Unnamed: 0'], fastates['Unnamed: 0'])

tempvec = falengths.values
fastates['partno'] = 0
y=0
p=1
for x in tempvec:
   how_long = int(x)
   for a in list(range(0,how_long)):
       fastates['partno'][y] = p
       y = y + 1
   p=p+1

fastates.columns = ['states','partno']

statepath = '%s/hmm2_states_fc.csv'%(opath)
lengthspath = '%s/concat_timeseries_fc_lengths.csv'%(opath)
fcstates = pd.read_csv(statepath)
fclengths = pd.read_csv(lengthspath)
del(fclengths['Unnamed: 0'], fcstates['Unnamed: 0'])

tempvec = fclengths.values
fcstates['partno'] = 0
y=0
p=1
for x in tempvec:
   how_long = int(x)
   for a in list(range(0,how_long)):
       fcstates['partno'][y] = p
       y = y + 1
   p=p+1

fcstates.columns = ['states','partno']

statepath = '%s/hmm2_states_ma.csv'%(opath)
lengthspath = '%s/concat_timeseries_ma_lengths.csv'%(opath)
mastates = pd.read_csv(statepath)
malengths = pd.read_csv(lengthspath)
del(malengths['Unnamed: 0'], mastates['Unnamed: 0'])

tempvec = malengths.values
mastates['partno'] = 0
y=0
p=1
for x in tempvec:
   how_long = int(x)
   for a in list(range(0,how_long)):
       mastates['partno'][y] = p
       y = y + 1
   p=p+1

mastates.columns = ['states','partno']

statepath = '%s/hmm2_states_mc.csv'%(opath)
lengthspath = '%s/concat_timeseries_mc_lengths.csv'%(opath)
mcstates = pd.read_csv(statepath)
mclengths = pd.read_csv(lengthspath)
del(mclengths['Unnamed: 0'], mcstates['Unnamed: 0'])

tempvec = mclengths.values
mcstates['partno'] = 0
y=0
p=1
for x in tempvec:
   how_long = int(x)
   for a in list(range(0,how_long)):
       mcstates['partno'][y] = p
       y = y + 1
   p=p+1

mcstates.columns = ['states','partno']


## load in subs data
pathsubfa = '%s/concat_timeseries_fa_subs.csv'%(opath)
pathsubfc = '%s/concat_timeseries_fc_subs.csv'%(opath)
pathsubma = '%s/concat_timeseries_ma_subs.csv'%(opath)
pathsubmc = '%s/concat_timeseries_mc_subs.csv'%(opath)
fasubs = pd.read_csv(pathsubfa)
fcsubs = pd.read_csv(pathsubfc)
masubs = pd.read_csv(pathsubma)
mcsubs = pd.read_csv(pathsubmc)
fasubs.columns = ['one','sub']
fcsubs.columns = ['one','sub']
masubs.columns = ['one','sub']
mcsubs.columns = ['one','sub']


#### intertransition interval (individual states)
faITI_overall_mean1 = []
faITI_overall_mean2 = []
faITI_overall_mean3 = []
faITI_overall_mean4 = []
faITI_overall_mean5 = []
faITI_overall_sd1 = []
faITI_overall_sd2 = []
faITI_overall_sd3 = []
faITI_overall_sd4 = []
faITI_overall_sd5 = []
for x in np.unique(fastates['partno'].values):
    ITI1 = []
    ITI2 = []
    ITI3 = []
    ITI4 = []
    ITI5 = []
    iti = 0
    temp = fastates.loc[fastates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 1
    for y in list(range(0, how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval-1]:
            iti = iti+1
        else:
            if temp['states'][tempval] == 0:
                ITI1 = np.append(ITI1, iti)
                iti = 0
            elif temp['states'][tempval] == 1:
                ITI2 = np.append(ITI2, iti)
                iti = 0
            elif temp['states'][tempval] == 2:
                ITI3 = np.append(ITI3, iti)
                iti = 0
            elif temp['states'][tempval] == 3:
                ITI4 = np.append(ITI4, iti)
                iti = 0
            else:
                ITI5 = np.append(ITI5, iti)
                iti = 0
        tempval = tempval+1
    if temp['states'][tempval-1] == 0:
        ITI1 = np.append(ITI1, iti)
    elif temp['states'][tempval-1] == 1:
        ITI2 = np.append(ITI2, iti)
    elif temp['states'][tempval-1] == 2:
        ITI3 = np.append(ITI3, iti)
    elif temp['states'][tempval-1] == 3:
        ITI4 = np.append(ITI4, iti)
    elif temp['states'][tempval-1] == 4:
        ITI5 = np.append(ITI5, iti)
    faITI_overall_mean1 = np.append(faITI_overall_mean1, np.mean(ITI1))
    faITI_overall_mean2 = np.append(faITI_overall_mean2, np.mean(ITI2))
    faITI_overall_mean3 = np.append(faITI_overall_mean3, np.mean(ITI3))
    faITI_overall_mean4 = np.append(faITI_overall_mean4, np.mean(ITI4))
    faITI_overall_mean5 = np.append(faITI_overall_mean5, np.mean(ITI5))
    faITI_overall_sd1 = np.append(faITI_overall_sd1, np.std(ITI1))
    faITI_overall_sd2 = np.append(faITI_overall_sd2, np.std(ITI2))
    faITI_overall_sd3 = np.append(faITI_overall_sd3, np.std(ITI3))
    faITI_overall_sd4 = np.append(faITI_overall_sd4, np.std(ITI4))
    faITI_overall_sd5 = np.append(faITI_overall_sd5, np.std(ITI5))
faITI_overall_mean1 = pd.DataFrame(faITI_overall_mean1)
faITI_overall_mean2 = pd.DataFrame(faITI_overall_mean2)
faITI_overall_mean3 = pd.DataFrame(faITI_overall_mean3)
faITI_overall_mean4 = pd.DataFrame(faITI_overall_mean4)
faITI_overall_mean5 = pd.DataFrame(faITI_overall_mean5)
faITI_overall_sd1 = pd.DataFrame(faITI_overall_sd1)
faITI_overall_sd2 = pd.DataFrame(faITI_overall_sd2)
faITI_overall_sd3 = pd.DataFrame(faITI_overall_sd3)
faITI_overall_sd4 = pd.DataFrame(faITI_overall_sd4)
faITI_overall_sd5 = pd.DataFrame(faITI_overall_sd5)

write_path1 = '%s/ITI2fa_means1.csv'%(opath)
faITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fa_means2.csv'%(opath)
faITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fa_means3.csv'%(opath)
faITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fa_means4.csv'%(opath)
faITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fa_means5.csv'%(opath)
faITI_overall_mean1.to_csv(write_path1)
write_path2 = '%s/ITI2fa_sd1.csv'%(opath)
faITI_overall_sd1.to_csv(write_path2)
write_path2 = '%s/ITI2fa_sd2.csv'%(opath)
faITI_overall_sd2.to_csv(write_path2)
write_path2 = '%s/ITI2fa_sd3.csv'%(opath)
faITI_overall_sd3.to_csv(write_path2)
write_path2 = '%s/ITI2fa_sd4.csv'%(opath)
faITI_overall_sd4.to_csv(write_path2)
write_path2 = '%s/ITI2fa_sd5.csv'%(opath)
faITI_overall_sd5.to_csv(write_path2)


fcITI_overall_mean1 = []
fcITI_overall_mean2 = []
fcITI_overall_mean3 = []
fcITI_overall_mean4 = []
fcITI_overall_mean5 = []
fcITI_overall_sd1 = []
fcITI_overall_sd2 = []
fcITI_overall_sd3 = []
fcITI_overall_sd4 = []
fcITI_overall_sd5 = []
for x in np.unique(fcstates['partno'].values):
    ITI1 = []
    ITI2 = []
    ITI3 = []
    ITI4 = []
    ITI5 = []
    iti = 0
    temp = fcstates.loc[fcstates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 1
    for y in list(range(0, how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval-1]:
            iti = iti+1
        else:
            if temp['states'][tempval] == 0:
                ITI1 = np.append(ITI1, iti)
                iti = 0
            elif temp['states'][tempval] == 1:
                ITI2 = np.append(ITI2, iti)
                iti = 0
            elif temp['states'][tempval] == 2:
                ITI3 = np.append(ITI3, iti)
                iti = 0
            elif temp['states'][tempval] == 3:
                ITI4 = np.append(ITI4, iti)
                iti = 0
            else:
                ITI5 = np.append(ITI5, iti)
                iti = 0
        tempval = tempval+1
    if temp['states'][tempval-1] == 0:
        ITI1 = np.append(ITI1, iti)
    elif temp['states'][tempval-1] == 1:
        ITI2 = np.append(ITI2, iti)
    elif temp['states'][tempval-1] == 2:
        ITI3 = np.append(ITI3, iti)
    elif temp['states'][tempval-1] == 3:
        ITI4 = np.append(ITI4, iti)
    elif temp['states'][tempval-1] == 4:
        ITI5 = np.append(ITI5, iti)
    fcITI_overall_mean1 = np.append(fcITI_overall_mean1, np.mean(ITI1))
    fcITI_overall_mean2 = np.append(fcITI_overall_mean2, np.mean(ITI2))
    fcITI_overall_mean3 = np.append(fcITI_overall_mean3, np.mean(ITI3))
    fcITI_overall_mean4 = np.append(fcITI_overall_mean4, np.mean(ITI4))
    fcITI_overall_mean5 = np.append(fcITI_overall_mean5, np.mean(ITI5))
    fcITI_overall_sd1 = np.append(fcITI_overall_sd1, np.std(ITI1))
    fcITI_overall_sd2 = np.append(fcITI_overall_sd2, np.std(ITI2))
    fcITI_overall_sd3 = np.append(fcITI_overall_sd3, np.std(ITI3))
    fcITI_overall_sd4 = np.append(fcITI_overall_sd4, np.std(ITI4))
    fcITI_overall_sd5 = np.append(fcITI_overall_sd5, np.std(ITI5))
fcITI_overall_mean1 = pd.DataFrame(fcITI_overall_mean1)
fcITI_overall_mean2 = pd.DataFrame(fcITI_overall_mean2)
fcITI_overall_mean3 = pd.DataFrame(fcITI_overall_mean3)
fcITI_overall_mean4 = pd.DataFrame(fcITI_overall_mean4)
fcITI_overall_mean5 = pd.DataFrame(fcITI_overall_mean5)
fcITI_overall_sd1 = pd.DataFrame(fcITI_overall_sd1)
fcITI_overall_sd2 = pd.DataFrame(fcITI_overall_sd2)
fcITI_overall_sd3 = pd.DataFrame(fcITI_overall_sd3)
fcITI_overall_sd4 = pd.DataFrame(fcITI_overall_sd4)
fcITI_overall_sd5 = pd.DataFrame(fcITI_overall_sd5)

write_path1 = '%s/ITI2fc_means1.csv'%(opath)
fcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fc_means2.csv'%(opath)
fcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fc_means3.csv'%(opath)
fcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fc_means4.csv'%(opath)
fcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2fc_means5.csv'%(opath)
fcITI_overall_mean1.to_csv(write_path1)
write_path2 = '%s/ITI2fc_sd1.csv'%(opath)
fcITI_overall_sd1.to_csv(write_path2)
write_path2 = '%s/ITI2fc_sd2.csv'%(opath)
fcITI_overall_sd2.to_csv(write_path2)
write_path2 = '%s/ITI2fc_sd3.csv'%(opath)
fcITI_overall_sd3.to_csv(write_path2)
write_path2 = '%s/ITI2fc_sd4.csv'%(opath)
fcITI_overall_sd4.to_csv(write_path2)
write_path2 = '%s/ITI2fc_sd5.csv'%(opath)
fcITI_overall_sd5.to_csv(write_path2)


maITI_overall_mean1 = []
maITI_overall_mean2 = []
maITI_overall_mean3 = []
maITI_overall_mean4 = []
maITI_overall_mean5 = []
maITI_overall_sd1 = []
maITI_overall_sd2 = []
maITI_overall_sd3 = []
maITI_overall_sd4 = []
maITI_overall_sd5 = []
for x in np.unique(mastates['partno'].values):
    ITI1 = []
    ITI2 = []
    ITI3 = []
    ITI4 = []
    ITI5 = []
    iti = 0
    temp = mastates.loc[mastates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 1
    for y in list(range(0, how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval-1]:
            iti = iti+1
        else:
            if temp['states'][tempval] == 0:
                ITI1 = np.append(ITI1, iti)
                iti = 0
            elif temp['states'][tempval] == 1:
                ITI2 = np.append(ITI2, iti)
                iti = 0
            elif temp['states'][tempval] == 2:
                ITI3 = np.append(ITI3, iti)
                iti = 0
            elif temp['states'][tempval] == 3:
                ITI4 = np.append(ITI4, iti)
                iti = 0
            else:
                ITI5 = np.append(ITI5, iti)
                iti = 0
        tempval = tempval+1
    if temp['states'][tempval-1] == 0:
        ITI1 = np.append(ITI1, iti)
    elif temp['states'][tempval-1] == 1:
        ITI2 = np.append(ITI2, iti)
    elif temp['states'][tempval-1] == 2:
        ITI3 = np.append(ITI3, iti)
    elif temp['states'][tempval-1] == 3:
        ITI4 = np.append(ITI4, iti)
    elif temp['states'][tempval-1] == 4:
        ITI5 = np.append(ITI5, iti)
    maITI_overall_mean1 = np.append(maITI_overall_mean1, np.mean(ITI1))
    maITI_overall_mean2 = np.append(maITI_overall_mean2, np.mean(ITI2))
    maITI_overall_mean3 = np.append(maITI_overall_mean3, np.mean(ITI3))
    maITI_overall_mean4 = np.append(maITI_overall_mean4, np.mean(ITI4))
    maITI_overall_mean5 = np.append(maITI_overall_mean5, np.mean(ITI5))
    maITI_overall_sd1 = np.append(maITI_overall_sd1, np.std(ITI1))
    maITI_overall_sd2 = np.append(maITI_overall_sd2, np.std(ITI2))
    maITI_overall_sd3 = np.append(maITI_overall_sd3, np.std(ITI3))
    maITI_overall_sd4 = np.append(maITI_overall_sd4, np.std(ITI4))
    maITI_overall_sd5 = np.append(maITI_overall_sd5, np.std(ITI5))
maITI_overall_mean1 = pd.DataFrame(maITI_overall_mean1)
maITI_overall_mean2 = pd.DataFrame(maITI_overall_mean2)
maITI_overall_mean3 = pd.DataFrame(maITI_overall_mean3)
maITI_overall_mean4 = pd.DataFrame(maITI_overall_mean4)
maITI_overall_mean5 = pd.DataFrame(maITI_overall_mean5)
maITI_overall_sd1 = pd.DataFrame(maITI_overall_sd1)
maITI_overall_sd2 = pd.DataFrame(maITI_overall_sd2)
maITI_overall_sd3 = pd.DataFrame(maITI_overall_sd3)
maITI_overall_sd4 = pd.DataFrame(maITI_overall_sd4)
maITI_overall_sd5 = pd.DataFrame(maITI_overall_sd5)

write_path1 = '%s/ITI2ma_means1.csv'%(opath)
maITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2ma_means2.csv'%(opath)
maITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2ma_means3.csv'%(opath)
maITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2ma_means4.csv'%(opath)
maITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2ma_means5.csv'%(opath)
maITI_overall_mean1.to_csv(write_path1)
write_path2 = '%s/ITI2ma_sd1.csv'%(opath)
maITI_overall_sd1.to_csv(write_path2)
write_path2 = '%s/ITI2ma_sd2.csv'%(opath)
maITI_overall_sd2.to_csv(write_path2)
write_path2 = '%s/ITI2ma_sd3.csv'%(opath)
maITI_overall_sd3.to_csv(write_path2)
write_path2 = '%s/ITI2ma_sd4.csv'%(opath)
maITI_overall_sd4.to_csv(write_path2)
write_path2 = '%s/ITI2ma_sd5.csv'%(opath)
maITI_overall_sd5.to_csv(write_path2)


mcITI_overall_mean1 = []
mcITI_overall_mean2 = []
mcITI_overall_mean3 = []
mcITI_overall_mean4 = []
mcITI_overall_mean5 = []
mcITI_overall_sd1 = []
mcITI_overall_sd2 = []
mcITI_overall_sd3 = []
mcITI_overall_sd4 = []
mcITI_overall_sd5 = []
for x in np.unique(mcstates['partno'].values):
    ITI1 = []
    ITI2 = []
    ITI3 = []
    ITI4 = []
    ITI5 = []
    iti = 0
    temp = mcstates.loc[mcstates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 1
    for y in list(range(0, how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval-1]:
            iti = iti+1
        else:
            if temp['states'][tempval] == 0:
                ITI1 = np.append(ITI1, iti)
                iti = 0
            elif temp['states'][tempval] == 1:
                ITI2 = np.append(ITI2, iti)
                iti = 0
            elif temp['states'][tempval] == 2:
                ITI3 = np.append(ITI3, iti)
                iti = 0
            elif temp['states'][tempval] == 3:
                ITI4 = np.append(ITI4, iti)
                iti = 0
            else:
                ITI5 = np.append(ITI5, iti)
                iti = 0
        tempval = tempval+1
    if temp['states'][tempval-1] == 0:
        ITI1 = np.append(ITI1, iti)
    elif temp['states'][tempval-1] == 1:
        ITI2 = np.append(ITI2, iti)
    elif temp['states'][tempval-1] == 2:
        ITI3 = np.append(ITI3, iti)
    elif temp['states'][tempval-1] == 3:
        ITI4 = np.append(ITI4, iti)
    elif temp['states'][tempval-1] == 4:
        ITI5 = np.append(ITI5, iti)
    mcITI_overall_mean1 = np.append(mcITI_overall_mean1, np.mean(ITI1))
    mcITI_overall_mean2 = np.append(mcITI_overall_mean2, np.mean(ITI2))
    mcITI_overall_mean3 = np.append(mcITI_overall_mean3, np.mean(ITI3))
    mcITI_overall_mean4 = np.append(mcITI_overall_mean4, np.mean(ITI4))
    mcITI_overall_mean5 = np.append(mcITI_overall_mean5, np.mean(ITI5))
    mcITI_overall_sd1 = np.append(mcITI_overall_sd1, np.std(ITI1))
    mcITI_overall_sd2 = np.append(mcITI_overall_sd2, np.std(ITI2))
    mcITI_overall_sd3 = np.append(mcITI_overall_sd3, np.std(ITI3))
    mcITI_overall_sd4 = np.append(mcITI_overall_sd4, np.std(ITI4))
    mcITI_overall_sd5 = np.append(mcITI_overall_sd5, np.std(ITI5))
mcITI_overall_mean1 = pd.DataFrame(mcITI_overall_mean1)
mcITI_overall_mean2 = pd.DataFrame(mcITI_overall_mean2)
mcITI_overall_mean3 = pd.DataFrame(mcITI_overall_mean3)
mcITI_overall_mean4 = pd.DataFrame(mcITI_overall_mean4)
mcITI_overall_mean5 = pd.DataFrame(mcITI_overall_mean5)
mcITI_overall_sd1 = pd.DataFrame(mcITI_overall_sd1)
mcITI_overall_sd2 = pd.DataFrame(mcITI_overall_sd2)
mcITI_overall_sd3 = pd.DataFrame(mcITI_overall_sd3)
mcITI_overall_sd4 = pd.DataFrame(mcITI_overall_sd4)
mcITI_overall_sd5 = pd.DataFrame(mcITI_overall_sd5)

write_path1 = '%s/ITI2mc_means1.csv'%(opath)
mcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2mc_means2.csv'%(opath)
mcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2mc_means3.csv'%(opath)
mcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2mc_means4.csv'%(opath)
mcITI_overall_mean1.to_csv(write_path1)
write_path1 = '%s/ITI2mc_means5.csv'%(opath)
mcITI_overall_mean1.to_csv(write_path1)
write_path2 = '%s/ITI2mc_sd1.csv'%(opath)
mcITI_overall_sd1.to_csv(write_path2)
write_path2 = '%s/ITI2mc_sd2.csv'%(opath)
mcITI_overall_sd2.to_csv(write_path2)
write_path2 = '%s/ITI2mc_sd3.csv'%(opath)
mcITI_overall_sd3.to_csv(write_path2)
write_path2 = '%s/ITI2mc_sd4.csv'%(opath)
mcITI_overall_sd4.to_csv(write_path2)
write_path2 = '%s/ITI2mc_sd5.csv'%(opath)
mcITI_overall_sd5.to_csv(write_path2)



#combine data
faITI_overall_mean1['type'] = 'fa'
fcITI_overall_mean1['type'] = 'fc'
maITI_overall_mean1['type'] = 'ma'
mcITI_overall_mean1['type'] = 'mc'
tempd = pd.concat((faITI_overall_mean1, fcITI_overall_mean1,
                   maITI_overall_mean1, mcITI_overall_mean1), axis=0)
write_path = '%s/ITI_data_combined1.csv'%(opath)
tempd.to_csv(write_path)
faITI_overall_mean2['type'] = 'fa'
fcITI_overall_mean2['type'] = 'fc'
maITI_overall_mean2['type'] = 'ma'
mcITI_overall_mean2['type'] = 'mc'
tempd = pd.concat((faITI_overall_mean2, fcITI_overall_mean2,
                   maITI_overall_mean2, mcITI_overall_mean2), axis=0)
write_path = '%s/ITI_data_combined2.csv'%(opath)
tempd.to_csv(write_path)
faITI_overall_mean3['type'] = 'fa'
fcITI_overall_mean3['type'] = 'fc'
maITI_overall_mean3['type'] = 'ma'
mcITI_overall_mean3['type'] = 'mc'
tempd = pd.concat((faITI_overall_mean3, fcITI_overall_mean3,
                   maITI_overall_mean3, mcITI_overall_mean3), axis=0)
write_path = '%s/ITI_data_combined3.csv'%(opath)
tempd.to_csv(write_path)
faITI_overall_mean4['type'] = 'fa'
fcITI_overall_mean4['type'] = 'fc'
maITI_overall_mean4['type'] = 'ma'
mcITI_overall_mean4['type'] = 'mc'
tempd = pd.concat((faITI_overall_mean4, fcITI_overall_mean4,
                   maITI_overall_mean4, mcITI_overall_mean4), axis=0)
write_path = '%s/ITI_data_combined4.csv'%(opath)
tempd.to_csv(write_path)
faITI_overall_mean5['type'] = 'fa'
fcITI_overall_mean5['type'] = 'fc'
maITI_overall_mean5['type'] = 'ma'
mcITI_overall_mean5['type'] = 'mc'
tempd = pd.concat((faITI_overall_mean5, fcITI_overall_mean5,
                   maITI_overall_mean5, mcITI_overall_mean5), axis=0)
write_path = '%s/ITI_data_combined5.csv'%(opath)
tempd.to_csv(write_path)
#


faITI_overall_sd1['type'] = 'fa'
fcITI_overall_sd1['type'] = 'fc'
maITI_overall_sd1['type'] = 'ma'
mcITI_overall_sd1['type'] = 'mc'
tempdsd = pd.concat((faITI_overall_sd1, fcITI_overall_sd1,
                     maITI_overall_sd1, mcITI_overall_sd1), axis=0)
write_pathsd = '%s/ITI_data_combined_sd1.csv'%(opath)
tempdsd.to_csv(write_pathsd)
faITI_overall_sd2['type'] = 'fa'
fcITI_overall_sd2['type'] = 'fc'
maITI_overall_sd2['type'] = 'ma'
mcITI_overall_sd2['type'] = 'mc'
tempdsd = pd.concat((faITI_overall_sd2, fcITI_overall_sd2,
                     maITI_overall_sd2, mcITI_overall_sd2), axis=0)
write_pathsd = '%s/ITI_data_combined_sd2.csv'%(opath)
tempdsd.to_csv(write_pathsd)
faITI_overall_sd3['type'] = 'fa'
fcITI_overall_sd3['type'] = 'fc'
maITI_overall_sd3['type'] = 'ma'
mcITI_overall_sd3['type'] = 'mc'
tempdsd = pd.concat((faITI_overall_sd3, fcITI_overall_sd3,
                     maITI_overall_sd3, mcITI_overall_sd3), axis=0)
write_pathsd = '%s/ITI_data_combined_sd3.csv'%(opath)
tempdsd.to_csv(write_pathsd)
faITI_overall_sd4['type'] = 'fa'
fcITI_overall_sd4['type'] = 'fc'
maITI_overall_sd4['type'] = 'ma'
mcITI_overall_sd4['type'] = 'mc'
tempdsd = pd.concat((faITI_overall_sd4, fcITI_overall_sd4,
                     maITI_overall_sd4, mcITI_overall_sd4), axis=0)
write_pathsd = '%s/ITI_data_combined_sd4.csv'%(opath)
tempdsd.to_csv(write_pathsd)
faITI_overall_sd5['type'] = 'fa'
fcITI_overall_sd5['type'] = 'fc'
maITI_overall_sd5['type'] = 'ma'
mcITI_overall_sd5['type'] = 'mc'
tempdsd = pd.concat((faITI_overall_sd5, fcITI_overall_sd5,
                     maITI_overall_sd5, mcITI_overall_sd5), axis=0)
write_pathsd = '%s/ITI_data_combined_sd5.csv'%(opath)
tempdsd.to_csv(write_pathsd)




