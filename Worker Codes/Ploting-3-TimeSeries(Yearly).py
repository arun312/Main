import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import geopandas as gp
from datetime import datetime

dataDIR="../Datasets/Nd_Winter.nc"
data = xr.open_dataset(dataDIR)
data['Nd'] = data['__xarray_dataarray_variable__']
data = data.drop(['__xarray_dataarray_variable__'])

Nd=data.Nd
Nd=Nd[:,:,:].astype(np.double)
Nd=Nd.sortby('time')
lon,lat,time=Nd.indexes.values()

a=[]

for i in range(2005,2021):
    
    start=datetime.strptime(str(i)+'-12-01','%Y-%m-%d')
    end=datetime.strptime(str(i+1)+'-02-28','%Y-%m-%d')

    xx=Nd.sel(time=slice(str(start),str(end)))
    mean=xx.mean(skipna=True)
    out='%s  %s'%(i,mean.data)
    
    print(mean.data)


print('########### \n')

#AOD
dataDIR="../Datasets/FINAL_MODIS_WINTER.nc"
data = xr.open_dataset(dataDIR)
AOD=data.AOD_550_Dark_Target_Deep_Blue_Combined_Mean
AOD=AOD[:,:,:].astype(np.double)
AOD=AOD.sortby('time')
lon,lat,time=AOD.indexes.values()
for i in range(2005,2021):
    
    start=datetime.strptime(str(i)+'-12-01','%Y-%m-%d')
    end=datetime.strptime(str(i+1)+'-02-28','%Y-%m-%d')

    xx=AOD.sel(time=slice(str(start),str(end)))
    mean=xx.mean(skipna=True)
    out='%s  %s'%(i,mean.data)
    print(mean.data)
