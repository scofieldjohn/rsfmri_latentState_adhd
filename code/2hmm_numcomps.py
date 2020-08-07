

#### number of components
import pandas as pd
import numpy as np
from hmmlearn import hmm
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore", category=DeprecationWarning)

############################## load in data
path = 'C:/Users/jel7c5/Desktop/adhd200'
fapath = '%s/concat_timeseries_fa.csv'%(path)
fapath2 = '%s/concat_timeseries_fa_lengths.csv'%(path)
fadat = pd.read_csv(fapath)
falen = pd.read_csv(fapath2)
del(fadat['Unnamed: 0'], falen['Unnamed: 0'])
fadat = fadat.iloc[:,0:190].values
falen = falen.values[:,0]

fcpath = '%s/concat_timeseries_fc.csv'%(path)
fcpath2 = '%s/concat_timeseries_fc_lengths.csv'%(path)
fcdat = pd.read_csv(fcpath)
fclen = pd.read_csv(fcpath2)
del(fcdat['Unnamed: 0'], fclen['Unnamed: 0'])
fcdat = fcdat.iloc[:,0:190].values
fclen = fclen.values[:,0]

mapath = '%s/concat_timeseries_ma.csv'%(path)
mapath2 = '%s/concat_timeseries_ma_lengths.csv'%(path)
madat = pd.read_csv(mapath)
malen = pd.read_csv(mapath2)
del(madat['Unnamed: 0'], malen['Unnamed: 0'])
madat = madat.iloc[:,0:190].values
malen = malen.values[:,0]

mcpath = '%s/concat_timeseries_mc.csv'%(path)
mcpath2 = '%s/concat_timeseries_mc_lengths.csv'%(path)
mcdat = pd.read_csv(mcpath)
mclen = pd.read_csv(mcpath2)
del(mcdat['Unnamed: 0'], mclen['Unnamed: 0'])
mcdat = mcdat.iloc[:,0:190].values
mclen = mclen.values[:,0]



## fit number of components
fa_scores = []
for x in list(range(1,11)):
    mod = hmm.GaussianHMM(n_components=x, covariance_type = 'diag',
                          verbose = False).fit(fadat, falen)
    fa_scores = np.append(fa_scores, mod.score(fadat,falen))
    print(x)

fc_scores = []
for x in list(range(1,11)):
    mod = hmm.GaussianHMM(n_components=x, covariance_type = 'diag',
                          verbose = False).fit(fcdat, fclen)
    fc_scores = np.append(fc_scores, mod.score(fcdat,fclen))
    print(x)
    
ma_scores = []
for x in list(range(1,11)):
    mod = hmm.GaussianHMM(n_components=x, covariance_type = 'diag',
                          verbose = False).fit(madat, malen)
    ma_scores = np.append(ma_scores, mod.score(madat,malen))
    print(x)
    
mc_scores = []
for x in list(range(1,11)):
    mod = hmm.GaussianHMM(n_components=x, covariance_type = 'diag',
                          verbose = False).fit(mcdat, mclen)
    mc_scores = np.append(mc_scores, mod.score(mcdat,mclen))
    print(x)
    

xv = [1,2,3,4,5,6,7,8,9,10]
fig, axarr = plt.subplots(2, 2)
axarr[0,0].plot(fa_scores)
axarr[0,0].set_title('FA components')
axarr[0,0].set_yticklabels([])
axarr[0,1].plot(fc_scores)
axarr[0,1].set_title('FC components')
axarr[0,1].set_yticklabels([])
axarr[1,0].plot(ma_scores)
axarr[1,0].set_title('MA components')
axarr[1,0].set_yticklabels([])
axarr[1,1].plot(mc_scores)
axarr[1,1].set_title('MC components')
axarr[1,1].set_yticklabels([])
plt.subplots_adjust(hspace=.5,wspace=.5)
plt.show()





