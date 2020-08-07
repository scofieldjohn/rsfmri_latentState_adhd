

import numpy as np
from sklearn.externals import joblib
np.random.seed(42)
import pandas as pd
import nibabel as nib
from nilearn import plotting
import numpy as np
from sklearn.preprocessing import normalize
from nilearn import surface
import matplotlib.pylab as plt
from nilearn import datasets

opath = 'C:/Users/jel7c5/Desktop/adhd200'


#### general note
#orig clust	
#1	  5	  fa
#2	  2	  fa
#3	  4	  fa
#4	  3	  fa
#5	  1	  fa
#1	  4	  fc
#2	  1	  fc
#3	  3	  fc
#4	  2	  fc
#5	  5	  fc
#1	  3	  ma
#2	  1	  ma
#3	  5	  ma
#4	  2	  ma
#5	  4	  ma
#1	  4	  mc
#2	  5	  mc
#3	  3	  mc
#4	  2	  mc
#5	  1	  mc


############### Load data
################################### load in overall HMM models
picklepath = '%s/hmm2_model_pickle_fa.pkl'%(opath)
fa_mod = joblib.load(picklepath)
fa_means = fa_mod.means_

picklepath = '%s/hmm2_model_pickle_fc.pkl'%(opath)
fc_mod = joblib.load(picklepath)
fc_means = fc_mod.means_

picklepath = '%s/hmm2_model_pickle_ma.pkl'%(opath)
ma_mod = joblib.load(picklepath)
ma_means = ma_mod.means_

picklepath = '%s/hmm2_model_pickle_mc.pkl'%(opath)
mc_mod = joblib.load(picklepath)
mc_means = mc_mod.means_



atpath = 'C:/Users/jel7c5/Desktop/adhd200/ADHD200_parcellate_200.nii.gz'
atlas_filename = nib.load(atpath)
atlas_filename.affine
atlas_filename.header
data = atlas_filename.get_data()

labellist = np.concatenate(([1,3,4,6,7,8,9,10],
                            list(range(12,25)),
                            list(range(26,34)),
                            list(range(35,68)),
                            list(range(69,82)),
                            list(range(83,95)),
                            list(range(96,126)),
                            list(range(127,191)),
                            list(range(192,201))
                            ), axis = 0)


################## make fa maps
fas1 = data.astype(float)
tfas1 = pd.DataFrame({'label': labellist,'value': fa_means[0]})
for x in list(range(0,len(tfas1))):
    fas1[fas1==tfas1.label[x]] = tfas1.value[x]
atlas_fas1 = nib.Nifti1Image(fas1, atlas_filename.affine, atlas_filename.header)

fas2 = data.astype(float)
tfas2 = pd.DataFrame({'label': labellist,'value': fa_means[1]})
for x in list(range(0,len(tfas2))):
    fas2[fas2==tfas2.label[x]] = tfas2.value[x]
atlas_fas2 = nib.Nifti1Image(fas2, atlas_filename.affine, atlas_filename.header)

fas3 = data.astype(float)
tfas3 = pd.DataFrame({'label': labellist,'value': fa_means[2]})
for x in list(range(0,len(tfas3))):
    fas3[fas3==tfas3.label[x]] = tfas3.value[x]
atlas_fas3 = nib.Nifti1Image(fas3, atlas_filename.affine, atlas_filename.header)

fas4 = data.astype(float)
tfas4 = pd.DataFrame({'label': labellist,'value': fa_means[3]})
for x in list(range(0,len(tfas4))):
    fas4[fas4==tfas4.label[x]] = tfas4.value[x]
atlas_fas4 = nib.Nifti1Image(fas4, atlas_filename.affine, atlas_filename.header)

fas5 = data.astype(float)
tfas5 = pd.DataFrame({'label': labellist,'value': fa_means[4]})
for x in list(range(0,len(tfas5))):
    fas5[fas5==tfas5.label[x]] = tfas5.value[x]
atlas_fas5 = nib.Nifti1Image(fas5, atlas_filename.affine, atlas_filename.header)

