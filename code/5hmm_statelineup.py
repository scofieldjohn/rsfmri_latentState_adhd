

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.externals import joblib
opath = 'C:/Users/jel7c5/Desktop/adhd200'

################################### load in overall HMM models
picklepath = '%s/hmm2_model_pickle_fa.pkl'%(opath)
fa_mod = joblib.load(picklepath)
fa_means = pd.DataFrame(fa_mod.means_)
fa_means['diag'] = 'fa'

picklepath = '%s/hmm2_model_pickle_fc.pkl'%(opath)
fc_mod = joblib.load(picklepath)
fc_means = pd.DataFrame(fc_mod.means_)
fc_means['diag'] = 'fc'

picklepath = '%s/hmm2_model_pickle_ma.pkl'%(opath)
ma_mod = joblib.load(picklepath)
ma_means = pd.DataFrame(ma_mod.means_)
ma_means['diag'] = 'ma'

picklepath = '%s/hmm2_model_pickle_mc.pkl'%(opath)
mc_mod = joblib.load(picklepath)
mc_means = pd.DataFrame(mc_mod.means_)
mc_means['diag'] = 'mc'

frames = [fa_means,fc_means,ma_means,mc_means]

bigD = pd.concat(frames)

target = bigD.diag.values

kmeans = KMeans(n_clusters=5, random_state=0).fit(bigD.iloc[:,0:190].values)
clust = kmeans.labels_


compare = pd.DataFrame({'estimate':clust,
                        'target':target})

writepath = '%s_analyses/cluster_analysis.csv'%(opath)
compare.to_csv(writepath)


#write out averaged maps for each state based on cluster analysis
state1 = pd.DataFrame(bigD.iloc[np.where(clust==0)[0],0:190].mean(axis=0)).T
state2 = pd.DataFrame(bigD.iloc[np.where(clust==1)[0],0:190].mean(axis=0)).T
state3 = pd.DataFrame(bigD.iloc[np.where(clust==2)[0],0:190].mean(axis=0)).T
state4 = pd.DataFrame(bigD.iloc[np.where(clust==3)[0],0:190].mean(axis=0)).T
state5 = pd.DataFrame(bigD.iloc[np.where(clust==4)[0],0:190].mean(axis=0)).T

path1 = '%s_analyses/state1_map.csv'%(opath)
path2 = '%s_analyses/state2_map.csv'%(opath)
path3 = '%s_analyses/state3_map.csv'%(opath)
path4 = '%s_analyses/state4_map.csv'%(opath)
path5 = '%s_analyses/state5_map.csv'%(opath)

state1.to_csv(path1)
state2.to_csv(path2)
state3.to_csv(path3)
state4.to_csv(path4)
state5.to_csv(path5)




