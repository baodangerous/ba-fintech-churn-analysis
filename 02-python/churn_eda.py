import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load data ──────────────────────────────────────────────
df = pd.read_csv('../01-data/Churn_Modelling.csv')
print(f"Dataset shape: {df.shape}")
print(f"Churn rate: {df['Exited'].mean():.1%}")

# ── 1. Churn by Age Group ──────────────────────────────────
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,30,40,50,60,70],
                        labels=['18-30','31-40','41-50','51-60','61-70'])
age_churn = df.groupby('AgeGroup')['Exited'].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=age_churn, x='AgeGroup', y='Exited', color='#1565C0')
plt.title('Churn Rate by Age Group')
plt.ylabel('Churn Rate')
plt.xlabel('Age Group')
plt.tight_layout()
plt.savefig('../05-insights/churn_by_age.png', dpi=150)
plt.close()
print("✓ Saved churn_by_age.png")

# ── 2. Churn by Number of Products ────────────────────────
prod_churn = df.groupby('NumOfProducts')['Exited'].mean().reset_index()

plt.figure(figsize=(6,5))
sns.barplot(data=prod_churn, x='NumOfProducts', y='Exited', color='#0277BD')
plt.title('Churn Rate by Number of Products')
plt.ylabel('Churn Rate')
plt.xlabel('Number of Products')
plt.tight_layout()
plt.savefig('../05-insights/churn_by_products.png', dpi=150)
plt.close()
print("✓ Saved churn_by_products.png")

# ── 3. Active vs Inactive Members ─────────────────────────
active_churn = df.groupby('IsActiveMember')['Exited'].mean().reset_index()
active_churn['Status'] = active_churn['IsActiveMember'].map({0:'Inactive', 1:'Active'})

plt.figure(figsize=(6,5))
sns.barplot(data=active_churn, x='Status', y='Exited', color='#1B6CA8')
plt.title('Churn Rate: Active vs Inactive Members')
plt.ylabel('Churn Rate')
plt.tight_layout()
plt.savefig('../05-insights/churn_by_activity.png', dpi=150)
plt.close()
print("✓ Saved churn_by_activity.png")

# ── 4. Churn by Geography ──────────────────────────────────
geo_churn = df.groupby('Geography')['Exited'].mean().reset_index()

plt.figure(figsize=(6,5))
sns.barplot(data=geo_churn, x='Geography', y='Exited', color='#0D47A1')
plt.title('Churn Rate by Geography')
plt.ylabel('Churn Rate')
plt.tight_layout()
plt.savefig('../05-insights/churn_by_geography.png', dpi=150)
plt.close()
print("✓ Saved churn_by_geography.png")

# ── Summary ────────────────────────────────────────────────
print("\n── KEY FINDINGS ──────────────────────────────────")
print(f"Age 51-60 churn: {df[df['AgeGroup']=='51-60']['Exited'].mean():.1%}")
print(f"3+ products churn: {df[df['NumOfProducts']>=3]['Exited'].mean():.1%}")
print(f"Inactive churn:  {df[df['IsActiveMember']==0]['Exited'].mean():.1%}")
print(f"Active churn:    {df[df['IsActiveMember']==1]['Exited'].mean():.1%}")
print(f"Germany churn:   {df[df['Geography']=='Germany']['Exited'].mean():.1%}")
