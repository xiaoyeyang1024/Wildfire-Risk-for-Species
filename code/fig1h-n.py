import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data2fig/Fig1_FSL_projection.csv")

colors = {
    "hist": "k",
    "ssp126": "#73d2de",
    "ssp245": "#218380",
    "ssp370": "#ffbc42",
    "ssp585": "#d81159",
}

positions = {
    "hist": [1],
    "ssp126": [1.5,2.6,3.7,4.8],
    "ssp245": [1.7,2.8,3.9,5.0],
    "ssp370": [1.9,3.0,4.1,5.2],
    "ssp585": [2.1,3.2,4.3,5.4],
}

def plot_region_from_csv(ax, region, title, ylabel):
    df_r = df[df["Region"] == region]

    d = df_r[(df_r.Scenario=="hist") & (df_r.Period=="P0")].iloc[0]
    ax.bxp([dict(q1=d.Q1,q3=d.Q3,med=d.Median,whislo=d.Whisker_low,whishi=d.Whisker_high,fliers=[])],
           positions=positions["hist"],
           widths=0.18,
           patch_artist=True,
           boxprops=dict(facecolor="white", edgecolor=colors["hist"], linewidth=2),
           whiskerprops=dict(color=colors["hist"], linewidth=1.5),
           capprops=dict(color=colors["hist"], linewidth=1.5),
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
               whiskerprops=dict(color=colors[scen], linewidth=1.5),
               capprops=dict(color=colors[scen], linewidth=1.5),
               medianprops=dict(color="k", linewidth=2))

    ax.set_xlim(0.8,5.6)
    ax.set_xticks([1,1.8,2.9,4.0,5.1])
    ax.set_xticklabels(["P0","P1","P2","P3","P4"], fontsize=19)
    ax.set_ylabel(ylabel, fontsize=19)
    ax.set_title(title, loc="left", fontsize=24, fontweight="bold")
    ax.yaxis.set_tick_params(width=1.5,length=5,labelsize=16)
    ax.xaxis.set_tick_params(width=1.5,length=5)
    sns.despine(ax=ax,left=False,right=True,top=True,bottom=False)
    ax.spines["left"].set_linewidth(1.5)
    ax.spines["bottom"].set_linewidth(1.5)

    
fig = plt.figure(figsize=(18,12))
region_titles = [("na","h. North America"),("sa","i. South America"),("eu","j. Europe"),
                 ("af","k. Africa"),("as","l. Asia"),("oc","m. Oceania"),("gl","n. Global")]
axes_pos = [[0.1,0.55,0.3,0.3],[0.45,0.55,0.3,0.3],[0.8,0.55,0.3,0.3],
            [1.15,0.55,0.3,0.3],[0.1,0.1,0.3,0.3],[0.45,0.1,0.3,0.3],[0.8,0.1,0.3,0.3]]

for (region,title),pos in zip(region_titles,axes_pos):
    ax = fig.add_axes(pos)
    plot_region_from_csv(ax, region, title, "Days")

# legend
import matplotlib.patches as mpatches
legend_patches = [
    mpatches.Patch(facecolor="white", edgecolor="k", linewidth=2, label="Historical"),
    mpatches.Patch(facecolor="white", edgecolor="#73d2de", linewidth=2, label="SSP1-2.6"),
    mpatches.Patch(facecolor="white", edgecolor="#218380", linewidth=2, label="SSP2-4.5"),
    mpatches.Patch(facecolor="white", edgecolor="#ffbc42", linewidth=2, label="SSP3-7.0"),
    mpatches.Patch(facecolor="white", edgecolor="#d81159", linewidth=2, label="SSP5-8.5")
]
ax.legend(handles=legend_patches, fontsize=26, bbox_to_anchor=(1.8,1.1), frameon=False)
ax.text(9.5,40,'P0: 1999-2014\nP1: 2021-2040\nP2: 2041-2060\nP3: 2061-2080\nP4: 2081-2100',fontsize=26)

plt.tight_layout()
plt.show()