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

dirs = ['/Users/lmatak/Downloads/meng','/Users/lmatak/Downloads/leo']

# for MYJ 'Maria','Dorian','Iota','Teddy','Lorenzo , Igor
HNS = ['maria']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '8km'


PBLS = ['YSU']
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




CLS = ['0p01','0p0001']

fig_name='_lvls_'
colors = ['grey', 'blue','green', 'red']
legend_names=['Real Track','Default Case',r'$K_{ m }\_lvl_{ 4 }$\_'+PBLS[0],r'$K_{ m }\_lvl_{ 6 }$\_'+PBLS[0]]


        


print(CLS)

Time_idx = '0'

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8.8,6.8),subplot_kw={'projection': ccrs.PlateCarree()})
fig.subplots_adjust(hspace=0.005,wspace=0.35)

dir_count=0
row_count=0
col_count=0
for dir in dirs:
    
    print('dir='+dir)
    for HN in HNS :
        print(HN)

        

        Input_Dir_1 = dir 



        
        cls_counter=0
        for CL in CLS:
                default_ls='-'

                #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                Hurricane_Setting = HN + '_' + GS + '_Clz_' + CL +'.csv'		
                print('plotting '+Hurricane_Setting)
                # print(Hurricane_Setting)
                csv_file = (Input_Dir_1+Hurricane_Setting)

                #you define empty lists which will contain the extracted data from the csv file, and plot them immediatle
                Eye_Lats = []
                Eye_Longs = []

                (Eye_Lats, Eye_Longs) = Extract_Coordinates_2 (Input_Dir_1, Hurricane_Setting,'min_lat', 'min_long')

                # print('CL is '+CL+' and color is: '+colors[cls_counter])
                
                ax[dir_count].plot(Eye_Longs[0:len(Eye_Lats)], Eye_Lats[0:len(Eye_Lats)], color=colors[cls_counter],  marker='.', 
                    linewidth='1.7',markersize='8', ls=default_ls,transform=ccrs.PlateCarree(), label= (CLS[cls_counter]))
                ax[dir_count].stock_img()
                ax[dir_count].set_extent([-68,-76, 19.5 , 28.5])

                gl = ax[dir_count].gridlines(color='gray',alpha=0.6,draw_labels=True,linewidth=0)
                gl.top_labels = False
                gl.right_labels = False
                gl.xlabel_style, gl.ylabel_style = {'fontsize':size }, {'fontsize': size}
    

                # ax[row_count,col_count].tick_params(axis='x', labelsize=size+10, length=10, direction = 'in', width = 2)
                # ax[row_count,col_count].tick_params(axis='y', labelsize=size, length=10, direction = 'in', width = 2)
                
                cls_counter+=1
    dir_count+=1





# h, l = ax[0,1].get_legend_handles_labels()
# plt.rc('legend',fontsize=size)
# legend_names1=['','',r'$C_{ k }$\_0.2\_'+PBLS[1],r'$C_{ k }$\_5.0\_'+PBLS[1]]
# if show =='lvls':
#     legend_names1=['','',r'$K_{ m }\_lvl_{ 4 }$\_'+PBLS[1],r'$K_{ m }\_lvl_{ 6 }$\_'+PBLS[1]]

# ##YSU##
# leg1=fig.legend(h, legend_names,ncol=4,frameon=False,bbox_to_anchor=(0.98, 0.95),
#           bbox_transform=fig.transFigure,)


# # ax[1,2].legend(h[2:], legend_names1[2:],ncol=1,frameon=False)


# ##MYJ##
# h, l = ax[1,1].get_legend_handles_labels()

# leg2=fig.legend(h[2:],legend_names1[2:],bbox_to_anchor=(0.7, 0.52),
#           bbox_transform=fig.transFigure,
#           ncol=4,frameon=False)

plt.legend()
plt.show()
# print('saved as: fig3_tracks_Dori_and_Lori'+fig_name+'.png')
# plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/fig3_tracks_Dori_and_Lori'+fig_name+'.png',bbox_inches='tight')