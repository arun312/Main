import os
import glob                                                                 
import numpy as np
import xarray as xr
from pyhdf.SD import SD, SDC
from datetime import datetime,date,timedelta
import rioxarray as rxr
import geopandas as gp
import matplotlib.pyplot as plt
from zmq import ctx_opt_names #for the Ploting purpose
import time
import pandas as pd
import shutil

import regionmask

st=time.time()
os.chdir('/Volumes/PtatoBasket/Datasets/N_MERRA2/MERRA2/PreMon')

# # Sorting to Winter and Premon
# for file in list(glob.glob('MERRA2_*.nc4')):
#     month=str(file)[-12:-10]
#     if month=='01':
#         shutil.move(file, 'Winter/'+file)
#     elif month=='02':
#         shutil.move(file, 'Winter/'+file)

#     elif month=='12':
#         shutil.move(file, 'Winter/'+file)

#     elif month=='03':
#         shutil.move(file, 'PreMon/'+file)

#     elif month=='04':
#         shutil.move(file, 'PreMon/'+file)

#     elif month=='05':
#         shutil.move(file, 'PreMon/'+file)

#Real Clipping
xxx=[]
a=[]
for file in list(glob.glob('MERRA2_*.nc4')):

    ds=xr.open_dataset(file)

    # Retrieve attributes.
    attrs = ds.attrs
    dat=attrs["RangeBeginningDate"]
    dat=datetime.strptime(dat,'%Y-%m-%d')
    xxx.append(dat)

    AOD=ds.TOTEXTTAU
    angstr=ds.TOTANGSTR

    #To Daily Data
    AOD=AOD.mean(dim='time', skipna=True)
    angstr=angstr.mean(dim='time', skipna=True)

    AOD=AOD[:,:].astype(np.double)
    angstr=angstr[:,:].astype(np.double)

    #Make AI
    AI=AOD*angstr
    lat,lon=AI.indexes.values()

    SULFATE_AOD=ds.SUEXTTAU
    SULFATE_AOD=SULFATE_AOD.mean(dim='time', skipna=True)
    SULFATE_AOD=SULFATE_AOD[:,:].astype(np.double)

    SEASALT_AOD=ds.SSEXTTAU
    SEASALT_AOD=SEASALT_AOD.mean(dim='time', skipna=True)
    SEASALT_AOD=SEASALT_AOD[:,:].astype(np.double)

    OC_AOD=ds.OCEXTTAU
    OC_AOD=OC_AOD.mean(dim='time', skipna=True)
    OC_AOD=OC_AOD[:,:].astype(np.double)

    BC_AOD=ds.BCEXTTAU
    BC_AOD=BC_AOD.mean(dim='time', skipna=True)
    BC_AOD=BC_AOD[:,:].astype(np.double)

    DUST_AOD=ds.DUEXTTAU
    DUST_AOD=DUST_AOD.mean(dim='time', skipna=True)
    DUST_AOD=DUST_AOD[:,:].astype(np.double)

    datam = np.ma.masked_array(AI, np.isnan(AI))
    df=xr.merge([xr.DataArray(AOD, name="AOD"),xr.DataArray(SULFATE_AOD, name="SULFATE_AOD"),xr.DataArray(SEASALT_AOD, name="SEASALT_AOD"),xr.DataArray(OC_AOD, name="OC_AOD"),xr.DataArray(BC_AOD, name="BC_AOD"),xr.DataArray(DUST_AOD, name="DUST_AOD"),xr.DataArray(AI, name="AI")],)

    #Clipping to shape File and Creating Mask File
    # shapefile ="/Volumes/ACIML/Main/SHPs/BOB_OCEAN/BOB_OCEAN.shp"
    # countries=gp.read_file(shapefile,engine='pyogrio')
    # c_list=list(countries['featurecla'])
    # c_list_unique=set(list(countries['featurecla']))
    # indexes=[c_list.index(x) for x in c_list_unique]
    # countries_mask_poly=regionmask.Regions(outlines=countries.geometry[indexes],name='featurecla',numbers=indexes,names=countries.featurecla[indexes])
    # mask=countries_mask_poly.mask(df,lat_name='lat',lon_name='lon')
    # mask.to_netcdf('/Volumes/ACIML/Main/SHPs/BOB_MASK-Merra2.nc')

    mask=xr.open_dataarray('/Volumes/ACIML/Main/SHPs/BOB_MASK-Merra2.nc')
    masked_shape=df.where(mask==0)

    min_lon = 78.00
    max_lon = 96.00
    min_lat = 8.00
    max_lat = 23.00

    cropped_ds = masked_shape.sel(lat=slice(min_lat,max_lat), lon=slice(min_lon,max_lon))
    a.append(cropped_ds)

fin=xr.concat(a,"time")
fin.coords['time']=xxx
fin=fin.sortby('time')

fname=str('N_MERRA-PreMon')
fin.to_netcdf('/Volumes/ACIML/Main/'+fname+'.nc')

print('Clipping completed in %s seconds'%(time.time()-st))