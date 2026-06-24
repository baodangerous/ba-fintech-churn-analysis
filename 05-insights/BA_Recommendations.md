# BA Insights & Recommendations Report
# Báo Cáo Phân Tích & Đề Xuất Chiến Lược Giảm Churn

**Prepared by / Thực hiện bởi:** Nguyen Le Bao Dang — Business Analyst  
**Dataset / Dữ liệu:** Bank Customer Churn (Kaggle) — 10,000 records  
**Analysis date / Ngày phân tích:** June 2025  
**Status / Trạng thái:** Draft for stakeholder review

---

## Executive Summary / Tóm Tắt Điều Hành

**EN:** Analysis of 10,000 bank customers reveals an overall churn rate of 20.4%. Eight distinct patterns were identified across product holdings, age group, member activity, geography, account balance, credit score, tenure, and gender. The three highest-priority findings are: customers holding 3+ products (85.9% churn), customers aged 51–60 (56.2% churn), and high-balance customers (avg $91,108 among churned vs $72,745 among retained). Addressing these three segments alone could meaningfully reduce overall churn and protect disproportionate revenue.

**VI:** Phân tích 10,000 khách hàng ngân hàng cho thấy tỷ lệ rời bỏ tổng thể là 20,4%. Tám mô hình churn khác biệt được xác định, bao gồm: số lượng sản phẩm, nhóm tuổi, mức độ hoạt động, địa lý, số dư tài khoản, điểm tín dụng, thâm niên khách hàng và giới tính. Ba phát hiện ưu tiên cao nhất là: khách hàng có 3+ sản phẩm (churn 85,9%), nhóm tuổi 51–60 (churn 56,2%) và khách hàng có số dư cao (trung bình $91,108 trong nhóm rời bỏ so với $72,745 trong nhóm ở lại). Giải quyết ba nhóm này sẽ tạo tác động doanh thu lớn nhất.

---

## Finding 1: Extreme Churn Among Customers with 3+ Products
## Phát Hiện 1: Churn Cực Cao Ở Nhóm Khách Hàng Có 3+ Sản Phẩm

**Finding / Phát hiện:**  
EN: Customers holding 3 or more products churn at 85.9% — 4x the overall average of 20.4%. This segment is 326 customers (3.3% of base). Customers with 4 products churn at a similar extreme rate regardless of tenure.  
VI: Khách hàng có từ 3 sản phẩm trở lên có tỷ lệ churn 85,9% — gấp 4 lần mức trung bình 20,4%. Nhóm này gồm 326 khách hàng (3,3% tổng số). Khách có 4 sản phẩm cũng có tỷ lệ churn tương tự bất kể thâm niên.

**So what / Ý nghĩa:**  
EN: Although small in volume, losing 85.9% of this group represents severe revenue risk. Multi-product customers hold higher balances and generate more fee income per account. Retaining even 30% of this segment would meaningfully protect revenue.  
VI: Dù nhỏ về số lượng, mất 85,9% nhóm này là rủi ro doanh thu nghiêm trọng. Khách hàng đa sản phẩm thường có số dư cao hơn và tạo ra nhiều thu nhập phí hơn mỗi tài khoản.

**Hypothesis / Giả thuyết:**  
EN: Over-selling — customers were pushed to acquire products they did not genuinely need, creating dissatisfaction. Alternative: product-market fit failure — 3rd and 4th products may not deliver sufficient value vs competitors.  
VI: Bán hàng quá mức — khách hàng bị thúc đẩy mua sản phẩm không thực sự cần, dẫn đến không hài lòng. Giả thuyết thay thế: sản phẩm thứ 3, 4 không đủ giá trị so với đối thủ.

**To confirm / Để xác nhận cần thêm:**  
- Customer complaint records segmented by number of products / Hồ sơ khiếu nại phân theo số sản phẩm  
- Sales incentive structure / Cấu trúc hoa hồng bán hàng  
- Product usage rates / Tỷ lệ sử dụng thực tế từng sản phẩm

**Recommendation / Đề xuất:**  
1. Conduct product bundle audit to identify which combinations correlate with highest churn / Kiểm toán gói sản phẩm để xác định tổ hợp nào gây churn cao nhất  
2. Limit cross-selling to customers with tenure < 2 years until root cause confirmed / Giới hạn bán chéo với khách hàng thâm niên < 2 năm  
3. Introduce 3-month post-acquisition satisfaction survey for 3rd product / Khảo sát hài lòng 3 tháng sau khi mua sản phẩm thứ 3

