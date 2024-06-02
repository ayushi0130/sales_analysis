# sales_analysis

Welcome to the Sales Analysis Data repository! This repository contains data and scripts used for analyzing sales performance over different periods, identifying trends, and providing insights into sales activities.

Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Data Description](#data-description)
- [Installation](#installation)
- [Usage](#usage)
- [Result](#result)

## Project Overview

### Sales_analysis

In this project we use Python Pandas & Python Matplotlib to analyze and answer business questions about 12 months worth of sales data. The data contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc.

We start by cleaning our data. Tasks during this section include:

- Drop NaN values from DataFrame
- Removing rows based on a condition
- Change the type of columns (to_numeric, to_datetime, astype)

Once we have cleaned up our data a bit, we move the data exploration section. In this section we explore 5 high level business questions related to our data:

- What was the best month for sales? How much was earned that month?
- What city sold the most product?
- What time should we display advertisements to maximize the \* likelihood of customer’s buying product?
- What products are most often sold together?
- What product sold the most? Why do you think it sold the most?

To answer these questions we walk through many different pandas & matplotlib methods. They include:

- Concatenating multiple csvs together to create a new DataFrame (pd.concat)
- Adding columns
- Parsing cells as strings to make new columns (.str)
- Using the .apply() method
- Using groupby to perform aggregate analysis
- Plotting bar charts and lines graphs to visualize our results
- Labeling our graphs

### diwali_sales_analysis

In this project we explore some business questions related to our data:

- who buy the product most?
- which city buy the product most?
- which sector person buying the product most?
- which product category they invest most?

## Directory Structure

```
 ├── README.md
 ├── diwali_sales_analysis
 │   ├── Diwali_Sales_Data.csv
 │   └── diwali_sales_analysis.py
 └── sales_analysis
     └── Sales_Data
         ├── Sales_April_2019.csv
         ├── Sales_August_2019.csv
         ├── Sales_December_2019.csv
         ├── Sales_February_2019.csv
         ├── Sales_January_2019.csv
         ├── Sales_July_2019.csv
         ├── Sales_June_2019.csv
         ├── Sales_March_2019.csv
         ├── Sales_May_2019.csv
         ├── Sales_November_2019.csv
         ├── Sales_October_2019.csv
         ├── Sales_September_2019.csv
         └── sales_analysis.py
```

- data/: Contains all the data files.
- scripts/: Python scripts for data cleaning, processing, analysis and exploratory data analysis (EDA) and visualizations.
- README.md: This file.

## Data Description

The primary dataset used in this analysis includes the following fields:

- Order Date: The date of the sale.
- Sales: The amount of sales in dollars.
- Product: The product name.
- Order ID: A unique identifier for each customer.
- Region: The geographical region of the sale.
  Additional datasets may include customer demographics, product details, and regional economic indicators.

## Installation

To set up the environment for this project, follow these steps:

Clone the repository:

```
git clone https://github.com/mangal0130/sales-analysis-data.git
```

Navigate to the project directory:

```
cd sales-analysis-data
```

## Usage

Here is a basic overview of how to use the contents of this repository:

1. Data Preparation: Place your raw data files in the data/raw/ directory.

2. Data Processing: Use the scripts in the scripts/ directory to process and clean the data.

3. Exploratory Data Analysis: Open the notebooks in the notebooks/ directory to explore and visualize the data.

4. Generate Reports: Use the processed data to generate reports.

## Result

### sales_analysis_data

- Best month for sale: <img width="642" alt="sales_month" src="https://github.com/ayushi0130/sales_analysis/assets/128896031/07d2dee0-5480-44ba-9892-ff7e810bc3c2">

- city has highest number of sales: ![city_highest_no](https://github.com/ayushi0130/sales_analysis/assets/128896031/b9a6cd60-8790-48f6-85e9-49811596e012)

- time to display the advertisements: ![advert_time](https://github.com/ayushi0130/sales_analysis/assets/128896031/0c7f4c1d-3375-4953-b29e-16ae83bc2fe2)

- product often sold together: ![prod_sold_together](https://github.com/ayushi0130/sales_analysis/assets/128896031/b0bd0f10-d2bd-48ba-97f9-46d924c9f573)

- product sold the most: ![prod_sold_most](https://github.com/ayushi0130/sales_analysis/assets/128896031/db616e8a-bb60-404d-908b-71ea22967054)

### diwali_analysis_data

As per the analysis Married women age group from 26-35 yrs from UP, Maharastra, Karnataka working in IT, Healthcare and Aviation are more likely to buy product from food, clothing and Electronics category.
