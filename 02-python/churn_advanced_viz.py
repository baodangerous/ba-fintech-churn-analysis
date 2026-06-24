import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import numpy as np

# Load data
df = pd.read_csv('../01-data/Churn_Modelling.csv')

# Setup style
sns.set_theme(style="whitegrid", font_scale=1.1)
BLUE = "#1565C0"
RED  = "#C62828"
GRAY = "#EEEEEE"

# 1. Correlation Heatmap
# Tai sao: thay duoc bien nao lien quan nhat den Exited
fig, ax = plt.subplots(figsize=(10, 8))
numeric_cols = ['CreditScore','Age','Tenure','Balance',
                'NumOfProducts','HasCrCard','IsActiveMember',
                'EstimatedSalary','Exited']
corr = df[numeric_cols].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f",
            cmap="coolwarm", center=0, ax=ax,
            linewidths=0.5, cbar_kws={"shrink": 0.8})
ax.set_title("Correlation Matrix — All Features vs Churn",
             fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('../05-insights/correlation_heatmap.png', dpi=150)
plt.close()
print("Saved correlation_heatmap.png")

# 2. Churn by Balance Tier
# Tai sao: kiem chung Finding 5 — khach so du cao churn nhieu hon
df['BalanceTier'] = pd.cut(df['Balance'],
    bins=[-1, 0, 50000, 100000, 150000, 300000],
    labels=['Zero','Low (<50k)','Mid (50-100k)',
            'High (100-150k)','Very High (>150k)'])
bal = df.groupby('BalanceTier', observed=False)['Exited'].mean()

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(bal.index, bal.values,
              color=[GRAY, GRAY, GRAY, BLUE, RED])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(df['Exited'].mean(), color='orange',
           linestyle='--', linewidth=1.5, label='Overall avg')
ax.legend()
ax.set_title("Churn Rate by Balance Tier",
             fontsize=14, fontweight='bold')
ax.set_xlabel("Balance Tier (USD)")
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, bal.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.005,
            f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('../05-insights/churn_by_balance_tier.png', dpi=150)
plt.close()
print("Saved churn_by_balance_tier.png")

# 3. Churn by Tenure
# Tai sao: kiem chung Finding 6 — khach moi churn cao hon
df['TenureBand'] = pd.cut(df['Tenure'],
    bins=[-1, 1, 3, 6, 10],
    labels=['0-1 yr','2-3 yr','4-6 yr','7-10 yr'])
ten = df.groupby('TenureBand', observed=False)['Exited'].mean()

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(ten.index, ten.values,
              color=[RED, BLUE, GRAY, GRAY])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(df['Exited'].mean(), color='orange',
           linestyle='--', linewidth=1.5, label='Overall avg')
ax.legend()
ax.set_title("Churn Rate by Customer Tenure",
             fontsize=14, fontweight='bold')
ax.set_xlabel("Tenure Band")
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, ten.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.003,
            f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('../05-insights/churn_by_tenure.png', dpi=150)
plt.close()
print("Saved churn_by_tenure.png")

# 4. Age x Activity heatmap
# Tai sao: thay duoc su ket hop nguy hiem nhat — tuoi cao + khong hoat dong
df['AgeGroup'] = pd.cut(df['Age'],
    bins=[18,30,40,50,60,70],
    labels=['18-30','31-40','41-50','51-60','61-70'])
pivot = df.groupby(
    ['AgeGroup','IsActiveMember'],
    observed=False)['Exited'].mean().unstack()
pivot.columns = ['Inactive','Active']

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(pivot, annot=True, fmt=".1%",
            cmap="YlOrRd", ax=ax, linewidths=0.5,
            cbar_kws={"label": "Churn Rate"})
ax.set_title("Churn Rate: Age Group x Member Activity",
             fontsize=14, fontweight='bold')
ax.set_xlabel("Member Status")
ax.set_ylabel("Age Group")
plt.tight_layout()
plt.savefig('../05-insights/churn_age_x_activity.png', dpi=150)
plt.close()
print("Saved churn_age_x_activity.png")

# 5. Gender x Geography
# Tai sao: visualize Finding 8 — gap gioi tinh nhat quan moi dia ly
gg = df.groupby(['Geography','Gender'])['Exited'].mean().reset_index()

fig, ax = plt.subplots(figsize=(9, 5))
x = ['France','Germany','Spain']
female = [gg[(gg.Geography==g)&(gg.Gender=='Female')]['Exited'].values[0] for g in x]
male   = [gg[(gg.Geography==g)&(gg.Gender=='Male')]['Exited'].values[0] for g in x]
xpos = range(len(x))
bars1 = ax.bar([p - 0.2 for p in xpos], female,
               width=0.4, label='Female', color=RED)
bars2 = ax.bar([p + 0.2 for p in xpos], male,
               width=0.4, label='Male', color=BLUE)
ax.set_xticks(list(xpos))
ax.set_xticklabels(x)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_title("Churn Rate by Gender x Geography",
             fontsize=14, fontweight='bold')
ax.set_ylabel("Churn Rate")
ax.legend()
for bar in list(bars1) + list(bars2):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.003,
            f'{bar.get_height():.1%}',
            ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('../05-insights/churn_gender_x_geography.png', dpi=150)
plt.close()
print("Saved churn_gender_x_geography.png")

print("\nAll 5 charts saved to 05-insights/")
