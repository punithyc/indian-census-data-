import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df=pd.read_csv('india.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')


st.sidebar.title('india data')


selected_state=st.sidebar.selectbox('select a state',list_of_states)
primary=st.sidebar.selectbox('select primary parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('select parameter parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represent secondary parameter')
    if selected_state=='Overall India':
        # plot for india
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=3,mapbox_style='carto-positron',size_max=35,width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot for state
        state_df=df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=3,
                                mapbox_style='carto-positron', size_max=35, width=1200, height=700)
        st.plotly_chart(fig, use_container_width=True)
