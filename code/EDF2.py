df = pd.read_csv("../data2fig/EDF2_FSL_projection.csv")

colors = {
    "his": "k",
    "ssp126": "#73d2de",
    "ssp245": "#218380",
    "ssp370": "#ffbc42",
    "ssp585": "#d81159",
}

positions = {
    "his": [1],
    "ssp126": [1.5, 2.6, 3.7, 4.8],
    "ssp245": [1.7, 2.8, 3.9, 5.0],
    "ssp370": [1.9, 3.0, 4.1, 5.2],
    "ssp585": [2.1, 3.2, 4.3, 5.4],
}

def plot_region_from_csv(ax, rid):
    df_r = df[df["Region"] == rid]

    d = df_r[(df_r.Scenario=="his") & (df_r.Period=="P0")].iloc[0]
    ax.bxp([dict(q1=d.Q1,q3=d.Q3,med=d.Median,whislo=d.Whisker_low,whishi=d.Whisker_high,fliers=[])],
           positions=positions["his"],
           widths=0.18,
           patch_artist=True,
           boxprops=dict(facecolor="white", edgecolor=colors["his"], linewidth=2),
           medianprops=dict(color="k", linewidth=2))

    for scen in ["ssp126","ssp245","ssp370","ssp585"]:
        stats = []
        for p in ["P1","P2","P3","P4"]:
            d = df_r[(df_r.Scenario==scen) & (df_r.Period==p)].iloc[0]
            stats.append(dict(q1=d.Q1,q3=d.Q3,med=d.Median,whislo=d.Whisker_low,whishi=d.Whisker_high,fliers=[]))

        ax.bxp(stats,
               positions=positions[scen],
               widths=0.18,
               patch_artist=True,
               boxprops=dict(facecolor="white", edgecolor=colors[scen], linewidth=2),
               medianprops=dict(color="k", linewidth=2))
    
    ax.set_xlim(0.8,5.6)
    ax.set_xticks([1,1.8,2.9,4.0,5.1])
    ax.set_xticklabels([])  

import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(9,5, figsize=(15,18))
axes = axes.flatten()

for i in range(43):
    plot_region_from_csv(axes[i], i+1)
    if i == 42:  
        axes[i].set_xticklabels(["P0","P1","P2","P3","P4"], fontsize=10)
sns.despine()

# hide empty axes
for j in range(43, 45):
    axes[j].axis("off")

plt.tight_layout()
plt.show()
