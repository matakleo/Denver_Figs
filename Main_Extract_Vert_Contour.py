from re import X
from all_functions import Calculate_Distance_Haversine,list_ncfiles,create_file
from math import (atan, cos, sin, sqrt)
from netCDF4 import Dataset
from wrf import getvar
import numpy as np
import math
import csv
import os



Input_Dir = '/Users/lmatak/Desktop/some_wrfout_files/new_ones/'
Output_Dir = '/Users/lmatak/Desktop/some_wrfout_files/new_ones/wtf_vert_contours/'



# Choose between :  'Florence', 'Gustav', 'Irma', 'Katrina', 'Maria'
# Choose between :  'Gordon', 'Helene', 'Jerry', 'Nadine', 'Sally'
HNS = ['Iota']#, 'Lorenzo', 'Igor']
# Choose the simulation duration: '48', '30', '48', '30', '48'
# Choose the simulation duration: '48', '72', '36', '30', '36'
# Choose between : '2km', '4km', '8km', '16km', '32km'
# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['8km']
PBL='YSU'
TM='NoTurb'
CLS=['250','1.0']
# CLS=['lvl_3','lvl_5','1.0']
#---------------------------------------------------------------------------------------
#Input_Dir = '/Users/oromdhan/Desktop/Test/'
#Output_Dir = '/Users/oromdhan/Desktop/Test/Output/'

# Choose between :  'Florence', 'Gustav', 'Irma', 'Katrina', 'Maria'
# Choose between :  'Gordon', 'Helene', 'Jerry', 'Nadine', 'Sally'
#HNS = ['Florence']
# Choose the simulation duration: '48', '30', '48', '30', '48'
# Choose the simulation duration: '48', '72', '36', '30', '36'
#HR = ['48']
# Choose between : '2km', '4km', '8km', '16km', '32km'
#GSS = ['32km']
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
#TMS = ['Smag2D']
# Choose between : 'cLh0p25', 'cLh0p5', 'cLh1p0', 'cLh1p5'
#CLHS = ['cLh0p25']
# Angles.
#Angles = [0, 45, 90]
Angles = [0, 90]
# Space step
DR   = 8 # km
RMAX = 201 #km
nlev = 12  # levels
Pi   = 3.14159265359
#-------------------------------------------------------------------------------------------------------------------
# Define all hurricane's settings 

