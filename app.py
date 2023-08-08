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
    ('Overall','Company-wise Analysis','Status of Mission', 'Rocket Analysis')
)

if user_menu=="Overall":
    st.title("Overall")
    st.dataframe(df)
    st.title("Description")
    st.write(df.describe())

if user_menu=="Company-wise Analysis":
    st.title("Companies and their space mission")
    temp = helper.Company_mission(df)
    st.dataframe(temp)
    list28 = np.random.randint(1, 100, size=28)
    company_names = ["Company 1", "Company 2", "Company 3", "Company 4", "Company 5",
                     "Company 6", "Company 7", "Company 8", "Company 9", "Company 10",
                     "Company 11", "Company 12", "Company 13", "Company 14", "Company 15",
                     "Company 16", "Company 17", "Company 18", "Company 19", "Company 20",
                     "Company 21", "Company 22", "Company 23", "Company 24", "Company 25",
                     "Company 26", "Company 27", "Company 28"]
    fig = plt.figure(figsize=(10, 6))
    plt.bar(list28, company_names)
    st.title("Analysis")
    fig_plotly = go.Figure(data=[go.Bar(x=list28, y=company_names)])
    st.write("Here is the graphical view of space mission by companies-")
    st.plotly_chart(fig_plotly)

if user_menu=="Status of Mission":
    st.title("Status of Mission")
    MS = helper.MissionStatus(df)
    st.dataframe(MS)
    SM = MS.copy()
    fig = plt.figure(figsize=(10, 5))
    ax = sns.barplot(data=SM, x=SM['Status Mission'], y=SM.Frequency, errwidth=1, palette="Paired")
    for p in ax.patches:
        ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x() + 0.1, p.get_height() + 1))
    st.write("Frequencies of Mission Status")
    st.pyplot(fig)


    RS = helper.RocketStatus(df)
    Rocket_status = df["Status Rocket"].value_counts()
    palette_color = sns.color_palette('muted')
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(Rocket_status, labels=Rocket_status.index, colors=palette_color, autopct='%.0f%%')
    ax.set_title("Rocket Status")
    st.title("Status of Rocket")
    st.pyplot(fig)

if user_menu=="Rocket Analysis":
    st.title("Company spend money")
    df_ = preprocessing.RA(df)
    st.dataframe(helper.Money(df))
    st.write("Here are top 5 rocket companies-")
    helper.RocketMoney(df_)
