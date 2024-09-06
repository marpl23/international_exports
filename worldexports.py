import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import kaggle

import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import os
import json
from PIL import Image
import requests
import plotly.graph_objs as go
import plotly.express as px

from scipy import stats
from scipy.stats import ttest_ind, skew

import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression

# ---------------------SITE--------------------------------------
st.set_page_config(page_title='International Trade Project', layout='wide', page_icon='🌎')

# --------------------IMG--------------------------
inttrade_path = r'img\INTERNATIONALTRADE.png'

# ------------------------DATA----------------------------
KAGGLE_USERNAME = "marpenalva"
KAGGLE_KEY = "ea42f53179cfa2f6eac83929293413f4"

kaggle.api.authenticate()

def download_file_from_kaggle(dataset, path):
    kaggle.api.dataset_download_files(dataset, path=path, unzip=True)

dataset = "appetukhov/international-trade-database"  # Dataset correcto
download_path = "data/"

if not os.path.exists(download_path):
    os.makedirs(download_path)

download_file_from_kaggle(dataset, download_path)


file_path = os.path.join(download_path, 'trade_1988_2021.csv')
trade_df = pd.read_csv(file_path)

# ---------------------MENU------------------------------
menu = st.sidebar.selectbox("Menu", ["Introduction", "Analysis", "A/B Testing", "Machine Learning", "Conclusion"])


if menu == "Introduction":
    st.image(inttrade_path, width=700)
    st.header("Introduction")
    st.write("This project analyzes a dataset extracted from Kaggle showing world exports by country from 1988 to 2021. The database is provided by UN Comtrade (a repository of official international trade statistics) for World Integrated Trade Solution (WITS) platform.")
    st.write("In this project we will look at exports at the global level, but for context we will also look at imports and the trade balance. We will focus the years from 2000 to 2020, and three countries, China, Germany and the United States, the three major economic forces at the turn of the century, analyzing them to understand the international context and how the crises affected the different continents.")
    st.write("This project will be divided into three parts: the first, the analysis and comparison of the selected data. Second, a hypothesis contrast (A/B Testing) and finally a future prediction with Machine Learning.")
    
# ----------------------FILTER---------------------------------- 
    st.write('Below you can filter the data to see the value of exports. ')
    
    reporter = st.selectbox('Select Reporter', trade_df['ReporterName'].unique())
    partner = st.selectbox('Select Partner', trade_df['PartnerName'].unique())
    year = st.selectbox('Select Year', sorted(trade_df['Year'].unique()))

    filtered_data = trade_df[
        (trade_df['ReporterName'] == reporter) &
        (trade_df['PartnerName'] == partner) &
        (trade_df['Year'] == year)
    ]

    st.dataframe(filtered_data)
    
#-------------------------ANALYSIS------------------------
  
elif menu == "Analysis":
    st.header("Data Analysis")
    analysis = option_menu(None, 
    ["World Exports", "World Imports", "Data by Country"])

#------------------------EXPORTS--------------------------

    if analysis == "World Exports":
        selected_year = st.selectbox('Select Year', list(range(2000, 2021)))
        col1, col2 = st.columns(2)

        with col1:
            st.image(f'graphs2/exp/top_exports_{selected_year}.png', caption=f'Top 10 Exports Countries in {selected_year}')
            
        with col2:
            st.image(f'graphs2/exp/bottom_exports_{selected_year}.png', caption=f'Bottom 10 Exports Countries in {selected_year}')
    
        
#------------------------IMPORTS--------------------------
    
    elif analysis == "World Imports":
        selected_year = st.selectbox('Select Year', list(range(2000, 2021)))
        col1, col2 = st.columns(2)

        with col1:
            st.image(f'graphs/imp/top_imports_{selected_year}.png', caption=f'Top 10 Exports Countries in {selected_year}')
            
        with col2:
            st.image(f'graphs/imp/bottom_imports_{selected_year}.png', caption=f'Bottom 10 Exports Countries in {selected_year}')
        
