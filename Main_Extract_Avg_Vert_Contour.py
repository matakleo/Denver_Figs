from cmath import nan
from all_functions import Calculate_Distance_Haversine,list_ncfiles,create_file

from math import (atan, cos, sin, sqrt)
from netCDF4 import Dataset
from wrf import getvar
import numpy as np
import math
import csv
import os




Input_Dir = '/Users/lmatak/Downloads/Meng_wrfout_vert_contors/'

Output_Dir = '/Users/lmatak/Downloads/Meng_wrfout_vert_contors/wtf_vert_contours/'

# Choose between :  'Florence', 'Gustav', 'Irma', 'Katrina', 'Maria'
# Choose between :  'Gordon', 'Helene', 'Jerry', 'Nadine', 'Sally'
HNS = ['Dorian']#,'Iota', 'Lorenzo', 'Igor','Dorian']

# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['8km']
PBL='YSU'
TM='NoTurb'
CLS=['changeClz_1p0000','changeClz_0p0100','changeClz_100p0000']
# Identify the time step
Time_Step = 6
# Identify the time index
Time_Idx = 0
# Space step
DR   = 8 # km
RMAX = 200 #km
nlev = 14  # levels
Pi   = 3.14159265359
#-------------------------------------------------------------------------------------------------------------------
# Define all hurricane's settings 

Idx = 0
for HN in HNS:
    for CL in CLS:

                
                    RMW = []
                    ncfiles = []
                    U1      = []
                    U2      = []
                    Z       = []
                    lat     = []
                    lon     = []
                    SLP     = []
                    UR      = np.zeros(([int(RMAX/DR)+1, nlev]))
                    UT      = np.zeros(([int(RMAX/DR)+1, nlev]))
                    
                    Hurricane_Setting = 'WRFONLY_NoTurb_8km_isftcflx_1_'+CL
                    print (Hurricane_Setting)
                    Input_Dir_1 = Input_Dir + '/' + HN + '/' +Hurricane_Setting
                    ncfiles = list_ncfiles (Input_Dir_1, ncfiles)
                    print(ncfiles)
                    for ncfile in ncfiles:
                        os.chdir(Input_Dir_1)
                        ncfile_name = ncfile[:-6]
                        ncfile = Dataset(ncfile)
                        U1      = np.array(getvar(ncfile, "U", Time_Idx))
                        U2      = np.array(getvar(ncfile, "V", Time_Idx))
                        Z       = np.array(getvar(ncfile, "z", Time_Idx))[:,0, 0]
                        SLP     = np.array(getvar(ncfile, "slp", Time_Idx))
                        lat     = np.array(getvar(ncfile, "XLAT", Time_Idx))[:,0]
                        lon     = np.array(getvar(ncfile, "XLONG", Time_Idx))[0,:]
                        Eye_idx = np.where(SLP == np.amin(SLP))
                        Count_H = 0
                        Count_V = 0
                        for R in range (0, RMAX, DR):
                            Avg_UR  = np.zeros((nlev))
                            Avg_UT  = np.zeros((nlev))
                            Count   = 0
                            for i in range (len(lat)):
                                for j in range (len(lon)):
                                    try:
                                        D = Calculate_Distance_Haversine(lat[Eye_idx[0]], lon[Eye_idx[1]], lat[i], lon[j])

                                        if R < D and D < R+DR:

                                            # Get the angle with repsect to the eye of the hurricane
                                            Delta_Lat = Calculate_Distance_Haversine (lat[Eye_idx[0]], lon[Eye_idx[1]], lat[i], lon[Eye_idx[1]])
                                            Delta_Lon = Calculate_Distance_Haversine (lat[Eye_idx[0]], lon[Eye_idx[1]], lat[Eye_idx[0]], lon[j])
                                            Theta = 0.0
                                            if (Delta_Lon == 0.0):
                                                if (lat[i] >= Eye_idx[0]):
                                                    
                                                    Theta = Pi/2
                                                else:
                                                    Theta = -Pi/2

                                                
                                            else:
                                                Theta = atan(Delta_Lat/Delta_Lon)
                                                if (lon[j] <= lon[Eye_idx[1]]) and (lat[i] >= lat[Eye_idx[0]]):                         # 2nd Quadrant
                                                        Theta = Pi - Theta
                                                if (lon[j] <= lon[Eye_idx[1]]) and (lat[i] <= lat[Eye_idx[0]]):                         # 3rd Quadrant
                                                        Theta = Pi + Theta
                                                if (lon[j] >= lon[Eye_idx[1]]) and (lat[i] <= lat[Eye_idx[0]]):                         # 4th Quadrant
                                                        Theta = - Theta
                                              

                                            # Project the wind intensity to cylindrical coordinates
                                            for k in range(nlev):
                                                
                                                Avg_UR[k] += U1 [k, i, j] * cos(Theta) + U2 [k, i, j] * sin(Theta)
                                                Avg_UT[k] += -U1 [k, i, j] * sin(Theta) + U2 [k, i, j] * cos(Theta)
                                                # if Avg_UT[k]==nan:
                                                #     Avg_UT[k]=0
                                                # if Avg_UR[k]==nan:
                                                #     Avg_UR[k]=0
                                            Count  += 1 
                                            # print(Avg_UT[0])
                                    except (TypeError):
                                        continue
                            UR[Count_H, :] = Avg_UR/Count
                            UT[Count_H, :] = Avg_UT/Count
                           
                            # if Avg_UR/Count == nan:
                            #     UR[Count_H, :]=0
                            # if Avg_UT/Count == nan:  
                            #     UT[Count_H, :] = 0  
                            
                            Count_H += 1

    # #-------------------------------------------------------------------------------------------------------------------
                        UR[np.isnan(UR)] = 0
                        UT[np.isnan(UT)] = 0

                        create_file (Output_Dir, HN)
                        create_file (Output_Dir + HN + '/', Hurricane_Setting)
                        # create_file (Output_Dir + HN + '/' + GS + '/', Hurricane_Setting)

    # Export Radial Data
                        create_file (Output_Dir + HN  + '/' + Hurricane_Setting + '/', 'Radial_Data')
                        
                        file_name = ncfile_name
                        MyFile=open("%s.csv" %file_name,'w')
                        MyFile.write(',')
                        for R in range (0, RMAX, DR):
                            MyFile.write(str(R) + ',')
                        MyFile.write('\n')
                        
                        for n in range(nlev):
                            MyFile.write(str(Z[n]) + ',')
                            for m in range (int(RMAX/DR)+1):
                                MyFile.write(str(UR[m,n]) + ',')
                            MyFile.write('\n')

    # Export Tangential Data
                        create_file (Output_Dir + HN  + '/' + Hurricane_Setting + '/', 'Tangential_Data')
                        
                        file_name = ncfile_name
                        MyFile=open("%s.csv" %file_name,'w')
                        MyFile.write(',')
                        for R in range (0, RMAX, DR):
                            MyFile.write(str(R) + ',')
                        MyFile.write('\n')
                        
                        for n in range(nlev):
                            MyFile.write(str(Z[n]) + ',')
                            for m in range (int(RMAX/DR)+1):
                                MyFile.write(str(UT[m,n]) + ',')
                            MyFile.write('\n')


                    print ("Done with " + Hurricane_Setting + "!")
        # Idx+=1                    