**Priority / Ưu tiên:** HIGH — 326 customers, 85.9% will be lost without intervention.

---

## Finding 2: High Churn in Age Group 51–60
## Phát Hiện 2: Churn Cao Ở Nhóm Tuổi 51–60

**Finding / Phát hiện:**  
EN: Customers aged 51–60 churn at 56.2% — more than double the 20.4% average. Even active members in this group churn at 52.1%, while inactive members reach 65.0%.  
VI: Khách hàng 51–60 tuổi có tỷ lệ churn 56,2% — hơn gấp đôi mức trung bình. Ngay cả thành viên hoạt động trong nhóm này cũng churn 52,1%, trong khi không hoạt động lên đến 65,0%.

**So what / Ý nghĩa:**  
EN: This age group is at peak earning and saving capacity — they hold larger balances and more complex products (mortgages, investments, retirement). Losing them creates disproportionate revenue impact.  
VI: Nhóm tuổi này đang ở đỉnh thu nhập và tiết kiệm — họ giữ số dư lớn hơn và sản phẩm phức tạp hơn. Mất họ tạo tác động doanh thu không tương xứng so với đầu người.

**Hypothesis / Giả thuyết:**  
EN: Different service channel expectations — this group may prefer branch or phone banking over digital-only. Alternatively, they are financially experienced and more likely to switch for better rates or dedicated wealth management.  
VI: Kỳ vọng kênh dịch vụ khác biệt — nhóm này có thể thích giao dịch tại chi nhánh hoặc qua điện thoại hơn là kỹ thuật số. Ngoài ra, họ có kinh nghiệm tài chính cao và dễ chuyển đổi để tìm lãi suất tốt hơn.

**To confirm / Để xác nhận cần thêm:**  
- Channel preference data by age group / Dữ liệu kênh ưa thích theo nhóm tuổi  
- Exit survey responses from churned 51–60 customers / Khảo sát lý do rời bỏ từ nhóm 51–60  
- Competitor rate comparison at time of churn / So sánh lãi suất đối thủ tại thời điểm churn

**Recommendation / Đề xuất:**  
1. Design retention campaign targeting 51–60 via preferred channel — not just push notification / Chiến dịch giữ chân qua kênh ưa thích, không chỉ thông báo app  
2. Assign relationship managers to high-balance customers in this segment / Phân công chuyên viên quan hệ cho khách hàng số dư cao  
3. Expand pre-retirement product offerings / Mở rộng sản phẩm phù hợp giai đoạn trước hưu

**Priority / Ưu tiên:** HIGH — largest churn driver by rate among meaningful segments.

---

## Finding 3: Inactive Members Churn at Nearly Double the Rate
## Phát Hiện 3: Thành Viên Không Hoạt Động Churn Gần Gấp Đôi

**Finding / Phát hiện:**  
EN: Inactive members churn at 26.9% vs 14.3% for active members — an 88% relative difference. This gap persists across all age groups, with the most extreme case being inactive customers aged 51–60 at 65.0% churn.  
VI: Thành viên không hoạt động churn 26,9% so với 14,3% của thành viên hoạt động — chênh lệch tương đối 88%. Khoảng cách này duy trì ở tất cả nhóm tuổi, cực đoan nhất là khách 51–60 tuổi không hoạt động với 65,0% churn.

**So what / Ý nghĩa:**  
EN: Inactivity is a leading indicator of churn, not just a symptom. By the time a customer is fully inactive, the exit decision is often already made. Early detection is critical.  
VI: Không hoạt động là chỉ báo sớm của churn, không chỉ là triệu chứng. Khi khách hàng hoàn toàn không hoạt động, quyết định rời bỏ thường đã được đưa ra.

**Hypothesis / Giả thuyết:**  
EN: Low perceived value — customer no longer sees a compelling reason to engage. May be driven by superior competitor experience, unresolved service friction, or lack of proactive outreach from the bank.  
VI: Giá trị cảm nhận thấp — khách hàng không còn lý do thuyết phục để tương tác. Có thể do trải nghiệm đối thủ tốt hơn, vấn đề dịch vụ chưa giải quyết, hoặc thiếu chăm sóc chủ động từ ngân hàng.

