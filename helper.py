import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
def Company_mission(df):
    temp = df["Company Name"].value_counts().reset_index()[:28]
    return temp
def MissionStatus(df):
    temp = df["Status Mission"].value_counts().reset_index()
    temp.columns = ["Status Mission", "Frequency"]
    return temp

def MSChart(temp, df):
    fig = px.pie(temp, values="Status Mission", names="index", title="Mission Status")
    fig.show()

def RocketStatus(df):
    Rocket_status = df["Status Rocket"].value_counts()
    return Rocket_status

def Money(df):
    df_money = df.groupby(["Company Name"])[" Rocket"].sum().reset_index()
    return df_money
def RocketMoney(df):
    df_money = df.groupby(["Company Name"])[" Rocket"].sum().reset_index()
    df_money_TOP5 = df_money.sort_values(by=[" Rocket"], ascending=False).reset_index()[:5]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df_money_TOP5, x=df_money_TOP5['Company Name'], y=df_money_TOP5[" Rocket"], errwidth=1, palette="coolwarm")
    ax.set_title("Top 5 Rocket Companies")
    ax.set_ylim(0, 15000)
    plt.xticks(rotation=90)
    st.pyplot(fig)