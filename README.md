# 📊 Project: Analysis of International Exports (2000-2020)

Welcome to the final project for my data analysis bootcamp at Upgrade-Hub. This project focuses on the analysis of global export trends over two decades, from 2000 to 2020, with the aim of understanding the impact of major global events, particularly the 2008 financial crisis, on international trade.

## 📌 Introduction

International trade plays a pivotal role in shaping the global economy, and export activities are a key indicator of a country's economic health and competitiveness. The period from 2000 to 2020 was marked by significant events, including the rapid growth of emerging economies, the global financial crisis of 2008, and the subsequent recovery. This project examines the export performance of key countries during these periods, analyzing the trends and drawing insights that can inform future economic strategies.


## :world_map: How to use it

1. You can see the Streamlit (worldexports.py) without having to download all the in 
2. To be able to use the notebooks, download the kaggle.json and place this file in the ~/.kaggle/ directory (on Unix/Linux/Mac) or C:\Usersers\<Your Username>\.kaggle (on Windows).
3. Run every .ipynb (all of them starting with the numbers 1, 2, 3 or 4) to make sure you download all the images in different folders
4. You can start using and editing the streamlit app (worldexports.py) in your terminal
5. You can see and interact with the PowerBI (.pbix) by downloading it and opening it on the app if you already have it.


## 🎯 Project Objectives

The main objectives of this project are to:

1. **Analyze Export Trends**: Examine the annual export data of major global economies (Germany, United States, and China) to identify growth patterns over different periods.
   
2. **Impact of the 2008 Financial Crisis**: Conduct an in-depth analysis of the effect of the 2008 financial crisis on export growth, comparing pre-crisis, crisis, and post-crisis periods.
   
3. **Predict Future Export Trends**: Utilize machine learning models to forecast future export trends, providing insights into potential economic trajectories for key countries.

4. **Perform A/B Testing**: Assess the statistical significance of the impact of the 2008 crisis on the export growth rates of Germany, comparing the pre-crisis and post-crisis periods.

## 🛠️ Data Collection and Processing

### Data Sources

The data for this project was sourced from various reputable global trade databases, providing comprehensive export information for multiple countries over the specified period. The data includes:

- **Reporter/ReporterName**: The country that reports the trade data.
- **ReporterISO3**: ISO3 from the country that reports the trade data.
- **Partner/PartnerName**: The trade partner country involved in the transaction.
- **PartnerISO3**: ISO3 from the trade partner country involved in the transaction.
- **Trade Value in 1000 USD**: The monetary value of exports, reported in thousands of USD.
- **TradeFlow**: Exports.
- **Year**: The year in which the trade occurred.

### Data Processing

The data underwent several preprocessing steps, including:

- **Aggregation**: Summing up export values for each country per year to get total annual exports.
- **Conversion**: Transforming the trade values from thousands to millions of USD for better readability.
- **Filtering**: Selecting only relevant countries (Germany, United States, and China) and years (2000-2020).

## 🔍 Analysis and Insights

### Exploratory Data Analysis (EDA)

An exploratory analysis was conducted to visualize the export trends and identify key patterns. The analysis included:

- **Line Graphs**: Visualizing annual export growth for each country.
- **Comparative Analysis**: Comparing export performance across the three key periods: pre-crisis (2000-2007), crisis (2008-2010), and post-crisis (2011-2020).
- **Pie Chart**: Visualizing the main export partners.

### A/B Testing

To evaluate the impact of the 2008 financial crisis on Germany's export growth, A/B testing was conducted:

- **Pre-crisis vs. Post-crisis**: The growth rates before and after the crisis were statistically compared to determine if the crisis had a lasting impact on export growth.

### Machine Learning Predictions

Machine learning models were developed to predict future export trends based on historical data:

- **Model Training**: Historical export data was used to train predictive models.
- **Forecasting**: Future export values were forecasted, providing insights into the potential economic outlook for the next decade.

## 📈 Visualization

To effectively communicate the results, the following visualizations were created:

- **Annual Export Growth**: Bar charts showing the average annual export growth during each period.
- **Total Growth**: Bar charts illustrating the total export growth over the entire analysis period.
- **Predictive Trends**: Line graphs depicting the forecasted export trends for the coming years.

## 📅 Conclusion

This project reveals that global events, particularly the 2008 financial crisis, significantly impacted international export trends. The findings suggest that while the crisis caused a temporary slowdown, economies eventually recovered, leading to renewed export growth. However, ongoing economic challenges and emerging trade dynamics suggest that future growth may be more uncertain.

## 💬 Acknowledgements

I would like to extend my sincere thanks to the instructors, mentors, and peers at Upgrade-Hub for their guidance and support throughout this project. Their insights and encouragement were invaluable in the successful completion of this analysis. I also appreciate the opportunity to apply and enhance my data analysis skills through this comprehensive exploration of global trade. Thank you!
