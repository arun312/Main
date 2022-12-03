import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import xarray as xr
import numpy as np

ax = plt.axes(projection=ccrs.PlateCarree())


# dataDIR="/Volumes/ACIML/Main/Codes/Nd.nc"
# data = xr.open_dataset(dataDIR)
# data['Nd'] = data['__xarray_dataarray_variable__']
# data = data.drop(['__xarray_dataarray_variable__'])

# Nd=data.Nd
# Nd=Nd[:,:,:].astype(np.double)


# Nd_mean=Nd.sel(time=slice('2005-03-01', '2005-05-31')).mean(dim='time', skipna=True)
# Nd_mean.plot(ax=ax) 
# lat, lon = Nd_mean.indexes.values()
# # plt.contourf(lon, lat, Nd_mean, 60,
# #              transform=ccrs.PlateCarree())
# plt.title("Nd_MEAN-PreMonsoon2005")
# ax.coastlines()
# gridlines = ax.gridlines(draw_labels=True,linewidth=0)
# gridlines.xlabels_top = False
# gridlines.ylabels_right = False
# plt.savefig('Nd_MEAN-PreMonsoon2005.png',dpi=300)
# # ax.legend()
# plt.show()


############AOD

dataDIR="/Volumes/ACIML/Clipped-MYD_AOD/AOD.nc"
data = xr.open_dataset(dataDIR)

AOD=data.AOD_550_Dark_Target_Deep_Blue_Combined_Mean
AOD=AOD[0:92,:,:].astype(np.double)

AOD_mean=AOD.mean(dim='sfc', skipna=True)
AOD_mean.plot(ax=ax) 
# time, lat, lon = AOD.indexes.values()
# # plt.contourf(lon, lat, Nd_mean, 60, d
# #              transform=ccrs.PlateCarree())
# plt.title("AOD_MEAN-PreMonsoon2005")
ax.coastlines()
gridlines = ax.gridlines(draw_labels=True,linewidth=0)
gridlines.xlabels_top = False
gridlines.ylabels_right = False
plt.savefig('AOD_MEAN-PreMonsoon2005.png',dpi=300)
plt.show()