**To confirm / Để xác nhận cần thêm:**  
- Days since last login / last transaction per customer / Số ngày kể từ lần đăng nhập / giao dịch cuối  
- Support ticket history for inactive customers / Lịch sử yêu cầu hỗ trợ của khách không hoạt động  
- App engagement metrics / Chỉ số tương tác ứng dụng

**Recommendation / Đề xuất:**  
1. Implement early warning system: flag customers with no transaction in 60 days / Hệ thống cảnh báo sớm: đánh dấu khách không giao dịch trong 60 ngày  
2. Design re-engagement program with personalised cashback or rewards / Chương trình tái kích hoạt với ưu đãi cá nhân hóa  
3. A/B test push notification campaigns targeting inactive segment / Thử nghiệm A/B chiến dịch thông báo cho nhóm không hoạt động

**Priority / Ưu tiên:** MEDIUM-HIGH — large segment with clear early intervention point.

---

## Finding 4: Germany Segment Has Disproportionately High Churn
## Phát Hiện 4: Phân Khúc Đức Có Tỷ Lệ Churn Cao Bất Thường

**Finding / Phát hiện:**  
EN: Germany churns at 32.4% vs France 16% and Spain 17%. The gap is consistent across gender — German female customers churn at 41.0%, German males at 31.7%.  
VI: Đức có tỷ lệ churn 32,4% so với Pháp 16% và Tây Ban Nha 17%. Khoảng cách này nhất quán theo giới tính — khách hàng nữ Đức churn 41,0%, nam Đức 31,7%.

**So what / Ý nghĩa:**  
EN: A geography-specific spike signals a localised issue that a global retention campaign will not solve. Misapplying one-size-fits-all approach risks wasting budget without addressing root cause.  
VI: Mức tăng đột biến theo địa lý báo hiệu vấn đề cục bộ mà chiến dịch giữ chân toàn cầu không giải quyết được.

**Hypothesis / Giả thuyết:**  
EN: Germany has a highly competitive banking landscape with strong local players (Sparkasse, DKB, ING Germany). Stricter GDPR enforcement expectations may also contribute to trust-related churn.  
VI: Thị trường ngân hàng Đức cạnh tranh cao với các ngân hàng nội địa mạnh. Kỳ vọng về bảo mật dữ liệu theo GDPR cũng có thể ảnh hưởng.

**To confirm / Để xác nhận cần thêm:**  
- Competitive landscape analysis for Germany / Phân tích cạnh tranh tại thị trường Đức  
- Customer satisfaction scores: Germany vs France vs Spain / Điểm hài lòng theo quốc gia  
- Product pricing comparison across geographies / So sánh giá sản phẩm theo địa lý

**Recommendation / Đề xuất:**  
1. Country-level audit — exit survey analysis and staff interviews / Kiểm toán cấp quốc gia — phân tích khảo sát và phỏng vấn nhân viên  
2. Review product pricing and features specifically for Germany / Xem xét lại giá và tính năng sản phẩm cho thị trường Đức  
3. Do not apply global campaigns to Germany until root cause confirmed / Không áp dụng chiến dịch toàn cầu cho Đức cho đến khi xác định nguyên nhân

**Priority / Ưu tiên:** MEDIUM — requires investigation before action.

---

## Finding 5: Churned Customers Hold Significantly Higher Balances
## Phát Hiện 5: Khách Hàng Rời Bỏ Có Số Dư Tài Khoản Cao Hơn Đáng Kể

**Finding / Phát hiện:**  
EN: Churned customers average $91,108 vs $72,745 for retained — a 25% gap. By balance tier: High ($100–150k) churns at 32.5%, Very High (>$150k) at 34.4%, compared to 24.5% for low-balance customers.  
VI: Khách hàng rời bỏ có số dư trung bình $91,108 so với $72,745 của nhóm ở lại — chênh lệch 25%. Theo phân khúc: số dư cao ($100–150k) churn 32,5%, rất cao (>$150k) churn 34,4%, so với 24,5% của nhóm số dư thấp.

