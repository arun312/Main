import os
import glob                                                                 
import numpy as np
import xarray as xr
from pyhdf.SD import SD, SDC
from datetime import datetime,date,timedelta
import rioxarray as rxr
import geopandas as gp
import matplotlib.pyplot as plt
# from zmq import ctx_opt_names #for the Ploting purpose
import time
import pandas as pd

st=time.time()

def data_correction(DATAFIELD):
    data2D = hdf.select(DATAFIELD)
    data = data2D[:,:].astype(np.double)

    # Retrieve attributes.
    attrs = data2D.attributes(full=1)
    aoa=attrs["add_offset"]
    add_offset = aoa[0]
    fva=attrs["_FillValue"]
    _FillValue = fva[0]
    sfa=attrs["scale_factor"]
    scale_factor = sfa[0]        
    ua=attrs["units"]
    units = ua[0]
    data[data == _FillValue] = np.nan
    data = (data - add_offset) * scale_factor 
    datam = np.ma.masked_array(data, np.isnan(data))
    return datam

a=[]

os.chdir('/Volumes/PtatoBasket/ACIML/Datasets/PrecipitableWater-MODIS/Winter/')

for file in list(glob.glob('A*.hdf')):

    reader = open(file)
    ds=xr.open_dataset(file)
    hdf = SD(file, SDC.READ)

    # Read geolocation dataset.
    lat = hdf.select('YDim')
    latitude = lat[:]
    lon = hdf.select('XDim')
    longitude = lon[:]

    # #Getting the dates from filename
    # arr=str(file).split(".")
    # year=str(arr[1])[1:5]
    # days=str(arr[1])[5:]
    # dat=datetime(int(year), 1, 1) + timedelta(int(days) - 1)
    # dat=(dat-datetime(2005,1,1)).days


    #Getting the dates from filename(UPDATED)
    arr=str(file).split(".")
    year=str(arr[0])[1:5]
    days=str(arr[0])[5:]
    dat=datetime(int(year), 1, 1) + timedelta(int(days) - 1)
    # dat=(dat-datetime(2005,1,1)).days
    # January 1st, 1900
    start_datetime = datetime(1900, 1, 1)

    # Calculate the time delta (difference) in hours
    dat = (dat - start_datetime).total_seconds() / 3600

    # Reading Variables
    # cer = data_correction('Cloud_Effective_Radius_Liquid_Mean')
    # cot=data_correction('Cloud_Optical_Thickness_Combined_Mean')
    # ctt=data_correction('Cloud_Top_Temperature_Mean')
    # ctp=data_correction('Cloud_Top_Pressure_Mean')
    # aod=data_correction('AOD_550_Dark_Target_Deep_Blue_Combined_Mean')
    lwp=data_correction('Atmospheric_Water_Vapor_QA_Mean')


    df = xr.Dataset(
            data_vars={'Atmospheric_Water_Vapor_QA_Mean':    (('latitude', 'longitude' ), lwp),
                        # 'Cloud_Optical_Thickness_Combined_Mean':(('latitude', 'longitude' ), cot),
                        # 'Cloud_Top_Temperature_Mean':(('latitude', 'longitude' ), ctt),
                        # 'Cloud_Top_Pressure_Mean':(('latitude', 'longitude' ), ctp),
                        # 'AOD_550_Dark_Target_Deep_Blue_Combined_Mean':(('latitude', 'longitude' ), aod),
                    },
            coords={'longitude': longitude,
                'latitude': latitude,
                'time':dat,
            })

    # df.Cloud_Effective_Radius_Liquid_Mean.attrs['long_name'] = 'Cloud Effective Radius'
    # df.Cloud_Optical_Thickness_Combined_Mean.attrs['long_name'] = 'Cloud Optical Radius'
    # df.Cloud_Top_Temperature_Mean.attrs['long_name'] = 'Cloud Top Temperautre'
    # df.Cloud_Top_Pressure_Mean.attrs['long_name'] = 'Cloud Top Pressure'
    df.LWP.attrs['long_name'] = 'Atmospheric_Water_Vapor_QA_Mean'

    df.longitude.attrs['standard_name'] = 'longitude'
    df.longitude.attrs['long_name'] = 'longitude'
    df.longitude.attrs['units'] = 'degrees_east'
    df.longitude.attrs['axis'] = 'X'

    df.latitude.attrs['standard_name'] = 'latitude'
    df.latitude.attrs['long_name'] = 'latitude'
    df.latitude.attrs['units'] = 'degrees_north'
    df.latitude.attrs['axis'] = 'Y'


    df.time.attrs['standard_name'] = 'time'
    df.time.attrs['axis'] = 'T'
    df.time.attrs['long_name'] = 'time'
    df.time.attrs['units'] = "hours since 1900-01-01 00:00:00.0"
    df.time.attrs['calendar'] ="gregorian" 

    #Clipping to shape File and Creating Mask File
    shapefile ="/Volumes/ACIML/Main/SHPs/BOB_OCEAN/BOB_OCEAN.shp"
    countries=gp.read_file(shapefile,engine='pyogrio')
    # c_list=list(countries['featurecla'])
    # c_list_unique=set(list(countries['featurecla']))
    # indexes=[c_list.index(x) for x in c_list_unique]
    # countries_mask_poly=regionmask.Regions(outlines=countries.geometry[indexes],name='featurecla',numbers=indexes,names=countries.featurecla[indexes])
    # print('It is Clipping')
    # mask=countries_mask_poly.mask(df,lat_name='latitude',lon_name='longitude')
    # mask.to_netcdf('BOB_MASK.nc')

    mask=xr.open_dataarray('/Volumes/ACIML/Main/SHPs/BOB_MASK.nc')
    masked_shape=df.where(mask==0)
    min_lon = 78.00
    max_lon = 96.00
    min_lat = 8.00
    max_lat = 23.00

    cropped_ds = masked_shape.sel(latitude=slice(max_lat,min_lat), longitude=slice(min_lon,max_lon))
    a.append(cropped_ds)

fin=xr.concat(a, dim="time")
# fname=str(file)[:-3]
fname=str('PreMonDaily_PrecipWaterTest')
# fin.to_netcdf('/Volumes/ACIML/Datasets/'+fname+'.nc')
fin.to_netcdf('../'+fname+'.nc')

# plt.figure(figsize=(12,8))
# ax=plt.axes()
# cropped_ds.Cloud_Top_Pressure_Mean.plot(ax=ax)
# countries.plot(ax=ax,alpha=0.8,facecolor='none')
# plt.show()

print('Clipping completed in %s seconds'%(time.time()-st))