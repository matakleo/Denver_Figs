
from all_functions import Extract_by_name,Extract_Coordinates_2,Extract_Track_Data
import cartopy.feature as cfeature
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter,LatitudeLocator

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import os
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('font', size=13)

Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'
Real_data_dir_long='/Users/lmatak/Desktop/leo_simulations/Real_Data_long'

fig = plt.figure(figsize=(12.3, 7.3),dpi=350)
ax1= fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
# ax1.stock_img()
os.environ["CARTOPY_USER_BACKGROUNDS"]='/Users/lmatak/Desktop/leo_python_scripts/Paper_Figs/figs_saved/cartopy_map/'
ax1.background_img(name='my_pic', resolution='high')
ax1.set_extent([-15,-90, 0 , 35])

colors = ['blue', 'black', 'red',  'cyan', 'lime','magenta','yellow']

Hurricanes = ['Dorian','Igor','Iota','Lorenzo','Maria']
dates=['08/30','09/02',
        '09/11','09/14',
        '11/15','11/16',
        '09/25','09/27',
        '09/17','09/19']


states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')

i=0
for HN in Hurricanes:

    ##plotting the long real data, all the points of hurricane existance, dotted lines##
    Real_Lats = []
    Real_Longs = []
    Real_Lats = Extract_Track_Data (Real_data_dir_long, Real_Lats, 'Lat',HN)
    print(HN+str(Real_Lats))
    Real_Longs = Extract_Track_Data (Real_data_dir_long, Real_Longs, 'Lon',HN)
    ax1.plot(Real_Longs,Real_Lats,transform=ccrs.PlateCarree(), marker='o', 
			markersize='3',
			linewidth='1.5',linestyle='dotted', color=colors[i])

    ##plotting the thick lines of simluation times
    #offset amount
    offset=(13,20)
    Real_Lats = []
    Real_Longs = []
    Real_Lats = Extract_Track_Data (Real_data_dir, Real_Lats, 'Lat',HN)
    print(HN+str(Real_Lats))
    Real_Longs = Extract_Track_Data (Real_data_dir, Real_Longs, 'Lon',HN)
    ax1.plot(Real_Longs,Real_Lats,transform=ccrs.PlateCarree(),label=(HN+"'s simulated track"),color=colors[i],
			linewidth='5')


    #specifying offset
    if HN == 'Igor' or HN=='Iota':
        offset=(20,18)
    if HN =='Maria' or HN == 'Dorian':
        offset=(25,17)
    offset2=offset
    if HN=='Lorenzo':
        offset2=(-5,-1)

    ##annotating dates
    ax1.annotate(dates[i*2], xy=(Real_Longs[0], Real_Lats[0]),  xycoords='data',
            xytext=offset, textcoords='offset points', color=colors[i],
            horizontalalignment='right', verticalalignment='top',
            )   
    ax1.annotate(dates[i*2+1], xy=(Real_Longs[-1], Real_Lats[-1]),  xycoords='data',
            xytext=offset2, textcoords='offset points', color=colors[i], 
            horizontalalignment='right', verticalalignment='top',
            
            )     
    i+=1
i=0


##adding borders

ax1.add_feature(cfeature.LAND)
# ax1.add_feature(cfeature.COASTLINE)
# ax1.add_feature(cfeature.OCEAN)
# ax1.add_feature(cfeature.BORDERS)
# ax1.add_feature(states_provinces, edgecolor='black')

ax1.set_xticks([-30, -40, -50, -60, -70, -80,], crs=ccrs.PlateCarree())
ax1.set_yticks([10, 15, 20, 25, 30,], crs=ccrs.PlateCarree())


##editing ticks
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax1.xaxis.set_major_formatter(lon_formatter)
ax1.yaxis.set_major_formatter(lat_formatter)
ax1.tick_params(axis='x', labelsize=24, length=6, direction = 'in', width = 2)
ax1.tick_params(axis='y', labelsize=24, length=6, direction = 'in', width = 2)


plt.rc('legend',fontsize=24)
plt.legend(loc='upper right',frameon='false')
# plt.show()
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Poster_figs/created_figs/hurricane_tracks_poster.png',bbox_inches='tight')