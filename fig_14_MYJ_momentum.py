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

Input_Dir = '/Users/lmatak/Downloads/MYJ_momentum/'
Input_Dir_2='/Users/lmatak/Downloads/MYJ_12th_hour/'
dirs=[Input_Dir,Input_Dir_2]
# /Users/lmatak/Downloads/MYJ_6th_hour
# for MYJ 'Maria','Dorian','Iota','Teddy','Lorenzo , Igor
HNS = ['Iota','Igor']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '8km'
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TM = 'NoTurb'
# Choose between : 'YSU_wrf_42',YSU_lin_63'
PBL = 'MYJ'

os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=17

Time_idx = '0'

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(13.8,7.8),sharey='row',sharex='col')
fig.subplots_adjust(hspace=0.15,wspace=0,bottom=0.13)


##HERE YOU OPERATE WHAT TO SHOW!!!##
show = 'lvls'
# show = 'lvls'
run_times=['1h','3h',r'$\geq$25h']
CLS = ['1.0','lvl_3','lvl_5']
plot_order = [1,2,0]
fig_name='_lvls_'
colors = ['black','blue', 'green', 'red']
legend_names=['Default Case',r'$K_{ m }\_lvl_{ 4 }$',r'$K_{ m }\_lvl_{ 6 }$']
if show == 'xkzm':
    fig_name='_xkzm_'
    colors = ['black','blue',  'red']
    CLS=['1.0','km_0.2','km_5.0']

    legend_names=['Default Case',r'$C_{ k }$\_0.2',r'$C_{ k }$\_5.0']

row_count=0
col_count=0
for HN in HNS :
    for j in range(1,4):
        
    
        Input_Dir_1 = Input_Dir+HN+str(j)+'/'
        print(Input_Dir_1)
        cls_counter=0
        for CL in CLS:
                    print(CL)
                    #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                    Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'		
                    # print(Hurricane_Setting)
                    csv_file = (Input_Dir_1+Hurricane_Setting)

                    #you define empty lists which will contain the extracted data from the csv file, and plot them immediatle
                    momentum_exchange = []

            
                    lvl_heights=[]
                    lvl_heights = Extract_by_name(csv_file, lvl_heights, 'lvl_heights')
                    momentum_exchange=Extract_by_name(csv_file, momentum_exchange,'avg_vert_exch_momentum')

                    number_of_lvls=9
                    print('row ',row_count)
                    print('col ',col_count)
                    ax[row_count,col_count].plot(momentum_exchange[0:number_of_lvls], lvl_heights[0:number_of_lvls], color=colors[cls_counter],  marker='.', 
                        linewidth='2',markersize='9', label= (CLS[cls_counter]), zorder=plot_order[cls_counter])
                    
                    cls_counter+=1
                    # ax[row_count,col_count].set_title(HN,fontsize=14)
                    # ax[row_count,col_count].yaxis.grid(True)
        ax[row_count,col_count].set_yticks(lvl_heights[0:number_of_lvls])
        ax[row_count,col_count].yaxis.set_tick_params(labelsize=size-4)
        ax[row_count,col_count].xaxis.set_tick_params(labelsize=size)
        ax[row_count,col_count].annotate('runtime duration '+run_times[col_count], xy=(0.93, 0.93), xycoords='axes fraction',
        xytext=(0, 0), textcoords='offset points',
        ha="right", va="top",size=size,
        
        )
        col_count+=1
        if col_count == 3:
            col_count =0
            row_count += 1
            next
        
        
ax[0,0].set_ylabel('Height (m)',fontsize=size)
ax[1,0].set_ylabel('Height (m)',fontsize=size)
ax[1,0].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)
ax[1,1].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)
ax[1,2].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)

ax[0,0].set_title('Iota',fontsize=20)
ax[0,1].set_title('Iota',fontsize=20)
ax[0,2].set_title('Iota',fontsize=20)
ax[1,0].set_title('Igor',fontsize=20)
ax[1,1].set_title('Igor',fontsize=20)
ax[1,2].set_title('Igor',fontsize=20)




            
# ax[1,2].annotate('MYJ', xy=(0.7, 1.2), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=22,
             
#              )
h, l = ax[1,1].get_legend_handles_labels()
plt.rc('legend',fontsize=size)


figl=plt.legend(h, legend_names,ncol=4,frameon=False,bbox_to_anchor=(0.68, 0.06),
          bbox_transform=fig.transFigure)
# plt.show()

print('saved as: fig14_MYJ_momentum_boxes.eps')
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig14_MYJ_momentum_boxes.eps',bbox_inches='tight')