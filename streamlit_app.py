import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import preprocessing
import helper

df = pd.read_csv('Space_Corrected.csv')
df = preprocessing.preprocess(df)
df_ = preprocessing.RA(df)

st.sidebar.title("Space Mission Analysis")
st.sidebar.image('./space-mission-img.jpg')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Overall','Country-wise Analysis','Status of Mission', 'Rocket Analysis')
)

if user_menu=="Overall":
    st.title("Overall")
    st.dataframe(df)
    st.title("Description")
    st.write(df.describe())

if user_menu=="Country-wise Analysis":
    st.title("Countries and their space mission")
    helper.Countries_mission(df)
    st.title("Show analysis with respect to country")
    selected_company = st.selectbox("Select country", helper.Countries_names(df))
    helper.companyCountries(df, selected_company)

if user_menu=="Status of Mission":
    st.title("Status of Mission")
    MS = helper.MissionStatus(df)
    st.dataframe(MS)
    SM = MS.copy()
    fig = plt.figure(figsize=(10, 5))
    ax = sns.barplot(data=SM, x=SM['Status Mission'], y=SM.Frequency, errwidth=1, palette="Paired")
    for p in ax.patches:
        ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x() + 0.1, p.get_height() + 1))
    st.title("Frequencies of Mission Status")
    st.pyplot(fig)


    RS = helper.RocketStatus(df)
    Rocket_status = df["Status Rocket"].value_counts()
    palette_color = sns.color_palette('muted')
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(Rocket_status, labels=Rocket_status.index, colors=palette_color, autopct='%.0f%%')
    ax.set_title("Rocket Status")
    st.title("Status of Rocket")
    st.pyplot(fig)

if user_menu == "Rocket Analysis":
    st.title("Company spend money")
    df_ = preprocessing.RA(df)
    money_by_company = helper.Money(df)

    st.dataframe(money_by_company)

    st.title("Here are top 5 rocket companies-")
    helper.RocketMoney(df_)

