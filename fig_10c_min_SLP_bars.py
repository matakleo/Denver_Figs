
from all_functions import Extract_by_name,Extract_Track_Data,list_csv_files_0, calculate_distance_error,calculate_intensity_error,calculate_intensity_error_slp
import matplotlib.gridspec as gridspec
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from intes_track_slp_error_function import min_SLP_xkzm , min_SLP_lvls

fig = plt.figure(figsize=(5, 3.3))
gs = gridspec.GridSpec(1,2,figure=fig)
ax1= fig.add_subplot(gs[:,:])

##  WHAT TO SHOW?? ##
# show = 'xkzm' #or 
show = 'lvls'
if show =='xkzm':
    ysu_mrw,ysu_percentile = min_SLP_xkzm('YSU')
    myj_mrw,myj_percentile = min_SLP_xkzm('MYJ')
    xticks=[0.15,1.15,2.15]
    GSS=[r'$C_{k}$_0.2','Default Case',r'$C_{k}$_5.0']
else:
    ysu_mrw,ysu_percentile = min_SLP_lvls('YSU')
    myj_mrw,myj_percentile = min_SLP_lvls('MYJ')
    GSS=[r'$K_{m}$'+'_'+r'$lvl_{4}$',r'$K_{m}$'+'_'+r'$lvl_{6}$','Default Case']
    xticks=[0.15,1.15,2.15]




BarWidth=0.3

ysu_color=['royalblue']
myj_color=['coral']
colors = ['royalblue', 'green', 'black', 'coral', 'orange', 'magenta','yellow']

for i in range(len(ysu_mrw)):
    if i ==0:
        ax1.bar(i,ysu_mrw[i],width=0.3,edgecolor='black',color=ysu_color,yerr=ysu_percentile[i],capsize=5,label='YSU')
        ax1.bar(i+BarWidth,myj_mrw[i],width=0.3,edgecolor='black',hatch='..',color=myj_color,yerr=myj_percentile[i],capsize=5,label='MYJ')
    else:
        ax1.bar(i,ysu_mrw[i],width=0.3,edgecolor='black',color=ysu_color,yerr=ysu_percentile[i],capsize=5,)
        ax1.bar(i+BarWidth,myj_mrw[i],width=0.3,edgecolor='black',color=myj_color,hatch='..',yerr=myj_percentile[i],capsize=5,)

plt.yscale('log')
ax1.set_ylabel('min SLP (mb)',fontsize=12)
# ax2.set_ylabel(r'$MAE_{track}$ (km)',fontsize=15)


ax1.set_xticks(xticks)
ax1.tick_params(axis='both', labelsize=12)

ax1.set_xticklabels(GSS)


ax1.yaxis.grid(True)


circ1 = mpatches.Patch(alpha=0,hatch='xx',label='YSU')
circ2= mpatches.Patch(alpha=0,hatch='..',label='MYJ')
plt.rc('legend',fontsize=13)
lgnd = fig.legend(loc = 'upper center',ncol = 2,frameon = False)



# plt.show()

print('saved as: fig10c_min_SLP_bars_'+show+'.eps')
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig10c_min_SLP_bars_'+show+'.eps',bbox_inches='tight')