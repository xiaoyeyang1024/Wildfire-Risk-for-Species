import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
df = pd.read_csv("../data2fig/EDF1_BA_projection.csv")

# =========================================================
fig, axes = plt.subplots(nrows=9, ncols=5, figsize=(15, 18))
axes = axes.flatten()

# =========================================================
for i in range(43):
    sub_ax = axes[i]
    sub_ax.patch.set_alpha(0.6)

    df_r = df[df["Region"] == i + 1]

    # ---------- HIST ----------
    d = df_r[(df_r["Scenario"] == "HIST") & (df_r["Period"] == "P0")].iloc[0]
    stats = [dict(
        q1=d.Q1,
        q3=d.Q3,
        med=d.Median,
        whislo=d.Whisker_low,
        whishi=d.Whisker_high,
        fliers=[]
    )]

    sub_ax.bxp(
        stats,
        positions=[1],
        widths=0.18,
        showfliers=False,
        patch_artist=True,
        boxprops=dict(facecolor="white", edgecolor="k", linewidth=2),
        whiskerprops=dict(color="k", linewidth=1.5),
        capprops=dict(color="k", linewidth=1.5),
        medianprops=dict(color="k", linewidth=2)
    )

    # ---------- SSPs ----------
    scenario_cfg = {
        "SSP1-2.6": ("#73d2de", [1.5, 2.6, 3.7, 4.8]),
        "SSP2-4.5": ("#218380", [1.7, 2.8, 3.9, 5.0]),
        "SSP3-7.0": ("#ffbc42", [1.9, 3.0, 4.1, 5.2]),
        "SSP5-8.5": ("#d81159", [2.1, 3.2, 4.3, 5.4]),
    }

    for scen, (color, xpos) in scenario_cfg.items():
        stats = []
        for p in ["P1", "P2", "P3", "P4"]:
            d = df_r[(df_r["Scenario"] == scen) & (df_r["Period"] == p)].iloc[0]
            stats.append(dict(
                q1=d.Q1,
                q3=d.Q3,
                med=d.Median,
                whislo=d.Whisker_low,
                whishi=d.Whisker_high,
                fliers=[]
            ))

        sub_ax.bxp(
            stats,
            positions=xpos,
            widths=0.18,
            showfliers=False,
            patch_artist=True,
            boxprops=dict(facecolor="white", edgecolor=color, linewidth=2),
            whiskerprops=dict(color=color, linewidth=1.5),
            capprops=dict(color=color, linewidth=1.5),
            medianprops=dict(color="k", linewidth=2)
        )

    sub_ax.set_xlim(0.8, 5.6)
    sub_ax.set_title(f"Region {i+1}", fontsize=10)
    sub_ax.yaxis.set_tick_params(width=1.5, length=5)
    sub_ax.xaxis.set_tick_params(width=1.5, length=5)

    sns.despine(ax=sub_ax, left=False, right=True, top=True, bottom=False)
    sub_ax.spines["left"].set_linewidth(1.5)
    sub_ax.spines["bottom"].set_linewidth(1.5)

    if i < 42:
        sub_ax.set_xticks([1, 1.8, 2.9, 4.0, 5.1])
        sub_ax.set_xticklabels([])
    else:
        sub_ax.set_xticks([1, 1.8, 2.9, 4.0, 5.1])
        sub_ax.set_xticklabels(["P0", "P1", "P2", "P3", "P4"], fontsize=10)

# =========================================================
for j in range(43, 45):
    axes[j].axis("off")

plt.tight_layout()
plt.show()
