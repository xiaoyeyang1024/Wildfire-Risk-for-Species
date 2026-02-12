import regionmask
###########POSITION OF PLOTS###########################
regions = regionmask.defined_regions.ar6.land
centroids = regions.centroids
centroids = np.vstack(centroids)[1:44]
centroids[3,0]+=5#R4
centroids[4,0]+=5#R5
centroids[9,0]+=5#R5
centroids[13,0]+=5#R5
centroids[24,0]-=3#R5
centroids[26,0]+=5#R5
centroids[39,0]-=8#R5
centroids[36,0]-=8#R5
centroids[42,0]+=5#R5

centroids[15,1]+=4#R5
centroids[16,1]+=2#R5
centroids[23,1]-=3#R5
centroids[25,1]-=3#R5
centroids[26,1]-=3#R5
centroids[29,1]+=2#R5
centroids[33,1]-=8#R5
centroids[36,1]-=11#R5
centroids[40,1]-=5#R5
centroids[41,1]-=3#R5

centroids_tmp = centroids.copy()

centroids_tmp[0,0]-=30
centroids_tmp[0,1]+=15

centroids_tmp[1,0]-=15
centroids_tmp[1,1]+=15

centroids_tmp[2,0]-=40
centroids_tmp[2,1]+=7

centroids_tmp[3,0]-=20
centroids_tmp[3,1]+=9

centroids_tmp[4,0]+=5
centroids_tmp[4,1]+=9

centroids_tmp[5,0]-=35
centroids_tmp[5,1]-=3

centroids_tmp[6,0]-=11
centroids_tmp[6,1]+=10

centroids_tmp[7,0]+=11
centroids_tmp[7,1]+=6

centroids_tmp[8,0]-=25

centroids_tmp[9,0]-=5
centroids_tmp[9,1]-=5

centroids_tmp[10,0]-=5
centroids_tmp[10,1]-=18

centroids_tmp[11,0]-=25
centroids_tmp[11,1]-=15

centroids_tmp[12,0]-=15
centroids_tmp[12,1]-=23

centroids_tmp[13,0]+=6
centroids_tmp[13,1]-=25

centroids_tmp[14,1]-=35

centroids_tmp[15,1]+=12

centroids_tmp[16,0]-=5
centroids_tmp[16,1]-=4

centroids_tmp[17,0]+=3
centroids_tmp[17,1]-=6

centroids_tmp[18,0]-=39
centroids_tmp[18,1]+=11

centroids_tmp[19,0]-=10

centroids_tmp[20,0]+=1
centroids_tmp[20,1]-=12

centroids_tmp[21,0]-=18
centroids_tmp[21,1]-=29

centroids_tmp[22,0]-=3
centroids_tmp[22,1]-=11

centroids_tmp[23,0]+=1
centroids_tmp[23,1]-=21

centroids_tmp[24,0]-=12
centroids_tmp[24,1]-=30

centroids_tmp[25,0]+=8.5
centroids_tmp[25,1]-=29.2

centroids_tmp[26,0]+=25
centroids_tmp[26,1]-=15

centroids_tmp[27,0]+=10
centroids_tmp[27,1]+=10

centroids_tmp[28,0]+=12
centroids_tmp[28,1]-=11

centroids_tmp[29,0]+=44
centroids_tmp[29,1]+=15

centroids_tmp[30,0]+=25
centroids_tmp[30,1]-=0

centroids_tmp[31,0]+=15
centroids_tmp[31,1]-=18

centroids_tmp[32,0]+=30
centroids_tmp[32,1]+=3

centroids_tmp[33,0]+=20
centroids_tmp[33,1]-=10

centroids_tmp[34,0]+=28
centroids_tmp[34,1]-=10

centroids_tmp[35,0]-=10
centroids_tmp[35,1]-=0

centroids_tmp[36,0]+=0
centroids_tmp[36,1]-=20

centroids_tmp[37,0]+=2
centroids_tmp[37,1]-=15

centroids_tmp[38,0]+=25
centroids_tmp[38,1]+=3

centroids_tmp[39,0]-=4
centroids_tmp[39,1]-=12

centroids_tmp[40,0]+=15
centroids_tmp[40,1]-=4

centroids_tmp[41,0]-=5
centroids_tmp[41,1]-=23

centroids_tmp[42,0]+=5
centroids_tmp[42,1]-=23

# -----------------------------

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import seaborn as sns

df = pd.read_csv("../data2fig/EDF1_EBA_CDF.csv")
colors = ['#73d2de', '#218380', '#ffbc42', '#d81159']
SSPs = ['SSP1-2.6', 'SSP2-4.5', 'SSP3-7.0', 'SSP5-8.5']
regions_count = 43
X = np.array([1,2,3,4,5,6])

fig = plt.figure(figsize=(18, 12))
ax = fig.add_axes([0.1, 0.1, 1.5, 1], projection=ccrs.Robinson())
ax.set_global()
ax.stock_img()

