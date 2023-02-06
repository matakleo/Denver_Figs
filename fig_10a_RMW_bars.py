
from all_functions import Extract_by_name,Extract_Track_Data,list_csv_files_0, calculate_distance_error,calculate_intensity_error,calculate_intensity_error_slp
import matplotlib.gridspec as gridspec
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from intes_track_slp_error_function import radius_of_max_wind_lvls, radius_of_max_wind_xkzm,max_windsp_xkzm,max_windsp_lvls


os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=18


fig = plt.figure(figsize=(8.5, 3.7),dpi=350)
fig.subplots_adjust(top=0.85)
gs = gridspec.GridSpec(2,2,figure=fig)
# ax1= fig.add_subplot(gs[0:1,0:1])
# ax2=fig.add_subplot(gs[0:1,1:2])
ax3= fig.add_subplot(gs[0:2,0:1])
ax4=fig.add_subplot(gs[0:2,1:2])

##  WHAT TO SHOW?? ##
show = 'xkzm' #or 
# show = 'lvls'     

ysu_mrw_xkzm,ysu_percentile_xkzm = radius_of_max_wind_xkzm('YSU')
myj_mrw_xkzm,myj_percentile_xkzm = radius_of_max_wind_xkzm('MYJ')
ysu_max_wspd_xkzm,ysu_max_wspd_percentile_xkzm = max_windsp_xkzm('YSU')
myj_max_wspd_xkzm,myj_max_wspd_percentile_xkzm = max_windsp_xkzm('MYJ')

GSS_xkzm=[r'$C_{ k }$\_0.2','Default Case',r'$C_{ k }$\_5.0']

ysu_mrw,ysu_percentile = radius_of_max_wind_lvls('YSU')
myj_mrw,myj_percentile = radius_of_max_wind_lvls('MYJ')
ysu_max_wspd,ysu_max_wspd_percentile = max_windsp_lvls('YSU')
myj_max_wspd,myj_max_wspd_percentile = max_windsp_lvls('MYJ')
GSS=[r'$K_{ m }\_lvl_{ 4 }$',r'$K_{ m }\_lvl_{ 6 }$','Default Case']
xticks=[0.15,1.15,2.15]




BarWidth=0.3

ysu_color=['royalblue']
myj_color=['coral']
colors = ['royalblue', 'green', 'black', 'coral', 'orange', 'magenta','yellow']

for i in range(len(ysu_mrw)):
    if i==0:
        ax3.bar(i,ysu_max_wspd_xkzm[i],width=0.3,edgecolor='black',color=ysu_color,yerr=ysu_max_wspd_percentile_xkzm[i],capsize=5,label='YSU')
        ax3.bar(i+BarWidth,myj_max_wspd_xkzm[i],width=0.3,edgecolor='black',hatch='..',color=myj_color,yerr=myj_max_wspd_percentile_xkzm[i],capsize=5,label='MYJ')
    else:

        ax3.bar(i,ysu_max_wspd_xkzm[i],width=0.3,edgecolor='black',color=ysu_color,yerr=ysu_max_wspd_percentile_xkzm[i],capsize=5,)
        ax3.bar(i+BarWidth,myj_max_wspd_xkzm[i],width=0.3,edgecolor='black',hatch='..',color=myj_color,yerr=myj_max_wspd_percentile_xkzm[i],capsize=5,)
       

    ax4.bar(i,ysu_mrw_xkzm[i],width=0.3,edgecolor='black',color=ysu_color,yerr=ysu_percentile_xkzm[i],capsize=5,)
    ax4.bar(i+BarWidth,myj_mrw_xkzm[i],width=0.3,edgecolor='black',color=myj_color,hatch='..',yerr=myj_percentile_xkzm[i],capsize=5,)

    

ax4.annotate('RMW (km)', xy=(-0.1, 0.70), xycoords='axes fraction',
                    xytext=(0, 0), textcoords='offset points',
                    ha="right", va="top",size=size,
                    rotation = 90
                    )
                    
ax3.annotate(r'Average max wind intensity \\ \hspace*{2.5cm} $\mathrm{(\,ms^{-1}) \,}$', xy=(-0.1, 1), xycoords='axes fraction',
                    xytext=(0, 0), textcoords='offset points',
                    ha="right", va="top",size=size,
                    rotation = 90
                    )
# ax2.set_ylabel('RMW [km]',fontsize=12)
# ax1.set_ylabel('Avg max wind intensity [m/s]',fontsize=12)




ax3.set_xticks(xticks)
ax3.tick_params(axis='both', labelsize=size)
ax3.set_xticklabels(GSS_xkzm)
ax3.yaxis.grid(True)
ax3.set_axisbelow(True)

ax4.set_xticks(xticks)
ax4.tick_params(axis='both', labelsize=size)
ax4.set_xticklabels(GSS_xkzm)
ax4.yaxis.grid(True)
ax4.set_axisbelow(True)

circ1 = mpatches.Patch(alpha=0,hatch='xx',label='YSU')
circ2= mpatches.Patch(alpha=0,hatch='..',label='MYJ')
plt.rc('legend',fontsize=size)
lgnd = fig.legend(loc = 'upper center',ncol = 2,frameon = False)



# plt.show()
# print('saved as: fig10_RMW_bars.eps')
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Poster_figs/created_figs/rmw_bars_poster.pdf',bbox_inches='tight')