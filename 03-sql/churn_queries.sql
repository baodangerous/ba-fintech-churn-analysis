
-- Customer Churn Analysis — SQL Queries
-- Dataset: Bank Customer Churn (Kaggle, 10,000 records)

-- ── 1. Overview — Overall Churn Summary ───────────────────
-- Purpose: Establish baseline churn rate before segment analysis
SELECT
    COUNT(*)                            AS total_customers,
    SUM(Exited)                         AS total_churned,
    ROUND(AVG(Exited) * 100, 1)         AS churn_rate_pct,
    ROUND(AVG(Balance), 0)              AS avg_balance,
    ROUND(AVG(CreditScore), 0)          AS avg_credit_score,
    ROUND(AVG(Age), 1)                  AS avg_age
FROM Churn_Modelling;

-- ── 2. Churn by Geography ──────────────────────────────────
-- Purpose: Identify geography-specific churn spikes (Finding 4)
SELECT
    Geography,
    COUNT(*)                            AS total,
    SUM(Exited)                         AS churned,
    ROUND(AVG(Exited) * 100, 1)         AS churn_rate_pct,
    ROUND(AVG(Balance), 0)              AS avg_balance
FROM Churn_Modelling
GROUP BY Geography
ORDER BY churn_rate_pct DESC;

-- ── 3. Churn by Number of Products ────────────────────────
-- Purpose: Identify over-selling signal (Finding 1 — 85.9% at 3+ products)
SELECT
    NumOfProducts,
    COUNT(*)                            AS total,
    SUM(Exited)                         AS churned,
    ROUND(AVG(Exited) * 100, 1)         AS churn_rate_pct,
    ROUND(AVG(Balance), 0)              AS avg_balance
FROM Churn_Modelling
GROUP BY NumOfProducts
ORDER BY NumOfProducts;

-- ── 4. Active vs Inactive Member Analysis ─────────────────
-- Purpose: Quantify engagement gap (Finding 3 — 26.9% vs 14.3%)
SELECT
    CASE WHEN IsActiveMember = 1 THEN 'Active'
         ELSE 'Inactive' END            AS member_status,
    COUNT(*)                            AS total,
    SUM(Exited)                         AS churned,
    ROUND(AVG(Exited) * 100, 1)         AS churn_rate_pct,
    ROUND(AVG(Balance), 0)              AS avg_balance,
    ROUND(AVG(NumOfProducts), 2)        AS avg_products
FROM Churn_Modelling
GROUP BY IsActiveMember
ORDER BY churn_rate_pct DESC;

-- ── 5. Churn by Age Group with Risk Ranking ───────────────
-- Purpose: Rank age segments by churn risk using Window Function
-- Window Function: RANK() assigns same rank to tied values
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 30 THEN '18-30'
        WHEN Age BETWEEN 31 AND 40 THEN '31-40'
        WHEN Age BETWEEN 41 AND 50 THEN '41-50'
        WHEN Age BETWEEN 51 AND 60 THEN '51-60'
        ELSE '61-70'
    END                                 AS age_group,
    COUNT(*)                            AS total,
    SUM(Exited)                         AS churned,
    ROUND(AVG(Exited) * 100, 1)         AS churn_rate_pct,
    RANK() OVER (
        ORDER BY AVG(Exited) DESC
    )                                   AS risk_rank
FROM Churn_Modelling
GROUP BY age_group
ORDER BY churn_rate_pct DESC;

-- ── 6. High-Risk Customers by Geography ───────────────────
-- Purpose: Identify top at-risk customers per country
-- Window Function: ROW_NUMBER() + PARTITION BY for per-group ranking
SELECT
    CustomerId,
    Age,
    Geography,
    Gender,
    NumOfProducts,
    Balance,
    IsActiveMember,
    ROW_NUMBER() OVER (
        PARTITION BY Geography
        ORDER BY Balance DESC
    )                                   AS rank_in_geo
FROM Churn_Modelling
WHERE Exited = 1
  AND Age BETWEEN 41 AND 60
  AND IsActiveMember = 0
ORDER BY Geography, Balance DESC;

-- ── 7. Balance Tier Analysis ──────────────────────────────
-- Purpose: Investigate balance-churn relationship (Finding 5)
-- Insight: Low balance (<50k) churns at 34.7% — highest of all tiers
SELECT
    CASE
        WHEN Balance = 0              THEN '1. Zero Balance'
        WHEN Balance <= 50000         THEN '2. Low (<50k)'
        WHEN Balance <= 100000        THEN '3. Mid (50-100k)'
        WHEN Balance <= 150000        THEN '4. High (100-150k)'
        ELSE                               '5. Very High (>150k)'
    END                               AS balance_tier,
    COUNT(*)                          AS total,
    SUM(Exited)                       AS churned,
    ROUND(AVG(Exited) * 100, 1)       AS churn_rate_pct,
    ROUND(AVG(Balance), 0)            AS avg_balance_in_tier
