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
PBLS = ['YSU','MYJ','YSU','MYJ']

#

Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

Time_idx = '0'

os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=22.5
fig, ax = plt.subplots(nrows=4, ncols=5, figsize=(21.8,15.8),sharex='col')
fig.subplots_adjust(hspace=0.4,wspace=0.13)
# show = 'xkzm'

# show = 'xkzm'

CLS = ['1.0','lvl_3','lvl_5']
CLS_xkzm = ['1.0','xkzm_0.20','xkzm_5.0'] 
fig_name='_lvls_'
plot_order = [1,2,0]
colors = ['grey','blue', 'green', 'red']
legend_names1=['Real Data',r'Default Case$\hspace{100pt}\phantom{A}$',r'$K_{ m }\_lvl_{ 4 }$',r'$K_{ m }\_lvl_{ 6 }$']
# if show == 'xkzm':
#     fig_name='_xkzm_'
#     colors = ['grey','blue',  'red']
#     CLS = ['1.0','xkzm_0.20','xkzm_5.0'] 
legend_names2=['Real Data','Default Case',r'$C_{ k }$\_0.2',r'$C_{ k }$\_5.0']


Times = [0,6, 12, 18, 24, 30, 36, 42, 48,54,60,66,72,80]
Real_Winds=[]
row_count=0
col_count=0
for PBL in PBLS:
    for HN in HNS :
        # print('PBL is '+PBL+' and HN is: '+HN)
        # print('row is ',row_count,' and col is: ',col_count)

        Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'
        Real_Hurricane_Data = Real_data_dir+'/Real_Data_'+HN+'.csv'

        Real_Winds = []

        Real_Winds = Extract_by_name(Real_Hurricane_Data,Real_Winds,'Wind Speed(kt)')
        # print(Real_Winds)
        ax[row_count,col_count].plot(Times[0:len(Real_Winds)], Real_Winds, color='k', linestyle='-',
                    marker='.', linewidth='3', markersize='9', label='Real WSPD')
        print('row count= ',row_count)
        
        if PBL=='MYJ'and row_count>1:
            CLS=['1.0','km_0.20','km_5.0']
        if PBL=='YSU'and row_count>1:
            CLS=['1.0','xkzm_0.20','xkzm_5.0']
            colors = ['grey','blue',  'red']
            default_linestyle='dashdot'
        else:
            default_linestyle='dashed'
        print(CLS)


        cls_counter=0
        for CL in CLS:
                if CL=='1.0' or row_count>1:
                    default_linestyle='dashdot'
                else:
                    default_linestyle='dashed'
            
                


                
                #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'		




                # print(Hurricane_Setting)
                csv_file = (Input_Dir_1+Hurricane_Setting)

                #you define empty lists which will contain the extracted data from the csv file, and plot them immediatle
                wind_intensities = []

            

                wind_intensities=Extract_by_name(csv_file, wind_intensities,'All_Max_WND_SPD_10')

                # if CL == '1.0':
                #     default_linestyle='dashdot'


                ax[row_count,col_count].plot(Times[0:len(Real_Winds)], wind_intensities,  linestyle=default_linestyle,color=colors[cls_counter],  marker='.', 
                    linewidth='3',markersize='9', label=CLS[cls_counter], zorder=plot_order[cls_counter] )
                cls_counter+=1
                ax[row_count,col_count].grid(axis='x',linestyle='--', linewidth=0.3)
               
        ax[row_count,col_count].set_title(HN,fontsize=size+1.5)
        ax[row_count,col_count].set_xticks(Times[0:len(Real_Winds)])
        if HN == 'Dorian' or HN == 'Igor':
            ax[row_count,col_count].set_xticks(Times[0:len(Real_Winds):2])
        ax[row_count,col_count].xaxis.set_tick_params(labelsize=size)
        ax[row_count,col_count].yaxis.set_tick_params(labelsize=size)
        
        # ax[row_count,col_count].set_yticks(wind_intensities[0:number_of_lvls])
        col_count+=1
        if col_count == 5:
            col_count =0
            row_count += 1
ax[0,0].set_ylabel(r'Wind intensity $\mathrm{(\,ms^{-1}) \,}$',fontsize=size)
ax[1,0].set_ylabel(r'Wind intensity $\mathrm{(\,ms^{-1}) \,}$',fontsize=size)
ax[2,0].set_ylabel(r'Wind intensity $\mathrm{(\,ms^{-1}) \,}$',fontsize=size)
ax[3,0].set_ylabel(r'Wind intensity $\mathrm{(\,ms^{-1}) \,}$',fontsize=size)
ax[3,0].set_xlabel('Time (h)',fontsize=size)
ax[3,1].set_xlabel('Time (h)',fontsize=size)
ax[3,2].set_xlabel('Time (h)',fontsize=size)
ax[3,3].set_xlabel('Time (h)',fontsize=size)
ax[3,4].set_xlabel('Time (h)',fontsize=size)


ax[0,2].annotate(r'\textbf{YSU}', xy=(0.61, 1.28), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=24, weight='bold',
             
             )
            
ax[1,2].annotate(r'\textbf{MYJ}', xy=(0.61, 1.28), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=24,weight='bold',
             
             )
ax[2,2].annotate(r'\textbf{YSU}', xy=(0.61, 1.28), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=24,weight='bold',
             
             )
            
ax[3,2].annotate(r'\textbf{MYJ}', xy=(0.61, 1.28), xycoords='axes fraction',
             xytext=(0, 0), textcoords='offset points',
             ha="right", va="top",size=24,weight='bold',
             
             )

h1, l1 = ax[1,1].get_legend_handles_labels()
h2, l2 = ax[3,1].get_legend_handles_labels()
plt.rc('legend',fontsize=size+2)
# ax[1,2].axis("off")
fig1=fig.legend(h1[0:2], legend_names1[0:2],ncol=2,frameon=False,bbox_to_anchor=(0.48, .94),
          bbox_transform=fig.transFigure)
fig2=fig.legend(h1[2:], legend_names1[2:4],ncol=2,frameon=False,bbox_to_anchor=(0.78, .94),
          bbox_transform=fig.transFigure)
fig3=fig.legend(h2[0:2], legend_names2[0:2],ncol=2,frameon=False,bbox_to_anchor=(0.48, .525),
          bbox_transform=fig.transFigure)
fig4=fig.legend(h2[2:], legend_names2[2:4],ncol=2,frameon=False,bbox_to_anchor=(0.76, .525),
          bbox_transform=fig.transFigure)
# fig2=fig.legend(h2, legend_names2,ncol=4,frameon=False,bbox_to_anchor=(0.69, .53),
#           bbox_transform=fig.transFigure)
# plt.show()

# print('saved as: fig6a_wind_intensity_boxes'+fig_name+'.eps')
# plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig6a_wind_intensity_boxes'+fig_name+'.eps',bbox_inches='tight')
plt.show()
# plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figure6_intensities_cl_km_'+PBLS[0]+'.eps',bbox_inches='tight')