################## make fc maps
fcs1 = data.astype(float)
tfcs1 = pd.DataFrame({'label': labellist,'value': fc_means[0]})
for x in list(range(0,len(tfcs1))):
    fcs1[fcs1==tfcs1.label[x]] = tfcs1.value[x]
atlas_fcs1 = nib.Nifti1Image(fcs1, atlas_filename.affine, atlas_filename.header)

fcs2 = data.astype(float)
tfcs2 = pd.DataFrame({'label': labellist,'value': fc_means[1]})
for x in list(range(0,len(tfcs2))):
    fcs2[fcs2==tfcs2.label[x]] = tfcs2.value[x]
atlas_fcs2 = nib.Nifti1Image(fcs2, atlas_filename.affine, atlas_filename.header)

fcs3 = data.astype(float)
tfcs3 = pd.DataFrame({'label': labellist,'value': fc_means[2]})
for x in list(range(0,len(tfcs3))):
    fcs3[fcs3==tfcs3.label[x]] = tfcs3.value[x]
atlas_fcs3 = nib.Nifti1Image(fcs3, atlas_filename.affine, atlas_filename.header)

fcs4 = data.astype(float)
tfcs4 = pd.DataFrame({'label': labellist,'value': fc_means[3]})
for x in list(range(0,len(tfcs4))):
    fcs4[fcs4==tfcs4.label[x]] = tfcs4.value[x]
atlas_fcs4 = nib.Nifti1Image(fcs4, atlas_filename.affine, atlas_filename.header)

fcs5 = data.astype(float)
tfcs5 = pd.DataFrame({'label': labellist,'value': fc_means[4]})
for x in list(range(0,len(tfcs5))):
    fcs5[fcs5==tfcs5.label[x]] = tfcs5.value[x]
atlas_fcs5 = nib.Nifti1Image(fcs5, atlas_filename.affine, atlas_filename.header)

################## make ma maps
mas1 = data.astype(float)
tmas1 = pd.DataFrame({'label': labellist,'value': ma_means[0]})
for x in list(range(0,len(tmas1))):
    mas1[mas1==tmas1.label[x]] = tmas1.value[x]
atlas_mas1 = nib.Nifti1Image(mas1, atlas_filename.affine, atlas_filename.header)

mas2 = data.astype(float)
tmas2 = pd.DataFrame({'label': labellist,'value': ma_means[1]})
for x in list(range(0,len(tmas2))):
    mas2[mas2==tmas2.label[x]] = tmas2.value[x]
atlas_mas2 = nib.Nifti1Image(mas2, atlas_filename.affine, atlas_filename.header)

mas3 = data.astype(float)
tmas3 = pd.DataFrame({'label': labellist,'value': ma_means[2]})
for x in list(range(0,len(tmas3))):
    mas3[mas3==tmas3.label[x]] = tmas3.value[x]
atlas_mas3 = nib.Nifti1Image(mas3, atlas_filename.affine, atlas_filename.header)

mas4 = data.astype(float)
tmas4 = pd.DataFrame({'label': labellist,'value': ma_means[3]})
for x in list(range(0,len(tmas4))):
    mas4[mas4==tmas4.label[x]] = tmas4.value[x]
atlas_mas4 = nib.Nifti1Image(mas4, atlas_filename.affine, atlas_filename.header)

mas5 = data.astype(float)
tmas5 = pd.DataFrame({'label': labellist,'value': ma_means[4]})
for x in list(range(0,len(tmas5))):
    mas5[mas5==tmas5.label[x]] = tmas5.value[x]
atlas_mas5 = nib.Nifti1Image(mas5, atlas_filename.affine, atlas_filename.header)

################## make mc maps
mcs1 = data.astype(float)
tmcs1 = pd.DataFrame({'label': labellist,'value': mc_means[0]})
for x in list(range(0,len(tmcs1))):
    mcs1[mcs1==tmcs1.label[x]] = tmcs1.value[x]
atlas_mcs1 = nib.Nifti1Image(mcs1, atlas_filename.affine, atlas_filename.header)

