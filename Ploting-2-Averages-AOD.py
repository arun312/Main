import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import geopandas as gp


#AOD-Premon
ax = plt.axes(projection=ccrs.PlateCarree())

dataDIR="../Datasets/Unclipped_MODIS_PreMon.nc"
data = xr.open_dataset(dataDIR)
AOD=data.AOD_550_Dark_Target_Deep_Blue_Combined_Mean
AOD=AOD[:,:,:].astype(np.double)

AOD_mean=AOD.mean(dim='time', skipna=True)
# AOD_mean.plot(ax=ax) 
lat, lon = AOD_mean.indexes.values()

plt.pcolor(lon, lat, AOD_mean,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=.20,vmax=.80)
plt.colorbar()    

plt.contourf(lon, lat, AOD_mean,60,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=.20,vmax=.80)
plt.title("Nd_MEAN-PreMon(2005-2021)(cm^-3)")
ax.coastlines()

gridlines = ax.gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False

plt.title("AOD_MEAN-PreMon(2005-2021)")
plt.savefig('Unclipped_AOD_MEAN-PreMon(2005-2021).png',dpi=300)
# plt.show()
plt.clf()


#AOD-WINTER
ax = plt.axes(projection=ccrs.PlateCarree())

dataDIR="../Datasets/Unclipped_MODIS_WINTER.nc"
data = xr.open_dataset(dataDIR)
AOD=data.AOD_550_Dark_Target_Deep_Blue_Combined_Mean
AOD=AOD[:,:,:].astype(np.double)

AOD_mean=AOD.mean(dim='time', skipna=True)
# AOD_mean.plot(ax=ax) 
lat, lon = AOD_mean.indexes.values()

plt.pcolor(lon, lat, AOD_mean,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=.20,vmax=.80)
plt.colorbar()    

plt.contourf(lon, lat, AOD_mean,60,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=.20,vmax=.80)
plt.title("Nd_MEAN-WINTER(2005-2021)(cm^-3)")
ax.coastlines()

gridlines = ax.gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False

plt.title("AOD_MEAN-WINTER(2005-2021)")
plt.savefig('Unclipped_AOD_MEAN-WINTER(2005-2021).png',dpi=300)
# plt.show()