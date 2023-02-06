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
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
import cartopy.feature as cfeature


Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'
Input_Dir = '/Users/lmatak/Desktop/some_wrfout_files/'
# Choose between : 'Gustav', 'Irma', 'Katrina', 'Maria'
HNS = ['Iota'] #,'Dorian','Iota','Igor']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['8km']
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TMS = ['NoTurb']
# Choose between : 'cLh0p2', 'cLh0p5', 'cLh1p0', 'cLh1p5'
PBLS=['YSU']

os.environ["PATH"]+=":/Library/TeX/texbin/"
print(os.environ["PATH"])
plt.rcParams.update({
    "text.usetex":True,
    "font.family":'Times New Roman'
})
size=35
#HERE YOU CHANGE
CLS = ['250','1.0'] #,'1000']
# CLS = ['xkzm_0.2','1.0','xkzm_5.0']

#don't change this!! ## CHANGE FEW ROWS UP!!
name_word='_lvls'


def some_fun(Alt,HN,PBL,CLS,Input_Dir):
    Time_idx=0
    max_wspds=[]
    Input_Dir = Input_Dir
    for CL in CLS:
        
        # for CL in CLS:
        ncfiles = []                    
        Hurricane_Setting = HN + '_8km_NoTurb_' + PBL +'_hpbl_'+CL
        Input_Dir_1 = Input_Dir +  Hurricane_Setting
        os.chdir(Input_Dir_1)

        ncfiles = list_ncfiles(Input_Dir_1, ncfiles)
        Data = Dataset(ncfiles[0])  
        # print('is something happening?')
        wspd = getvar(Data, "wspd", timeidx = Time_idx)
        height = getvar(Data, "height_agl")
        wspd_500 = interplevel(wspd, height, Alt)
        
        max_wspds.append(float(np.max(wspd_500)))
    print('max spd',max_wspds)
    return(max_wspds[0])



# Choose between: '0', '1', '2', '3', '4', '5'
Time_idx = 0
row=0
col=0
# Choose the altitude:
Alt = 500
max_wspd=0
nbins=7
cmap_name='my_colors'
#coolwarm is the red-blue one
# cmap=plt.get_cmap(
#     'plasma')
cmap=plt.get_cmap(
    'twilight_shifted')
# Create a figure
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15.9, 8.2),subplot_kw={'projection': crs.PlateCarree()},dpi=350)
# fig.subplots_adjust(wspace=0,right=0.3)
# colors=['lightyellow','indigo','lightgreen','lightblue','blue','yellow','red','black']
# cm = LinearSegmentedColormap.from_list(
#         cmap_name, colors, N=nbins)