FROM Churn_Modelling
GROUP BY balance_tier
ORDER BY balance_tier;

-- ── 8. Gender x Geography Cross Analysis ──────────────────
-- Purpose: Validate gender gap is consistent across all markets (Finding 8)
SELECT
    Geography,
    Gender,
    COUNT(*)                          AS total,
    SUM(Exited)                       AS churned,
    ROUND(AVG(Exited) * 100, 1)       AS churn_rate_pct
FROM Churn_Modelling
GROUP BY Geography, Gender
ORDER BY Geography, churn_rate_pct DESC;

-- ── 9. CTE — Multi-Segment Risk Scoring ───────────────────
-- Purpose: Combine multiple risk factors into a single risk score per customer
-- CTE: Common Table Expression — breaks complex logic into readable steps
WITH customer_flags AS (
    -- Step 1: Flag each risk factor per customer
    SELECT
        CustomerId,
        Age,
        Geography,
        Balance,
        NumOfProducts,
        IsActiveMember,
        Exited,
        CASE WHEN Age BETWEEN 41 AND 60      THEN 1 ELSE 0 END AS flag_age,
        CASE WHEN NumOfProducts >= 3          THEN 1 ELSE 0 END AS flag_products,
        CASE WHEN IsActiveMember = 0          THEN 1 ELSE 0 END AS flag_inactive,
        CASE WHEN Geography = 'Germany'       THEN 1 ELSE 0 END AS flag_germany,
        CASE WHEN Balance BETWEEN 1 AND 50000 THEN 1 ELSE 0 END AS flag_low_balance
    FROM Churn_Modelling
),
customer_scores AS (
    -- Step 2: Sum flags into composite risk score (0-5)
    SELECT
        CustomerId,
        Age,
        Geography,
        Balance,
        NumOfProducts,
        IsActiveMember,
        Exited,
        (flag_age + flag_products + flag_inactive +
         flag_germany + flag_low_balance)       AS risk_score
    FROM customer_flags
)
-- Step 3: Analyze churn rate by risk score tier
SELECT
    risk_score,
    COUNT(*)                                    AS total_customers,
    SUM(Exited)                                 AS churned,
    ROUND(AVG(Exited) * 100, 1)                 AS churn_rate_pct
FROM customer_scores
GROUP BY risk_score
ORDER BY risk_score DESC;

-- ── 10. CTE — Retention Priority List ─────────────────────
-- Purpose: Generate actionable list of at-risk customers for retention team
-- Business use: Export this list to CRM for targeted outreach campaign
WITH risk_customers AS (
    SELECT
        CustomerId,
        Age,
        Geography,
        Gender,
        Balance,
        NumOfProducts,
        IsActiveMember,
        CreditScore,
        Tenure,
        Exited,
        -- Composite risk score
        (CASE WHEN Age BETWEEN 41 AND 60      THEN 2 ELSE 0 END +
         CASE WHEN NumOfProducts >= 3          THEN 3 ELSE 0 END +
         CASE WHEN IsActiveMember = 0          THEN 1 ELSE 0 END +
         CASE WHEN Geography = 'Germany'       THEN 1 ELSE 0 END +
         CASE WHEN Balance BETWEEN 1 AND 50000 THEN 1 ELSE 0 END
        )                                      AS risk_score
    FROM Churn_Modelling
    WHERE Exited = 0  -- Focus on customers who have NOT yet churned
),
ranked AS (
    SELECT
        *,
        RANK() OVER (ORDER BY risk_score DESC, Balance DESC) AS priority_rank
    FROM risk_customers
)
SELECT
    priority_rank,
    CustomerId,
    Age,
    Geography,
    Gender,
    ROUND(Balance, 0)                           AS balance,
    NumOfProducts,
    CASE WHEN IsActiveMember = 1
         THEN 'Active' ELSE 'Inactive' END       AS status,
    risk_score,
    CASE
        WHEN risk_score >= 4 THEN 'CRITICAL'
        WHEN risk_score >= 2 THEN 'HIGH'
        ELSE 'MEDIUM'
    END                                          AS priority_level
FROM ranked
WHERE risk_score >= 2
ORDER BY priority_rank
LIMIT 50;
