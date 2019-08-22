# -*- coding: utf-8 -*-

__author__      = "Leidinice Silva"
__email__       = "leidinicesilva@gmail.com"
__date__        = "12/26/2018"
__description__ = "This script plot climatology graphics from Rec_EXP models end OBS basedata"


import os
import netCDF4
import statistics
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib as mpl

# mpl.use('agg')

from pylab import *
from netCDF4 import Dataset
from sklearn import metrics
from scipy.stats import norm
from matplotlib.font_manager import FontProperties


def import_sim(exp):
	
	param = 'pr' # pr or tas
	area  = 'amz_neb' # amz or neb
	date  = '2001-2010'

	path  = '/home/nice/Documents/ufrn/papers/regcm_pbl/datas'
	arq   = '{0}/{1}_{2}_{3}_mon_{4}.nc'.format(path, param, area, exp, date)	
	
	data  = netCDF4.Dataset(arq)
	var   = data.variables[param][:] 
	lat   = data.variables['lat'][:]
	lon   = data.variables['lon'][:]
	value = var[:][:,:,:]

	exp_mdl = np.nanmean(np.nanmean(value, axis=1), axis=1)

	mdl_clim = []
	for mon in range(1, 12 + 1):
		mdl = np.nanmean(exp_mdl[mon::12], axis=0)
		mdl_clim.append(mdl)

	return mdl_clim


def import_obs(obs):
	
	param = 'precip' # precip, pre or tmp
	area  = 'amz_neb' # amz or neb
	date  = '2001-2010'

	path  = '/home/nice/Documents/ufrn/papers/regcm_pbl/datas'
	arq   = '{0}/{1}_{2}_{3}_mon_{4}.nc'.format(path, param, area, obs, date)	
		
	data  = netCDF4.Dataset(arq)
	var   = data.variables[param][:] 
	lat   = data.variables['lat'][:]
	lon   = data.variables['lon'][:]
	value = var[:][:,:,:]

	obs_data = np.nanmean(np.nanmean(value, axis=1), axis=1)

	obs_clim = []
	for mon in range(1, 12 + 1):
		obs = np.nanmean(obs_data[mon::12], axis=0)
		obs_clim.append(obs)
	
	return obs_clim
	              
               
# Import regcm exps model end obs database climatology
exp  = u'regcm_exp1'
exp1_clim = import_sim(exp)
		
exp  = u'regcm_exp2'
exp2_clim = import_sim(exp)

obs  = u'gpcp_v2.2_obs'
obs_clim = import_obs(obs)

median_exp1=statistics.median(exp1_clim)
median_exp2=statistics.median(exp2_clim)
median_obs=statistics.median(obs_clim)

# Plot model end obs data climatology
fig = plt.figure()
time = np.arange(1, 13)
bar_width = .30

# Subplot one
plt.subplot(311)
plt_clim1 = plt.bar(time, exp1_clim, alpha=0.8, color='blue', label='Reg_Exp1', width = 0.25, edgecolor='black')
plt_clim2 = plt.bar(time + .30, exp2_clim, alpha=0.8, color='red', label='Reg_Exp2', width = 0.25, edgecolor='black')
plt_clim3 = plt.bar(time + .60, obs_clim, alpha=0.8, color='black', label='GPCP', width = 0.25, edgecolor='black')

plt.axhline(median_exp1, linewidth=1, linestyle='dashed', color='blue', alpha=0.8)
plt.axhline(median_exp2, linewidth=1, linestyle='dashed', color='red', alpha=0.8)
plt.axhline(median_obs, linewidth=1, linestyle='dashed', color='black', alpha=0.8)
plt.ylabel('Precipitação (mm)', fontsize=8, fontweight='bold')
plt.title('Climatologia de Precipitação (2001-2010)', fontsize=8, fontweight='bold')
plt.text(0.5, 10, u'A) NAMZ', fontsize=8, fontweight='bold')
plt.xticks(time + .30, ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'))
plt.yticks(np.arange(0, 14, 2))
plt.legend(loc='upper center', shadow=True, ncol=3, prop=FontProperties(size=8))
plt.tick_params(axis='both', which='major', labelsize=8, length=5, width=1.5, pad=1.5, labelcolor='black')

# Subplot two
plt.subplot(312)
plt_clim1 = plt.bar(time, exp1_clim, alpha=0.8, color='blue', label='Reg_Exp1', width = 0.25, edgecolor='black')
plt_clim2 = plt.bar(time + .30, exp2_clim, alpha=0.8, color='red', label='Reg_Exp2', width = 0.25, edgecolor='black')
plt_clim3 = plt.bar(time + .60, obs_clim, alpha=0.8, color='black', label='GPCP', width = 0.25, edgecolor='black')

plt.axhline(median_exp1, linewidth=1, linestyle='dashed', color='blue', alpha=0.8)
plt.axhline(median_exp2, linewidth=1, linestyle='dashed', color='red', alpha=0.8)
plt.axhline(median_obs, linewidth=1, linestyle='dashed', color='black', alpha=0.8)
plt.ylabel('Precipitação (mm)', fontsize=8, fontweight='bold')
plt.text(0.5, 10, u'B) SAMZ', fontsize=8, fontweight='bold')
plt.xticks(time + .30, ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'))
plt.yticks(np.arange(0, 14, 2))
plt.tick_params(axis='both', which='major', labelsize=8, length=5, width=1.5, pad=1.5, labelcolor='black')

# Subplot three
plt.subplot(313)
plt_clim1 = plt.bar(time, exp1_clim, alpha=0.8, color='blue', label='Reg_Exp1', width = 0.25, edgecolor='black')
plt_clim2 = plt.bar(time + .30, exp2_clim, alpha=0.8, color='red', label='Reg_Exp2', width = 0.25, edgecolor='black')
plt_clim3 = plt.bar(time + .60, obs_clim, alpha=0.8, color='black', label='GPCP', width = 0.25, edgecolor='black')

plt.axhline(median_exp1, linewidth=1, linestyle='dashed', color='blue', alpha=0.8)
plt.axhline(median_exp2, linewidth=1, linestyle='dashed', color='red', alpha=0.8)
plt.axhline(median_obs, linewidth=1, linestyle='dashed', color='black', alpha=0.8)
plt.xlabel('Meses', fontsize=8, fontweight='bold')
plt.text(0.5, 10, u'C) NEB', fontsize=8, fontweight='bold')
plt.ylabel('Precipitação (mm)', fontsize=8, fontweight='bold')
plt.xticks(time + .30, ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'))
plt.yticks(np.arange(0, 14, 2))
plt.tick_params(axis='both', which='major', labelsize=8, length=5, width=1.5, pad=1.5, labelcolor='black')

# Path out to save figure
path_out = '/home/nice/Documents/ufrn/papers/regcm_pbl/results'
name_out = 'pyplt_clim_pr_regcm_pbl_obs_2001-2010.png'
if not os.path.exists(path_out):
	create_path(path_out)
plt.savefig(os.path.join(path_out, name_out), dpi=400, bbox_inches='tight')

plt.show()
exit()





