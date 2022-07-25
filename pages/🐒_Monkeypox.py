import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date
today = date.today()
st.header("Monkeypox Cases for " + today.strftime("%B %d, %Y"))
df = pd.read_csv("https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv", low_memory=False)
data_df1 = df[['Date_confirmation','ID']].groupby('Date_confirmation').agg('count').reset_index()
data_df1['Accumulated Cases'] = data_df1['ID'].cumsum()
data_df1.rename({'ID':'Count'}, axis = 1, inplace = True)
fig = px.line(data_df1,x='Date_confirmation',y='Accumulated Cases',markers=True,title='Daily Cases for Monkeypox')

fig
fig = px.pie(df, values=df['Symptoms'].value_counts().nlargest(10), names=df['Symptoms'].value_counts().nlargest(10).index
             , title='Common Symptoms for Monkeypox',hole = .5)
fig
df2 = df[['Country_ISO3','ID']].groupby('Country_ISO3').agg('count').reset_index()
df2.rename({'ID':'Total'}, axis = 1, inplace = True)
fig = px.scatter_geo(df2, locations="Country_ISO3",
                     color="Total",
                     hover_name="Country_ISO3",
                     size="Total",
                     title = 'Distribution of Confirmed Cases',
                     projection="natural earth",
                     color_continuous_scale =px.colors.sequential.Rainbow
                    )
fig
fig.update_geos(lataxis_showgrid = True,
                lonaxis_showgrid = True,
                showcountries = True,
               )
fig = px.choropleth(df2,
                    locations = "Country_ISO3",
                    color = "Total",
                    hover_name = "Country_ISO3",
                    color_continuous_scale =px.colors.sequential.Rainbow,
                    projection = 'orthographic',
                    title = 'Distribution of Confirmed Cases in World Map',
                    height = 600,
                    width = 1000,
                   )


fig.update_geos(lataxis = {'gridcolor':'#333333'},
                lonaxis = {'gridcolor':'#333333'},
               )
fig