#----------------------COUNTRIES----------------------
    
    elif analysis == "Data by Country": 
        
        with open(f"graphs/balance/tradebalance.html", "r", encoding="utf-8") as file:
            plot_html = file.read()
    
        st.components.v1.html(plot_html, height=400, width=1000)
        
        data_by_country = st.selectbox(
            "Select one:",
            ["Germany", "China", "United States"]
        )
#-----------------------CHINA-------------------------
        if data_by_country == 'China':
            with open(f"graphs2/china/tb.html", "r", encoding="utf-8") as file:
                plot_html = file.read()
    
            st.components.v1.html(plot_html, height=600, width=1000)
            
            with open(f"graphs2/china/main.html", "r", encoding="utf-8") as file:
                plot_html = file.read()
    
            st.components.v1.html(plot_html, height=1000, width=1000)

#------------------------USA------------------------
        elif data_by_country == 'United States':
            with open(f"graphs2/usa/tb.html", "r", encoding="utf-8") as file:
                plot_html = file.read()
    
            st.components.v1.html(plot_html, height=600, width=1000)
            
            with open(f"graphs2/usa/main.html", "r", encoding="utf-8") as file:
                plot_html = file.read()
    
            st.components.v1.html(plot_html, height=1000, width=1000)
        
#-----------------------------GER---------------------
        elif data_by_country == 'Germany':
            with open(f"graphs2/germany/tb.html", "r", encoding="utf-8") as file:
                plot_html = file.read()
    
            st.components.v1.html(plot_html, height=600, width=1000)
            
            with open(f"graphs2/germany/main.html", "r", encoding="utf-8") as file:
                plot_html = file.read()
    
            st.components.v1.html(plot_html, height=1000, width=1000)
            
#--------------------------CDA------------------------
    
elif menu == "A/B Testing":
    st.header("A/B Testing")
    st.markdown("Hypothesis: The 2008 Financial Crisis negatively influenced exports and imports of the most developed countries in the world. We will now analyze how the 2008 crisis affected exports in China, the United States and Germany, as they are the best example to represent the three continents with the largest trade flows (Asia, America and Europe).")
    st.markdown("""
    We are going to divide our data in 2 groups for every country:
    - **Group A (Pre-Crisis): 2000-2008**
    - **Group B (Post-Crisis): 2009-2020**

    For a better understanding of the crisis magnitude, we will also use another intermediate group (**2008-2009**).
    """)
    st.markdown('''
    - Null Hypothesis (H0): The 2008 crisis has not significantly affected export growth.
    - Alternative Hypothesis (H1): The 2008 crisis has significantly affected export growth.)
    ''')
    
    col1, col2 = st.columns(2)

    with col1:
        with open("graphs/cda/annual_growth.html", "r", encoding="utf-8") as file:
            plot_html_1 = file.read()
        st.components.v1.html(plot_html_1, height=600, width=700)

    with col2:
        with open("graphs/cda/growth.html", "r", encoding="utf-8") as file:
            plot_html_2 = file.read()
        st.components.v1.html(plot_html_2, height=600, width=700)
    
    cda_country = st.selectbox(
         "Select one:",
        ["Germany", "China", "United States"]
        )

