import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

X_labels = ['<0', '0~25', '25~50', '50~75', '75~100', '>100']

bar_df = pd.read_csv("../data2fig/EDF2_SSP245_EBA.csv")

fig, axes = plt.subplots(8, 6, figsize=(18, 22), sharex=True)
axes = axes.flatten()

for i, region in enumerate(range(1, 44)):
    df = bar_df[bar_df['Region'] == region].copy()
    
    sns.barplot(data=df, x='Category', y='Value', ax=axes[i], edgecolor='black', linewidth=1.5)
    sns.despine(ax=axes[i], left=False, right=True, top=True, bottom=False) 
    axes[i].spines["left"].set_linewidth(1.5)
    axes[i].spines["left"].set_color("black")
    axes[i].spines["bottom"].set_linewidth(1.5)
    axes[i].spines["bottom"].set_color("black")
    for p in axes[i].patches:
        if p.get_height() > 0.05:
            axes[i].annotate(f'{p.get_height():.1f}', 
                             (p.get_x() + p.get_width() / 2., p.get_height()), 
                             ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    axes[i].set_title(f"Region {region}", fontsize=16, fontweight='bold')
    axes[i].set_ylabel("", fontsize=14)
    axes[i].tick_params(axis='x', labelrotation=30, labelsize=12)
    axes[i].tick_params(axis='y', labelsize=12)
    
    y_max = df['Value'].max()
    axes[i].set_ylim(0, y_max + 5)

for j in range(43, 48):
    axes[j].axis('off')

axes[42].set_ylabel("Proportion of species (%)", fontsize=14)
axes[42].set_xlabel("EBA Change (%)", fontsize=14)

plt.tight_layout()
plt.show()