regions.plot(regions=range(1, 44), add_ocean=True, ax=ax,
             line_kws={"color":"gray","linewidth":3,"linestyle":"-"},
             ocean_kws={"facecolor":"lightblue"})

for text in ax.texts:
    text.set_visible(False)

projection = ax.projection

for i in range(regions_count):
    x, y = projection.transform_point(centroids_tmp[i][0], centroids_tmp[i][1], ccrs.PlateCarree())
    ax_extent = ax.get_extent(crs=projection)
    fig_x = (x - ax_extent[0]) / (ax_extent[1] - ax_extent[0])
    fig_y = (y - ax_extent[2]) / (ax_extent[3] - ax_extent[2])
    ax_pos = ax.get_position()
    sub_fig_x = ax_pos.x0 + ax_pos.width * fig_x - 0.06
    sub_fig_y = ax_pos.y0 + ax_pos.height * fig_y - 0.06
    sub_ax = fig.add_axes([sub_fig_x, sub_fig_y, 0.11, 0.11])
    sub_ax.patch.set_alpha(0.6)

    for ssp_idx, ssp in enumerate(SSPs):
        tmp = df[df.Region==i+1][df.SSP==ssp]['ESL_class'].values
        if len(tmp) == 0:
            continue
        sorted_data = np.sort(tmp)
        cdf_values = np.arange(1, len(sorted_data)+1)/len(sorted_data)
        sub_ax.step(sorted_data, cdf_values, color=colors[ssp_idx], label=ssp, where='post', lw=4)

    sub_ax.set_ylim(0,1)
    sub_ax.set_xlim(0.5,6.5)
    sub_ax.set_title(f"Region {i+1}", fontsize=24)
    sub_ax.set_xticklabels([])
    sub_ax.set_yticklabels([])
    sub_ax.yaxis.set_tick_params(width=1.5,length=5)
    sub_ax.xaxis.set_tick_params(width=1.5,length=5)
    sns.despine(ax=sub_ax,left=False,right=True,top=True,bottom=False)
    sub_ax.spines["left"].set_linewidth(1.5)
    sub_ax.spines["bottom"].set_linewidth(1.5)

ax.text(0,1.1,'a. Changes in EBA under different scenarios', transform=ax.transAxes,
        fontsize=36,fontweight='bold',ha='left',va='center')

plt.show()

##################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

colors = ['#73d2de','#218380','#ffbc42','#d81159']
groups_order = ["North America","South America","Europe","Africa","Asia","Oceania","Global"]
labels_dict = {
    "North America": "b. North America",
    "South America": "c. South America",
    "Europe": "d. Europe",
    "Africa": "e. Africa",
    "Asia": "f. Asia",
    "Oceania": "g. Oceania",
    "Global": "h. Global"
}

cdf_df = pd.read_csv("../data2fig/EDF1_CDF_group.csv")
X_labels = ['<0','0~25','25~50','50~75','75~100','>100']

fig = plt.figure(figsize=(18, 12))
positions = [
    [0.1, 0.55, 0.3, 0.3],
    [0.45, 0.55, 0.3, 0.3],
    [0.8, 0.55, 0.3, 0.3],
    [1.15, 0.55, 0.3, 0.3],
    [0.1, 0.1, 0.3, 0.3],
    [0.45, 0.1, 0.3, 0.3],
    [0.8, 0.1, 0.3, 0.3]
]

for idx, group in enumerate(groups_order):
    ax_pos = positions[idx]
    ax = fig.add_axes(ax_pos)
    for ssp_idx, ssp in enumerate(['SSP1-2.6','SSP2-4.5','SSP3-7.0','SSP5-8.5']):
        tmp_df = cdf_df[(cdf_df['Group']==group) & (cdf_df['SSP']==ssp)]
        if tmp_df.empty:
            continue
        ax.step(tmp_df['X'], tmp_df['CDF'], color=colors[ssp_idx], label=ssp, where='post', lw=4)
    
    ax.set_ylim(0,1)
    ax.set_xlim(0.5,6.5)
    ax.set_title(labels_dict[group], loc='left', fontsize=24, fontweight='bold')
    ax.set_xticks([1,2,3,4,5,6])
    ax.set_xticklabels(X_labels, rotation=30, fontsize=19)
    ax.set_yticks([0,0.2,0.4,0.6,0.8,1])
    ax.set_yticklabels(['0','20%','40%','60%','80%','100%'], fontsize=19)
    if group in ["Asia","Oceania"]:
        ax.set_xlabel('Relative Change (%)', fontsize=21)
    if group in ["North America","Asia"]:
        ax.set_ylabel('Cumulative Distribution', fontsize=21)

ax.legend(fontsize=26, bbox_to_anchor=(1.9,0.7))
plt.show()