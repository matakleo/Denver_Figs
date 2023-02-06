from unittest import skip
from numpy.core.function_base import linspace
from all_functions import Extract_by_name,Extract_Coordinates_2,Extract_Track_Data
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
HNS = ['Dorian','Lorenzo']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '8km'
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TM = 'NoTurb'

PBLS = ['YSU','MYJ']
os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=15

##here make the change
show = 'lvls'
# show = 'lvls'



plot_order = [2,3,1]
CLS = ['1.0','lvl_3','lvl_5']
fig_name='_lvls_'
colors = ['grey', 'blue','green', 'red']
legend_names=['Real Track','Default Case',r'$K_{ m }\_lvl_{ 4 }$\_'+PBLS[0],r'$K_{ m }\_lvl_{ 6 }$\_'+PBLS[0]]
if show == 'xkzm':
    fig_name='_xkzm_'
    colors = ['grey', 'blue', 'red']
    CLS=['1.0','km_0.20','km_5.0']
    legend_names=['Real Track','Default Case',r'$C_{ k }$\_0.2\_'+PBLS[0],r'$C_{ k }$\_5.0\_'+PBLS[0]]
    if PBLS[0]=='YSU':
        CLS = ['1.0','xkzm_0.20','xkzm_5.0'] 

        


print(CLS)

Time_idx = '0'

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8.8,6.8),subplot_kw={'projection': ccrs.PlateCarree()},dpi=350)
fig.subplots_adjust(hspace=0.005,wspace=0.35)


row_count=0
col_count=0
for PBL in PBLS:
    if PBL=='MYJ' and show=='xkzm':
        CLS=['1.0','km_0.20','km_5.0']
    for HN in HNS :
        print(HN)
        print('row=',row_count)
        print('col=',col_count)
        

        Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'

        Real_Lats = []
        Real_Longs = []
        Real_Lats = Extract_Track_Data (Real_data_dir, Real_Lats, 'Lat',HN)
        Real_Longs = Extract_Track_Data (Real_data_dir, Real_Longs, 'Lon',HN)


        lat_cor_first = Real_Lats[0]
        lat_cor_last = Real_Lats[-1]
        lon_cor_first = Real_Longs[0]
        lon_cor_last = Real_Longs[-1]

        ax[row_count,col_count].stock_img()
        ax[row_count,col_count].set_extent([lon_cor_last-1.5,lon_cor_first+1.5, lat_cor_first-1.5 , lat_cor_last+1.5])

        # gl = ax[row_count,col_count].gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
        #             linewidth=5, color='gray', alpha=0, linestyle='--')
        # gl.top_labels = False
        # gl.right_labels = False
        # ax[row_count,col_count].xlabel_style = {'size': 0.2}
        # ax[row_count,col_count].xlabel_style = {'color': 'black'}
        ax[row_count,col_count].add_feature(cfeature.COASTLINE)
        ax[row_count,col_count].coastlines('50m', linewidth=0.8)

        ax[row_count,col_count].plot(Real_Longs, Real_Lats, color='k', linestyle='--',
                    marker='*', linewidth='2', markersize='9',transform=ccrs.PlateCarree(), label='Real Track')
        ax[row_count,col_count].set_title(HN,size=size)


        
        cls_counter=0
        for CL in CLS:
                default_ls='-'
                if PBL=='MYJ':
                    default_ls='dashdot'

                #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'		
                # print(Hurricane_Setting)
                csv_file = (Input_Dir_1+Hurricane_Setting)

                #you define empty lists which will contain the extracted data from the csv file, and plot them immediatle
                Eye_Lats = []
                Eye_Longs = []

                (Eye_Lats, Eye_Longs) = Extract_Coordinates_2 (Input_Dir_1, Hurricane_Setting,'min_lat', 'min_long')

                # print('CL is '+CL+' and color is: '+colors[cls_counter])
                
                ax[row_count,col_count].plot(Eye_Longs[0:len(Eye_Lats)], Eye_Lats[0:len(Eye_Lats)], color=colors[cls_counter],  marker='.', 
                    linewidth='1.7',markersize='8', ls=default_ls,transform=ccrs.PlateCarree(), label= (CLS[cls_counter]+PBL),zorder=plot_order[cls_counter])
                

                gl = ax[row_count,col_count].gridlines(color='gray',alpha=0.6,draw_labels=True,linewidth=0)
                gl.top_labels = False
                gl.right_labels = False
                gl.xlabel_style, gl.ylabel_style = {'fontsize':size }, {'fontsize': size}
    

                # ax[row_count,col_count].tick_params(axis='x', labelsize=size+10, length=10, direction = 'in', width = 2)
                # ax[row_count,col_count].tick_params(axis='y', labelsize=size, length=10, direction = 'in', width = 2)
                
                cls_counter+=1
        col_count+=1
        
        
        if col_count == 2:
            col_count =0
            row_count += 1

# ax[0,1].annotate('YSU', xy=(0, 1.2), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=25,
             
#              )


# ax[1,1].annotate('MYJ', xy=(0, 1.2), xycoords='axes fraction',
#              xytext=(0, 0), textcoords='offset points',
#              ha="right", va="top",size=25,
             
#              )

# h1, l = ax[0,1].get_legend_handles_labels()
# h2,l=ax[1,1].get_legend_handles_labels()
# plt.rc('legend',fontsize=size)


h, l = ax[0,1].get_legend_handles_labels()
plt.rc('legend',fontsize=size)
legend_names1=['','',r'$C_{ k }$\_0.2\_'+PBLS[1],r'$C_{ k }$\_5.0\_'+PBLS[1]]
if show =='lvls':
    legend_names1=['','',r'$K_{ m }\_lvl_{ 4 }$\_'+PBLS[1],r'$K_{ m }\_lvl_{ 6 }$\_'+PBLS[1]]

##YSU##
leg1=fig.legend(h, legend_names,ncol=4,frameon=False,bbox_to_anchor=(0.98, 0.95),
          bbox_transform=fig.transFigure,)


# ax[1,2].legend(h[2:], legend_names1[2:],ncol=1,frameon=False)


##MYJ##
h, l = ax[1,1].get_legend_handles_labels()

leg2=fig.legend(h[2:],legend_names1[2:],bbox_to_anchor=(0.7, 0.52),
          bbox_transform=fig.transFigure,
          ncol=4,frameon=False)
# ax[3,2].axis("off")
# plt.rc('legend',fontsize=size)
# ax[3,2].legend(h, legend_names,ncol=1,frameon=False)
# handles, labels = fig.gca().get_legend_handles_labels()

# by_label = dict(zip(labels, handles))
# print(by_label.keys())

# lgnd = fig.legend(by_label.values(),legend_names,loc = 'upper center',ncol = 5,frameon = False)

# plt.show()
print('saved as: fig3_tracks_Dori_and_Lori'+fig_name+'.png')
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig3_tracks_Dori_and_Lori'+fig_name+'.png',bbox_inches='tight')