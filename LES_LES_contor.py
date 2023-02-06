from turtle import right
from typing import Counter
from wrf import (getvar, interplevel, smooth2d, to_np, latlon_coords, get_cartopy, cartopy_xlim, cartopy_ylim)
from all_functions import Extract_Track_Data,list_ncfiles
from cartopy.mpl.gridliner import LongitudeFormatter, LATITUDE_FORMATTER
from cartopy.feature import NaturalEarthFeature
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
from netCDF4 import Dataset
import cartopy.crs as crs
import numpy as np
import imageio
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
import cartopy.feature as cfeature


fig, ax = plt.subplots(nrows=1, ncols=2,subplot_kw={'projection': crs.PlateCarree()},figsize=(12.3, 7.3))


cmap=plt.get_cmap(
    'twilight_shifted')
cmap2=plt.get_cmap(
    'plasma'
)


titles=['YSU parent dx=1500m','LES nest dx=300m']
max_wspd=0
agl=50
time_idx=5
Input_Dir = '/Users/lmatak/Downloads/YSU_LES_3/'
os.chdir(Input_Dir)
ncfiles=[]
ncfiles = list_ncfiles(Input_Dir, ncfiles)
for i in range(len(ncfiles)):
    Data = Dataset(ncfiles[i])
    height = getvar(Data, "height_agl",time_idx)
    z=getvar(Data,"z",time_idx)
    wspd = getvar(Data, "PM2_5_DRY",time_idx)
    lvls=[]

    wspd_100=interplevel(wspd,height,agl)
    if np.amax(wspd_100)>max_wspd:
        max_wspd=np.amax(wspd_100)
    # co_agl=interplevel(co,height,agl)


    ax[i].stock_img()
    ax[i].coastlines('50m', linewidth=0.8)
    ax[i].add_feature(cfeature.LAND)
    # ax[0].add_feature(cfeature.STATES)
    ax[i].add_feature(cfeature.OCEAN)

    lats1, lons1 = latlon_coords(wspd_100)

    ax[i].set_extent([float(lons1[0][0])-i/3*1,float(lons1[-1][-1])+i/3*1,float(lats1[0][0])-i/3*1,float(lats1[-1][-1])+i/3*1])
    # ax[1].set_extent([slp_coord_long+15,slp_coord_long-15,slp_coord_lat-15,slp_coord_lat+15])
    # # Get the cartopy mapping object
    cart_proj = get_cartopy(wspd_100)
    ax[i].contourf(to_np(lons1), to_np(lats1), to_np(wspd_100), 255, 
        transform=crs.PlateCarree(), 
        cmap=cmap)
    ax[i].set_title(titles[i])
    gl = ax[i].gridlines(crs=crs.PlateCarree(), draw_labels=True,
                        linewidth=0.2, color='black', alpha=0.2, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xlabel_style= {'size': 12, 'color': 'black'}  
    gl.ylabel_style= {'size': 12, 'color': 'black'}
# ax[1].contourf(to_np(lons1), to_np(lats1), to_np(co_agl), 255, 
#     transform=crs.PlateCarree(), 
#     cmap=cmap)
norm1 = mpl.colors.Normalize(vmin=0, vmax=max_wspd)

cbar1=fig.colorbar(mpl.cm.ScalarMappable(norm=norm1, cmap=cmap),
ax=ax[1], orientation='vertical',  extend='both',
label="PM2.5 @50m")
# cbar2=fig.colorbar(mpl.cm.ScalarMappable(norm=norm2, cmap=cmap2),
# ax=ax[1], orientation='horizontal',  extend='both',
# label="co ppmv")

    





# h,l=ax[0].get_legend_handles_labels()
# ax[0].legend(h,l)

plt.show()