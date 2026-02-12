data = np.load("../data2fig/EDF3_EBA_change.npz")

regions = regionmask.defined_regions.ar6.land
centroids = regions.centroids
centroids = np.vstack(centroids)[1:44]

mean_tmp = data['mean_array'][:, 0] # 0 for LC, 1 for NT,....
std_tmp = data['std_array'][:, 0] # 0 for LC, 1 for NT,....

fig3 = plt.figure(figsize=(12, 8))
ax = fig3.add_axes([0.1, 0.1, 0.8, 0.6], projection=ccrs.Robinson())
ax.set_global()
regions.plot(regions=range(1, 44), add_ocean=True, ax=ax,
             line_kws={"color": "gray", "linewidth": 1, "linestyle": "-"},
             ocean_kws={"facecolor": "white"})

for text in ax.texts:
    text.set_visible(False)

markers = []
for std in std_tmp:
    if np.isnan(std):
        markers.append(None)  
    elif std < 25:
        markers.append('o')  
    elif 25 <= std < 50:
        markers.append('s')  
    else:
        markers.append('^')  

for i in range(len(centroids)):
    if not np.isnan(std_tmp[i]):  
        ax.scatter(centroids[i, 0], centroids[i, 1], c=mean_tmp[i], ec='k', s=250,
                   transform=ccrs.PlateCarree(), zorder=4, cmap=cmaps.MPL_PuOr, vmin=-50, vmax=100,
                   marker=markers[i])

ax.text(0, 1.05, 'a. EBA change for LC species ', transform=ax.transAxes, fontsize=22, fontweight='bold', ha='left', va='center')


plt.show()