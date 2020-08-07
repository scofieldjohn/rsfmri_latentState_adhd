

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



#look at transition probability matrices
plt.rcParams["font.family"] = "Times New Roman"
fig, axarr = plt.subplots(2, 2, figsize = (7,7), dpi=400)
sns.heatmap(fa_tpm, mask=np.zeros_like(fa_tpm, dtype=np.bool), 
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=axarr[0,0],
            xticklabels = [1,2,3,4,5],yticklabels = [1,2,3,4,5],
            cbar=False)
axarr[0,0].set_title('Girls ADHD')
sns.heatmap(fc_tpm, mask=np.zeros_like(fc_tpm, dtype=np.bool), 
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=axarr[0,1],
            xticklabels = [1,2,3,4,5],yticklabels = [1,2,3,4,5])
axarr[0,1].set_title('Girls Control')
sns.heatmap(ma_tpm, mask=np.zeros_like(ma_tpm, dtype=np.bool), 
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=axarr[1,0],
            xticklabels = [1,2,3,4,5],yticklabels = [1,2,3,4,5],
            cbar=False)
axarr[1,0].set_title('Boys ADHD')
sns.heatmap(mc_tpm, mask=np.zeros_like(mc_tpm, dtype=np.bool), 
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=axarr[1,1],
            xticklabels = [1,2,3,4,5],yticklabels = [1,2,3,4,5])
axarr[1,1].set_title('Boys Control')
plt.subplots_adjust(hspace=0.5,wspace=0.1)
plt.show()

#mean sd of on and off diagonal



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
path_states = '%s/hmm22_states_fa.csv'%(opath)
fastates.to_csv(path_states)

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
path_states = '%s/hmm22_states_fc.csv'%(opath)
fcstates.to_csv(path_states)

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
path_states = '%s/hmm22_states_ma.csv'%(opath)
mastates.to_csv(path_states)

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
path_states = '%s/hmm22_states_mc.csv'%(opath)
mcstates.to_csv(path_states)


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


### fractional occupancy
faFO_dat = pd.DataFrame()
faFO_dat['state'] = [0,1,2,3,4]
for x in np.unique(fastates['partno'].values):  
    temp = fastates.loc[fastates['partno'] == x]
    how_long = len(temp)
    counts = temp['states'].value_counts()
    counts = counts.reset_index()
    counts = counts.sort_values(by=['index'])
    counts['states'] = counts['states']/how_long
    faFO_dat[str(x)] = counts['states']
where_are = np.isnan(faFO_dat)
faFO_dat[where_are] = 0


del(faFO_dat['state'])
faFO = faFO_dat.T
faFO['sub'] = fasubs['sub'].values
write_path = '%s/FO2fa_data.csv'%(opath)
faFO.to_csv(write_path)

fcFO_dat = pd.DataFrame()
fcFO_dat['state'] = [0,1,2,3,4]
for x in np.unique(fcstates['partno'].values):  
    temp = fcstates.loc[fcstates['partno'] == x]
    how_long = len(temp)
    counts = temp['states'].value_counts()
    counts = counts.reset_index()
    counts = counts.sort_values(by=['index'])
    counts['states'] = counts['states']/how_long
    fcFO_dat[str(x)] = counts['states']
where_are = np.isnan(fcFO_dat)
fcFO_dat[where_are] = 0

del(fcFO_dat['state'])
fcFO = fcFO_dat.T
fcFO['sub'] = fcsubs['sub'].values
write_path = '%s/FO2fc_data.csv'%(opath)
fcFO.to_csv(write_path)

maFO_dat = pd.DataFrame()
maFO_dat['state'] = [0,1,2,3,4]
for x in np.unique(mastates['partno'].values):  
    temp = mastates.loc[mastates['partno'] == x]
    how_long = len(temp)
    counts = temp['states'].value_counts()
    counts = counts.reset_index()
    counts = counts.sort_values(by=['index'])
    counts['states'] = counts['states']/how_long
    maFO_dat[str(x)] = counts['states']
where_are = np.isnan(maFO_dat)
maFO_dat[where_are] = 0

del(maFO_dat['state'])
maFO = maFO_dat.T
maFO['sub'] = masubs['sub'].values
write_path = '%s/FO2ma_data.csv'%(opath)
maFO.to_csv(write_path)

mcFO_dat = pd.DataFrame()
mcFO_dat['state'] = [0,1,2,3,4]
for x in np.unique(mcstates['partno'].values):  
    temp = mcstates.loc[mcstates['partno'] == x]
    how_long = len(temp)
    counts = temp['states'].value_counts()
    counts = counts.reset_index()
    counts = counts.sort_values(by=['index'])
    counts['states'] = counts['states']/how_long
    mcFO_dat[str(x)] = counts['states']
