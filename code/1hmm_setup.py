

import numpy as np
import pandas as pd
import os
np.random.seed(42)
from scipy.stats.mstats import zscore

path = 'C:/Users/jel7c5/Desktop/adhd200'
sites = ['KKI','NeuroIMAGE','NYU','OHSU','Peking_1','Peking_2',
         'Peking_3','Pittsburgh','WashU']

for x in sites:
    path2 = '%s/%s/%s_phenotypic.csv'%(path,x,x)
    globals()['dat_%s'%(x)] = pd.read_csv(path2)
    globals()['dat_%s'%(x)]['Site2'] = x
    
frames = [dat_KKI,dat_NYU,dat_NeuroIMAGE,dat_OHSU,dat_Peking_1,dat_Peking_2,
          dat_Peking_3,dat_Pittsburgh,dat_WashU]
bigdat = pd.concat(frames)

npath = '%s/ID_site.csv'%(path)
bigdat.to_csv(npath)

#bigdat.groupby(["Site2", "Gender","DX"]).size()
#exclude sites 7 & 8 - no ADHD
bigdat = bigdat[bigdat['Site'] < 7]
print(bigdat.groupby(["Site2", "Gender","DX"]).size())

Fd = bigdat[bigdat['Gender'] == 0]
Md = bigdat[bigdat['Gender'] == 1]

FAd = Fd[Fd['DX'] > 0].reset_index(drop=True)
MAd = Md[Md['DX'] > 0].reset_index(drop=True)
FCd = Fd[Fd['DX'] == 0].reset_index(drop=True)
MCd = Md[Md['DX'] == 0].reset_index(drop=True)


