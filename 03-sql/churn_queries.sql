-- ── 1. Overview ───────────────────────────────────────────
SELECT
    COUNT(*) AS total_customers,
    SUM(Exited) AS churned,
    ROUND(AVG(Exited) * 100, 1) AS churn_rate_pct
FROM Churn_Modelling;

-- ── 2. Churn by Geography ──────────────────────────────────
SELECT
    Geography,
    COUNT(*) AS total,
    SUM(Exited) AS churned,
    ROUND(AVG(Exited) * 100, 1) AS churn_rate_pct
FROM Churn_Modelling
GROUP BY Geography
ORDER BY churn_rate_pct DESC;

-- ── 3. Churn by Number of Products ────────────────────────
SELECT
    NumOfProducts,
    COUNT(*) AS total,
    SUM(Exited) AS churned,
    ROUND(AVG(Exited) * 100, 1) AS churn_rate_pct
FROM Churn_Modelling
GROUP BY NumOfProducts
ORDER BY NumOfProducts;

-- ── 4. Active vs Inactive ──────────────────────────────────
SELECT
    CASE WHEN IsActiveMember = 1 THEN 'Active' ELSE 'Inactive' END AS status,
    COUNT(*) AS total,
    SUM(Exited) AS churned,
    ROUND(AVG(Exited) * 100, 1) AS churn_rate_pct
FROM Churn_Modelling
GROUP BY IsActiveMember;

-- ── 5. Churn by Age Group (Window Function) ───────────────
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 30 THEN '18-30'
        WHEN Age BETWEEN 31 AND 40 THEN '31-40'
        WHEN Age BETWEEN 41 AND 50 THEN '41-50'
        WHEN Age BETWEEN 51 AND 60 THEN '51-60'
        ELSE '61+' END AS age_group,
    COUNT(*) AS total,
    SUM(Exited) AS churned,
    ROUND(AVG(Exited) * 100, 1) AS churn_rate_pct,
    RANK() OVER (ORDER BY AVG(Exited) DESC) AS risk_rank
FROM Churn_Modelling
GROUP BY age_group
ORDER BY churn_rate_pct DESC;

-- ── 6. High-Risk Customer Segments ────────────────────────
SELECT
    CustomerId,
    Age,
    Geography,
    NumOfProducts,
    IsActiveMember,
    Exited,
    ROW_NUMBER() OVER (PARTITION BY Geography ORDER BY Balance DESC) AS rank_in_geo
FROM Churn_Modelling
WHERE Exited = 1
  AND Age BETWEEN 51 AND 60
  AND IsActiveMember = 0
ORDER BY Geography, Balance DESC;