where_are = np.isnan(mcFO_dat)
mcFO_dat[where_are] = 0

del(mcFO_dat['state'])
mcFO = mcFO_dat.T
mcFO['sub'] = mcsubs['sub'].values
write_path = '%s/FO2mc_data.csv'%(opath)
mcFO.to_csv(write_path)


print(faFO.mean(axis=0))
print(fcFO.mean(axis=0))
print(maFO.mean(axis=0))
print(mcFO.mean(axis=0))

tempdat = pd.DataFrame({'FO':faFO.iloc[:,0],
                        'type': 'fa',
                        'sex': 'F',
                        'diag': 'A',
                        'sub':faFO['sub'].values})
tempdat2 = pd.DataFrame({'FO':fcFO.iloc[:,0],
                        'type': 'fc',
                        'sex': 'F',
                        'diag': 'C',
                        'sub':fcFO['sub'].values})
tempdat3 = pd.DataFrame({'FO':maFO.iloc[:,0],
                        'type': 'ma',
                        'sex': 'M',
                        'diag': 'A',
                        'sub':maFO['sub'].values})
tempdat4 = pd.DataFrame({'FO':mcFO.iloc[:,0],
                        'type': 'mc',
                        'sex': 'M',
                        'diag': 'C',
                        'sub':mcFO['sub'].values})

FO_common_dat = pd.concat((tempdat,tempdat2,tempdat3,tempdat4),axis=0)
write_path = '%s/hmm2_frac_occ_common.csv'%(opath)
FO_common_dat.to_csv(write_path)


#### intertransition interval (across all states)
faITI_overall_mean = []
faITI_overall_sd = []
for x in np.unique(fastates['partno'].values):
    ITI = []
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
            ITI = np.append(ITI, iti)
            iti = 0
        tempval = tempval+1
    ITI = np.append(ITI,iti)
    faITI_overall_mean = np.append(faITI_overall_mean, np.mean(ITI))
    faITI_overall_sd = np.append(faITI_overall_sd, np.std(ITI))
faITI_overall_mean = pd.DataFrame(faITI_overall_mean)
faITI_overall_sd = pd.DataFrame(faITI_overall_sd)

write_path1 = '%s/ITI2fc_means.csv'%(opath)
write_path2 = '%s/ITI2fc_sd.csv'%(opath)
faITI_overall_mean.to_csv(write_path1)
faITI_overall_sd.to_csv(write_path2)

fcITI_overall_mean = []
fcITI_overall_sd = []
for x in np.unique(fcstates['partno'].values):
    ITI = []
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
            ITI = np.append(ITI, iti)
            iti = 0
        tempval = tempval+1
    ITI = np.append(ITI,iti)
    fcITI_overall_mean = np.append(fcITI_overall_mean, np.mean(ITI))
    fcITI_overall_sd = np.append(fcITI_overall_sd, np.std(ITI))
fcITI_overall_mean = pd.DataFrame(fcITI_overall_mean)
fcITI_overall_sd = pd.DataFrame(fcITI_overall_sd)

write_path1 = '%s/ITI2fc_means.csv'%(opath)
write_path2 = '%s/ITI2fc_sd.csv'%(opath)
fcITI_overall_mean.to_csv(write_path1)
fcITI_overall_sd.to_csv(write_path2)

maITI_overall_mean = []
maITI_overall_sd = []
for x in np.unique(mastates['partno'].values):
    ITI = []
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
            ITI = np.append(ITI, iti)
            iti = 0
        tempval = tempval+1
    ITI = np.append(ITI,iti)
    maITI_overall_mean = np.append(maITI_overall_mean, np.mean(ITI))
    maITI_overall_sd = np.append(maITI_overall_sd, np.std(ITI))
maITI_overall_mean = pd.DataFrame(maITI_overall_mean)
maITI_overall_sd = pd.DataFrame(maITI_overall_sd)

write_path1 = '%s/ITI2ma_means.csv'%(opath)
write_path2 = '%s/ITI2ma_sd.csv'%(opath)
maITI_overall_mean.to_csv(write_path1)
maITI_overall_sd.to_csv(write_path2)

mcITI_overall_mean = []
mcITI_overall_sd = []
for x in np.unique(mcstates['partno'].values):
    ITI = []
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
            ITI = np.append(ITI, iti)
            iti = 0
        tempval = tempval+1
    ITI = np.append(ITI,iti)
    mcITI_overall_mean = np.append(mcITI_overall_mean, np.mean(ITI))
    mcITI_overall_sd = np.append(mcITI_overall_sd, np.std(ITI))