**So what / Ý nghĩa:**  
EN: This is the most financially impactful finding. Losing one high-balance customer ($150k+) is equivalent to losing 2–3 average customers in revenue terms. The bank is losing its most valuable segment at above-average rates.  
VI: Đây là phát hiện có tác động tài chính lớn nhất. Mất một khách hàng số dư cao ($150k+) tương đương mất 2–3 khách hàng trung bình về doanh thu.

**Hypothesis / Giả thuyết:**  
EN: Two factors likely combine: (1) competitive poaching — high-balance customers are actively targeted by competitors offering better rates and premium services; (2) unmet premium expectations — customers with significant deposits expect personalised, high-touch service that the bank may not deliver consistently.  
VI: Hai yếu tố có thể kết hợp: (1) đối thủ cạnh tranh chủ động tiếp cận khách hàng số dư cao bằng lãi suất tốt hơn và dịch vụ cao cấp; (2) kỳ vọng dịch vụ cao cấp không được đáp ứng.

**To confirm / Để xác nhận cần thêm:**  
- Exit survey data segmented by balance tier / Khảo sát lý do rời bỏ theo phân khúc số dư  
- Competitor deposit rate comparison / So sánh lãi suất tiền gửi với đối thủ  
- Customer service interaction history for high-balance churned customers / Lịch sử tương tác dịch vụ của khách số dư cao đã rời bỏ

**Recommendation / Đề xuất:**  
1. Introduce high-value customer tier (balance > $80,000) with premium benefits: dedicated RM, priority support, preferential rates / Tạo phân hạng khách hàng cao giá trị với số dư > $80,000 và quyền lợi cao cấp  
2. Proactive retention outreach for high-balance customers showing early churn signals / Chăm sóc chủ động cho khách số dư cao có dấu hiệu rời bỏ sớm  
3. Benchmark deposit rates vs top 3 competitors quarterly / So sánh lãi suất tiền gửi với 3 đối thủ hàng đầu theo quý

**Priority / Ưu tiên:** HIGH — highest revenue impact per churned customer.

---

## Finding 6: New Customers (Tenure 0–1 Year) Churn at Highest Rate
## Phát Hiện 6: Khách Hàng Mới (Thâm Niên 0–1 Năm) Có Tỷ Lệ Churn Cao Nhất

**Finding / Phát hiện:**  
EN: Customers with tenure 0–1 year churn at 29.1%, decreasing to 24.3% at 4–6 years and 24.4% at 7–10 years. New customers with 3+ products churn at 74.1% even in their first year.  
VI: Khách hàng thâm niên 0–1 năm churn 29,1%, giảm xuống 24,3% ở 4–6 năm và 24,4% ở 7–10 năm. Khách hàng mới có 3+ sản phẩm churn 74,1% ngay trong năm đầu tiên.

**So what / Ý nghĩa:**  
EN: The first 1–2 years are the most critical period for customer loyalty formation. Poor onboarding experience or premature cross-selling in this window sets a negative trajectory that is hard to reverse.  
VI: 1–2 năm đầu là giai đoạn quan trọng nhất để hình thành lòng trung thành khách hàng. Trải nghiệm onboarding kém hoặc bán chéo quá sớm tạo ra xu hướng tiêu cực khó đảo ngược.

**Hypothesis / Giả thuyết:**  
EN: Onboarding experience is insufficient to establish perceived value early enough. Customers who joined for a promotional offer may leave once the offer expires. Premature cross-selling in year 1 may accelerate early churn.  
VI: Trải nghiệm onboarding không đủ để thiết lập giá trị cảm nhận sớm. Khách hàng tham gia vì ưu đãi có thể rời khi ưu đãi hết hạn. Bán chéo quá sớm trong năm đầu có thể đẩy nhanh churn.

**To confirm / Để xác nhận cần thêm:**  
- Acquisition channel data (promo vs organic vs referral) / Kênh thu thập khách hàng  
- Onboarding completion rates / Tỷ lệ hoàn thành onboarding  
- First 90-day product usage data / Dữ liệu sử dụng sản phẩm 90 ngày đầu

**Recommendation / Đề xuất:**  
1. Redesign onboarding journey: structured 90-day engagement program for new customers / Thiết kế lại hành trình onboarding: chương trình tương tác 90 ngày có cấu trúc  
2. Implement "no cross-sell" policy for first 6 months / Chính sách không bán chéo trong 6 tháng đầu  
3. Assign onboarding specialist or chatbot check-ins at Day 7, 30, 90 / Phân công chuyên viên onboarding kiểm tra ở ngày 7, 30, 90

