# Winter=['01','02','12']
# Premon=['03','04','05']
# for i in range(2005,2021):
#     #FOR WINTER
#     # if (i%4)==0:
#     #     k=29
#     # else:
#     #     k=28
#     # s='%s-01-01..%s-02-%s'%(i,i,k)
#     # print(s)
#     # s='%s-12-01..%s-12-31'%(i,i)
#     # print(s)

#     #FOR PREMON
#     s='%s-03-01..%s-05-31'%(i,i)
#     print(s)

import os,sys #user to create and modify file name and save it
from netCDF4 import Dataset#to read the .nc files
import pandas as pd #for dataframe activities
from datetime import datetime,timedelta #for the time related activities
import matplotlib.pyplot as plt #for the Ploting purpose
import numpy as np #numerical fucntions
import datetime 
import warnings #to ignore unnecessary warnings
import xarray as xr
import numpy as np
import regionmask
import geopandas as gp
import glob                                                                 
from pyhdf.SD import SD, SDC
import pymannkendall as mk
# from zmq import ctx_opt_names #for the Ploting purpose
warnings.filterwarnings('ignore')

m=xr.DataArray('Nd.nc')
a=(m.indexes.values())