mcs2 = data.astype(float)
tmcs2 = pd.DataFrame({'label': labellist,'value': mc_means[1]})
for x in list(range(0,len(tmcs2))):
    mcs2[mcs2==tmcs2.label[x]] = tmcs2.value[x]
atlas_mcs2 = nib.Nifti1Image(mcs2, atlas_filename.affine, atlas_filename.header)

mcs3 = data.astype(float)
tmcs3 = pd.DataFrame({'label': labellist,'value': mc_means[2]})
for x in list(range(0,len(tmcs3))):
    mcs3[mcs3==tmcs3.label[x]] = tmcs3.value[x]
atlas_mcs3 = nib.Nifti1Image(mcs3, atlas_filename.affine, atlas_filename.header)

mcs4 = data.astype(float)
tmcs4 = pd.DataFrame({'label': labellist,'value': mc_means[3]})
for x in list(range(0,len(tmcs4))):
    mcs4[mcs4==tmcs4.label[x]] = tmcs4.value[x]
atlas_mcs4 = nib.Nifti1Image(mcs4, atlas_filename.affine, atlas_filename.header)

mcs5 = data.astype(float)
tmcs5 = pd.DataFrame({'label': labellist,'value': mc_means[4]})
for x in list(range(0,len(tmcs5))):
    mcs5[mcs5==tmcs5.label[x]] = tmcs5.value[x]
atlas_mcs5 = nib.Nifti1Image(mcs5, atlas_filename.affine, atlas_filename.header)





fsaverage = datasets.fetch_surf_fsaverage('fsaverage')


#########################################################################################################

###################################### Plot state 1
### FA5; FC2; MA2; MC5

## FA5 DONE
textL = surface.vol_to_surf(atlas_fas5, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fas5, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## FC2 DONE
textL = surface.vol_to_surf(atlas_fcs2, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fcs2, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MA2 DONE
textL = surface.vol_to_surf(atlas_mas2, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mas2, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MC5 DONE
textL = surface.vol_to_surf(atlas_mcs5, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mcs5, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

###################################### Plot state 2
### FA2; FC4; MA4; MC4

## FA2 DONE
textL = surface.vol_to_surf(atlas_fas2, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fas2, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## FC4 DONE
textL = surface.vol_to_surf(atlas_fcs4, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fcs4, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MA4 DONE
textL = surface.vol_to_surf(atlas_mas4, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mas4, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MC4 DONE
textL = surface.vol_to_surf(atlas_mcs4, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mcs4, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

###################################### Plot state 3
### FA4; FC3; MA1; MC3

## FA4 DONE
textL = surface.vol_to_surf(atlas_fas4, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fas4, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## FC3 DONE
textL = surface.vol_to_surf(atlas_fcs3, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fcs3, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MA1 DONE
textL = surface.vol_to_surf(atlas_mas1, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mas1, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MC3 DONE
textL = surface.vol_to_surf(atlas_mcs3, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mcs3, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

###################################### Plot state 4
### FA3; FC1; MA5; MC1

## FA3 DONE
textL = surface.vol_to_surf(atlas_fas3, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fas3, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## FC1 DONE
textL = surface.vol_to_surf(atlas_fcs1, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fcs1, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MA5 DONE
textL = surface.vol_to_surf(atlas_mas5, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mas5, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MC1 DONE
textL = surface.vol_to_surf(atlas_mcs1, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mcs1, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()


###################################### Plot state 5
### FA1; FC5; MA3; MC2

## FA1 DONE
textL = surface.vol_to_surf(atlas_fas1, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fas1, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## FC5 DONE
textL = surface.vol_to_surf(atlas_fcs5, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_fcs5, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MA3 DONE
textL = surface.vol_to_surf(atlas_mas3, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mas3, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

## MC2 DONE
textL = surface.vol_to_surf(atlas_mcs2, fsaverage.pial_left)
textR = surface.vol_to_surf(atlas_mcs2, fsaverage.pial_right)
fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .20,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = textL,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .20,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = textR,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .20,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()


