# Customer Churn Analysis — Fintech Retention Strategy

**Role:** Business Analyst / Data Analyst  
**Domain:** Fintech · Digital Banking · Customer Retention  
**Stack:** Python · SQL · Looker Studio · Excel  
**Dataset:** [Bank Customer Churn — Kaggle](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling) (10,000 records)

---

## Problem Statement

A fictional retail bank is experiencing high customer churn. As the Business Analyst, I was tasked with identifying key churn drivers from historical customer data and translating findings into actionable retention recommendations for the product and marketing teams.

---

## What I Did

| Step | Activity | Output |
|------|----------|--------|
| 1 | Exploratory Data Analysis in Python | Charts, churn distribution by segment |
| 2 | Advanced SQL queries (Window Functions, CTEs) | Cohort segmentation, risk scoring |
| 3 | Looker Studio dashboard | KPI cards, bar charts, geo heat map |
| 4 | BA recommendation report | 3 retention strategies for business team |

---

## Key Findings

- **Age 51–60** has the highest churn rate at **56.2%** vs 20.4% average
- Customers with **3+ products** churn at **85.9%** — critical over-selling signal
- **Inactive members** churn at 26.9% vs 14.3% for active members
- **Germany segment** churn at 32.4% — requires country-level audit
- **High-balance customers** (>$150k) churn at **34.4%** — competitive poaching risk
- **New customers** (tenure 0–1 yr) churn at **29.1%** — onboarding gap identified
- **Female customers** churn at **25.1%** vs 16.5% male — product-fit gap
---

## BA Recommendations

1. **Retention campaign** targeting age 51–60 with personalised offers
2. **Engagement program** for inactive members (push notifications, rewards)
3. **Country-level audit** for Germany — investigate product-market fit

---

## Repository Structure
ba-fintech-churn-analysis/

├── 01-data/              # Raw dataset + data dictionary

├── 02-python/            # EDA scripts (pandas, seaborn, matplotlib)

├── 03-sql/               # SQL queries (overview → cohort → risk scoring)

├── 04-powerbi/           # Dashboard screenshots + Excel source

├── 05-insights/          # Key findings charts + BA recommendation report

└── 06-presentation/      # Executive summary PDF + slide deck


---

## Skills Demonstrated

`Requirements Analysis` `Data-driven Decision Making` `SQL Window Functions`  
`Python EDA` `Power BI` `Stakeholder Communication` `Fintech Domain`

---
## Key Visualizations

### Churn by Age Group
![Churn by Age](05-insights/churn_by_age.png)

### Churn by Balance Tier
![Churn by Balance](05-insights/churn_by_balance_tier.png)

### Correlation Heatmap
![Correlation](05-insights/correlation_heatmap.png)

### Age × Activity Heatmap
![Age x Activity](05-insights/churn_age_x_activity.png)

*Project by Nguyen Le Bao Dang — Business Analyst candidate*  
*[LinkedIn](https://www.linkedin.com/in/nguyenlebaodang/)*