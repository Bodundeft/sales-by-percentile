import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np

 

st.set_page_config(page_title="Dashboard ", page_icon="📈", layout="wide")  
st.header("Percentile -- Categorical Data Overview")
st.markdown("##")

theme_plotly = None # None or streamlit
     
df=pd.read_excel('data.xlsx', sheet_name='Sheet1')

tab1, tab2 = st.tabs(["My Excel Database","Sales By percentiles"])

with tab1:
 with st.expander("Show Workbook"):
  shwdata = st.multiselect('Filter :', df.columns, default=["SALES","ORDERDATE","STATUS","YEAR_ID","PRODUCTLINE","CUSTOMERNAME","CITY","COUNTRY"])
  st.dataframe(df[shwdata],use_container_width=True
  )
  
with tab2.caption("Sales By percentiles"):
   c1,c2,c3,c4,c5=st.columns(5)
with c1:
   st.info('Percentile 25 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 25):,.2f}")
with c2:
   st.info('Percentile 50 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 50):,.2f}")
with c3:
   st.info('Percentile 75 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 75):,.2f}")
with c4:
   st.info('Percentile 100 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 100):,.2f}")
with c5:
   st.info('Percentile 0 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 0):,.2f}")
   
   def filterData():
    column = st.sidebar.selectbox('Select a column', df.columns)
    type_of_column = st.sidebar.radio("What kind of analysis", ['Categorical', 'Numerical'])

    if type_of_column == 'Categorical':
        dist = pd.DataFrame(df[column].value_counts())
        fig = px.bar(dist, title='Category by count', orientation="v")
        fig.update_layout(legend_title=None, xaxis_title="Observation", yaxis_title='Count')
        st.write(fig, theme=theme_plotly)
    else:
        st.subheader("Numerical Summary")
        st.write(df[column].describe())  # Display descriptive statistics

filterData()
