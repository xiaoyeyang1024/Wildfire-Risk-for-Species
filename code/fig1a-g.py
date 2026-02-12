import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data2fig/Fig1_BA_projection.csv")

colors = {
    "his": "k",
    "ssp126": "#73d2de",
    "ssp245": "#218380",
    "ssp370": "#ffbc42",
    "ssp585": "#d81159",
}

positions = {
    "his": [1],
    "ssp126": [1.5,2.6,3.7,4.8],
    "ssp245": [1.7,2.8,3.9,5.0],
    "ssp370": [1.9,3.0,4.1,5.2],
    "ssp585": [2.1,3.2,4.3,5.4],
}

def plot_region_from_csv(ax, region, title, ylabel):

    df_r = df[df["Region"] == region]

    # ---------- historical ----------
    d = df_r[(df_r.Scenario=="his") & (df_r.Period=="P0")].iloc[0]
    ax.bxp(
        [dict(
            q1=d.Q1, q3=d.Q3, med=d.Median,
            whislo=d.Whisker_low, whishi=d.Whisker_high,
            fliers=[]
        )],
        positions=positions["his"],
        widths=0.18,
        patch_artist=True,
        boxprops=dict(facecolor="white", edgecolor=colors["his"], linewidth=2),
        whiskerprops=dict(color=colors["his"], linewidth=1.5),
        capprops=dict(color=colors["his"], linewidth=1.5),
        medianprops=dict(color="k", linewidth=2),
    )

    # ---------- future ----------
    for scen in ["ssp126","ssp245","ssp370","ssp585"]:
        stats = []
        for p in ["P1","P2","P3","P4"]:
            d = df_r[(df_r.Scenario==scen) & (df_r.Period==p)].iloc[0]
            stats.append(dict(
                q1=d.Q1, q3=d.Q3, med=d.Median,
                whislo=d.Whisker_low, whishi=d.Whisker_high,
                fliers=[]
            ))

        ax.bxp(
            stats,
            positions=positions[scen],
            widths=0.18,
            patch_artist=True,
            boxprops=dict(facecolor="white", edgecolor=colors[scen], linewidth=2),
            whiskerprops=dict(color=colors[scen], linewidth=1.5),
            capprops=dict(color=colors[scen], linewidth=1.5),
            medianprops=dict(color="k", linewidth=2),
        )

    ax.set_xlim(0.8,5.6)
    ax.set_xticks([1,1.8,2.9,4.0,5.1])
    ax.set_xticklabels(["P0","P1","P2","P3","P4"], fontsize=18)
    ax.set_ylabel(ylabel, fontsize=18)
    ax.set_title(title, loc="left", fontsize=22, fontweight="bold")

    ax.yaxis.set_tick_params(width=1.5, length=5, labelsize=16)
    ax.xaxis.set_tick_params(width=1.5, length=5)

    sns.despine(ax=ax)
    ax.spines["left"].set_linewidth(1.5)
    ax.spines["bottom"].set_linewidth(1.5)

    
fig = plt.figure(figsize=(18,12))

plot_region_from_csv(fig.add_axes([0.1,0.55,0.3,0.3]),
                     "North America", "a. North America", r"$10^5$ km$^2$")
plot_region_from_csv(fig.add_axes([0.45,0.55,0.3,0.3]),
                     "South America", "b. South America", r"$10^5$ km$^2$")
plot_region_from_csv(fig.add_axes([0.8,0.55,0.3,0.3]),
                     "Europe", "c. Europe", r"$10^5$ km$^2$")
plot_region_from_csv(fig.add_axes([1.15,0.55,0.3,0.3]),
                     "Africa", "d. Africa", r"$10^6$ km$^2$")
plot_region_from_csv(fig.add_axes([0.1,0.1,0.3,0.3]),
                     "Asia", "e. Asia", r"$10^5$ km$^2$")
plot_region_from_csv(fig.add_axes([0.45,0.1,0.3,0.3]),
                     "Oceania", "f. Oceania", r"$10^5$ km$^2$")
plot_region_from_csv(fig.add_axes([0.8,0.1,0.3,0.3]),
                     "Global", "g. Global", r"$10^6$ km$^2$")

plt.tight_layout()
plt.show()