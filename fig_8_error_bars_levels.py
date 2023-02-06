from all_functions import Extract_by_name,Extract_Track_Data,list_csv_files_0, calculate_distance_error,calculate_intensity_error,calculate_intensity_error_slp
import matplotlib.gridspec as gridspec
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from intes_track_slp_error_function import gimme_errors_tribars_fixes_HBLS,gimme_errors_tribars_lvls,gimme_errors_tribars_xkzm

os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=18
fig = plt.figure(figsize=(15.0, 13))
# plt.rcParams['figure.constrained_layout.use'] = True
gs0 = gridspec.GridSpec(29,3,figure=fig,wspace=0.237,hspace=17)
# fig.tight_layout()
# gs00 = gs0[0].subgridspec(2, 3)
# gs01 = gs0[1].subgridspec(2, 3)
ax1= fig.add_subplot(gs0[1:9,0:1])
ax2= fig.add_subplot(gs0[1:9,1:2])
ax3=fig.add_subplot(gs0[1:9,2:3])

ax4= fig.add_subplot(gs0[10:18,0:1])
ax5= fig.add_subplot(gs0[10:18,1:2])
ax6= fig.add_subplot(gs0[10:18,2:3])

ax7= fig.add_subplot(gs0[21:29,0:1])
ax8= fig.add_subplot(gs0[21:29,1:2])
ax9= fig.add_subplot(gs0[21:29,2:3])


ysu_intensities_fixed,ysu_track_fixed,ysu_slp_fixed,wind_percentile_ysu_fixed,track_percentile_ysu_fixed, slp_percentile_ysu_fixed, avg_def_pblh = gimme_errors_tribars_fixes_HBLS('YSU')
ysu_intensities_lvls,ysu_track_lvls,ysu_slp_lvls,wind_percentile_ysu_lvls,track_percentile_ysu_lvls, slp_percentile_ysu_lvls = gimme_errors_tribars_lvls('YSU')
myj_intensities_lvls,myj_track_lvls,myj_slp_lvls,wind_percentile_myj_lvls,track_percentile_myj_lvls,slp_percentile_myj_lvls = gimme_errors_tribars_lvls('MYJ')

BarWidth=0
column_width=1.5
FIXED_HGHT=['PBL height = 250m','Default case (Average YSU PBL height = 409m)','PBL height = 1000m']
LVLS=[r'$K_{ m }\_lvl_{ 4 }$',r'$K_{ m }\_lvl_{ 6 }$','Default Case']
colors_fixed_hght=['darkturquoise','grey','brown']
colors = ['royalblue', 'green', 'grey', 'red', 'orange', 'magenta','yellow']

for i in range(len(ysu_intensities_lvls[0])):

    ax1.bar(i+BarWidth,ysu_intensities_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=wind_percentile_ysu_lvls[i],capsize=5,label=LVLS[i])
    ax7.bar(i+BarWidth,myj_intensities_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=wind_percentile_myj_lvls[i],capsize=5)
    ax2.bar(i+BarWidth,ysu_track_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=track_percentile_ysu_lvls[i],capsize=5)
    ax3.bar(i+BarWidth,ysu_slp_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=slp_percentile_ysu_lvls[i],capsize=5)
    ax8.bar(i+BarWidth,myj_track_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=track_percentile_myj_lvls[i],capsize=5)
    ax9.bar(i+BarWidth,myj_slp_lvls[0][i],width=column_width,edgecolor='black',color=colors[i],yerr=slp_percentile_myj_lvls[i],capsize=5)
    
    if i != 1:
        ax4.bar(i+BarWidth,ysu_intensities_fixed[0][i],hatch="\\\\", width=column_width,edgecolor='black',color=colors_fixed_hght[i],yerr=wind_percentile_ysu_fixed[i],capsize=5,label=FIXED_HGHT[i])
        ax5.bar(i+BarWidth,ysu_track_fixed[0][i],hatch="\\\\",width=column_width,edgecolor='black',color=colors_fixed_hght[i],yerr=track_percentile_ysu_fixed[i],capsize=5)
        ax6.bar(i+BarWidth,ysu_slp_fixed[0][i],hatch="\\\\",width=column_width,edgecolor='black',color=colors_fixed_hght[i],yerr=slp_percentile_ysu_fixed[i],capsize=5)
    else:
        ax4.bar(i+BarWidth,ysu_intensities_fixed[0][i], width=column_width,edgecolor='black',color=colors_fixed_hght[i],yerr=wind_percentile_ysu_fixed[i],capsize=5,label=FIXED_HGHT[i])
        ax5.bar(i+BarWidth,ysu_track_fixed[0][i],width=column_width,edgecolor='black',color=colors_fixed_hght[i],yerr=track_percentile_ysu_fixed[i],capsize=5)
        ax6.bar(i+BarWidth,ysu_slp_fixed[0][i],width=column_width,edgecolor='black',color=colors_fixed_hght[i],yerr=slp_percentile_ysu_fixed[i],capsize=5)

    
    BarWidth+=column_width
    print(ysu_track_lvls[0][i])
    print(ysu_track_fixed[0][i])
    

