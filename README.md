# NST DVA Capstone 2 - Retail Analytics: End-to-End Data Pipeline & Interactive Dashboard

**Newton School of Technology | Data Visualization & Analytics**  
A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.

## Before You Start
- [x] Rename the repository using the format `SectionName_TeamID_ProjectName`.
- [x] Fill in the project details and team table below.
- [x] Add the raw dataset to `data/raw/`.
- [x] Complete the notebooks in order from 01 to 05.
- [x] Publish the final dashboard and add the public link in `tableau/dashboard_links.md`.
- [x] Export the final report and presentation as PDFs into `reports/`.

## Quick Start

If you are working locally:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

If you are working in Google Colab:
- Upload or sync the notebooks from `notebooks/`
- Keep the final `.ipynb` files committed to GitHub
- Export any cleaned datasets into `data/processed/`

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Retail Analytics: End-to-End Data Pipeline & Interactive Dashboard |
| **Sector** | Retail & E-Commerce |
| **Team ID** | SectionB Group 3 |
| **Section** | B |
| **Faculty Mentor** | Please add mentor name |
| **Institute** | Newton School of Technology |
| **Submission Date** | April 29, 2026 |

## Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Team Lead & Visualization | Bulbul Agarwalla | bulbul.agarwalla |
| Data Engineer / Analyst | Shourya Pratap | shouryapratap |
| Data Engineer / Analyst | Varun Udata | github-handle |
| Analyst / Visualization | Nishant Sharma | github-handle |
| Data Engineer / Analyst | Anant Lalwani | github-handle |
| Analyst | Parul | github-handle |

*(Roles approximated based on the contribution matrix)*

## Business Problem

The retail sector increasingly depends on data-driven decision-making to remain competitive. This project addresses the challenge of transforming 302,010 raw retail transactions into actionable intelligence for business leaders. Without proper analysis, key patterns in customer behaviour, product performance, and operational efficiency remain hidden, leading to suboptimal business decisions.

### Core Business Question
How can a retail organisation transform 302,010 raw transactional records into a structured, interactive analytics system that enables data-driven decision-making across sales, customer, product, and operational dimensions?

### Decision Supported
This analysis serves Chief Revenue Officers, Chief Marketing Officers, and Operations Managers. It enables improved customer targeting (potentially increasing conversion by 15-20%), operational efficiency gains to reduce cancellations (5-8%), and data-driven product decisions to optimize inventory costs (10-15%).

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | `new_retail_data_2.csv` |
| **Direct Access Link** | To be filled by team |
| **Row Count** | 302,010 transactions |
| **Column Count** | 30+ (25 original + 9 engineered) |
| **Time Period Covered** | Full calendar year (Jan-Dec) |
| **Format** | CSV |

### Key Columns Used

| Column Name | Description | Role in Analysis |
|---|---|---|
| `Total_Amount` | Total transaction value in Rs. | Revenue and value segmentation |
| `Customer_Segment` | New / Regular / Premium | Customer segmentation and behavior |
| `Product_Category` | Product category name | Product performance |
| `Order_Status` | Delivered / Shipped / Processing / Pending | Operational efficiency |

