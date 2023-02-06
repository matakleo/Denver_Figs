from numpy.core.function_base import linspace
from all_functions import Extract_by_name,Extract_Coordinates_2,Extract_Track_Data, Extract_the_shit2
import cartopy.feature as cfeature
import matplotlib.gridspec as gridspec
#from Func_Map_Setting import map_setting
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter,LatitudeLocator





Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

Input_Dir = '/Users/lmatak/Desktop/leo_simulations/WRF_Output_PBLHS/diff_hpbls'

# for MYJ 'Maria','Dorian','Iota','Teddy','Lorenzo , Igor
HNS = ['Iota','Maria','Dorian','Lorenzo','Igor']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '8km'
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TM = 'NoTurb'
# Choose between : 'YSU_wrf_42',YSU_lin_63'
PBLS = ['YSU','MYJ']
# PBLS = ['YSU_additional_changs']

Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

Time_idx = '0'
os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=17

fig, ax = plt.subplots(nrows=2, ncols=5, figsize=(13.8,8.8),sharey='row')
fig.subplots_adjust(hspace=0.3,wspace=0)

show = 'xkzm'
# show = 'lvls'

CLS = ['1.0','lvl_3','lvl_5']
fig_name='_lvls_'
colors = ['grey','blue', 'green', 'red']
plot_order = [1,3,0]
legend_names=['Real Data','Default Case',r'$K_{ m }\_lvl_{ 4 }$',r'$K_{ m }\_lvl_{ 6 }$']
if show == 'xkzm':
    fig_name='_xkzm_'
    colors = ['grey','blue',  'red']
    CLS = ['1.0','xkzm_0.20','xkzm_5.0'] 
    legend_names=['Real Data','Default Case',r'$C_{ k }$\_0.2',r'$C_{ k }$\_5.0']
Times = [0,6, 12, 18, 24, 30, 36, 42, 48,54,60,66,72,80]
Real_Winds=[]
row_count=0
col_count=0
for PBL in PBLS:
    if PBL=='MYJ'and show=='xkzm':
        CLS=['1.0','km_0.20','km_5.0']
    for HN in HNS :

        Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'
        Real_Hurricane_Data = Real_data_dir+'/Real_Data_'+HN+'.csv'

        Real_SLP = []

        Real_SLP = Extract_by_name(Real_Hurricane_Data,Real_SLP,'Pressure (mb) ')
        print(Real_SLP)
        ax[row_count,col_count].plot(Times[0:len(Real_SLP)], Real_SLP, color='k', linestyle='-',
                    marker='.', linewidth='3', markersize='9', label='Real min SLP')

        cls_counter=0
        for CL in CLS:

                    default_linestyle='--'

                    #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                    Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'		




                    # print(Hurricane_Setting)
                    csv_file = (Input_Dir_1+Hurricane_Setting)

                    #you define empty lists which will contain the extracted data from the csv file, and plot them immediatle
                    min_slps = []

            

                    min_slps=Extract_by_name(csv_file, min_slps,'min_slp')
                    # print(min_slps)

                    if CL == '1.0':
                        default_linestyle='dashdot'

                    ax[row_count,col_count].plot(Times[0:len(min_slps)], min_slps, color=colors[cls_counter], linestyle=default_linestyle,
                    marker='.', markersize='9',  
                        linewidth='3', label= (CLS[cls_counter]),zorder=plot_order[cls_counter])
                    
                    cls_counter+=1
        ax[row_count,col_count].set_title(HN,fontsize=size+1.5)
        ax[row_count,col_count].set_yticks([900,950,1000])
        ax[row_count,col_count].set_ylim([895,1005])
        ax[row_count,col_count].yaxis.grid(True,linestyle='--')
        ax[row_count,col_count].xaxis.set_tick_params(labelsize=size)
        ax[row_count,col_count].yaxis.set_tick_params(labelsize=size)
        ax[row_count,col_count].set_xticks(Times[0:len(min_slps)])
        if HN == 'Dorian' or HN == 'Igor':
            ax[row_count,col_count].set_xticks(Times[0:len(min_slps):2])
            # ax[row_count,col_count].set_yticks(wind_intensities[0:number_of_lvls])
        col_count+=1
        if col_count == 5:
            col_count =0
            row_count = 1
ax[0,0].set_ylabel('min SLP (mb)',fontsize=size)
ax[1,0].set_ylabel('min SLP (mb)',fontsize=size)
ax[1,0].set_xlabel('Time (h)',fontsize=size)
ax[1,1].set_xlabel('Time (h)',fontsize=size)
ax[1,2].set_xlabel('Time (h)',fontsize=size)
ax[1,3].set_xlabel('Time (h)',fontsize=size)
ax[1,4].set_xlabel('Time (h)',fontsize=size)

ax[0,2].annotate('YSU', xy=(0.63, 1.2), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=22,
             
             )
            
ax[1,2].annotate('MYJ', xy=(0.63, 1.182), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=22,
             
             )
h, l = ax[1,1].get_legend_handles_labels()
plt.rc('legend',fontsize=size)


figl=plt.legend(h, legend_names,ncol=4,frameon=False,bbox_to_anchor=(0.78, 0.06),
          bbox_transform=fig.transFigure)
# plt.show()

print('saved as: fig7_min_slp_boxes'+fig_name+'.eps')
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig7_min_slp_boxes'+fig_name+'.eps',bbox_inches='tight')
# plt.show()