ax1.yaxis.set_tick_params(labelsize=size+1)

ax2.yaxis.set_tick_params(labelsize=size+1)
ax3.yaxis.set_tick_params(labelsize=size+1)
ax4.yaxis.set_tick_params(labelsize=size+1)
ax5.yaxis.set_tick_params(labelsize=size+1)
ax6.yaxis.set_tick_params(labelsize=size+1)
ax7.yaxis.set_tick_params(labelsize=size+1)
ax8.yaxis.set_tick_params(labelsize=size+1)
ax9.yaxis.set_tick_params(labelsize=size+1)

ax1.set_axisbelow(True)
ax2.set_axisbelow(True)
ax3.set_axisbelow(True)
ax4.set_axisbelow(True)
ax5.set_axisbelow(True)
ax6.set_axisbelow(True)
ax7.set_axisbelow(True)
ax8.set_axisbelow(True)
ax9.set_axisbelow(True)








bbox_args = dict(boxstyle="round4", fc="0.9")
arrow_args = dict(arrowstyle="->")

# ax1.annotate('a)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )
# ax2.annotate('b)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )
# ax3.annotate('c)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )
#             #TITLE1
# ax2.set_title('YSU',fontsize=22)
# # ax2.annotate('YSU', xy=(0.5, 1.2), xycoords='axes fraction',
# #              xytext=(0, 0), textcoords='offset points',
# #              ha="right", va="top",size=22,
             
#             #  )

# ax4.annotate('d)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )
# ax5.annotate('e)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )

#              #Title1#
# ax8.set_title('MYJ',fontsize=22)
# # ax8.annotate('MYJ', xy=(0.5, 1.2), xycoords='axes fraction',
# #              xytext=(0, 0), textcoords='offset points',
# #              ha="right", va="top",size=22,
             
# #              )
    
# ax6.annotate('f)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )

# ax7.annotate('g)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )
# ax8.annotate('h)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )
# ax9.annotate('i)', xy=(0.1, 0.95), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=15,
#              bbox=bbox_args,
#              )


ax1.set_xticks([])
ax2.set_xticks([])
ax3.set_xticks([])
ax4.set_xticks([])
ax5.set_xticks([])
ax6.set_xticks([])
ax7.set_xticks([])
ax8.set_xticks([])
ax9.set_xticks([])

hfont = {'fontname':'Times New Roman',
        'fontstyle':'italic',
        }

ax1.set_ylabel(r'$MAPE_{ intensity }$(\,\%) \,',fontsize=size,labelpad=-0.2)
ax2.set_ylabel(r'$MAE_{ track }$(\,km) \,',fontsize=size,labelpad=-0.2)
ax3.set_ylabel(r'$MAE_{ SLP }$(\,mb) \,',fontsize=size,labelpad=-0.2)

ax4.set_ylabel(r'$MAPE_{ intensity }$(\,\%) \,',fontsize=size,labelpad=-0.2)
ax5.set_ylabel(r'$MAE_{ track }$(\,km) \,',fontsize=size,labelpad=-0.2)
ax6.set_ylabel(r'$MAE_{ SLP }$(\,mb) \,',fontsize=size,labelpad=-0.2)

ax7.set_ylabel(r'$MAPE_{ intensity }$(\,\%) \,',fontsize=size,labelpad=-0.2)
ax8.set_ylabel(r'$MAE_{ track }$(\,km) \,',fontsize=size,labelpad=-0.2)
ax9.set_ylabel(r'$MAE_{ SLP }$(\,mb) \,',fontsize=size,labelpad=-0.2)

ax3.set_ylim(0)


ax1.yaxis.grid(True)
ax2.yaxis.grid(True)
ax3.yaxis.grid(True)
ax4.yaxis.grid(True)
ax5.yaxis.grid(True)
ax6.yaxis.grid(True)
ax7.yaxis.grid(True)
ax8.yaxis.grid(True)
ax9.yaxis.grid(True)

# circ1 = mpatches.Patch(alpha=0,hatch='xx',label='YSU')
# circ2= mpatches.Patch(alpha=0,hatch='..',label='MYJ')
# plt.rc('legend',fontsize=20)
h1, l = ax1.get_legend_handles_labels()
h2,l=ax4.get_legend_handles_labels()
plt.rc('legend',fontsize=size)


leg1=fig.legend(h1, LVLS,ncol=4,frameon=False,bbox_to_anchor=(0.7, 0.93),
          bbox_transform=fig.transFigure,)

leg2=fig.legend(h2,FIXED_HGHT,bbox_to_anchor=(0.94, 0.390),
          bbox_transform=fig.transFigure,
          ncol=4,frameon=False)
# plt.show()



# first_legend = fig.legend(handles=first_handler,loc = 'lower center',ncol = 3,frameon = False, fontsize=15)
# fig.add_artist(first_legend)
# second_legend = fig.legend(handles=second_handler,loc = 'lower center',ncol = 3,frameon = False, fontsize=15)


# plt.show()
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Poster_figs/created_figs/ERROR_BARS.eps',bbox_inches='tight')
# plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig8_error_bars_lvls.eps',bbox_inches='tight')