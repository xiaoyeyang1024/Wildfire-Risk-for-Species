import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import regionmask
import matplotlib.patheffects as path_effects
import cmaps
import regionmask
regions = regionmask.defined_regions.ar6.land

ds = xr.open_dataset("../data2fig/EDF5_WSL_changes.nc")

lon_1 = ds["lon"].values
lat_1 = ds["lat"].values
data_dict = {
    "SSP1-2.6": ds["SSP1_2_6"].values,
    "SSP2-4.5": ds["SSP2_4_5"].values,
    "SSP3-7.0": ds["SSP3_7_0"].values,
    "SSP5-8.5": ds["SSP5_8_5"].values,
}

levels = np.array([-100,0,0.5,1, 1.5, 2, 200])*100
norm = mcolors.BoundaryNorm(boundaries=levels, ncolors=cmaps.MPL_RdYlGn_r[40:-20].N)

fig = plt.figure(figsize=(12, 8))
projections = [(0.1, 0.8), (0.95, 0.8), (0.1, 0.1), (0.95, 0.1)]
titles = list(data_dict.keys())

for pos, title in zip(projections, titles):
    ax = fig.add_axes([pos[0], pos[1], 0.8, 0.6], projection=ccrs.Robinson())
    regions.plot(regions=range(1, 44), add_ocean=True, ax=ax,
                 line_kws={"color": "gray", "linewidth": 1},
                 ocean_kws={"facecolor": "white"})
    
    for text in ax.texts:
        text.set_visible(True)
        text.set_bbox(None)
        text.set_fontweight('bold')
        text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='white'),
                               path_effects.Normal()])
    
    c = ax.pcolormesh(lon_1, lat_1, data_dict[title], norm=norm,
                      cmap=cmaps.MPL_PuOr[40:-20], transform=ccrs.PlateCarree(), zorder=1)
    ax.set_global()
    ax.text(0.1, 1.1, title, transform=ax.transAxes, fontsize=26, fontweight='bold', ha='left', va='center')

# colorbar
cax = fig.add_axes([0.63, -0.03, 0.6, 0.02])
cbar = fig.colorbar(c, cax=cax, orientation='horizontal')
cbar.set_label("unit: %", fontsize=16)
tick_positions = (levels[:-1] + levels[1:]) / 2
cbar.set_ticks(tick_positions)
cbar.set_ticklabels(['<0', '0~50', '50~100', '100~150', '150~200', '>200'])
cbar.ax.tick_params(labelsize=14)

plt.show()