For full column definitions, see `docs/data_dictionary.md`.

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| Total Revenue | Overall sum of transaction amounts | `SUM(Total_Amount)` |
| Total Orders | Volume of business activity | `COUNT(Transaction_ID)` |
| Average Order Value (AOV) | Customer spending efficiency | `AVG(avg_order_value)` |
| Order Success Rate | Operational efficiency | `SUM(order_success)/COUNT(*)` |
| Total Unique Customers | Customer base size | `COUNTD(Customer_ID)` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | [Product Performance Analysis](https://public.tableau.com/app/profile/bulbul.agarwalla/viz/SectionB_RetailAnalysis_G3/ProductPerformanceAnalysis?publish=yes) |
| **Executive View** | Sales & Revenue Overview with total revenue, order trends, and regional performance |
| **Operational View** | Operational Insights Overview focusing on order success, shipping methods, and feedback |
| **Main Filters** | Interactive filters for dynamic analysis across product, region, and time |

Store dashboard screenshots in `tableau/screenshots/` and document the public links in `tableau/dashboard_links.md`.

## Key Insights

1. **Regular Customers:** Regular customers drive 48% of total revenue, making retention of this segment the highest-priority business action.
2. **Seasonal Peaks:** April is the peak revenue month generating Rs. 57 Cr, while November/December records the lowest revenue, indicating seasonal patterns requiring targeted promotions.
3. **Shipping Preferences:** Same-Day shipping generates the highest revenue (Rs. 142Cr) and is the most preferred method, suggesting investment in fast delivery infrastructure.
4. **Operational Performance:** 94.7% order success rate indicates strong operational performance, with the remaining 5.3% representing ~Rs. 22Cr in recoverable revenue through process improvement.
5. **Pending Orders:** 16% of orders are pending, representing a process bottleneck requiring operational review to prevent customer churn.
6. **Premium Spending:** Premium customers spend significantly more (confirmed via t-test), validating the business case for a Premium customer acquisition programme.
7. **Age Demographics:** The 26-35 age group is the largest customer segment; marketing messaging should be optimised for early-career digital-native consumers.
8. **Weekday Dominance:** Weekdays generate 71.7% of revenue; B2B promotional strategies should focus on weekday engagement.

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Regular customers drive 48% of revenue | Launch a Regular Customer Loyalty Programme to increase retention. | 10-15% increase in repeat purchase rate, +Rs. 20-30Cr annual revenue. |
| 2 | December is the lowest revenue month | Introduce November/December promotional campaigns with bundle offers. | 15-20% revenue uplift in December, +Rs. 8-10Cr seasonal revenue. |
| 3 | Same-Day shipping generates Rs. 142Cr | Expand Same-Day delivery capacity to all regions through partnerships. | 10-12% increase in Same-Day adoption, +Rs. 14-17Cr annual revenue. |
| 4 | 16% of orders remain pending | Implement automated order processing triggers and SLA monitoring. | Reduction of pending rate to 8%, recovering Rs. 10-15Cr at-risk. |
| 5 | Premium customers spend significantly more | Create a Regular-to-Premium upgrade pathway with personalised offers. | 5% conversion of Regular to Premium adds +Rs. 10Cr annually. |

## Repository Structure

```text
SectionB_G3_RetailAnalytics/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- README.md
|   |-- project_report_template.md
|   `-- presentation_outline.md
|
|-- docs/
|   `-- data_dictionary.md
```

## Analytical Pipeline

The project follows a structured 7-step workflow:

1. **Define** - Sector selected, problem statement scoped, mentor approval obtained.
2. **Extract** - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb`.
4. **Analyze** - EDA and statistical analysis performed in notebooks 03 and 04.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - Data-backed business recommendations delivered.
7. **Report** - Final project report and presentation deck completed and exported to PDF in `reports/`.

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |

**Recommended Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `scikit-learn`

## Evaluation Rubric

| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

## Submission Checklist

**GitHub Repository**
- [x] Public repository created with the correct naming convention (`SectionB_G3_RetailAnalytics`)
- [x] All notebooks committed in `.ipynb` format
- [ ] `data/raw/` contains the original, unedited dataset
- [ ] `data/processed/` contains the cleaned pipeline output
- [ ] `tableau/screenshots/` contains dashboard screenshots
- [x] `tableau/dashboard_links.md` contains the Tableau Public URL
- [x] `docs/data_dictionary.md` is complete
- [x] `README.md` explains the project, dataset, and team
- [ ] All members have visible commits and pull requests

**Tableau Dashboard**
- [x] Published on Tableau Public and accessible via public URL
- [x] At least one interactive filter included
- [x] Dashboard directly addresses the business problem

**Project Report**
- [ ] Final report exported as PDF into `reports/`
- [ ] Cover page, executive summary, sector context, problem statement
- [ ] Data description, cleaning methodology, KPI framework
- [ ] EDA with written insights, statistical analysis results
- [ ] Dashboard screenshots and explanation
- [ ] 8-12 key insights in decision language
- [ ] 3-5 actionable recommendations with impact estimates
- [ ] Contribution matrix matches GitHub history

**Presentation Deck**
- [ ] Final presentation exported as PDF into `reports/`
- [ ] Title slide through recommendations, impact, limitations, and next steps

**Individual Assets**
- [ ] DVA-oriented resume updated to include this capstone
- [ ] Portfolio link or project case study added

## Contribution Matrix

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| **Bulbul Agarwalla** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Shourya Pratap** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Nishant Sharma** |  |  | ✓ | ✓ |  |  | ✓ |
| **Udata Varun** |  |  |  |  |  | ✓ | ✓ |
| **Anant Lalwani** |  | ✓ |  |  |  |  | ✓ |
| **Parul** | ✓ |  |  |  |  |  | ✓ |

*Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts.*

**Team Lead Signature:** Bulbul Agarwalla  
**Date:** April 29, 2026

## Academic Integrity
All analysis, code, and recommendations in this repository must be the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.
