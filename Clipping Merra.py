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
os.chdir('/Volumes/PtatoBasket/Datasets/MERRA2/Winter')

#Sorting to Winter and Premon
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

    AOD=ds.TOTSCATAU
    angstr=ds.TOTANGSTR

    #To Daily Data
    AOD=AOD.mean(dim='time', skipna=True)
    angstr=angstr.mean(dim='time', skipna=True)

    AOD=AOD[:,:].astype(np.double)
    angstr=angstr[:,:].astype(np.double)

    #Make AI
    AI=AOD*angstr
    lat,lon=AI.indexes.values()
    datam = np.ma.masked_array(AI, np.isnan(AI))
    df=xr.merge([xr.DataArray(AOD, name="AOD"),xr.DataArray(AI, name="AI")])

    mask=xr.open_dataarray('/Volumes/ACIML/Main/SHPs/BOB_MASK-Merra1.nc')
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

fname=str('MERRA-Winter')
fin.to_netcdf('/Volumes/ACIML/Main/'+fname+'.nc')

print('Clipping completed in %s seconds'%(time.time()-st))