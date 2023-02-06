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
HNS = ['Lorenzo','Iota',] #'Igor','','']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '8km'
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TM = 'NoTurb'
# Choose between : 'YSU_wrf_42',YSU_lin_63'
PBLS = ['YSU']

#

Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

Time_idx = '0'

os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=27
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(13.3, 5.3))
fig.subplots_adjust(wspace=0.2,bottom=0.3)
# show = 'xkzm'

show = 'xkzm'

fig_name='_lvls_'
plot_order = [1,2,0]
colors = ['grey','blue', 'green', 'red']
legend_names=['Real Data','Default Case',r'$K_{ m }\_lvl_{ 4 }$',r'$K_{ m }\_lvl_{ 6 }$']
if show == 'xkzm':
    fig_name='_xkzm_'
    colors = ['grey','blue',  'red']
    CLS = ['1.0','xkzm_0.20','xkzm_5.0'] 
    


CLS = ['1.0','250','1000']
legend_names=['Real Data','Default Case','Reduced PBL Depth','Increased PBL Depth']
Times = [0,6, 12, 18, 24, 30, 36, 42, 48,54,60,66,72,80]
Real_Winds=[]
row_count=0
col_count=0
for PBL in PBLS:
    # if PBL=='MYJ'and show=='xkzm':
    #     CLS=['1.0','km_0.20','km_5.0']

    for HN in HNS :
        # print('PBL is '+PBL+' and HN is: '+HN)
        # print('row is ',row_count,' and col is: ',col_count)

        Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'
        Real_Hurricane_Data = Real_data_dir+'/Real_Data_'+HN+'.csv'

        Real_Winds = []

        Real_Winds = Extract_by_name(Real_Hurricane_Data,Real_Winds,'Wind Speed(kt)')
        # print(Real_Winds)
        ax[col_count].plot(Times[0:len(Real_Winds)], Real_Winds, color='k', linestyle='-',
                    marker='.', linewidth='4', markersize='11', label='Real WSPD')

        cls_counter=0
        for CL in CLS:
                
                default_linestyle='dashed'

                
                #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'		




                # print(Hurricane_Setting)
                csv_file = (Input_Dir_1+Hurricane_Setting)
                print(csv_file)
                #you define empty lists which will contain the extracted data from the csv file, and plot them immediatle
                wind_intensities = []

            

                wind_intensities=Extract_by_name(csv_file, wind_intensities,'All_Max_WND_SPD_10')
                if HN =='Lorenzo' and PBL=='YSU':
                    print(wind_intensities)
                if CL == '1.0':
                    default_linestyle='dashdot'


                ax[col_count].plot(Times[0:len(Real_Winds)], wind_intensities,  linestyle=default_linestyle,color=colors[cls_counter],  marker='.', 
                    linewidth='4',markersize='11', label=CLS[cls_counter], zorder=plot_order[cls_counter] )
                cls_counter+=1
        
        ax[col_count].set_title(HN,fontsize=size+1.5)
        ax[col_count].set_xticks(Times[0:len(Real_Winds)])
        if HN == 'Dorian' or HN == 'Igor':
            ax[col_count].set_xticks(Times[0:len(Real_Winds):2])
        ax[col_count].xaxis.set_tick_params(labelsize=size)
        ax[col_count].yaxis.set_tick_params(labelsize=size)
        
        # ax[col_count].set_yticks(wind_intensities[0:number_of_lvls])
        col_count+=1
        if col_count == 5:
            col_count =0
            row_count = 1
ax[0].set_ylabel(r'Wind intensity $\mathrm{(\,ms^{-1}) \,}$',fontsize=size)
# ax[1,0].set_ylabel(r'Wind intensity $\mathrm{(\,ms^{-1}) \,}$',fontsize=size)
ax[0].set_xlabel('Time (h)',fontsize=size)
ax[1].set_xlabel('Time (h)',fontsize=size)
# ax[1,2].set_xlabel('Time (h)',fontsize=size)
# ax[1,3].set_xlabel('Time (h)',fontsize=size)
# ax[1,4].set_xlabel('Time (h)',fontsize=size)


# ax[0,2].annotate('YSU', xy=(0.7, 1.2), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=22,
             
#              )
            
# ax[1,2].annotate('MYJ', xy=(0.7, 1.182), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=22,
             
#              )

h, l = ax[0].get_legend_handles_labels()
plt.rc('legend',fontsize=size)
# ax[1,2].axis("off")
figl=plt.legend(h, legend_names,ncol=4,frameon=False,bbox_to_anchor=(1.015, 0.16),
          bbox_transform=fig.transFigure)
# plt.show()

# print('saved as: fig6_wind_intensity_boxes'+fig_name+'.eps')
# plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig6_wind_intensity_boxes'+fig_name+'.eps',bbox_inches='tight')
# plt.show()
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Poster_figs/created_figs/time_series_poster.eps')