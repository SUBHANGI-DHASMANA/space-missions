import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import streamlit as st


def Countries_mission(df):
    df['Country'] = df['Location'].str.split(',').str[-1].str.strip()

    counts = df['Country'].value_counts()
    countries = counts.index.tolist()

    plt.figure(figsize=(8, 8))
    ax = sns.barplot(x=counts, y=countries, palette="viridis")
    ax.set_title("Space Missions of Each Country")
    ax.set_xlabel("Count")
    ax.set_ylabel("Country")

    st.pyplot(fig=plt.gcf())

def Company_names(df):
    company_list = df['Company Name'].unique().tolist()
    company_list.remove("Arm??e de l'Air")
    return company_list

def Countries_names(df):
    df['Country'] = df['Location'].str.split(',').str[-1].str.strip()
    country_list = df['Country'].unique().tolist()
    return country_list

def companyCountries(df, country):
    country_df = df[df['Country'] == country]
    country_companies = country_df['Company Name'].unique()
    country_counts = country_df['Company Name'].value_counts()
    
    plt.figure(figsize=(8, 8))
    ax = sns.barplot(x=country_counts, y=country_companies, palette="viridis")
    ax.set_title(f"Space Missions by Companies in the {country}")
    ax.set_xlabel("Count")
    ax.set_ylabel("Company Name")
    st.pyplot(fig=plt.gcf())

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
    df[' Rocket'] = df[' Rocket'].str.replace(',', '', regex=True)
    df[' Rocket'] = pd.to_numeric(df[' Rocket'], errors='coerce')

    df_money = df.groupby("Company Name")[" Rocket"].sum().reset_index()
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