## load in FA data
fa_dat = pd.DataFrame()
fa_len = []
fa_sub = []
for x in list(range(0,len(FAd))):
    tpath = '%s/%s/%s/snwmrda%s_session_1_rest_1_cc200_TCs.1D '%(path, FAd.loc[x,'Site2'], FAd.loc[x,'ScanDirID'],FAd.loc[x,'ScanDirID'])
    tpath2 = '%s/%s/%s/snwmrda%s_session_1_rest_2_cc200_TCs.1D '%(path, FAd.loc[x,'Site2'], FAd.loc[x,'ScanDirID'],FAd.loc[x,'ScanDirID'])
    tpath3 = '%s/%s/%s/snwmrda%s_session_1_rest_3_cc200_TCs.1D '%(path, FAd.loc[x,'Site2'], FAd.loc[x,'ScanDirID'],FAd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = FAd.loc[x,'ScanDirID']
        tdat2['site'] = FAd.loc[x,'Site2']
        fa_dat = fa_dat.append(tdat2)
        fa_len.append(len(tdat2))
        fa_sub.append(FAd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath2):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = FAd.loc[x,'ScanDirID']
        tdat2['site'] = FAd.loc[x,'Site2']
        fa_dat = fa_dat.append(tdat2)
        fa_len.append(len(tdat2))
        fa_sub.append(FAd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath3):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = FAd.loc[x,'ScanDirID']
        tdat2['site'] = FAd.loc[x,'Site2']
        fa_dat = fa_dat.append(tdat2)
        fa_len.append(len(tdat2))
        fa_sub.append(FAd.loc[x,'ScanDirID'])

## load in FC data
fc_dat = pd.DataFrame()
fc_len = []
fc_sub = []
for x in list(range(0,len(FCd))):
    tpath = '%s/%s/%s/snwmrda%s_session_1_rest_1_cc200_TCs.1D '%(path, FCd.loc[x,'Site2'], FCd.loc[x,'ScanDirID'],FCd.loc[x,'ScanDirID'])
    tpath2 = '%s/%s/%s/snwmrda%s_session_1_rest_2_cc200_TCs.1D '%(path, FCd.loc[x,'Site2'], FCd.loc[x,'ScanDirID'],FCd.loc[x,'ScanDirID'])
    tpath3 = '%s/%s/%s/snwmrda%s_session_1_rest_3_cc200_TCs.1D '%(path, FCd.loc[x,'Site2'], FCd.loc[x,'ScanDirID'],FCd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = FCd.loc[x,'ScanDirID']
        tdat2['site'] = FCd.loc[x,'Site2']
        fc_dat = fc_dat.append(tdat2)
        fc_len.append(len(tdat2))
        fc_sub.append(FCd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath2):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = FCd.loc[x,'ScanDirID']
        tdat2['site'] = FCd.loc[x,'Site2']
        fc_dat = fc_dat.append(tdat2)
        fc_len.append(len(tdat2))
        fc_sub.append(FCd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath3):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = FCd.loc[x,'ScanDirID']
        tdat2['site'] = FCd.loc[x,'Site2']
        fc_dat = fc_dat.append(tdat2)
        fc_len.append(len(tdat2))
        fc_sub.append(FCd.loc[x,'ScanDirID'])

## load in MA data
ma_dat = pd.DataFrame()
ma_len = []
ma_sub = []
for x in list(range(0,len(MAd))):
    tpath = '%s/%s/%s/snwmrda%s_session_1_rest_1_cc200_TCs.1D '%(path, MAd.loc[x,'Site2'], MAd.loc[x,'ScanDirID'],MAd.loc[x,'ScanDirID'])
    tpath2 = '%s/%s/%s/snwmrda%s_session_1_rest_2_cc200_TCs.1D '%(path, MAd.loc[x,'Site2'], MAd.loc[x,'ScanDirID'],MAd.loc[x,'ScanDirID'])
    tpath3 = '%s/%s/%s/snwmrda%s_session_1_rest_3_cc200_TCs.1D '%(path, MAd.loc[x,'Site2'], MAd.loc[x,'ScanDirID'],MAd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = MAd.loc[x,'ScanDirID']
        tdat2['site'] = MAd.loc[x,'Site2']
        ma_dat = ma_dat.append(tdat2)
        ma_len.append(len(tdat2))
        ma_sub.append(MAd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath2):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = MAd.loc[x,'ScanDirID']
        tdat2['site'] = MAd.loc[x,'Site2']
        ma_dat = ma_dat.append(tdat2)
        ma_len.append(len(tdat2))
        ma_sub.append(MAd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath3):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = MAd.loc[x,'ScanDirID']
        tdat2['site'] = MAd.loc[x,'Site2']
        ma_dat = ma_dat.append(tdat2)
        ma_len.append(len(tdat2))
        ma_sub.append(MAd.loc[x,'ScanDirID'])

## load in MC data
mc_dat = pd.DataFrame()
mc_len = []
mc_sub = []
for x in list(range(0,len(MCd))):
    tpath = '%s/%s/%s/snwmrda%s_session_1_rest_1_cc200_TCs.1D '%(path, MCd.loc[x,'Site2'], MCd.loc[x,'ScanDirID'],MCd.loc[x,'ScanDirID'])
    tpath2 = '%s/%s/%s/snwmrda%s_session_1_rest_2_cc200_TCs.1D '%(path, MCd.loc[x,'Site2'], MCd.loc[x,'ScanDirID'],MCd.loc[x,'ScanDirID'])
    tpath3 = '%s/%s/%s/snwmrda%s_session_1_rest_3_cc200_TCs.1D '%(path, MCd.loc[x,'Site2'], MCd.loc[x,'ScanDirID'],MCd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = MCd.loc[x,'ScanDirID']
        tdat2['site'] = MCd.loc[x,'Site2']
        mc_dat = mc_dat.append(tdat2)
        mc_len.append(len(tdat2))
        mc_sub.append(MCd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath2):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = MCd.loc[x,'ScanDirID']
        tdat2['site'] = MCd.loc[x,'Site2']
        mc_dat = mc_dat.append(tdat2)
        mc_len.append(len(tdat2))
        mc_sub.append(MCd.loc[x,'ScanDirID'])
    if os.path.isfile(tpath3):
        tdat = pd.read_table(tpath)
        tdat = tdat.iloc[:,2:]
        tdat2 = pd.DataFrame(zscore(tdat))
        tdat2['partno'] = MCd.loc[x,'ScanDirID']
        tdat2['site'] = MCd.loc[x,'Site2']
        mc_dat = mc_dat.append(tdat2)
        mc_len.append(len(tdat2))
        mc_sub.append(MCd.loc[x,'ScanDirID'])


## write out data
path = 'C:/Users/jel7c5/Desktop/adhd200'

fapath = '%s/concat_timeseries_fa.csv'%(path)
fa_dat.to_csv(fapath)
fa_len = pd.DataFrame(fa_len)
fapath2 = '%s/concat_timeseries_fa_lengths.csv'%(path)
fa_len.to_csv(fapath2)
fapath3 = '%s/concat_timeseries_fa_subs.csv'%(path)
fa_sub = pd.DataFrame(fa_sub)
fa_sub.to_csv(fapath3)

fcpath = '%s/concat_timeseries_fc.csv'%(path)
fc_dat.to_csv(fcpath)
fc_len = pd.DataFrame(fc_len)
fcpath2 = '%s/concat_timeseries_fc_lengths.csv'%(path)
fc_len.to_csv(fcpath2)
fcpath3 = '%s/concat_timeseries_fc_subs.csv'%(path)
fc_sub = pd.DataFrame(fc_sub)
fc_sub.to_csv(fcpath3)

mapath = '%s/concat_timeseries_ma.csv'%(path)
ma_dat.to_csv(mapath)
ma_len = pd.DataFrame(ma_len)
mapath2 = '%s/concat_timeseries_ma_lengths.csv'%(path)
ma_len.to_csv(mapath2)
mapath3 = '%s/concat_timeseries_ma_subs.csv'%(path)
ma_sub = pd.DataFrame(ma_sub)
ma_sub.to_csv(mapath3)

mcpath = '%s/concat_timeseries_mc.csv'%(path)
mc_dat.to_csv(mcpath)
mc_len = pd.DataFrame(mc_len)
mcpath2 = '%s/concat_timeseries_mc_lengths.csv'%(path)
mc_len.to_csv(mcpath2)
mcpath3 = '%s/concat_timeseries_mc_subs.csv'%(path)
mc_sub = pd.DataFrame(mc_sub)
mc_sub.to_csv(mcpath3)

##descriptives
fa_sub.columns = ['a']
fc_sub.columns = ['a']
ma_sub.columns = ['a']
mc_sub.columns = ['a']

print(len(fa_sub.groupby('a').count()))
print(len(fa_sub))

print(len(fc_sub.groupby('a').count()))
print(len(fc_sub))

print(len(ma_sub.groupby('a').count()))
print(len(ma_sub))

print(len(mc_sub.groupby('a').count()))
print(len(mc_sub))