#-------------------------CDA-CHINA------------------------
    if cda_country == 'China':
        china_data = trade_df[trade_df['ReporterName'] == 'China']
    
        pre_crisis = (2000, 2008)
        post_crisis = (2009, 2020)

        def calculate_annual_growth(data, start_year, end_year):
            annual_growths = []
            for year in range(start_year, end_year):
                start_value = data[data['Year'] == year]['TradeValue in 1000 USD'].sum()
                end_value = data[data['Year'] == (year + 1)]['TradeValue in 1000 USD'].sum()

                annual_growth = ((end_value - start_value) / start_value) * 100
                annual_growths.append(annual_growth)
        
            return annual_growths

        pre_crisis_growths = calculate_annual_growth(china_data, pre_crisis[0], pre_crisis[1])
        post_crisis_growths = calculate_annual_growth(china_data, post_crisis[0], post_crisis[1])

        skewness_pre_crisis = skew(pre_crisis_growths)
        skewness_post_crisis = skew(post_crisis_growths)

        t_stat, p_value = ttest_ind(pre_crisis_growths, post_crisis_growths)

        st.subheader("Results of the Analysis")

        st.write(f"**Pre-Crisis ({pre_crisis[0]}-{pre_crisis[1]}):**")
        st.write(f"- Average Annual Growth: {pd.Series(pre_crisis_growths).mean():.2f}%")
        st.write(f"- Skewness: {skewness_pre_crisis:.4f}")

        st.write(f"**Post-Crisis ({post_crisis[0]}-{post_crisis[1]}):**")
        st.write(f"- Average Annual Growth: {pd.Series(post_crisis_growths).mean():.2f}%")
        st.write(f"- Skewness: {skewness_post_crisis:.4f}")

        st.write(f"**Result of the Hypothesis Test:**")
        st.write(f"- T-Statistic: {t_stat:.4f}")
        st.write(f"- P-Value: {p_value:.4f}")

        if p_value < 0.05:
            st.write("**Conclusion:** We reject the null hypothesis. There is a significant difference in China's annual export growth before and after the crisis of 2008.")
        else:
            st.write("**Conclusion:** We cannot reject the null hypothesis. There is no significant difference in China's annual export growth before and after the 2008 crisis.")

        st.subheader("Visualisation of Annual Growth")
        years_pre_crisis = list(range(pre_crisis[0], pre_crisis[1]))
        years_post_crisis = list(range(post_crisis[0], post_crisis[1]))

        fig = go.Figure()
        fig.add_trace(go.Scatter(
                x=years_pre_crisis, 
                y=pre_crisis_growths, 
                mode='lines+markers', 
                name='Pre-Crisis',
                line=dict(color='blue')
            ))

        fig.add_trace(go.Scatter(
                x=years_post_crisis, 
                y=post_crisis_growths, 
                mode='lines+markers', 
                name='Post-Crisis',
                line=dict(color='green')
            ))

        fig.add_trace(go.Scatter(
                x=[2008, 2008],
                y=[min(pre_crisis_growths + post_crisis_growths), max(pre_crisis_growths + post_crisis_growths)],
                mode='lines',
                name='Beginning of the Crisis',
                line=dict(color='red', dash='dash')
            ))

        fig.update_layout(
                title='Annual Growth of Chinese Exports',
                xaxis_title='Year',
                yaxis_title='Annual Growth (%)',
                width=800, 
                height=500
            )

        st.plotly_chart(fig)
        
        