**Priority / Ưu tiên:** MEDIUM-HIGH — highest leverage point for long-term retention ROI.

---

## Finding 7: Low Credit Score Customers Show Slightly Higher Churn
## Phát Hiện 7: Khách Hàng Điểm Tín Dụng Thấp Có Tỷ Lệ Churn Cao Hơn Nhẹ

**Finding / Phát hiện:**  
EN: Very Poor credit score customers (350–500) churn at 29.1%, vs 24.0% for Good and Exceptional segments. However, the correlation between credit score and churn is weak (-0.021), suggesting credit score is not a primary driver.  
VI: Khách hàng điểm tín dụng rất kém (350–500) churn 29,1%, so với 24,0% của nhóm tốt và xuất sắc. Tuy nhiên tương quan giữa điểm tín dụng và churn yếu (-0,021), cho thấy đây không phải yếu tố chính.

**So what / Ý nghĩa:**  
EN: While the difference exists, credit score alone should not be used as a churn predictor. Focusing retention efforts primarily on credit score segments would be misallocating resources.  
VI: Mặc dù có sự chênh lệch, điểm tín dụng đơn lẻ không nên được dùng làm yếu tố dự đoán churn. Tập trung giữ chân dựa trên điểm tín dụng sẽ phân bổ nguồn lực sai.

**Hypothesis / Giả thuyết:**  
EN: Low credit score customers may have limited access to certain products, leading to lower engagement and higher churn. However, other variables (age, activity, products) are far stronger predictors.  
VI: Khách hàng điểm tín dụng thấp có thể bị hạn chế tiếp cận một số sản phẩm, dẫn đến tương tác thấp hơn và churn cao hơn. Tuy nhiên, các biến khác mạnh hơn nhiều.

**To confirm / Để xác nhận cần thêm:**  
- Product eligibility rules by credit score / Quy định đủ điều kiện sản phẩm theo điểm tín dụng  
- Multivariate analysis controlling for age and activity / Phân tích đa biến kiểm soát tuổi và mức độ hoạt động

**Recommendation / Đề xuất:**  
1. Do not use credit score as primary segmentation variable for retention targeting / Không dùng điểm tín dụng là biến phân khúc chính cho chiến lược giữ chân  
2. Include credit score as one of multiple inputs in a churn prediction model / Đưa điểm tín dụng vào mô hình dự đoán churn như một trong nhiều đầu vào

**Priority / Ưu tiên:** LOW — weak signal, use as supplementary variable only.

---

## Finding 8: Gender Gap in Churn Is Not Explained by Balance
## Phát Hiện 8: Khoảng Cách Churn Theo Giới Tính Không Được Giải Thích Bởi Số Dư

**Finding / Phát hiện:**  
EN: Female customers churn at 25.1% vs 16.5% for males — a 52% relative difference. Female customers actually have lower average balance ($75,659) than males ($77,174), meaning higher churn is not driven by wealth level. The gap is consistent across all geographies: France (27.9% F vs 18.1% M), Germany (41.0% F vs 31.7% M), Spain (26.0% F vs 18.9% M).  
VI: Khách hàng nữ churn 25,1% so với 16,5% của nam — chênh lệch tương đối 52%. Khách hàng nữ thực ra có số dư trung bình thấp hơn nam ($75,659 vs $77,174), nghĩa là churn cao hơn không do mức độ tài sản. Khoảng cách nhất quán ở tất cả địa lý.

**So what / Ý nghĩa:**  
EN: A gender-based churn gap consistent across all geographies suggests a systemic issue with how the bank serves female customers — in product design, communication, or service delivery. This also represents an underserved growth opportunity.  
VI: Khoảng cách churn theo giới tính nhất quán trên mọi địa lý cho thấy vấn đề hệ thống trong cách ngân hàng phục vụ khách hàng nữ — trong thiết kế sản phẩm, giao tiếp, hoặc cung cấp dịch vụ.

