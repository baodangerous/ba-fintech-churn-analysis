import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import numpy as np

df = pd.read_csv('01-data/Churn_Modelling.csv')
sns.set_theme(style="whitegrid", font_scale=1.1)
BLUE, RED, GRAY = "#1565C0", "#C62828", "#EEEEEE"
AVG = df['Exited'].mean()

# ── 1. Age Group ───────────────────────────────────────────
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,30,40,50,60,70],
    labels=['18-30','31-40','41-50','51-60','61-70'])
age = df.groupby('AgeGroup', observed=False)['Exited'].mean()
fig, ax = plt.subplots(figsize=(9,5))
bars = ax.bar(age.index, age.values,
              color=[GRAY, GRAY, BLUE, RED, BLUE])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(AVG, color='orange', linestyle='--', lw=1.5, label=f'Avg {AVG:.1%}')
ax.legend()
ax.set_title("Churn Rate by Age Group", fontsize=14, fontweight='bold')
ax.set_xlabel("Age Group")
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, age.values):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height()+0.005, f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('05-insights/churn_by_age.png', dpi=150)
plt.close()
print("churn_by_age.png")

# ── 2. Balance Tier ────────────────────────────────────────
df['BalanceTier'] = pd.cut(df['Balance'],
    bins=[-1, 0, 50000, 100000, 150000, 300000],
    labels=['Zero','Low (<50k)','Mid (50-100k)','High (100-150k)','Very High (>150k)'])
bal = df.groupby('BalanceTier', observed=False)['Exited'].mean()
fig, ax = plt.subplots(figsize=(10,5))
bars = ax.bar(bal.index, bal.values,
              color=[GRAY, RED, GRAY, BLUE, GRAY])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(AVG, color='orange', linestyle='--', lw=1.5, label=f'Avg {AVG:.1%}')
ax.legend()
ax.set_title("Churn Rate by Balance Tier", fontsize=14, fontweight='bold')
ax.set_xlabel("Balance Tier (USD)")
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, bal.values):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height()+0.005, f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('05-insights/churn_by_balance_tier.png', dpi=150)
plt.close()
print("churn_by_balance_tier.png")

# ── 3. Number of Products ──────────────────────────────────
prod = df.groupby('NumOfProducts')['Exited'].mean()
fig, ax = plt.subplots(figsize=(7,5))
bars = ax.bar(prod.index.astype(str), prod.values,
              color=[GRAY, GRAY, RED, RED])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(AVG, color='orange', linestyle='--', lw=1.5, label=f'Avg {AVG:.1%}')
ax.legend()
ax.set_title("Churn Rate by Number of Products", fontsize=14, fontweight='bold')
ax.set_xlabel("Number of Products")
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, prod.values):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height()+0.005, f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('05-insights/churn_by_products.png', dpi=150)
plt.close()
print("churn_by_products.png")

# ── 4. Geography ───────────────────────────────────────────
geo = df.groupby('Geography')['Exited'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(7,5))
bars = ax.bar(geo.index, geo.values, color=[RED, GRAY, GRAY])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(AVG, color='orange', linestyle='--', lw=1.5, label=f'Avg {AVG:.1%}')
ax.legend()
ax.set_title("Churn Rate by Geography", fontsize=14, fontweight='bold')
ax.set_xlabel("Country")
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, geo.values):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height()+0.005, f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('05-insights/churn_by_geography.png', dpi=150)
plt.close()
print("churn_by_geography.png")

# ── 5. Active vs Inactive ──────────────────────────────────
act = df.groupby('IsActiveMember')['Exited'].mean()
fig, ax = plt.subplots(figsize=(6,5))
bars = ax.bar(['Inactive','Active'], act.values, color=[RED, GRAY])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(AVG, color='orange', linestyle='--', lw=1.5, label=f'Avg {AVG:.1%}')
ax.legend()
ax.set_title("Churn Rate: Active vs Inactive Members", fontsize=14, fontweight='bold')
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, act.values):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height()+0.005, f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('05-insights/churn_by_activity.png', dpi=150)
plt.close()
print("churn_by_activity.png")

# ── 6. Gender ──────────────────────────────────────────────
gen = df.groupby('Gender')['Exited'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(6,5))
bars = ax.bar(gen.index, gen.values, color=[RED, GRAY])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.axhline(AVG, color='orange', linestyle='--', lw=1.5, label=f'Avg {AVG:.1%}')
ax.legend()
ax.set_title("Churn Rate by Gender", fontsize=14, fontweight='bold')
ax.set_ylabel("Churn Rate")
for bar, val in zip(bars, gen.values):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height()+0.005, f'{val:.1%}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('05-insights/churn_by_gender.png', dpi=150)
plt.close()
print("churn_by_gender.png")