mcITI_overall_mean = pd.DataFrame(mcITI_overall_mean)
mcITI_overall_sd = pd.DataFrame(mcITI_overall_sd)

write_path1 = '%s/ITI2mc_means.csv'%(opath)
write_path2 = '%s/ITI2mc_sd.csv'%(opath)
mcITI_overall_mean.to_csv(write_path1)
mcITI_overall_sd.to_csv(write_path2)


faITI_overall_mean['type'] = 'fa'
fcITI_overall_mean['type'] = 'fc'
maITI_overall_mean['type'] = 'ma'
mcITI_overall_mean['type'] = 'mc'
tempd = pd.concat((faITI_overall_mean, fcITI_overall_mean, maITI_overall_mean, mcITI_overall_mean), axis=0)
write_path = '%s/ITI_data_combined.csv'%(opath)
tempd.to_csv(write_path)

faITI_overall_sd['type'] = 'fa'
fcITI_overall_sd['type'] = 'fc'
maITI_overall_sd['type'] = 'ma'
mcITI_overall_sd['type'] = 'mc'
tempdsd = pd.concat((faITI_overall_sd, fcITI_overall_sd, maITI_overall_sd, mcITI_overall_sd), axis=0)
write_pathsd = '%s/ITI_data_combined_sd.csv'%(opath)
tempdsd.to_csv(write_pathsd)



#### number of transitions
fanumber_transitions = []
for x in np.unique(fastates['partno'].values):
    num_trans = []
    temp = fastates.loc[fastates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 0
    for y in list(range(0,how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval+1]:
            num_trans = np.append(num_trans,0)
        else:
            num_trans = np.append(num_trans, 1)
        tempval = tempval + 1
    fanumber_transitions = np.append(fanumber_transitions, sum(num_trans)/how_long)

fanumber_transitions = pd.DataFrame(fanumber_transitions)
write_path = '%s/NT2fa_data.csv'%(opath)
fanumber_transitions.to_csv(write_path) 

fcnumber_transitions = []
for x in np.unique(fcstates['partno'].values):
    num_trans = []
    temp = fcstates.loc[fcstates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 0
    for y in list(range(0,how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval+1]:
            num_trans = np.append(num_trans,0)
        else:
            num_trans = np.append(num_trans, 1)
        tempval = tempval + 1
    fcnumber_transitions = np.append(fcnumber_transitions, sum(num_trans)/how_long)

fcnumber_transitions = pd.DataFrame(fcnumber_transitions)
write_path = '%s/NT2fc_data.csv'%(opath)
fcnumber_transitions.to_csv(write_path) 

manumber_transitions = []
for x in np.unique(mastates['partno'].values):
    num_trans = []
    temp = mastates.loc[mastates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 0
    for y in list(range(0,how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval+1]:
            num_trans = np.append(num_trans,0)
        else:
            num_trans = np.append(num_trans, 1)
        tempval = tempval + 1
    manumber_transitions = np.append(manumber_transitions, sum(num_trans)/how_long)

manumber_transitions = pd.DataFrame(manumber_transitions)
write_path = '%s/NT2ma_data.csv'%(opath)
manumber_transitions.to_csv(write_path) 

mcnumber_transitions = []
for x in np.unique(mcstates['partno'].values):
    num_trans = []
    temp = mcstates.loc[mcstates['partno'] == x]
    temp = temp.reset_index()
    del(temp['index'])
    how_long = len(temp)
    tempval = 0
    for y in list(range(0,how_long-1)):
        if temp['states'][tempval] == temp['states'][tempval+1]:
            num_trans = np.append(num_trans,0)
        else:
            num_trans = np.append(num_trans, 1)
        tempval = tempval + 1
    mcnumber_transitions = np.append(mcnumber_transitions, sum(num_trans)/how_long)

mcnumber_transitions = pd.DataFrame(mcnumber_transitions)
write_path = '%s/NT2mc_data.csv'%(opath)
mcnumber_transitions.to_csv(write_path) 




fanumber_transitions['type'] = 'fa'
fcnumber_transitions['type'] = 'fc'
manumber_transitions['type'] = 'ma'
mcnumber_transitions['type'] = 'mc'

tempd = pd.concat((fanumber_transitions, fcnumber_transitions, manumber_transitions, mcnumber_transitions), axis=0)
write_path = '%s/NT_data_combined.csv'%(opath)
tempd.to_csv(write_path)














