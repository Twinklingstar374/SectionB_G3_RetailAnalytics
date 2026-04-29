# Data Dictionary
## Retail Analytics | SectionB Group 3

## Dataset Info
| Property | Value |
|---|---|
| File | tableau_ready_dataset.csv |
| Rows | 302,010 |
| Columns | 30+ |
| Source | new_retail_data_2.csv |

---

## Original Columns

| Column | Type | Example | Description |
|---|---|---|---|
| Transaction_ID | String | TXN001 | Unique transaction identifier |
| Customer_ID | String | CUST001 | Unique customer identifier |
| Age | Integer | 34 | Customer age in years |
| Gender | String | Male/Female | Customer gender |
| Income | String | High/Medium/Low/Premium | Customer income level |
| Customer_Segment | String | Regular/New/Premium | Customer segment type |
| Date | Date | 2024-01-15 | Transaction date |
| Year | Integer | 2024 | Year of transaction |
| Month | String | January | Month of transaction |
| Time | String | 14:30 | Time of transaction |
| Day | Integer | 15 | Day of month |
| City | String | Mumbai | Customer city |
| State | String | Maharashtra | Customer state |
| Country | String | India | Customer country |
| Total_Purchases | Integer | 5 | Number of items purchased |
| Amount | Float | 1500.00 | Unit price in ₹ |
| Total_Amount | Float | 7500.00 | Total transaction value in ₹ |
| Product_Category | String | Electronics | Product category |
| Product_Brand | String | Samsung | Brand name |
| Product_Type | String | Mobile | Product type |
| Products | String | Samsung Galaxy | Product name |
| Feedback | String | Positive/Negative/Neutral | Customer feedback |
| Shipping_Method | String | Same-Day/Express/Standard | Shipping method |
| Payment_Method | String | Credit Card/Cash/UPI | Payment method |
| Order_Status | String | Delivered/Pending/Processing | Order status |
| Ratings | Float | 4.2 | Customer rating (1-5) |

---

## Engineered Columns
(Created in 02_cleaning.ipynb)

| Column | Type | Values | Description |
|---|---|---|---|
| avg_order_value | Float | 0 - ∞ | Total_Amount / Total_Purchases |
| age_group | String | 18-25, 26-35, 36-45, 46-60, 60+ | Customer age bracket |
| purchase_category | String | Low/Medium/High/Very High | Based on Total_Purchases count |
| revenue_category | String | Low/Medium/High/Premium | Based on Total_Amount value |
| weekday | String | Monday - Sunday | Day name from Date |
| is_weekend | Boolean | True/False | True if Saturday or Sunday |
| order_success | Integer | 0 or 1 | 1 = Delivered, 0 = Otherwise |
| rating_category | String | Poor/Average/Good/Excellent | Based on Ratings score |
| customer_value_segment | String | Low/Medium/High/Very High Value | Based on Total_Amount |

---

## Column Value Definitions

### Customer_Segment
| Value | Meaning |
|---|---|
| Regular | Existing loyal customer |
| New | First time or recent customer |
| Premium | High spending VIP customer |

### Order_Status
| Value | Meaning |
|---|---|
| Delivered | Order successfully delivered |
| Shipped | Order dispatched, in transit |
| Processing | Order being prepared |
| Pending | Order not yet processed |
| Cancelled | Order cancelled |

### Feedback
| Value | Meaning |
|---|---|
| Positive | Customer satisfied |
| Neutral | Customer neither satisfied nor dissatisfied |
| Negative | Customer dissatisfied |
| No Feedback | Customer did not provide feedback |

### Rating_Category
| Value | Range | Meaning |
|---|---|---|
| Excellent | 4.5 - 5.0 | Outstanding experience |
| Good | 3.5 - 4.4 | Positive experience |
| Average | 2.5 - 3.4 | Neutral experience |
| Poor | 1.0 - 2.4 | Negative experience |

### Age_Group
| Value | Range |
|---|---|
| 18-25 | Young adults |
| 26-35 | Early career |
| 36-45 | Mid career |
| 46-60 | Senior professionals |
| 60+ | Retired/Senior citizens |

### Customer_Value_Segment
| Value | Total_Amount Range |
|---|---|
| Low Value | ₹0 - ₹5,000 |
| Medium Value | ₹5,001 - ₹20,000 |
| High Value | ₹20,001 - ₹50,000 |
| Very High Value | ₹50,001+ |

---

## Dropped Columns (PII)
These columns were removed in 02_cleaning.ipynb
for privacy and data protection:

| Column | Reason |
|---|---|
| Name | Personal Identifiable Information |
| Email | Personal Identifiable Information |
| Phone | Personal Identifiable Information |
| Address | Personal Identifiable Information |
| Zipcode | Personal Identifiable Information |

---

## Data Quality Summary

| Metric | Value |
|---|---|
| Original Rows | 302,010 |
| Duplicate Rows Removed | ~258 |
| Columns after PII drop | 25 |
| Engineered Columns Added | 9 |
| Final Columns | 30+ |
| Null Values after cleaning | 0 |