**Hypothesis / Giả thuyết:**  
EN: Three possible contributing causes: (1) product-preference mismatch — portfolio may be skewed toward financial behaviours more common among males; (2) communication and UX gaps — marketing tone or app design may not resonate equally; (3) financial life stage differences — female customers may face different milestones (career breaks, caregiving) that current products do not accommodate.  
VI: Ba nguyên nhân có thể: (1) sản phẩm không phù hợp thị hiếu nữ giới; (2) giọng điệu truyền thông hoặc UX chưa phù hợp; (3) sự khác biệt về giai đoạn tài chính — khách hàng nữ có thể đối mặt với các mốc khác nhau mà sản phẩm hiện tại chưa đáp ứng.

**To confirm / Để xác nhận cần thêm:**  
- Product usage breakdown by gender / Tỷ lệ sử dụng sản phẩm theo giới tính  
- NPS/CSAT scores by gender / Điểm NPS/CSAT theo giới tính  
- Marketing engagement rates by gender / Tỷ lệ tương tác marketing theo giới tính

**Recommendation / Đề xuất:**  
1. Conduct gender-segmented customer experience audit / Kiểm toán trải nghiệm khách hàng theo phân khúc giới tính  
2. Introduce targeted products for female financial life stages / Giới thiệu sản phẩm phù hợp giai đoạn tài chính của nữ giới  
3. Review marketing tone and app UX for gender inclusivity / Xem xét giọng điệu marketing và UX ứng dụng cho tính toàn diện giới tính

**Priority / Ưu tiên:** MEDIUM-HIGH — large segment, significant rate gap, actionable with further research.

---

## Summary Table / Bảng Tóm Tắt

| # | Finding | Churn Rate | vs Average | Priority |
|---|---------|-----------|------------|----------|
| 1 | 3+ Products | 85.9% | +65.5pp | HIGH |
| 2 | Age 51-60 | 56.2% | +35.8pp | HIGH |
| 5 | High Balance (>$150k) | 34.4% | +14.0pp | HIGH |
| 4 | Germany | 32.4% | +12.0pp | MEDIUM |
| 6 | Tenure 0-1 year | 29.1% | +8.7pp | MEDIUM-HIGH |
| 3 | Inactive Members | 26.9% | +6.5pp | MEDIUM-HIGH |
| 8 | Female customers | 25.1% | +4.7pp | MEDIUM-HIGH |
| 7 | Very Poor Credit Score | 29.1% | +8.7pp | LOW |

---

## Correlation Summary / Tóm Tắt Tương Quan

| Variable | Correlation with Churn | Interpretation |
|----------|----------------------|----------------|
| Age | +0.285 | Strong positive — older = higher churn |
| NumOfProducts | +0.147 | Moderate positive — more products = higher churn |
| IsActiveMember | -0.149 | Moderate negative — active = lower churn |
| Balance | +0.047 | Weak positive — higher balance = slightly higher churn |
| Tenure | -0.037 | Weak negative — longer tenure = slightly lower churn |
| CreditScore | -0.021 | Very weak — not a primary driver |
| EstimatedSalary | -0.000 | No relationship |

---

## Limitations & Next Steps / Hạn Chế & Bước Tiếp Theo

**Limitations / Hạn chế:**  
- Dataset is a historical static snapshot — does not reflect real-time behaviour / Dữ liệu là ảnh tĩnh lịch sử, không phản ánh hành vi thời gian thực  
- All findings are correlational — causality requires further validation / Tất cả phát hiện là tương quan — nhân quả cần xác nhận thêm  
- No exit survey, complaint, or channel preference data available / Không có dữ liệu khảo sát lý do rời bỏ, khiếu nại, hoặc kênh ưa thích  

**Recommended next steps / Bước tiếp theo:**  
1. Present findings to Product and Marketing teams for hypothesis prioritisation / Trình bày kết quả cho nhóm Sản phẩm và Marketing  
2. Request supplementary data: exit surveys, channel logs, complaint records / Yêu cầu dữ liệu bổ sung  
3. Build churn prediction model using Age, NumOfProducts, IsActiveMember as primary features / Xây dựng mô hình dự đoán churn  
4. Re-run analysis quarterly post-intervention to track improvement / Chạy lại phân tích hàng quý sau can thiệp  

---

*This document is a BA portfolio project based on a public Kaggle dataset.*  
*Tài liệu này là dự án portfolio BA dựa trên dataset công khai từ Kaggle.*  
*All findings are analytical observations, not confirmed business intelligence.*
