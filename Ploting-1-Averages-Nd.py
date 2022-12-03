import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import geopandas as gp

# -ND-PREMON
ax = plt.axes(projection=ccrs.PlateCarree())
dataDIR="../Datasets/Nd_PreMon.nc"
data = xr.open_dataset(dataDIR)
data['Nd'] = data['__xarray_dataarray_variable__']
data = data.drop(['__xarray_dataarray_variable__'])

Nd=data.Nd
Nd=Nd[:,:,:].astype(np.double)


Nd_mean=Nd.mean(dim='time', skipna=True)
# Nd_mean.plot(ax=ax) 
lat, lon = Nd_mean.indexes.values()

plt.pcolor(lon, lat, Nd_mean,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=20,vmax=50)
plt.colorbar()    

plt.contourf(lon, lat, Nd_mean,60,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=20,vmax=50)
plt.title("Nd_MEAN-PreMon(2005-2021)(cm^-3)")
ax.coastlines()
gridlines = ax.gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False
plt.savefig('Nd_MEAN-PreMon(2005-2021).png',dpi=300)
# # ax.legend()
# plt.show()
plt.clf()

# ND-WINTER
ax = plt.axes(projection=ccrs.PlateCarree())
dataDIR="../Datasets/Nd_Winter.nc"
data = xr.open_dataset(dataDIR)
data['Nd'] = data['__xarray_dataarray_variable__']
data = data.drop(['__xarray_dataarray_variable__'])

Nd=data.Nd
Nd=Nd[:,:,:].astype(np.double)


Nd_mean=Nd.mean(dim='time', skipna=True)
# Nd_mean.plot(ax=ax) 
lat, lon = Nd_mean.indexes.values()

plt.pcolor(lon, lat, Nd_mean,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=20,vmax=50)
plt.colorbar()    

plt.contourf(lon, lat, Nd_mean,60,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=20,vmax=50)

plt.title("Nd_MEAN-WINTER(2005-2021)(cm^-3)")
ax.coastlines()
gridlines = ax.gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False
plt.savefig('Nd_MEAN-WINTER(2005-2021).png',dpi=300)
# ax.legend()
# plt.show()