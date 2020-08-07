

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



############### Load data
path = 'C:/Users/jel7c5/Desktop/adhd200_analyses'

state1 = pd.read_csv('%s/state1_map.csv'%(path))
state2 = pd.read_csv('%s/state2_map.csv'%(path))
state3 = pd.read_csv('%s/state3_map.csv'%(path))
state4 = pd.read_csv('%s/state4_map.csv'%(path))
state5 = pd.read_csv('%s/state5_map.csv'%(path))

del(state1['Unnamed: 0'], state2['Unnamed: 0'],
    state3['Unnamed: 0'], state4['Unnamed: 0'],
    state5['Unnamed: 0'])

state1x = state1.values[0]
state2x = state2.values[0]
state3x = state3.values[0]
state4x = state4.values[0]
state5x = state5.values[0]


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
state1x_norm = normalize(state1x[:,np.newaxis], axis=0).ravel()
state2x_norm = normalize(state2x[:,np.newaxis], axis=0).ravel()
state3x_norm = normalize(state3x[:,np.newaxis], axis=0).ravel()
state4x_norm = normalize(state4x[:,np.newaxis], axis=0).ravel()
state5x_norm = normalize(state5x[:,np.newaxis], axis=0).ravel()



################## make maps
LOstate1 = data.astype(float)
temp0state1 = pd.DataFrame({'label': labellist,'value': state1x_norm})
for x in list(range(0,len(temp0state1))):
    LOstate1[LOstate1==temp0state1.label[x]] = temp0state1.value[x]
atlas_0state1 = nib.Nifti1Image(LOstate1, atlas_filename.affine, atlas_filename.header)

LOstate2 = data.astype(float)
temp0state2 = pd.DataFrame({'label': labellist,'value': state2x_norm})
for x in list(range(0,len(temp0state2))):
    LOstate2[LOstate2==temp0state2.label[x]] = temp0state2.value[x]
atlas_0state2 = nib.Nifti1Image(LOstate2, atlas_filename.affine, atlas_filename.header)

LOstate3 = data.astype(float)
temp0state3 = pd.DataFrame({'label': labellist,'value': state3x_norm})
for x in list(range(0,len(temp0state3))):
    LOstate3[LOstate3==temp0state3.label[x]] = temp0state3.value[x]
atlas_0state3 = nib.Nifti1Image(LOstate3, atlas_filename.affine, atlas_filename.header)

LOstate4 = data.astype(float)
temp0state4 = pd.DataFrame({'label': labellist,'value': state4x_norm})
for x in list(range(0,len(temp0state4))):
    LOstate4[LOstate4==temp0state4.label[x]] = temp0state4.value[x]
atlas_0state4 = nib.Nifti1Image(LOstate4, atlas_filename.affine, atlas_filename.header)

LOstate5 = data.astype(float)
temp0state5 = pd.DataFrame({'label': labellist,'value': state5x_norm})
for x in list(range(0,len(temp0state5))):
    LOstate5[LOstate5==temp0state5.label[x]] = temp0state5.value[x]
atlas_0state5 = nib.Nifti1Image(LOstate5, atlas_filename.affine, atlas_filename.header)

fsaverage = datasets.fetch_surf_fsaverage('fsaverage')



####### Plot state 1
texturestate1_l = surface.vol_to_surf(atlas_0state1, fsaverage.pial_left)
texturestate1_r = surface.vol_to_surf(atlas_0state1, fsaverage.pial_right)

fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate1_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate1_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate1_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .084,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate1_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .084,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()


####### Plot state 2
texturestate2_l = surface.vol_to_surf(atlas_0state2, fsaverage.pial_left)
texturestate2_r = surface.vol_to_surf(atlas_0state2, fsaverage.pial_right)

fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate2_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate2_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate2_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .084,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate2_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .084,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

####### Plot state 3
texturestate3_l = surface.vol_to_surf(atlas_0state3, fsaverage.pial_left)
texturestate3_r = surface.vol_to_surf(atlas_0state3, fsaverage.pial_right)

fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate3_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate3_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate3_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .084,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate3_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .084,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

####### Plot state 4
texturestate4_l = surface.vol_to_surf(atlas_0state4, fsaverage.pial_left)
texturestate4_r = surface.vol_to_surf(atlas_0state4, fsaverage.pial_right)

fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate4_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate4_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate4_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .084,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate4_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .084,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

####### Plot state 5
texturestate5_l = surface.vol_to_surf(atlas_0state5, fsaverage.pial_left)
texturestate5_r = surface.vol_to_surf(atlas_0state5, fsaverage.pial_right)

fig, axs = plt.subplots(ncols=4,nrows=1, subplot_kw={'projection': '3d'}, figsize=(22,5))
fig.tight_layout()
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate5_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[0])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate5_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'lateral', threshold = .084,
                            colorbar = False, axes = axs[1])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_left, stat_map = texturestate5_l,
                            bg_map = fsaverage.sulc_left, hemi = 'left',
                            view = 'medial', threshold = .084,
                            colorbar = False, axes = axs[2])
plotting.plot_surf_stat_map(surf_mesh = fsaverage.infl_right, stat_map = texturestate5_r,
                            bg_map = fsaverage.sulc_right, hemi = 'right',
                            view = 'medial', threshold = .084,
                            colorbar = True, axes = axs[3])
plt.subplots_adjust(hspace = 0.01, wspace = 0.01)
plt.show()