#------------------------CDA-USA------------------------
    elif cda_country == 'United States':
        us_data = trade_df[trade_df['ReporterName'] == 'United States']
    
        pre_crisis = (2000, 2008)
        post_crisis = (2009, 2020)

        def calculate_annual_growth(data, start_year, end_year):
            annual_growths = []
            for year in range(start_year, end_year):
                start_value = data[data['Year'] == year]['TradeValue in 1000 USD'].sum()
                end_value = data[data['Year'] == (year + 1)]['TradeValue in 1000 USD'].sum()

                annual_growth = ((end_value - start_value) / start_value) * 100
                annual_growths.append(annual_growth)
        
            return annual_growths

        pre_crisis_growths = calculate_annual_growth(us_data, pre_crisis[0], pre_crisis[1])
        post_crisis_growths = calculate_annual_growth(us_data, post_crisis[0], post_crisis[1])

        skewness_pre_crisis = skew(pre_crisis_growths)
        skewness_post_crisis = skew(post_crisis_growths)

        t_stat, p_value = ttest_ind(pre_crisis_growths, post_crisis_growths)

        st.subheader("Results of the Analysis")

        st.write(f"**Pre-Crisis ({pre_crisis[0]}-{pre_crisis[1]}):**")
        st.write(f"- Average Annual Growth: {pd.Series(pre_crisis_growths).mean():.2f}%")
        st.write(f"- Skewness: {skewness_pre_crisis:.4f}")

        st.write(f"**Post-Crisis ({post_crisis[0]}-{post_crisis[1]}):**")
        st.write(f"- Average Annual Growth: {pd.Series(post_crisis_growths).mean():.2f}%")
        st.write(f"- Skewness: {skewness_post_crisis:.4f}")

        st.write(f"**Result of the Hypothesis Test:**")
        st.write(f"- T-Statistic: {t_stat:.4f}")
        st.write(f"- P-Value: {p_value:.4f}")

        if p_value < 0.05:
            st.write("**Conclusion:** We reject the null hypothesis. There is a significant difference in US's annual export growth before and after the crisis of 2008.")
        else:
            st.write("**Conclusion:** We cannot reject the null hypothesis. There is no significant difference in US's annual export growth before and after the 2008 crisis.")

        st.subheader("Visualisation of Annual Growth")
        years_pre_crisis = list(range(pre_crisis[0], pre_crisis[1]))
        years_post_crisis = list(range(post_crisis[0], post_crisis[1]))

        fig = go.Figure()
        fig.add_trace(go.Scatter(
                x=years_pre_crisis, 
                y=pre_crisis_growths, 
                mode='lines+markers', 
                name='Pre-Crisis',
                line=dict(color='blue')
            ))

        fig.add_trace(go.Scatter(
                x=years_post_crisis, 
                y=post_crisis_growths, 
                mode='lines+markers', 
                name='Post-Crisis',
                line=dict(color='green')
            ))

        fig.add_trace(go.Scatter(
                x=[2008, 2008],
                y=[min(pre_crisis_growths + post_crisis_growths), max(pre_crisis_growths + post_crisis_growths)],
                mode='lines',
                name='Beginning of the Crisis',
                line=dict(color='red', dash='dash')
            ))

        fig.update_layout(
                title='Annual Growth of US Exports',
                xaxis_title='Year',
                yaxis_title='Annual Growth (%)',
                width=800, 
                height=500
            )

        st.plotly_chart(fig)

#-----------------------CDA-GERMANY------------------------------------------
    elif cda_country == 'Germany':
        germany_data = trade_df[trade_df['ReporterName'] == 'Germany']
    
        pre_crisis = (2000, 2008)
        post_crisis = (2009, 2020)

        def calculate_annual_growth(data, start_year, end_year):
            annual_growths = []
            for year in range(start_year, end_year):
                start_value = data[data['Year'] == year]['TradeValue in 1000 USD'].sum()
                end_value = data[data['Year'] == (year + 1)]['TradeValue in 1000 USD'].sum()

                annual_growth = ((end_value - start_value) / start_value) * 100
                annual_growths.append(annual_growth)
        
            return annual_growths

        pre_crisis_growths = calculate_annual_growth(germany_data, pre_crisis[0], pre_crisis[1])
        post_crisis_growths = calculate_annual_growth(germany_data, post_crisis[0], post_crisis[1])

        skewness_pre_crisis = skew(pre_crisis_growths)
        skewness_post_crisis = skew(post_crisis_growths)

        t_stat, p_value = ttest_ind(pre_crisis_growths, post_crisis_growths)

        st.subheader("Results of the Analysis")

        st.write(f"**Pre-Crisis ({pre_crisis[0]}-{pre_crisis[1]}):**")
        st.write(f"- Average Annual Growth: {pd.Series(pre_crisis_growths).mean():.2f}%")
        st.write(f"- Skewness: {skewness_pre_crisis:.4f}")

        st.write(f"**Post-Crisis ({post_crisis[0]}-{post_crisis[1]}):**")
        st.write(f"- Average Annual Growth: {pd.Series(post_crisis_growths).mean():.2f}%")
        st.write(f"- Skewness: {skewness_post_crisis:.4f}")

        st.write(f"**Result of the Hypothesis Test:**")
        st.write(f"- T-Statistic: {t_stat:.4f}")
        st.write(f"- P-Value: {p_value:.4f}")

        if p_value < 0.05:
            st.write("**Conclusion:** We reject the null hypothesis. There is a significant difference in Germany's annual export growth before and after the crisis of 2008.")
        else:
            st.write("**Conclusion:** We cannot reject the null hypothesis. There is no significant difference in Germany's annual export growth before and after the 2008 crisis.")

        st.subheader("Visualisation of Annual Growth")
        years_pre_crisis = list(range(pre_crisis[0], pre_crisis[1]))
        years_post_crisis = list(range(post_crisis[0], post_crisis[1]))

        fig = go.Figure()
        fig.add_trace(go.Scatter(
                x=years_pre_crisis, 
                y=pre_crisis_growths, 
                mode='lines+markers', 
                name='Pre-Crisis',
                line=dict(color='blue')
            ))

        fig.add_trace(go.Scatter(
                x=years_post_crisis, 
                y=post_crisis_growths, 
                mode='lines+markers', 
                name='Post-Crisis',
                line=dict(color='green')
            ))

        fig.add_trace(go.Scatter(
                x=[2008, 2008],
                y=[min(pre_crisis_growths + post_crisis_growths), max(pre_crisis_growths + post_crisis_growths)],
                mode='lines',
                name='Beginning of the Crisis',
                line=dict(color='red', dash='dash')
            ))

        fig.update_layout(
                title='Annual Growth of German Exports',
                xaxis_title='Year',
                yaxis_title='Annual Growth (%)',
                width=800, 
                height=500
            )

        st.plotly_chart(fig)
    
