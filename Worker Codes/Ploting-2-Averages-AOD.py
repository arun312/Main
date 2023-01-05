import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import geopandas as gp


font = {'weight' : 'bold',
        'size'   : 16}
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('font', **font)

#AOD-Premon
ax = plt.axes(projection=ccrs.PlateCarree())

dataDIR="../Datasets/FINAL_MODIS_PreMon.nc"
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
# plt.title("Nd_MEAN-PreMon(2005-2021)(cm^-3)")
ax.coastlines()

gridlines = ax.gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.bottom_labels=False

major_tick = [80,84,88,92,96]
minor_tick = [78,82,86,90,94]
ax.set_xticks(minor_tick) # Grid
ax.set_xticks(major_tick, minor=True)

major_tick1 = ['78°E','82°E','86°E','90°E','94°E']
ax.set_xticklabels(major_tick1) # Grid

# plt.title("AOD_MEAN-PreMon(2005-2021)")
plt.savefig('AOD_MEAN-PreMon(2005-2021).png',dpi=300)
# plt.show()
plt.clf()


#AOD-WINTER
ax = plt.axes(projection=ccrs.PlateCarree())

dataDIR="../Datasets/FINAL_MODIS_WINTER.nc"
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
# plt.title("Nd_MEAN-WINTER(2005-2021)(cm^-3)")
ax.coastlines()

gridlines = ax.gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.bottom_labels=False

major_tick = [80,84,88,92,96]
minor_tick = [78,82,86,90,94]
ax.set_xticks(minor_tick) # Grid
ax.set_xticks(major_tick, minor=True)

major_tick1 = ['78°E','82°E','86°E','90°E','94°E']
ax.set_xticklabels(major_tick1) # Grid

# plt.title("AOD_MEAN-WINTER(2005-2021)")
plt.savefig('AOD_MEAN-WINTER(2005-2021).png',dpi=300)
# plt.show()