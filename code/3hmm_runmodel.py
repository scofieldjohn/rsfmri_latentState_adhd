

import numpy as np
from hmmlearn import hmm
from sklearn.externals import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
np.random.seed(42)
opath = 'C:/Users/jel7c5/Desktop/adhd200'

############################## run HMM female adhd
fapath = '%s/concat_timeseries_fa.csv'%(opath)
fapath2 = '%s/concat_timeseries_fa_lengths.csv'%(opath)
fadat = pd.read_csv(fapath)
falen = pd.read_csv(fapath2)
del(fadat['Unnamed: 0'], falen['Unnamed: 0'])
fadat = fadat.iloc[:,0:190].values
falen = falen.values[:,0]

fa_mod = hmm.GaussianHMM(n_components=5, covariance_type="diag", verbose = False).fit(fadat, falen)
fa_mod.score(fadat, falen)
states = fa_mod.predict(fadat, falen)
means = fa_mod.means_
covars = fa_mod.covars_
np.diag(fa_mod.covars_[0])
tpm = fa_mod.transmat_

path_states = '%s/hmm2_states_fa.csv'%(opath)
states = pd.DataFrame(states)
states.to_csv(path_states)
path_means = '%s/hmm2_means_fa.csv'%(opath)
means = pd.DataFrame(means)
means.to_csv(path_means)
path_covars = '%s/hmm2_covars_fa.txt'%(opath)
covars.tofile(path_covars)
path_tpm = '%s/hmm2_tpm_fa.csv'%(opath)
tpm = pd.DataFrame(tpm)
tpm.to_csv(path_tpm)
picklepath = '%s/hmm2_model_pickle_fa.pkl'%(opath)
joblib.dump(fa_mod, picklepath)

############################## run HMM female control
fcpath = '%s/concat_timeseries_fc.csv'%(opath)
fcpath2 = '%s/concat_timeseries_fc_lengths.csv'%(opath)
fcdat = pd.read_csv(fcpath)
fclen = pd.read_csv(fcpath2)
del(fcdat['Unnamed: 0'], fclen['Unnamed: 0'])
fcdat = fcdat.iloc[:,0:190].values
fclen = fclen.values[:,0]

fc_mod = hmm.GaussianHMM(n_components=5, covariance_type="diag", verbose = False).fit(fcdat, fclen)
fc_mod.score(fcdat, fclen)
states = fc_mod.predict(fcdat, fclen)
means = fc_mod.means_
covars = fc_mod.covars_
np.diag(fc_mod.covars_[0])
tpm = fc_mod.transmat_

path_states = '%s/hmm2_states_fc.csv'%(opath)
states = pd.DataFrame(states)
states.to_csv(path_states)
path_means = '%s/hmm2_means_fc.csv'%(opath)
means = pd.DataFrame(means)
means.to_csv(path_means)
path_covars = '%s/hmm2_covars_fc.txt'%(opath)
covars.tofile(path_covars)
path_tpm = '%s/hmm2_tpm_fc.csv'%(opath)
tpm = pd.DataFrame(tpm)
tpm.to_csv(path_tpm)
picklepath = '%s/hmm2_model_pickle_fc.pkl'%(opath)
joblib.dump(fc_mod, picklepath)

############################## run HMM male adhd
mapath = '%s/concat_timeseries_ma.csv'%(opath)
mapath2 = '%s/concat_timeseries_ma_lengths.csv'%(opath)
madat = pd.read_csv(mapath)
malen = pd.read_csv(mapath2)
del(madat['Unnamed: 0'], malen['Unnamed: 0'])
madat = madat.iloc[:,0:190].values
malen = malen.values[:,0]

ma_mod = hmm.GaussianHMM(n_components=5, covariance_type="diag", verbose = False).fit(madat, malen)
ma_mod.score(madat, malen)
states = ma_mod.predict(madat, malen)
means = ma_mod.means_
covars = ma_mod.covars_
np.diag(ma_mod.covars_[0])
tpm = ma_mod.transmat_

path_states = '%s/hmm2_states_ma.csv'%(opath)
states = pd.DataFrame(states)
states.to_csv(path_states)
path_means = '%s/hmm2_means_ma.csv'%(opath)
means = pd.DataFrame(means)
means.to_csv(path_means)
path_covars = '%s/hmm2_covars_ma.txt'%(opath)
covars.tofile(path_covars)
path_tpm = '%s/hmm2_tpm_ma.csv'%(opath)
tpm = pd.DataFrame(tpm)
tpm.to_csv(path_tpm)
picklepath = '%s/hmm2_model_pickle_ma.pkl'%(opath)
joblib.dump(ma_mod, picklepath)

############################## run HMM male control
mcpath = '%s/concat_timeseries_mc.csv'%(opath)
mcpath2 = '%s/concat_timeseries_mc_lengths.csv'%(opath)
mcdat = pd.read_csv(mcpath)
mclen = pd.read_csv(mcpath2)
del(mcdat['Unnamed: 0'], mclen['Unnamed: 0'])
mcdat = mcdat.iloc[:,0:190].values
mclen = mclen.values[:,0]

mc_mod = hmm.GaussianHMM(n_components=5, covariance_type="diag", verbose = False).fit(mcdat, mclen)
mc_mod.score(mcdat, mclen)
states = mc_mod.predict(mcdat, mclen)
means = mc_mod.means_
covars = mc_mod.covars_
np.diag(mc_mod.covars_[0])
tpm = mc_mod.transmat_

path_states = '%s/hmm2_states_mc.csv'%(opath)
states = pd.DataFrame(states)
states.to_csv(path_states)
path_means = '%s/hmm2_means_mc.csv'%(opath)
means = pd.DataFrame(means)
means.to_csv(path_means)
path_covars = '%s/hmm2_covars_mc.txt'%(opath)
covars.tofile(path_covars)
path_tpm = '%s/hmm2_tpm_mc.csv'%(opath)
tpm = pd.DataFrame(tpm)
tpm.to_csv(path_tpm)
picklepath = '%s/hmm2_model_pickle_mc.pkl'%(opath)
joblib.dump(mc_mod, picklepath)






