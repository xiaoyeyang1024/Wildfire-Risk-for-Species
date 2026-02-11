import regionmask
import matplotlib.patheffects as path_effects

ba_change245 = xr.open_dataset("../data2fig/fig2a_BA_change245.nc").BA

regions = regionmask.defined_regions.ar6.land
f_ar6_regions = xr.open_dataset('../ar6_region_mask.nc')
ar6_region_mask = f_ar6_regions.ar6_region_mask.values

levels = np.array([-100,0,0.25,0.5, 0.75, 1, 200])*100

norm = mcolors.BoundaryNorm(boundaries=levels, ncolors=cmaps.MPL_PuOr[50:-10].N)

fig = plt.figure(figsize=(12, 8))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.6],projection = ccrs.Robinson())
regions.plot(regions=range(1, 44),  add_ocean=True, ax=ax ,line_kws={"color": "gray", "linewidth": 1, "linestyle": "-"},
             ocean_kws={"facecolor": "white"})
for text in ax.texts:
    text.set_visible(True)
    text.set_bbox(None)
    text.set_fontweight('bold')
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'), 
        path_effects.Normal()  
    ])

c7 = ax.pcolormesh(lon_1, lat_1,ba_change245 , norm=norm, 
                   cmap=cmaps.MPL_PuOr[50:-10], transform=ccrs.PlateCarree(),zorder=1)
ax.set_global()
ax.text(0.05, 1.05, 'a. Percentage Increase in Burned Area ', transform=ax.transAxes, fontsize=18, fontweight='bold', ha='left', va='center')
cbarx = fig.add_axes([0.2, 0.17, 0.6, 0.02])
cbar = fig.colorbar(c7, cax=cbarx,orientation='horizontal')
cbar.set_label("unit: %", fontsize=16)  
tick_positions = (levels[:-1] + levels[1:]) / 2
cbar.set_ticks(tick_positions)  
cbar.set_ticklabels(['<0', '0~25', '25~50', '50~75', '75~100', '>100'])
cbar.ax.tick_params(labelsize=14) 

###############################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df_all = pd.read_csv('../data2fig/Fig2_EBA_change.csv')

colors = ['#73d2de', '#218380', '#ffbc42', '#d81159']

fig = plt.figure(figsize=(18, 12))

# --- North America ---
ax = fig.add_axes([0.1, 0.1+0.15*6, 0.8, 0.1])
df = df_all[df_all['Region']=='North America']
ax = sns.barplot(data=df, x='Category', y='Value', hue='SSP', palette=colors,
                 edgecolor='black', linewidth=2)