# ── 7. Gender x Geography ──────────────────────────────────
gg = df.groupby(['Geography','Gender'])['Exited'].mean().reset_index()
fig, ax = plt.subplots(figsize=(9,5))
x = ['France','Germany','Spain']
female = [gg[(gg.Geography==g)&(gg.Gender=='Female')]['Exited'].values[0] for g in x]
male   = [gg[(gg.Geography==g)&(gg.Gender=='Male')]['Exited'].values[0] for g in x]
xpos = range(len(x))
b1 = ax.bar([p-0.2 for p in xpos], female, width=0.4, label='Female', color=RED)
b2 = ax.bar([p+0.2 for p in xpos], male,   width=0.4, label='Male',   color=BLUE)
ax.set_xticks(list(xpos))
ax.set_xticklabels(x)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_title("Churn Rate by Gender x Geography", fontsize=14, fontweight='bold')
ax.set_ylabel("Churn Rate")
ax.legend()
for bar in list(b1)+list(b2):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height()+0.003, f'{bar.get_height():.1%}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('05-insights/churn_gender_x_geography.png', dpi=150)
plt.close()
print("churn_gender_x_geography.png")

# ── 8. Age x Activity Heatmap ──────────────────────────────
pivot = df.groupby(['AgeGroup','IsActiveMember'],
                   observed=False)['Exited'].mean().unstack()
pivot.columns = ['Inactive','Active']
fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(pivot, annot=True, fmt=".1%", cmap="YlOrRd",
            ax=ax, linewidths=0.5, cbar_kws={"label":"Churn Rate"})
ax.set_title("Churn Rate: Age Group x Member Activity",
             fontsize=14, fontweight='bold')
ax.set_xlabel("Member Status")
ax.set_ylabel("Age Group")
plt.tight_layout()
plt.savefig('05-insights/churn_age_x_activity.png', dpi=150)
plt.close()
print("churn_age_x_activity.png")

# ── 9. Correlation Heatmap ─────────────────────────────────
numeric_cols = ['CreditScore','Age','Tenure','Balance',
                'NumOfProducts','HasCrCard','IsActiveMember',
                'EstimatedSalary','Exited']
corr = df[numeric_cols].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f",
            cmap="coolwarm", center=0, ax=ax,
            linewidths=0.5, cbar_kws={"shrink":0.8})
ax.set_title("Correlation Matrix — All Features vs Churn",
             fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('05-insights/correlation_heatmap.png', dpi=150)
plt.close()
print("correlation_heatmap.png")

# ── REAL NUMBERS ───────────────────────────────────────────
print("\n=== REAL NUMBERS FOR README & RECOMMENDATIONS ===")
print(f"Overall churn rate:        {AVG:.1%}")
print(f"Age 51-60 churn:           {df[df['AgeGroup']=='51-60']['Exited'].mean():.1%}")
print(f"Age 41-50 churn:           {df[df['AgeGroup']=='41-50']['Exited'].mean():.1%}")
print(f"Age 61-70 churn:           {df[df['AgeGroup']=='61-70']['Exited'].mean():.1%}")
print(f"3+ products churn:         {df[df['NumOfProducts']>=3]['Exited'].mean():.1%}")
print(f"Inactive churn:            {df[df['IsActiveMember']==0]['Exited'].mean():.1%}")
print(f"Active churn:              {df[df['IsActiveMember']==1]['Exited'].mean():.1%}")
print(f"Germany churn:             {df[df['Geography']=='Germany']['Exited'].mean():.1%}")
print(f"France churn:              {df[df['Geography']=='France']['Exited'].mean():.1%}")
print(f"Spain churn:               {df[df['Geography']=='Spain']['Exited'].mean():.1%}")
print(f"Female churn:              {df[df['Gender']=='Female']['Exited'].mean():.1%}")
print(f"Male churn:                {df[df['Gender']=='Male']['Exited'].mean():.1%}")
low = df[(df['Balance']>0) & (df['Balance']<=50000)]
zero = df[df['Balance']==0]
print(f"Low balance (<50k) churn:  {low['Exited'].mean():.1%}")
print(f"Zero balance churn:        {zero['Exited'].mean():.1%}")
print(f"Churned avg balance:       ${df[df['Exited']==1]['Balance'].mean():,.0f}")
print(f"Retained avg balance:      ${df[df['Exited']==0]['Balance'].mean():,.0f}")
print(f"Tenure 0-1yr churn:        {df[df['Tenure']<=1]['Exited'].mean():.1%}")
print(f"Tenure 7-10yr churn:       {df[df['Tenure']>=7]['Exited'].mean():.1%}")
print(f"Total customers:           {len(df):,}")
print(f"3+ products count:         {len(df[df['NumOfProducts']>=3]):,}")