#--------------------------------------------ML-----------------------------
elif menu == "Machine Learning":
    st.header("Machine Learning - Regression Model")
    st.write("Here you can observe the future prediction of China's, Germany's and the USA's exports for the years 2021 to 2030")

    with open(f"graphs\ML\comparative.html", "r", encoding="utf-8") as file:
            plot_html = file.read()
    
    st.components.v1.html(plot_html, height=600, width=1000)
            
    st.write('Before and After dispersion mapping by country:')        
    data_ml_country = st.selectbox(
        "Select one:",
        ["Germany", "China", "United States"]
        )
    
    if data_ml_country == 'China':
        col1, col2 = st.columns(2)

        with col1:
            st.image(r'graphs/ML/china_past.png', caption='China exports 2000 - 2020')
        with col2:
            st.image(r'graphs/ML/china_future.png', caption='China exports 2021 - 2030')

    elif data_ml_country == 'Germany':
        col1, col2 = st.columns(2)

        with col1:
            st.image(r'graphs/ML/germany_past.png', caption='Germany exports 2000 - 2020')
        with col2:
            st.image(r'graphs/ML/germany_future.png', caption='Germany exports 2021 - 2030')
        
    elif data_ml_country == 'United States':
        col1, col2 = st.columns(2)
            
        with col1:    
            st.image(r'graphs/ML/USA_past.png', caption='USA exports 2000 - 2020')
        with col2:    
            st.image(r'graphs/ML/USA_future.png', caption='USA exports 2021 - 2030')
            
#---------------------------CONCLUSION--------------------------------------
elif menu == "Conclusion":
    st.header("Conclusion")
    st.write("Analysis of international exports between 2000 and 2020 identifies three key phases in the global economy. In the pre-crisis growth phase (2000-2007), globalisation and the rise of emerging economies drove a sustained increase in exports. The 2008 financial crisis caused a huge slowdown in international trade, mainly affecting developed economies such as Germany and the United States. Finally, in the post-crisis phase (2011-2020), exports gradually recovered, although trade tensions and protectionist policies generated new uncertainties.")
    st.write("I hope you have enjoyed this world exports analysis, you can also interact with a PowerBI dowloading it on the following link.")
    
    file_url = "https://uphubgrade-my.sharepoint.com/:u:/g/personal/mar_penalva_lozano_bootcamp-upgrade_com/EdU1sWyhwA1Au4CN1mZiq1sBG0IeFDlGXKdHraTCPJRufQ?e=kV9hBq"

    link_text = "Click here and next click Download to see the World Exports PowerBI"

    st.markdown(f"[{link_text}]({file_url})")



