import matplotlib.pyplot as plt

from cartopy import config
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import geopandas as gp
from mpl_toolkits.axes_grid1 import make_axes_locatable

font = {'weight' : 'bold',
        'size'   : 12}
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('font', **font)

#BC_AOD-Premon

w, h=plt.figaspect(2.2)
fig,ax=plt.subplots(nrows=2,subplot_kw={'projection':ccrs.PlateCarree()})
fig.set_size_inches(w,h)
# ax = plt.axes(projection=ccrs.PlateCarree())

dataDIR="../Datasets/N_MERRA-PreMon.nc"
data = xr.open_dataset(dataDIR)
BC_AOD=data.BC_AOD
BC_AOD=BC_AOD[:,:,:].astype(np.double)

BC_AOD_mean=BC_AOD.mean(dim='time', skipna=True)
# BC_AOD_mean.plot(ax=ax) 
lat, lon = BC_AOD_mean.indexes.values()

ax[0].pcolor(lon, lat, BC_AOD_mean,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=0,vmax=.08)
# plt.colorbar()    

ax[0].contourf(lon, lat, BC_AOD_mean,60,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=0,vmax=.08)
# plt.title("Nd_MEAN-PreMon(2005-2021)(cm^-3)")
ax[0].coastlines()

gridlines = ax[0].gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.bottom_labels=False

ax[0].set_ylim(bottom=8.5,top=23)


# major_tick = [80,84,88,92,96]
# minor_tick = [78,82,86,90,94]
# ax[0].set_xticks(minor_tick) # Grid
# ax[0].set_xticks(major_tick, minor=True)

# major_tick1 = ['78°E','82°E','86°E','90°E','94°E']
# ax[0].set_xticklabels(major_tick1) # Grid

# plt.title("BC_AOD_MEAN-PreMon(2005-2021)")
# plt.savefig('MERRA_BC_AOD_MEAN-PreMon(2005-2021).png',dpi=300)
# plt.show()
# plt.clf()


#BC_AOD-WINTER
# ax[1] = plt.axes(projection=ccrs.PlateCarree())

dataDIR="../Datasets/N_MERRA-Winter.nc"
data = xr.open_dataset(dataDIR)
BC_AOD=data.BC_AOD
BC_AOD=BC_AOD[:,:,:].astype(np.double)

BC_AOD_mean=BC_AOD.mean(dim='time', skipna=True)
# BC_AOD_mean.plot(ax=ax) 
lat, lon = BC_AOD_mean.indexes.values()

im = ax[1].pcolor(lon, lat, BC_AOD_mean,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=0,vmax=.08)
# ax[1].colorbar()    
ax[1].contourf(lon, lat, BC_AOD_mean,60,
            transform=ccrs.PlateCarree(),cmap='jet',vmin=0,vmax=.08)
# plt.title("Nd_MEAN-WINTER(2005-2021)(cm^-3)")
ax[1].coastlines()

gridlines = ax[1].gridlines(draw_labels=True,linewidth=0)
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.bottom_labels=False

ax[1].set_ylim(bottom=8.5,top=23)

major_tick = [80,84,88,92,96]
minor_tick = [78,82,86,90,94]
ax[1].set_xticks(minor_tick) # Grid
ax[1].set_xticks(major_tick, minor=True)

major_tick1 = ['78°E','82°E','86°E','90°E','94°E']
ax[1].set_xticklabels(major_tick1) # Grid

#ADDING COLOUR BAR
# p=ax[1].get_position().get_points().flatten()
# ax_cbar=fig.add_axes([p[0],0,p[2]-p[0],0.05])

# divider=make_axes_locatable(ax[1])
# cax=divider.new_vertical(size='5%',pad=0.7,pack_start=True,projection=ccrs.PlateCarree())
# fig.add_axes(cax)
fig.colorbar(im,ax=ax[:],shrink=.9,orientation='horizontal',pad=.07)
# plt.colorbar(im,cax=cax,orientation='horizontal')
# plt.title("BC_AOD_MEAN-WINTER(2005-2021)")


plt.savefig('MERRA-BC_AOD_MEAN(2005-2021).png',dpi=300)
