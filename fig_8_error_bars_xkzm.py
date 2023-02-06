from all_functions import Extract_by_name,Extract_Track_Data,list_csv_files_0, calculate_distance_error,calculate_intensity_error,calculate_intensity_error_slp
import matplotlib.gridspec as gridspec
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from intes_track_slp_error_function import gimme_errors_tribars_lvls,gimme_errors_tribars_xkzm

fig = plt.figure(figsize=(10, 6.5))

###FOR FATEME THIS IS IMPORTANT: HERE YOU HAVE TO ADD THIS TO YOUR PATH ###

os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})

###FOR FATEME THIS IS IMPORTANT: HERE YOU HAVE TO ADD THIS TO YOUR PATH ###



size=14
gs = gridspec.GridSpec(2,3,figure=fig,wspace=0.265,hspace=0.30)
ax1= fig.add_subplot(gs[0:1,0:1])
ax2= fig.add_subplot(gs[0:1,1:2])
ax3=fig.add_subplot(gs[0:1,2:3])

ax4= fig.add_subplot(gs[1:2,0:1])
ax5= fig.add_subplot(gs[1:2,1:2])
ax6= fig.add_subplot(gs[1:2,2:3])




ysu_intensities_lvls,ysu_track_lvls,ysu_slp_lvls,wind_percentile_ysu_lvls,track_percentile_ysu_lvls, slp_percentile_ysu_lvls = gimme_errors_tribars_xkzm('YSU')
myj_intensities_lvls,myj_track_lvls,myj_slp_lvls,wind_percentile_myj_lvls,track_percentile_myj_lvls,slp_percentile_myj_lvls = gimme_errors_tribars_xkzm('MYJ')


# print(slp_percentile_myj_lvls)
# print(myj_intensities_lvls)
BarWidth=0
column_width=2.5
LVLS=[r'$C_{ k }$\_0.2','Default Case',r'$C_{ k }$\_5.0']
colors = ['royalblue', 'grey', 'red', 'orange', 'magenta','yellow']

for i in range(len(ysu_intensities_lvls[0])):

    ax1.bar(i+BarWidth,ysu_intensities_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=wind_percentile_ysu_lvls[i],capsize=5,label=LVLS[i])
    ax4.bar(i+BarWidth,myj_intensities_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=wind_percentile_myj_lvls[i],capsize=5)
    ax2.bar(i+BarWidth,ysu_track_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=track_percentile_ysu_lvls[i],capsize=5)
    ax3.bar(i+BarWidth,ysu_slp_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=slp_percentile_ysu_lvls[i],capsize=5)
    ax5.bar(i+BarWidth,myj_track_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=track_percentile_myj_lvls[i],capsize=5)
    ax6.bar(i+BarWidth,myj_slp_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=slp_percentile_myj_lvls[i],capsize=5)
    BarWidth+=column_width
    print(myj_slp_lvls[0][i])
    




bbox_args = dict(boxstyle="round4", fc="0.9")
arrow_args = dict(arrowstyle="->")

ax1.annotate('a)', xy=(0.12, 0.95), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=size,
             bbox=bbox_args,
             )
ax2.annotate('b)', xy=(0.11, 0.95), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=size,
             bbox=bbox_args,
             )
ax3.annotate('c)', xy=(0.115, 0.95), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=size,
             bbox=bbox_args,
             )
            #TITLE1
ax2.annotate('YSU', xy=(0.5, 1.2), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=22,
             
             )

ax4.annotate('d)', xy=(0.125, 0.95), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=size,
             bbox=bbox_args,
             )
ax5.annotate('e)', xy=(0.11, 0.95), xycoords='axes fraction',
             xytext=(00, 0), textcoords='offset points',
             ha="right", va="top",size=size,
             bbox=bbox_args,
             )

             #Title1#
ax5.annotate('MYJ', xy=(0.5, 1.2), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=22,
             
             )
    
ax6.annotate('f)', xy=(0.12, 0.95), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=size,
             bbox=bbox_args,
             )


ax1.set_xticks([])
ax2.set_xticks([])
ax3.set_xticks([])
ax4.set_xticks([])
ax5.set_xticks([])
ax6.set_xticks([])

#### FATEME HERE IS THE LABELING, THE WAY YOU HAVE TO WRITE IT ###
ax1.set_ylabel(r'$MAPE_{ intensity }$(\,\%) \,',fontsize=size,labelpad=-0.2)
ax2.set_ylabel(r'$MAE_{ track }$(\,km) \,',fontsize=size,labelpad=-0.2)
ax3.set_ylabel(r'$MAE_{ SLP }$(\,mb) \,',fontsize=size,labelpad=-0.2)

ax4.set_ylabel(r'$MAPE_{ intensity }$(\,\%) \,',fontsize=size,labelpad=-0.2)
ax5.set_ylabel(r'$MAE_{ track }$(\,km) \,',fontsize=size,labelpad=-0.2)
ax6.set_ylabel(r'$MAE_{ SLP }$(\,mb) \,',fontsize=size,labelpad=-0.2)

ax5.set_ylim(0)


ax1.yaxis.grid(True)
ax2.yaxis.grid(True)
ax3.yaxis.grid(True)
ax4.yaxis.grid(True)
ax5.yaxis.grid(True)
ax6.yaxis.grid(True)
ax1.set_axisbelow(True)
ax2.set_axisbelow(True)
ax3.set_axisbelow(True)
ax4.set_axisbelow(True)
ax4.set_axisbelow(True)
ax5.set_axisbelow(True)
ax6.set_axisbelow(True)


# circ1 = mpatches.Patch(alpha=0,hatch='xx',label='YSU')
# circ2= mpatches.Patch(alpha=0,hatch='..',label='MYJ')
# plt.rc('legend',fontsize=20)
lgnd = fig.legend(loc = 'lower center',ncol = 3,frameon = False, fontsize=size)



# plt.show()

# plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig8b_error_bars_xkzm.eps',bbox_inches='tight')