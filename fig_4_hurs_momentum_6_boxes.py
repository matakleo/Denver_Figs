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
HNS = ['Iota','Lorenzo']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '8km'
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TM = 'NoTurb'
# Choose between : 'YSU_wrf_42',YSU_lin_63'
PBLS = ['YSU'] #,'MYJ']
hfont = {'fontname':'Times New Roman',
        'fontstyle':'italic',
        'size':7}
size=20

os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
Time_idx = '0'

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8.5,6.5),sharey='row',dpi=350)
fig.subplots_adjust(wspace=0.01,bottom=0.20)


##HERE YOU OPERATE WHAT TO SHOW!!!##
# show = 'xkzm'
show = 'xkzm'

CLS = ['1.0','lvl_3','lvl_5']
plot_order = [1,2,0]
fig_name='_lvls_'
colors = ['black','blue', 'green', 'red']
legend_names=['Default Case',r'$K_{ m }\_lvl_{ 4 }$',r'$K_{ m }\_lvl_{ 6 }$']


if show == 'xkzm':
    fig_name='_xkzm_'
    colors = ['black','blue',  'red']
    CLS=['1.0','km_0.20','km_5.0']

    legend_names=['Default Case',r'$C_{ k }$\_0.2',r'$C_{ k }$\_5.0',]
    if PBLS[0]=='YSU':
        CLS = ['1.0','xkzm_0.20','xkzm_5.0'] 
row_count=0
col_count=0
for PBL in PBLS:
    if PBL=='MYJ' and show=='xkzm':
        CLS=['1.0','km_0.20','km_5.0']
    for HN in HNS :

        Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'
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
                    ax[col_count].plot(momentum_exchange[0:number_of_lvls], lvl_heights[0:number_of_lvls], color=colors[cls_counter],  marker='.', 
                        linewidth='4',markersize='14', label= (CLS[cls_counter]), zorder=plot_order[cls_counter])
                    
                    cls_counter+=1
                    ax[col_count].set_title(HN,fontsize=size)
                    # ax[col_count].yaxis.grid(True)
                    ax[col_count].set_yticks(lvl_heights[0:number_of_lvls])
                    
                    ax[col_count].xaxis.set_tick_params(labelsize=size)
                    ax[col_count].yaxis.set_tick_params(labelsize=size)
        col_count+=1

if show =='lvls':
    ax[1,3].set_xticks([0,50,95])
ax[0].set_ylabel('Height (m)',fontsize=size)
# ax[1].set_ylabel('Height (m)',fontsize=size)
# ax[1,0].set_xlabel(r'${\fontfamily{cmr}\selectfont\
# \textsl${K_mlvl_4}$}',fontsize=size)
ax[0].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)
ax[1].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)
# ax[1,2].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)
# ax[1,3].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)
# ax[1,4].set_xlabel(r'$K_{ m }\mathrm{(\,m^{2}s^{-1}) \,}$',fontsize=size)

# ax[0].annotate('YSU', xy=(0.7, 1.2), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=22,
             
#              )

h, l = ax[0].get_legend_handles_labels()
plt.rc('legend',fontsize=size)
plt.rc('font',family='Times New Roman')
plt.rcParams["font.style"]='italic'
figl=plt.legend(h, legend_names,ncol=4,frameon=False,bbox_to_anchor=(0.88, 0.1),
          bbox_transform=fig.transFigure)
# plt.show()



plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Poster_figs/created_figs/momentum_profiles_poster.eps',bbox_inches='tight')