sns.despine(ax=ax, left=False, right=True, top=True, bottom=False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["bottom"].set_color("black")
for p in ax.patches:
    if p.get_height()>0.05:
        ax.annotate(f'{p.get_height():.1f}', 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.title("b. North America (1279)", loc='left', fontsize=20, fontweight='bold')
plt.xlabel("")
plt.ylabel("", fontsize=21)
plt.xticks([])
plt.yticks(fontsize=19)
plt.ylim(0,65)
ax.legend_.remove()

# --- South America ---
ax = fig.add_axes([0.1, 0.1+0.15*5, 0.8, 0.1])
df = df_all[df_all['Region']=='South America']
ax = sns.barplot(data=df, x='Category', y='Value', hue='SSP', palette=colors,
                 edgecolor='black', linewidth=2)
sns.despine(ax=ax, left=False, right=True, top=True, bottom=False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["bottom"].set_color("black")
for p in ax.patches:
    if p.get_height()>0.05:
        ax.annotate(f'{p.get_height():.1f}', 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.title("c. South America (1440)", loc='left', fontsize=20, fontweight='bold')
plt.xlabel("")
plt.ylabel("", fontsize=21)
plt.xticks([])
plt.yticks(fontsize=19)
plt.ylim(0,55)
ax.legend_.remove()

# --- Europe ---
ax = fig.add_axes([0.1, 0.1+0.15*4, 0.8, 0.1])
df = df_all[df_all['Region']=='Europe']
ax = sns.barplot(data=df, x='Category', y='Value', hue='SSP', palette=colors,
                 edgecolor='black', linewidth=2)
sns.despine(ax=ax, left=False, right=True, top=True, bottom=False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["bottom"].set_color("black")
for p in ax.patches:
    if p.get_height()>0.05:
        ax.annotate(f'{p.get_height():.1f}', 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.title("d. Europe (1057)", loc='left', fontsize=20, fontweight='bold')
plt.xlabel("")
plt.ylabel("", fontsize=21)
plt.xticks([])
plt.yticks(fontsize=19)
ax.legend_.remove()

# --- Africa ---
ax = fig.add_axes([0.1, 0.1+0.15*3, 0.8, 0.1])
df = df_all[df_all['Region']=='Africa']
ax = sns.barplot(data=df, x='Category', y='Value', hue='SSP', palette=colors,
                 edgecolor='black', linewidth=2)
sns.despine(ax=ax, left=False, right=True, top=True, bottom=False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["bottom"].set_color("black")
for p in ax.patches:
    if p.get_height()>0.05:
        ax.annotate(f'{p.get_height():.1f}', 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.title("e. Africa (2833)", loc='left', fontsize=20, fontweight='bold')
plt.xlabel("")
plt.ylabel("", fontsize=21)
plt.xticks([])
plt.yticks(fontsize=19)
ax.legend_.remove()

# --- Asia ---
ax = fig.add_axes([0.1, 0.1+0.15*2, 0.8, 0.1])
df = df_all[df_all['Region']=='Asia']
ax = sns.barplot(data=df, x='Category', y='Value', hue='SSP', palette=colors,
                 edgecolor='black', linewidth=2)
sns.despine(ax=ax, left=False, right=True, top=True, bottom=False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["bottom"].set_color("black")
for p in ax.patches:
    if p.get_height()>0.05:
        ax.annotate(f'{p.get_height():.1f}', 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.title("f. Asia (866)", loc='left', fontsize=20, fontweight='bold')
plt.xlabel("")
plt.ylabel("", fontsize=21)
plt.xticks([])
plt.yticks(fontsize=19)
ax.legend_.remove()

# --- Oceania ---
ax = fig.add_axes([0.1, 0.1+0.15*1, 0.8, 0.1])
df = df_all[df_all['Region']=='Oceania']
ax = sns.barplot(data=df, x='Category', y='Value', hue='SSP', palette=colors,
                 edgecolor='black', linewidth=2)
sns.despine(ax=ax, left=False, right=True, top=True, bottom=False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["bottom"].set_color("black")
for p in ax.patches:
    if p.get_height()>0.05:
        ax.annotate(f'{p.get_height():.1f}', 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.title("g. Oceania (781)", loc='left', fontsize=20, fontweight='bold')
plt.xlabel("")
plt.ylabel("", fontsize=21)
plt.xticks([])
plt.yticks(fontsize=19)
ax.legend_.remove()

# --- Global ---
ax = fig.add_axes([0.1, 0.1+0.15*0, 0.8, 0.1])
df = df_all[df_all['Region']=='Global']
ax = sns.barplot(data=df, x='Category', y='Value', hue='SSP', palette=colors,
                 edgecolor='black', linewidth=2)
sns.despine(ax=ax, left=False, right=True, top=True, bottom=False)
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["bottom"].set_color("black")
for p in ax.patches:
    if p.get_height()>0.05:
        ax.annotate(f'{p.get_height():.1f}', 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.title("h. Global (9592)", loc='left', fontsize=20, fontweight='bold')
plt.xlabel("EBA Change (%)", fontsize=21, fontweight='bold')
plt.ylabel("", fontsize=21)
plt.xticks(fontsize=19)
plt.yticks(fontsize=19)
plt.legend(fontsize=20, bbox_to_anchor=(1,10.5), ncol=4)

fig.text(0.05,0.45,"Proportion of (%)",rotation=90, fontsize=23, fontweight='bold')

plt.show()
