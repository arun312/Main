import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import geopandas as gp
from datetime import datetime
import time as t
import pandas as pd

st=t.time()

dataDIR="../Datasets/Nd_PreMon.nc"
data = xr.open_dataset(dataDIR)
data['Nd'] = data['__xarray_dataarray_variable__']
data = data.drop(['__xarray_dataarray_variable__'])

Nd=data.Nd
Nd=Nd[:,:,:].astype(np.double)
Nd=Nd.sortby('time')
lon,lat,time=Nd.indexes.values()
tt=pd.to_datetime(time)

# #AOD
dataDIR="../Datasets/FINAL_MODIS_PreMon.nc"
data = xr.open_dataset(dataDIR)
AOD=data.AOD_550_Dark_Target_Deep_Blue_Combined_Mean
AOD=AOD[:,:,:].astype(np.double)
AOD=AOD.sortby('time')




dNd=[]
dAOD=[]
dDate=[]

day=[]

# for i in range(2005,2021):
#     try:
#         xxx=str(i)+'-02-29'
#         Nd = Nd.drop([np.datetime64(xxx)], dim='time')
      
#     except Exception as e:
#         print(e)

#     try:
#         xxx=str(i)+'-02-29'
#         AOD = AOD.drop([np.datetime64(xxx)], dim='time')
#     except Exception as e:
#         print(e)

lon,lat,time=AOD.indexes.values()

for i in range(0,time.size):
    dd=time[i].replace(year=2005)
    day.append(str(dd.timetuple().tm_yday ))
    dDate.append(str(dd.strftime("%B-%d")))



Nd.coords['time']=day
AOD.coords['time']=day

meanNd=Nd.groupby('time').mean()
meanAOD=AOD.groupby('time').mean()


for i in range(0,92):
    dNd.append(meanNd[i,:,:].mean().data)
    dAOD.append(meanAOD[i,:,:].mean().data)

array=[]
array.append(dDate[0:92])
array.append(dNd)
array.append(dAOD)

df=pd.DataFrame(array).T
df.to_excel(excel_writer='Daily-TimeSeries_PreMon1.xlsx')

print('Writing completed in %s seconds'%(t.time()-st))