for HN in HNS:
    for GS in GSS:
        for TM in TMS:
            i = 0
            for PBL in PBLS:
                for CL in CLS: 

                    print('row',row,'col',col)
                    ncfiles = []                    
                    Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL
                    Input_Dir_1 = Input_Dir +  Hurricane_Setting
                    # Set the working space.
                    os.chdir(Input_Dir_1)

                    ncfiles = list_ncfiles(Input_Dir_1, ncfiles)
                    Data = Dataset(ncfiles[0])  
                

                    
                    # Open the NetCDF file
                    

                    #Extract the necessary data to plot the contour map.
                    slp = getvar(Data, "slp", timeidx = Time_idx)
                    z = getvar(Data, "z", timeidx = Time_idx)
                    wspd = getvar(Data, "wspd", timeidx = Time_idx)
                    p = getvar(Data,'pressure')
                    height = getvar(Data, "height_agl")

                    

                    # print('row = ',row)
                    # print('col = ',col)
                    ax[col].stock_img()
                    # ax[row,col].coastlines('50m', linewidth=0.8)
                    # ax[col].add_feature(cfeature.LAND)
                    # ax[col].add_feature(cfeature.OCEAN)
                    gl = ax[col].gridlines(crs=crs.PlateCarree(), draw_labels=True,
                        linewidth=0.2, color='black', alpha=0.2, linestyle='--')
                    gl.top_labels = False
                    gl.right_labels = False
                    gl.xlabel_style= {'size': size-3, 'color': 'black'}  
                    gl.ylabel_style= {'size': size-3, 'color': 'black'}
                    # if (row == 0 and col == 2):
                    #     lon_formatter = LongitudeFormatter(zero_direction_label=True)
                    #     ax[row,col].xaxis.set_major_formatter(lon_formatter)

                    #     gl.left_labels = False
                    #     gl.bottom_labels = False
                    #     ax[row,col].set_xticks([-60.5, -61.3, -62])
                    #     ax[row,col].tick_params(axis='x', labelsize=9, pad=5, length=0, direction = 'in', width = 2)
                    
                    if col != 0:
                        gl.left_labels = False
                    
                    # ax[row,col].tick_params(axis='y', labelsize=8, length=0, direction = 'in', width = 2)
                    

                    # Interpolate geopotential height, u, and v winds to 500 hPa
                    wspd_500 = interplevel(wspd, height, Alt)

                    # print(CL+' max wspd = ',np.max(wspd))

                    # Get the latitude and longitude points
                    lats, lons = latlon_coords(wspd_500)
                    
                    lat_min_slp=np.where(slp == np.amin(slp))[0]
                    lon_min_slp=np.where(slp == np.amin(slp))[1]
                    # print(lat_min_slp,lon_min_slp)

                    slp_coord_lat= float(lats[lat_min_slp][0][0])

                    slp_coord_long=float(lons[0][lon_min_slp])
                    # Get the cartopy mapping object
                    cart_proj = get_cartopy(wspd_500)

                    if col==0:
                        print('this is for '+HN)
                        w_max=some_fun(Alt,HN,PBL,CLS,Input_Dir)
                        if HN == 'Igor' and CL =='xkzm_0.2' and PBL =='YSU' :

                            w_max=w_max+7
                        if PBL == 'MYJ':
                            w_max=w_max+7
                        # print('wmax=',w_max)
                        w_min=0

                    w_max=70
                    im_cbar = ax[col].contourf(to_np(lons), to_np(lats), to_np(wspd_500), 300, vmin=w_min, vmax =w_max, 
                        transform=crs.PlateCarree(), 
                        cmap=cmap)
                    # cmap.set_over('red')
                    # cmap.set_under('blue')
                    # if col == 0:
                        
                    #     cbar_ax = fig.add_axes([0.85, 0.75-row/6.3, 0.025, 0.15])
                    if col==1:
                        divnorm = mpl.colors.TwoSlopeNorm(vmin=w_min, vcenter=(w_min+w_max)/2, vmax=w_max)
                        norm = mpl.colors.Normalize(vmin=w_min, vmax=73)
                        cax1= plt.axes([0.91, 0.15, 0.01, 0.68]) 
                        cbar=fig.colorbar(mpl.cm.ScalarMappable(norm=divnorm, cmap=cmap),
                        cax=cax1, orientation='vertical', aspect=20, extend='max',
                        )
                        cbar.ax.tick_params(labelsize=size) 
                        cbar.set_label(r'Wind Speed $\mathrm{(\,ms^{-1}) \,}$', size=size)
                        

                    CS = ax[col].contour(to_np(lons), to_np(lats), to_np(slp), 6, colors="black", alpha=1,
                        transform=crs.PlateCarree(), linewidths = 1)

                    ax[col].set_extent([slp_coord_long+0.8,slp_coord_long-0.8,slp_coord_lat-0.65,slp_coord_lat+0.65])

                    
                        
                    ax[col].clabel(CS, CS.levels, inline=True, fontsize=8, inline_spacing=8,  use_clabeltext=True)
                    
                    col+=1
                    if col==2:
                        row=1
                        col =0




if CLS[0] == 'xkzm_0.2':

    ax[0].set_title(r'$C_{ k }$\_0.2\_'+PBLS[0], size=size)
    ax[1].set_title('Default Case '+PBLS[0],size=size)
    # ax[0,2].set_title(r'$C_{ k }$\_5.0\_'+PBLS[0],size=size)
else:   
    # ax[0,0].set_title(r'$K_{ m }\_lvl_{ 4 }$\_'+PBLS[0], size=size)
    # ax[0,1].set_title(r'$K_{ m }\_lvl_{ 6 }$\_'+PBLS[0] ,size=size)
    # ax[0,2].set_title('Default Case - '+PBLS[0],size=size)
    ax[0].set_title(r'Reduced PBL Depth', size=size)
    # ax[0,2].set_title(r'Increased PBL height' ,size=size)
    ax[1].set_title('Default PBL Depth',size=size)


        

for i in range(len(HNS)):
    if (HNS[i] == 'Dorian' or HNS[i] == 'Lorenzo'):
        ax[i,0].annotate(HNS[i], xy=(-0.35, 0.85), xycoords='axes fraction',
                xytext=(0, 0), textcoords='offset points',
                ha="right", va="top",size=size,
                rotation = 90
                )
    else:
        ax[i].annotate(HNS[i], xy=(-0.25, 0.65), xycoords='axes fraction',
                    xytext=(0, 0), textcoords='offset points',
                    ha="right", va="top",size=size,
                    rotation = 90
                    )

                    #x axis


# plt.show()
# print('saved fig as: CONTOURS_DENVER_ABS.pdf')
plt.savefig('/Users/lmatak/Desktop/leo_python_scripts/Poster_figs/created_figs/CONTOURS_DENVER_ABS.png',bbox_inches='tight')