import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import seaborn as sns

colors = ['#73d2de', '#218380', '#ffbc42', '#d81159']
ssp_list = ['SSP1-2.6', 'SSP2-4.5', 'SSP3-7.0', 'SSP5-8.5']
X = np.arange(1, 7)
X_labels = ['<0','0~25','25~50','50~75','75~100','>100']

df_samples = pd.read_csv("../data2fig/EDF6_ESL_CDF.csv")

fig = plt.figure(figsize=(18, 12))
ax = fig.add_axes([0.1, 0.1, 1.5, 1], projection=ccrs.Robinson())
ax.set_global()
ax.stock_img()
regions.plot(regions=range(1, 44), add_ocean=True, ax=ax,
             line_kws={"color": "gray", "linewidth": 3, "linestyle": "-"},
             ocean_kws={"facecolor": "lightblue"})
for text in ax.texts:
    text.set_visible(False)
projection = ax.projection

for i in range(43):
    x, y = projection.transform_point(centroids_tmp[i][0], centroids_tmp[i][1], ccrs.PlateCarree())
    ax_extent = ax.get_extent(crs=projection)
    fig_x = (x - ax_extent[0]) / (ax_extent[1] - ax_extent[0])
    fig_y = (y - ax_extent[2]) / (ax_extent[3] - ax_extent[2])
    ax_pos = ax.get_position()
    sub_fig_x = ax_pos.x0 + ax_pos.width * fig_x - 0.06
    sub_fig_y = ax_pos.y0 + ax_pos.height * fig_y - 0.06
    sub_ax = fig.add_axes([sub_fig_x, sub_fig_y, 0.11, 0.11])

    sub_ax.patch.set_alpha(0.6)
    
    for data_idx, ssp in enumerate(ssp_list):
        sample_data = df_samples[(df_samples['Region']==i+1) & (df_samples['SSP']==ssp)]['ESL_class'].values
        if len(sample_data) == 0:
            continue
        sorted_data = np.sort(sample_data)
        cdf_values = np.arange(1, len(sorted_data)+1) / len(sorted_data)
        sub_ax.step(sorted_data, cdf_values, color=colors[data_idx], label=ssp, where='post', lw=2)
    
    sub_ax.set_ylim(0, 1)
    sub_ax.set_xlim(0.5, 6.5)
    sub_ax.set_title(f"Region {i+1}", fontsize=16)
    sub_ax.set_xticklabels([])
    sub_ax.set_yticklabels([])
    sns.despine(ax=sub_ax, left=False, right=True, top=True, bottom=False)
    sub_ax.spines["left"].set_linewidth(1.5)
    sub_ax.spines["bottom"].set_linewidth(1.5)

ax_ref = fig.add_axes([0.21, 0.15, 0.25, 0.3])
ax_ref.patch.set_alpha(0.1)
ax_ref.set_ylim(0, 1)
ax_ref.set_xlim(0.5, 6.5)
ax_ref.set_xticks(X)
ax_ref.set_xticklabels(X_labels, rotation=30, fontsize=10, fontweight='bold')
ax_ref.set_yticks([0,0.2,0.4,0.6,0.8,1])
ax_ref.set_yticklabels(['0','20%','40%','60%','80%','100%'], fontsize=10, fontweight='bold')
ax_ref.set_ylabel('Cumulative Distribution', fontsize=12, fontweight='bold')
ax_ref.set_xlabel('ESL Change (%)', fontsize=12, fontweight='bold')
sns.despine(ax=ax_ref, left=False, right=True, top=True, bottom=False)
ax_ref.spines["left"].set_linewidth(1.5)
ax_ref.spines["bottom"].set_linewidth(1.5)

########################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.feature as cfeature

sns.set_theme(style="whitegrid")

latitude_mean_df_percentage = pd.read_csv("../data2fig/EDF6_latitude_ESL.csv")

fig = plt.figure(figsize=(18, 12))

ax = fig.add_axes([0.1, 0.1, 1.5, 1], projection=ccrs.Robinson())
ax.set_global()
ax.stock_img()
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), ec='gray')
ax.plot([-180, 180], [0, 0], transform=ccrs.PlateCarree(), color='gray', linewidth=4, linestyle='--')

positions = [0.18, 0.41, 0.64, 0.87, 1.1, 1.33]
categories = ["< 0","0 ~ 25","25 ~ 50","50 ~ 75","75 ~ 100","> 100"]
colors = ["#86B8CE","#759688","#EBD088","#E79D7E","#D88080","#92140c"]
xlims = [20,60,100,100,100,100]

for pos, cat, color, xlim in zip(positions, categories, colors, xlims):
    ax_bar = fig.add_axes([pos, 0.1, 0.2, 1])
    ax_bar.patch.set_alpha(0.6)
    
    sns.barplot(
        y="latitude",
        x=cat,
        data=latitude_mean_df_percentage,
        color=color,
        orient="h",
        ax=ax_bar
    )
    
    ax_bar.set_xlim(0, xlim)
    ax_bar.set_ylim(-1,38)
    ax_bar.set_xlabel("Values (%)", fontsize=22)
    if cat == "< 0":
        ax_bar.set_ylabel("Latitude", fontsize=32, fontweight='bold')
        ax_bar.set_yticks([2,5,8,11,14,17,20,23,26,29,32,35])
        ytick_labels = [f"{abs(y)}°{'S' if y < 0 else 'N'}" for y in [-82.5,-67.5,-52.5,-37.5,-22.5,-7.5,7.5,22.5,37.5,52.5,67.5,82.5]]
        ax_bar.set_yticklabels(ytick_labels, fontdict={'fontsize': 45})
    else:
        ax_bar.set_yticklabels([])
        ax_bar.set_ylabel("")
    
    ax_bar.tick_params(axis="both", labelsize=22)
    ax_bar.set_title(cat, loc='center', fontsize=28, fontweight='bold')
    sns.despine(ax=ax_bar, left=False, right=True, top=True, bottom=True)
    ax_bar.spines["left"].set_linewidth(3)
    ax_bar.spines["left"].set_color("black")

plt.show()
