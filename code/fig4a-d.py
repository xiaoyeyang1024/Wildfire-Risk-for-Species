import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import cartopy.feature as cfeature

data = np.load("../data2fig/Fig4_EBA&ESL_avoidable.npz")
wsl_dif_370 = data['wsl_dif_370']
wsl_dif_585 = data['wsl_dif_585']
eba_dif_370 = data['eba_dif_370']
eba_dif_585 = data['eba_dif_585']

norm = mcolors.Normalize(vmin=-100, vmax=100)
cmap = cm.RdYlGn_r

fig3 = plt.figure(figsize=(12, 8))

# ------------------- a. WSL SSP3-7.0 -------------------
ax = fig3.add_axes([0.1, 0.8, 0.8, 0.6], projection=ccrs.Robinson())
ax.set_global()
for i in range(43):
    color = cmap(norm(wsl_dif_370[i]))
    regions.plot(regions=i+1, add_ocean=True, ax=ax,
                 line_kws={"color": "k", "linewidth": 0, "linestyle": "-", "facecolor": color, "alpha": 1},
                 ocean_kws={"facecolor": "white"})
    
ax.add_feature(cfeature.OCEAN.with_scale('50m'), fc='white', zorder=2)
ax.add_feature(cfeature.LAND.with_scale('50m'), fc='white', zorder=0)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), ec='k', lw=0.3, zorder=3)
regions.plot(regions=range(1,44), add_ocean=False, ax=ax,
             line_kws={"color": "gray", "linewidth": 1, "linestyle": "-", "zorder": 4})

for text in ax.texts:
    text.set_visible(True)
    text.set_bbox(None)
    text.set_fontweight('bold')
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),
        path_effects.Normal()
    ])

for spine in ax.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(1)

ax.text(0, 1.05, 'a. Avoidable ESL growth', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')
ax.text(0.8, 1.05, 'SSP3-7.0', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')

# ------------------- b. WSL SSP5-8.5 -------------------
ax = fig3.add_axes([1, 0.8, 0.8, 0.6], projection=ccrs.Robinson())
ax.set_global()
for i in range(43):
    color = cmap(norm(wsl_dif_585[i]))
    regions.plot(regions=i+1, add_ocean=True, ax=ax,
                 line_kws={"color": "k", "linewidth": 0, "linestyle": "-", "facecolor": color, "alpha": 1},
                 ocean_kws={"facecolor": "white"})
    
ax.add_feature(cfeature.OCEAN.with_scale('50m'), fc='white', zorder=2)
ax.add_feature(cfeature.LAND.with_scale('50m'), fc='white', zorder=0)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), ec='k', lw=0.3, zorder=3)
regions.plot(regions=range(1,44), add_ocean=False, ax=ax,
             line_kws={"color": "gray", "linewidth": 1, "linestyle": "-", "zorder": 4})

for text in ax.texts:
    text.set_visible(True)
    text.set_bbox(None)
    text.set_fontweight('bold')
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),
        path_effects.Normal()
    ])

for spine in ax.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(1)

ax.text(0, 1.05, 'b. Avoidable ESL growth', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')
ax.text(0.8, 1.05, 'SSP5-8.5', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')

# ------------------- c. EBA SSP3-7.0 -------------------
ax = fig3.add_axes([0.1, 0.1, 0.8, 0.6], projection=ccrs.Robinson())
ax.set_global()
for i in range(43):
    color = cmap(norm(eba_dif_370[i]))
    regions.plot(regions=i+1, add_ocean=True, ax=ax,
                 line_kws={"color": "k", "linewidth": 0, "linestyle": "-", "facecolor": color, "alpha": 1},
                 ocean_kws={"facecolor": "white"})
    
ax.add_feature(cfeature.OCEAN.with_scale('50m'), fc='white', zorder=2)
ax.add_feature(cfeature.LAND.with_scale('50m'), fc='white', zorder=0)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), ec='k', lw=0.3, zorder=3)
regions.plot(regions=range(1,44), add_ocean=False, ax=ax,
             line_kws={"color": "gray", "linewidth": 1, "linestyle": "-", "zorder": 4})

for text in ax.texts:
    text.set_visible(True)
    text.set_bbox(None)
    text.set_fontweight('bold')
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),
        path_effects.Normal()
    ])

for spine in ax.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(1)

ax.text(0, 1.05, 'c. Avoidable EBA growth', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')
ax.text(0.8, 1.05, 'SSP3-7.0', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')

# ------------------- d. EBA SSP5-8.5 -------------------
ax = fig3.add_axes([1, 0.1, 0.8, 0.6], projection=ccrs.Robinson())
ax.set_global()
for i in range(43):
    color = cmap(norm(eba_dif_585[i]))
    regions.plot(regions=i+1, add_ocean=True, ax=ax,
                 line_kws={"color": "k", "linewidth": 0, "linestyle": "-", "facecolor": color, "alpha": 1},
                 ocean_kws={"facecolor": "white"})
    
ax.add_feature(cfeature.OCEAN.with_scale('50m'), fc='white', zorder=2)
ax.add_feature(cfeature.LAND.with_scale('50m'), fc='white', zorder=0)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), ec='k', lw=0.3, zorder=3)
regions.plot(regions=range(1,44), add_ocean=False, ax=ax,
             line_kws={"color": "gray", "linewidth": 1, "linestyle": "-", "zorder": 4})

for text in ax.texts:
    text.set_visible(True)
    text.set_bbox(None)
    text.set_fontweight('bold')
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),
        path_effects.Normal()
    ])

for spine in ax.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(1)

ax.text(0, 1.05, 'd. Avoidable EBA growth', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')
ax.text(0.8, 1.05, 'SSP5-8.5', transform=ax.transAxes, fontsize=20, fontweight='bold', ha='left', va='center')

# ------------------- colorbar -------------------
cbarx = fig3.add_axes([0.65, 0.03, 0.6, 0.02])
cb = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbarx, orientation='horizontal')
cb.set_label("unit: %", fontsize=26)
cb.ax.tick_params(labelsize=26)

plt.show()
