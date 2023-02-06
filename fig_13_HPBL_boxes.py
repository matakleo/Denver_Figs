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
PBLS = ['YSU']

#
os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=17
Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

Time_idx = '0'

fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(15.8,4.8),sharey='all')
fig.subplots_adjust(hspace=None,wspace=0)

CLS = ['250','1.0','1000']
fig_name='_fixed_hpbls_'
colors = ['blue','grey','red']
legend_names=['PBL height = 250m','Average PBL height = 409m','PBL height = 1000m']
Times=[0,6,12,18,24,30,36,42,48,54,60]
row_count=0
col_count=0
for PBL in PBLS:

    for HN in HNS :

        Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'
        Real_Hurricane_Data = Real_data_dir+'/Real_Data_'+HN+'.csv'
        cls_counter=0
        for CL in CLS:
                
                default_linestyle='dashed'

                #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'		




                # print(Hurricane_Setting)
                csv_file = (Input_Dir_1+Hurricane_Setting)

                #you define empty lists which will contain the extracted data from the csv file, and plot them immediatle
                PBLHs = []

                PBLHs = Extract_by_name(csv_file,PBLHs,'PBLH')
                print(PBLHs)
                PBLHs[0]=PBLHs[1]
                print(Times[0:len(PBLHs)])
                if CL == '1.0':
                    default_linestyle='dashdot'
                # print(row_count,col_count)
                # ax[0].plot(Times[0:len(PBLHs)], PBLHs)

                ax[col_count].plot(Times[0:len(PBLHs)], PBLHs,  linestyle=default_linestyle,color=colors[cls_counter],  marker='.', 
                    linewidth='3',markersize='9', label=CLS[cls_counter] )
                cls_counter+=1
        ax[col_count].set_ylim([0,1100])
        ax[col_count].set_title(HN,size=size)
        ax[col_count].set_xticks(Times[0:len(PBLHs)])
        ax[col_count].set_yticks([0,250,409,1000])
        
        ax[col_count].grid(axis='y',linewidth=1)
        if HN == 'Igor' or HN =='Dorian':
            ax[col_count].set_xticks(Times[0:len(PBLHs):2])
            
        ax[col_count].yaxis.grid(True,linestyle='--')
        # ax[row_count,col_count].set_yticks(wind_intensities[0:number_of_lvls])
        col_count+=1
        if col_count == 5:
            col_count =0
            row_count = 1

ax[0].set_ylabel('PBLH (m)',fontsize=size)
ax[0].set_xlabel('Time (h)',fontsize=size)
ax[1].set_xlabel('Time (h)',fontsize=size)
ax[2].set_xlabel('Time (h)',fontsize=size)
ax[3].set_xlabel('Time (h)',fontsize=size)
ax[4].set_xlabel('Time (h)',fontsize=size)


h, l = ax[1].get_legend_handles_labels()
plt.rc('legend',fontsize=size)
# ax[1,2].axis("off")
fig.legend(h, legend_names,ncol=4,frameon=False,loc='upper center')
# plt.show()

print('saved as: fig13_hpbl_boxes.eps')
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig13_hpbl_boxes.eps',bbox_inches='tight')
# plt.show()
# plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figure6_intensities_cl_km_'+PBLS[0]+'.eps',bbox_inches='tight')