Idx = 0
for CL in CLS:
    for HN in HNS:
        for GS in GSS:

                    for Time_Idx in range(5):
                        try:
                            RMW = []
                            ncfiles = []
                            U1      = []
                            U2      = []
                            Z       = []
                            lat     = []
                            lon     = []
                            SLP     = []


                            Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL + '_hpbl_' +CL
                            print ('Hurr setting: '+Hurricane_Setting)
                            Input_Dir_1 = Input_Dir  + Hurricane_Setting
                            ncfiles = list_ncfiles (Input_Dir_1, ncfiles)
                            

                            for ncfile in ncfiles:
                                os.chdir(Input_Dir_1)
                                print('Input dir: '+Input_Dir_1)
                                ncfile_name = ncfile
                                print('ncfile: '+ncfile)
                                ncfile = Dataset(ncfile)
                                U1      = np.array(getvar(ncfile, "U", Time_Idx))
                                U2      = np.array(getvar(ncfile, "V", Time_Idx))
                                Z       = np.array(getvar(ncfile, "z", Time_Idx))[:,0, 0]
                                SLP     = np.array(getvar(ncfile, "slp", Time_Idx))
                                lat     = np.array(getvar(ncfile, "XLAT", Time_Idx))[:,0]
                                lon     = np.array(getvar(ncfile, "XLONG", Time_Idx))[0,:]
                                Eye_idx = np.where(SLP == np.amin(SLP))

            #--------------------------------------------------------Angle = 0-----------------------------------------------------------      
                                for Angle in Angles:
                                    print (Angle)
                                    if (Angle == 0) :
                                        UR      = np.zeros(([int(2*RMAX/DR)+5, nlev]))
                                        UT      = np.zeros(([int(2*RMAX/DR)+5, nlev]))
                                        Rd      = []
                                        Count_H   = 0
                                        for j in range (len(lon)):
                                            try:
                                                Theta = 0
                                                D = Calculate_Distance_Haversine(lat[Eye_idx[0]], lon[Eye_idx[1]], lat[Eye_idx[0]], lon[j])
                                                if lon[j] < lon[Eye_idx[1]]:
                                                    D     = -D
                                                    Theta = Pi
                                                if (abs(D) < RMAX):
                                                    # Project the wind intensity to cylindrical coordinates
                                                    Rd.append(D)
                                                    for k in range(nlev):
                                                        UR[Count_H, k] = U1 [k, [Eye_idx[0]], j] * cos(Theta) + U2 [k, [Eye_idx[0]], j] * sin(Theta)
                                                        UT[Count_H, k] = -U1 [k, [Eye_idx[0]], j] * sin(Theta) + U2 [k, [Eye_idx[0]], j] * cos(Theta)
                                                    Count_H += 1

                                            except (TypeError):
                                                continue

                #--------------------------------------------------------Angle = 90-----------------------------------------------------------      
                                    elif (Angle == 90) :
                                        UR      = np.zeros(([int(2*RMAX/DR)+5, nlev]))
                                        UT      = np.zeros(([int(2*RMAX/DR)+5, nlev]))
                                        Rd      = []
                                        Count_H   = 0
                                        for i in range (len(lat)):
                                            try:
                                                Theta = 90
                                                D = Calculate_Distance_Haversine(lat[Eye_idx[0]], lon[Eye_idx[1]], lat[i], lon[Eye_idx[1]])
                                                if lat[i] < lat[Eye_idx[0]]:
                                                    D     = -D
                                                    Theta = -Pi/2
                                                if (abs(D) < RMAX):
                                                    # Project the wind intensity to cylindrical coordinates
                                                    Rd.append(D)
                                                    for k in range(nlev):
                                                        UR[Count_H, k] = U1 [k, i, Eye_idx[1]] * cos(Theta) + U2 [k, i, Eye_idx[1]] * sin(Theta)
                                                        UT[Count_H, k] = -U1 [k, i, Eye_idx[1]] * sin(Theta) + U2 [k, i, Eye_idx[1]] * cos(Theta)
                                                    Count_H += 1

                                            except (TypeError):
                                                continue

                #--------------------------------------------------------Angle = 45-----------------------------------------------------------      
                                    elif (Angle == 45) :
                                        UR      = np.zeros(([int(2*RMAX/DR)+5, nlev]))
                                        UT      = np.zeros(([int(2*RMAX/DR)+5, nlev]))
                                        Rd      = []
                                        Count_H   = 0
                                        x = 0
                                        y = 0
                                        if Eye_idx[0] > Eye_idx[1]:
                                            x = Eye_idx[0] - Eye_idx[1]
                                        elif Eye_idx[0] < Eye_idx[1]:
                                            y = Eye_idx[1] - Eye_idx[0]
                                        for i in range (np.min(([len(lat)-int(x), len(lon)-int(y)]))):
                                            try:
                                                Theta = 45
                                                D = Calculate_Distance_Haversine(lat[Eye_idx[0]], lon[Eye_idx[1]], lat[x+i], lon[y+i])
                                                if lat[i] < lat[Eye_idx[0]]:
                                                    D     = -D
                                                    Theta = -3*Pi/4
                                                if (abs(D) < RMAX):
                                                    #print (D)
                                                    # Project the wind intensity to cylindrical coordinates
                                                    Rd.append(D)
                                                    for k in range(nlev):
                                                        UR[Count_H, k] = U1 [k, i, i] * cos(Theta) + U2 [k, i, i] * sin(Theta)
                                                        UT[Count_H, k] = -U1 [k, i, i] * sin(Theta) + U2 [k, i, i] * cos(Theta)
                                                    Count_H += 1

                                            except (TypeError):
                                                continue

                #-------------------------------------------------------------------------------------------------------------------

                                    UR[np.isnan(UR)] = 0
                                    UT[np.isnan(UT)] = 0

                                    create_file (Output_Dir, HN)
                                    create_file (Output_Dir + HN + '/', GS)
                                    create_file (Output_Dir + HN + '/' + GS + '/', Hurricane_Setting)

                # Export Radial Data
                                    create_file (Output_Dir + HN + '/' + GS + '/' + Hurricane_Setting + '/', 'Radial_Data')
                                    
                                    file_name = ncfile_name + '_POSTER_' + str(Angle) + 'degrees' + '_' + str(Time_Idx)
                                    print('file name:  '+file_name)
                                    MyFile=open("%s.csv" %file_name,'w')
                                    MyFile.write(',')
                                    for i in range (len(Rd)):
                                        MyFile.write(str(Rd[i]) + ',')
                                    MyFile.write('\n')
                                    
                                    for n in range(nlev):
                                        MyFile.write(str(Z[n]) + ',')
                                        for m in range (len(Rd)):
                                            MyFile.write(str(UR[m,n]) + ',')
                                        MyFile.write('\n')

                # Export Tangential Data
                                    create_file (Output_Dir + HN + '/' + GS + '/' + Hurricane_Setting + '/', 'Tangential_Data')
                                    
                                    file_name = ncfile_name + '_POSTER_' + str(Angle) + 'degrees' + '_' + str(Time_Idx)
                                    MyFile=open("%s.csv" %file_name,'w')
                                    MyFile.write(',')
                                    for i in range (len(Rd)):
                                        MyFile.write(str(Rd[i]) + ',')
                                    MyFile.write('\n')
                                    
                                    for n in range(nlev):
                                        MyFile.write(str(Z[n]) + ',')
                                        for m in range (len(Rd)):
                                            MyFile.write(str(UT[m,n]) + ',')
                                        MyFile.write('\n')


                            print ("Done with " + Hurricane_Setting + "!")
                        except:continue
        Idx+=1         
#-------------------------------------------------------------------------------------------------------------------
            
