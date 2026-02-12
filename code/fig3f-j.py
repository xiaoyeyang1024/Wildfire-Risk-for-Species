import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from matplotlib.patches import Patch  

df = pd.read_csv("../data2fig/Fig3_hotspots.csv")

colors = [cmaps.MPL_PuOr(0.4), cmaps.MPL_PuOr(0.6), cmaps.MPL_PuOr(0.75)] 
legend_labels = ['50~75','75~100','>100']  

fig = plt.figure(figsize=(18, 12))

# ------------------- f. Caribbean -------------------
ax = fig.add_axes([0.1, 0.8, 0.4, 0.5])
df_caribbean = df[df['Region'] == 'f. Caribbean']
bottom = np.zeros(len(df_caribbean))
for idx, col in enumerate(['50~75','75~100','>100']):
    bars = ax.bar(df_caribbean['Category'], df_caribbean[col], bottom=bottom, color=colors[idx],
                  edgecolor='black', linewidth=1.5)
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + h/2, f'{h:.1f}',
                    ha='center', va='center', fontsize=28, fontweight='bold')
    bottom += df_caribbean[col].values
ax.set_title("f. Caribbean", fontsize=36, fontweight='bold', loc='left')

handles = [Patch(facecolor=colors[i], edgecolor='black', label=legend_labels[i]) for i in range(3)]
ax.legend(handles=handles, title="EBA Growth (%)", fontsize=30, title_fontsize=30)

sns.despine()
ax.grid(axis='y', linestyle="--", alpha=0.6)
plt.xticks(fontsize=0)
plt.ylim(0,12)
plt.yticks([0,3,6,9,12], fontsize=36)

# ------------------- g. South America -------------------
ax = fig.add_axes([0.55, 0.8, 0.4, 0.5])
df_samerica = df[df['Region'] == 'g. South America']
bottom = np.zeros(len(df_samerica))
for idx, col in enumerate(['50~75','75~100','>100']):
    bars = ax.bar(df_samerica['Category'], df_samerica[col], bottom=bottom, color=colors[idx],
                  edgecolor='black', linewidth=1.5)
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + h/2, f'{h:.1f}',
                    ha='center', va='center', fontsize=28, fontweight='bold')
    bottom += df_samerica[col].values
ax.set_title("g. South America", fontsize=36, fontweight='bold', loc='left')

sns.despine()
ax.grid(axis='y', linestyle="--", alpha=0.6)
plt.xticks(fontsize=0)
plt.yticks(fontsize=36)

# ------------------- h. South Asia -------------------
ax = fig.add_axes([0.1, 0.1, 0.4, 0.5])
df_sasia = df[df['Region'] == 'h. South Asia']
bottom = np.zeros(len(df_sasia))
for idx, col in enumerate(['50~75','75~100','>100']):
    bars = ax.bar(df_sasia['Category'], df_sasia[col], bottom=bottom, color=colors[idx],
                  edgecolor='black', linewidth=1.5)
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + h/2, f'{h:.1f}',
                    ha='center', va='center', fontsize=28, fontweight='bold')
    bottom += df_sasia[col].values
ax.set_title("h. South Asia", fontsize=36, fontweight='bold', loc='left')

sns.despine()
ax.grid(axis='y', linestyle="--", alpha=0.6)
plt.xticks(ticks=[0,1,2,3,4], labels=['LC','NT','VU','EN','CR'], fontsize=36)
plt.yticks(fontsize=36)

# ------------------- i. Australia -------------------
ax = fig.add_axes([0.55, 0.1, 0.4, 0.5])
df_australia = df[df['Region'] == 'i. Australia']
bottom = np.zeros(len(df_australia))
for idx, col in enumerate(['50~75','75~100','>100']):
    bars = ax.bar(df_australia['Category'], df_australia[col], bottom=bottom, color=colors[idx],
                  edgecolor='black', linewidth=1.5)
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + h/2, f'{h:.1f}',
                    ha='center', va='center', fontsize=28, fontweight='bold')
    bottom += df_australia[col].values
ax.set_title("i. Australia", fontsize=36, fontweight='bold', loc='left')

sns.despine()
ax.grid(axis='y', linestyle="--", alpha=0.6)
plt.xticks(ticks=[0,1,2,3,4], labels=['LC','NT','VU','EN','CR'], fontsize=36)
plt.yticks(fontsize=36)

fig.text(-0.03,0.4,"Proportion of species (%)", rotation=90, fontsize=46, fontweight='bold')
fig.text(0.38,-0.03,"Threatened level", fontsize=46, fontweight='bold')

plt.show()