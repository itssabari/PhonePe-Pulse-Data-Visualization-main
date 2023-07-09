import time
import pandas as pd
import os
import json
import psycopg2
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_player import st_player
from streamlit_pandas_profiling import st_profile_report
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space
import io


#conn = psycopg2.connect(host="localhost", user="postgres", password="vengatesh", port=5432, database="PhonePe")
#cur = conn.cursor()

Agg_trans_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Agg_trans.csv')
Agg_user_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Agg_user.csv')
Map_trans_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Map_trans.csv')
Map_user_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Map_user.csv')
Top_trans_dist_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Top_trans_dist.csv')
Top_trans_pin_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Top_trans_pin.csv')
Top_user_dist_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Top_user_dist.csv')
Top_user_pin_df = pd.read_csv(r'C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Misci\Top_user_pin.csv')



if 'options' not in st.session_state:
    st.session_state['options'] = {
        'Aggregate Transaction': 'Agg_trans_df',
        'Aggregate User': 'Agg_user_df',
        'Map Transaction': 'Map_trans_df',
        'Map User': 'Map_user_df',
        'Top Transaction Districtwise': 'Top_trans_dist_df',
        'Top Transaction Pincodewise': 'Top_trans_pin_df',
        'Top User Districtwise': 'Top_user_dist_df',
        'Top User Pincodewise': 'Top_user_pin_df'
    }

df_names = [
            var_name for var_name in globals() 
            if isinstance(globals()[var_name], pd.core.frame.DataFrame) and var_name.endswith('_df')
            ]

if 'df_list' not in st.session_state:
    st.session_state['df_list'] = []
    
    for var_name in df_names:
        st.session_state[var_name] = globals()[var_name]
        st.session_state['df_list'].append(var_name)


def year_to_str(df):
    df['Year'] = df["Year"].astype(str)

for df_name in st.session_state['df_list']:
    df = globals()[df_name]
    year_to_str(df)
    globals()[df_name] = df

st.set_page_config(page_title = 'PhonePe Data Visualization', layout = 'wide',
                    page_icon = "💱")

reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0rem;}
        div.Sidebar   {padding-top:0rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

hide_st_style ="""
        <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """      
st.markdown(hide_st_style,unsafe_allow_html=True)

with st.sidebar:
    st_lottie("https://assets4.lottiefiles.com/packages/lf20_bevt4rfh.json") 
    

with st.sidebar:
    opt = option_menu(
        menu_title="Menu",
        options=["Home","About", "Transaction","Users","Insights"],
        icons=["bank","book-half","currency-exchange","people", "map"],
        menu_icon="menu-up",
        default_index=0)
    
if opt == "Home":
    st.image("phead.png")
    st.markdown("#### Welcome to the **:blue[PhonePe Pulse]** Data Visualization! ")
    st.write("PhonePe was founded in December 2015 and has emerged as India’s largest payments app, enabling digital inclusion for consumers and merchants alike. With 46+ crore (460+ Million) registered users, one in four Indians are now on PhonePe. The company has also successfully digitized 3.5+ crore (35+ Million) offline merchants spread across Tier 2,3,4 and beyond, covering 99% pin codes in the country. PhonePe is also the leader in Bharat Bill Pay System (BBPS), processing over 45% of the transactions on the BBPS platform. PhonePe forayed into financial services in 2017, providing users with safe and convenient investing options on its platform. Since then, the company has introduced several Mutual Funds and Insurance products that offer every Indian an equal opportunity to unlock the flow of money and access to services. PhonePe has been recognized as the Most Trusted Brand for Digital Payments as per the Brand Trust Report for two consecutive years (2022 & 2023) by Trust Research Advisory (TRA).")
    add_vertical_space(2)
    
    st_player(url = "https://youtu.be/c_1H6vivsiA", height = 480)
    
    col1, col2, col3 = st.columns(3)
    
    total_reg_users = Top_user_dist_df['Registered_users'].sum()
    col1.metric(
            label = 'Total Registered Users',
            value = '{:.2f} Cr'.format(total_reg_users/100000000),
            delta = 'Forward Trend',
            delta_color="off"
            )
    total_app_opens = Map_user_df['App_opens'].sum()
    col2.metric(
            label = 'Total App Opens', value = '{:.2f} Cr'.format(total_app_opens/100000000),
            delta = 'Forward Trend',
            delta_color="off"
            )

    col3.metric(label = 'Total Transaction Count', value = '2000 Cr +', delta = 'Forward Trend',delta_color="off")

    style_metric_cards(background_color='200329') 
    
     
    st.image('phgif.gif', use_column_width = 100)

    

elif opt == "About":
            st.header("📒Problem Statement")
            st.write("The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.")
            st.caption("The solution must include the following steps:")
            st.write("1. Extract data from the Phonepe pulse Github repository through scripting and clone it.")
            st.write("2. Transform the data into a suitable format and perform any necessary cleaning and pre-processing steps.")
            st.write("3. Insert the transformed data into a MySQL database for efficient storage and retrieval.")
            st.write("4. Create a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually appealing manner.")
            st.write("5. Fetch the data from the MySQL database to display in the dashboard and Provide at least 10 different dropdown options for users to select different facts and figures to display on the dashboard.")
            
            st.write('Tools and Libraries Used👨🏻‍💻 :blue[Python, PostgreSQL,Plotly & Streamlit]')
            
elif opt == "Transaction":
    st.subheader(':blue[Transaction amount breakdown]') 
    Agg_trans = trans_df = trans_df_2 = st.session_state["Agg_trans_df"]
    Map_df = st.session_state["Map_trans_df"]

    states = Agg_trans["State"].unique()
    years = Agg_trans["Year"].unique()
    quarters = Agg_trans["Quarter"].unique()

    if 'states' not in st.session_state:
        st.session_state["states"] = states
        if 'years' not in st.session_state:
         st.session_state["years"] = years
    if 'quarters' not in st.session_state:
         st.session_state["quarters"] = quarters

    col1, col2, col3 = st.columns([5, 3, 1])

    state1 = col1.selectbox("State", states, key='state1')
    year1 = col2.selectbox("Year", years, key='year1')
    quarter_options = ["All"] + list(map(str, quarters))
    quarter1 = col3.selectbox("Quarter", quarter_options, key='quarter1')

    trans_df = trans_df[(trans_df["State"] == state1) & (trans_df["Year"] == year1)]

    if quarter1 != 'All':
     trans_df = trans_df[(trans_df["Quarter"] == int(quarter1))]

    trans_df = trans_df.sort_values("Transaction_amount", ascending=False).reset_index(drop = True)

    suffix1 = " quarters" if quarter1 == 'All' else "st" if quarter1 == '1' else "nd" if quarter1 == '2' else "rd" if quarter1 == '3' else "th"

    title1 = f"Transaction details of {state1} for {quarter1.lower()}{suffix1} {'' if quarter1 == 'All' else 'quarter'} of {year1}"

    fig1 = px.bar(
             trans_df, x="Transaction_type", y="Transaction_amount", 
             color="Transaction_type", 
             color_discrete_sequence=px.colors.qualitative.Plotly,
             title=title1,
             labels=dict(Transaction_amount='Transaction Amount', Transaction_type='Transaction Type'),
             hover_data={'Quarter': True}
             )

    fig1.update_layout(
                   showlegend=False, 
                   title={
                       'x': 0.5,
                       'xanchor': 'center',
                       'y': 0.9,
                       'yanchor': 'top'
                       },
                   width = 900, height = 500
                   )

    fig1.update_traces(marker = dict(line = dict(width = 1, color = 'DarkSlateGrey')))

    st.plotly_chart(fig1)

    expander1 = st.expander(label = 'Detailed view')
    expander1.write(trans_df.loc[:, ['Quarter', 'Transaction_type', 'Transaction_amount']].reset_index(drop=True))


    st.subheader(':blue[Transaction Hotspots - Districts]')


    year_col, quarter_col, buff = st.columns([1,1,4])

    year2 = year_col.selectbox("Year", years, key = 'year2')
    quarter2 = quarter_col.selectbox("Quarter", quarter_options, key = 'quarter2')

    map_df = Map_df[Map_df["Year"] == year2]

    if quarter2 != 'All':
        map_df = map_df[(map_df["Quarter"] == int(quarter2))]

    suffix2 = " quarters" if quarter2 == 'All' else "st" if quarter2 == '1' else "nd" if quarter2 == '2' else "rd" if quarter2 == '3' else "th"

    title2 = f"Transaction hotspots for {quarter2.lower()}{suffix2} {'' if quarter2 == 'All' else 'quarter'} of {year2}"


    fig2 = px.scatter_mapbox(map_df, lat = "Latitude", lon = "Longitude",
                        size = "Transaction_amount", hover_name = "District",
                        hover_data = {"Transaction_count": True, "Transaction_amount": True, 'Quarter': True},
                        title = title2,
                        color_discrete_sequence= px.colors.sequential.Plotly3
                        )

    fig2.update_layout(mapbox_style = 'carto-positron',
                   mapbox_zoom = 3.45, mapbox_center = {"lat": 20.93684, "lon": 78.96288},
                   geo=dict(scope = 'asia', projection_type = 'equirectangular'), 
                   title={
                          'x': 0.5,
                          'xanchor': 'center',
                          'y': 0.04,
                          'yanchor': 'bottom',
                          'font': dict(color='black')
                         },
                   margin={"r":0,"t":0,"l":0,"b":0}, width = 900, height = 500
                  )

    st.plotly_chart(fig2)

    expander2 = st.expander(label = 'Detailed view')
    expander2.write(map_df.loc[:, ['State', 'District', 'Quarter', 'Transaction_amount']].reset_index(drop=True))


    st.subheader(":blue[Breakdown by transaction count proportion]")


    state_pie, year_pie, quarter_pie = st.columns([5, 3, 1])

    state3 = state_pie.selectbox('State', options = states, key = 'state3')
    year3 = year_pie.selectbox('Year', options = years, key = 'year3')
    quarter3 = quarter_pie.selectbox('Quarter', options = quarter_options, key = 'quarter3')

    filtered_trans = trans_df_2[(trans_df_2.State == state3) & (trans_df_2.Year == year3)]

    if quarter3 != 'All':
        filtered_trans = filtered_trans[filtered_trans.Quarter == int(quarter3)]

    fig3 = px.pie(
              filtered_trans, names = 'Transaction_type',
              values = 'Transaction_count', hole = .65
              )

    fig3.update_layout(width = 900, height = 500)

    st.plotly_chart(fig3)

    expander3 = st.expander(label = 'Detailed view')
    expander3.write(filtered_trans.loc[:, ['Quarter', 'Transaction_type', 'Transaction_count']].reset_index(drop = True))




elif opt == "Users":
    st.subheader(':blue[Transaction Count and Percentage by Brand]')
    

    Agg_user_df1 = st.session_state["Agg_user_df"]
    Map_user_df1 = st.session_state["Map_user_df"]
    Top_user_dist_df1 = st.session_state["Top_user_dist_df"]

    col1, col2, col3 = st.columns([5, 3, 1])

    state_options = ['All'] + [state for state in st.session_state['states']]
    quarter_options = ["All"] + list(map(str, st.session_state['quarters']))

    state1 = col1.selectbox('State', options=state_options, key='state1')
    year1 = col2.selectbox('Year', options=st.session_state['years'], key='year1')
    quarter1 = col3.selectbox("Quarter", options=quarter_options, key='quarter1')

    if state1 == "All":
    
       Agg_user_df_filtered = Agg_user_df1[(Agg_user_df1['Year'] == year1)]
    
       if quarter1 != 'All':
          Agg_user_df_filtered = Agg_user_df_filtered[Agg_user_df_filtered['Quarter'] == int(quarter1)]
    
       suffix1 = " quarters" if quarter1 == 'All' else "st" if quarter1 == '1' else "nd" if quarter1 == '2' else "rd" if quarter1 == '3' else "th"
    
       title1=f"Transaction Count and Percentage across all states for {quarter1.lower()}{suffix1} {'' if quarter1 == 'All' else 'quarter'} of {year1}"

    else:
    
       Agg_user_df_filtered = Agg_user_df1[(Agg_user_df1['State'] == state1) & (Agg_user_df1['Year'] == year1)]
    
       if quarter1 != 'All':
        agg_user_df_filtered = Agg_user_df_filtered[Agg_user_df_filtered['Quarter'] == int(quarter1)]
    
       suffix1 = " quarters" if quarter1 == 'All' else "st" if quarter1 == '1' else "nd" if quarter1 == '2' else "rd" if quarter1 == '3' else "th"
    
       title1=f"Transaction Count and Percentage in {state1} for {quarter1.lower()}{suffix1} {'' if quarter1 == 'All' else 'quarter'} of {year1}"


    fig1 = px.treemap(
                  Agg_user_df_filtered,
                  path=['Brand'],
                  values='Transaction_count',
                  color='Percentage',
                  color_continuous_scale='ylorbr',
                  hover_data={'Percentage': ':.2%'},
                  hover_name='Brand'
                  )

    fig1.update_layout(
                   width=975, height=600,
                   coloraxis_colorbar=dict(tickformat='.1%', len = 0.85),
                   margin=dict(l=20, r=20, t=0, b=20),
                   title = {
                            "text": title1 ,
                             'x': 0.45,
                             'xanchor': 'center',
                             'y': 0.007,
                             'yanchor': 'bottom'
                             }
                   )

    fig1.update_traces(
                    hovertemplate = 
                    '<b>%{label}</b><br>Transaction Count: %{value}<br>Percentage: %{color:.2%}<extra></extra>'
                    )

    st.plotly_chart(fig1)

    expander1 = st.expander(label = 'Detailed view')
    expander1.write(Agg_user_df_filtered.loc[:, ['State', 'Quarter', 'Brand', 'Percentage']])

    add_vertical_space(2)


#2


    st.subheader(':blue[Registered Users Hotspots - Disrict]')

    col4, col5, col6 = st.columns([5, 3, 1])

    state2 = col4.selectbox('State', options=state_options, key='state2')
    year2 = col5.selectbox('Year', options=st.session_state['years'], key='year2')
    quarter2 = col6.selectbox("Quarter", options=quarter_options, key='quarter2')

    if state2 == 'All':
      map_user_df_filtered = Map_user_df1[(Map_user_df1["Year"] == year2)]
    
      if quarter2 != 'All':
        map_user_df_filtered = map_user_df_filtered[map_user_df_filtered['Quarter'] == int(quarter2)]    
    else:
      map_user_df_filtered = Map_user_df1[(Map_user_df1["State"] == state2) & (Map_user_df1["Year"] == year2)]
    
      if quarter2 != 'All':
        map_user_df_filtered = map_user_df_filtered[map_user_df_filtered['Quarter'] == int(quarter2)]

    fig2 = px.scatter_mapbox(
                         map_user_df_filtered, 
                         lat="Latitude", 
                         lon="Longitude", 
                         size="Registered_users", 
                         hover_name="District",
                         hover_data={'State': True, 'Quarter': True},
                         title=f"Registered Users by District",
                         color_discrete_sequence= px.colors.sequential.Plotly3
                     )

    fig2.update_layout(
                   mapbox_style = 'carto-positron',
                   mapbox_zoom = 3.5, mapbox_center = {"lat": 20.93684, "lon": 78.96288},
                   geo=dict(scope = 'asia', projection_type = 'equirectangular'),
                   title={
                          'x': 0.5,
                          'xanchor': 'center',
                          'y': 0.05,
                          'yanchor': 'bottom',
                          'font': dict(color='black')
                          },
                   height=600, width=900,
                   margin={"r":0,"t":0,"l":0,"b":0}
                  )

    st.plotly_chart(fig2)

    expander2 = st.expander(label = 'Detailed view')
    expander2.write(map_user_df_filtered.loc[:, ['District', 'Quarter', 'Registered_users']].reset_index(drop=True))

    add_vertical_space(2)


#3


    st.subheader(':blue[Top Districts by Registered Users]')

    col7, col8, buff1 = st.columns([5, 2, 5])

    state3 = col7.selectbox('State', options = state_options, key='state3')
    year3 = col8.selectbox('Year', options = st.session_state['years'], key='year3')

    if state3 == "All":
    
      top_user_dist_df_filtered = Top_user_dist_df1[
                                                  Top_user_dist_df1['Year']==year3
                                                  ].groupby('District').sum().reset_index()
    
      top_user_dist_df_filtered = top_user_dist_df_filtered.sort_values(
                                                                      by = 'Registered_users',
                                                                      ascending = False
                                                                      ).head(10)
    
      title3 = f'Top 10 districts across all states by registered users in {year3}'

    else:
    
      top_user_dist_df_filtered = Top_user_dist_df1[
                                                   (Top_user_dist_df1['State']==state3)
                                                                 & 
                                                  (Top_user_dist_df1['Year']==year3)
                                                   ].groupby('District').sum().reset_index()
    
      top_user_dist_df_filtered = top_user_dist_df_filtered.sort_values(
                                                                      by = 'Registered_users',
                                                                      ascending = False
                                                                      ).head(10)
    
      title3 = f'Top districts in {state3} by registered users in {year3}'

    fig3 = px.bar(
              top_user_dist_df_filtered, 
              x='Registered_users', 
              y='District', 
              color='Registered_users', 
              color_continuous_scale='Greens', 
              orientation='h', labels={'Registered_users': 'Registered Users'},
              hover_name='District', 
              hover_data=['Registered_users']
              )

    fig3.update_traces(hovertemplate='<b>%{hovertext}</b><br>Registered users: %{x:,}<br>')

    fig3.update_layout(
                   height=500, width=950,
                   yaxis=dict(autorange="reversed"),
                   title={
                          'text': title3,
                          'x': 0.5,
                          'xanchor': 'center',
                          'y': 0.007,
                          'yanchor': 'bottom'
                          }
                   )

    st.plotly_chart(fig3)

    expander3 = st.expander(label = 'Detailed view')
    expander3.write(top_user_dist_df_filtered.loc[:, ['District', 'Registered_users']].reset_index(drop=True))

    add_vertical_space(2)


#4


    st.subheader(':blue[Number of app opens by District]')

    col9, col10, buff2 = st.columns([2, 2, 7])

    year_options = [year for year in st.session_state['years'] if year != '2018']

    year4 = col9.selectbox('Year', options=year_options, key='year4')

    if year4 == '2019':
      quarter_options.remove('1')
    
      quarter4 = col10.selectbox("Quarter", options=quarter_options, key='quarter4')

      map_user_df_filtered = Map_user_df1[(Map_user_df1["Year"]==year4)]

    if quarter4 != 'All':
      map_user_df_filtered = map_user_df_filtered[map_user_df_filtered['Quarter']==int(quarter4)]

    map_user_df_filtered = map_user_df_filtered[map_user_df_filtered["App_opens"] != 0]


    fig4 = px.density_mapbox(
                         map_user_df_filtered,
                         lat='Latitude', lon='Longitude',
                         z='App_opens', radius=20,
                         center=dict(lat=20.5937,lon=78.9629),
                         zoom=3, hover_name='District',
                         mapbox_style="stamen-watercolor",
                         opacity=0.8, labels={'App_opens': 'App Opens'},
                         hover_data={
                                     'Latitude': False,
                                     'Longitude': False,
                                     'State': True
                                     },
                        color_continuous_scale = 'Blues'
                        )

    fig4.update_layout(
                   margin=dict(l=20, r=20, t=60, b=20),
                   mapbox=dict(layers=[
                                       dict(
                                            sourcetype='geojson',
                                            source=st.session_state['geojson'],
                                            type='line',
                                            color='white',
                                            opacity=0.8,
                                            )
                                        ]
                               ),
                   width=925, height=600,
                   coloraxis_colorbar=dict(len=0.9),
                   title={
                          'text': 'App Opens Density Map',
                          'x': 0.43,
                          'xanchor': 'center',
                          'y': 0.09,
                          'yanchor': 'bottom',
                          'font': dict(color='black')
                          }
                   )

    st.plotly_chart(fig4)

    expander4 = st.expander(label = 'Detailed view')
    expander4.write(map_user_df_filtered.loc[:, ['District', 'Quarter', 'App_opens']].reset_index(drop=True))




elif opt == "Insights":
  
      st.title(':blue[Overview]')
        
      Agg_trans = st.session_state["Agg_trans_df"]
      Map_trans = st.session_state["Map_trans_df"]
      Map_user = st.session_state["Map_user_df"]
    
      st.subheader(":blue[Transaction Breakdown by Type]")
      trans_type_count = Agg_trans.groupby('Transaction_type')['Transaction_count'].sum()

      total_trans_count = Agg_trans['Transaction_count'].sum()

      trans_type_perc = round(trans_type_count / total_trans_count * 100, 2).reset_index()

      trans_type_fig = px.pie(
                        trans_type_perc, names='Transaction_type',
                        values='Transaction_count', hole=.65,
                        hover_data={'Transaction_count': False}
                        )

      trans_type_fig.update_layout(width = 900, height = 500)


#2

      st.subheader(":blue[Transaction Count by State]")

      trans_state = Agg_trans.groupby('State')['Transaction_count'].sum().reset_index()
      trans_state_sorted = trans_state.sort_values(by='Transaction_count', ascending=False).head(15)
 
      trans_state_fig = px.bar(
                          trans_state_sorted, x='Transaction_count',
                         y='State', orientation='h',
                         text='Transaction_count', text_auto='.2s',
                         labels = {'Transaction_count': "Transaction Count"}
                         )

      trans_state_fig.update_layout(
                                yaxis=dict(autorange="reversed"),
                                width = 900, height = 500
                                )


#3

      st.subheader(":blue[Transaction Count by District]")


      trans_district = Map_trans.groupby(['State', 'District'])[['Transaction_count']].sum().reset_index()
 
      trans_district_sorted = trans_district.sort_values(by='Transaction_count', ascending=False).head(15)

      trans_district_fig = px.bar(
                            trans_district_sorted, x='Transaction_count',
                            y='District', orientation='h',
                            text='Transaction_count', text_auto='.2s',
                            labels = {'Transaction_count': "Transaction Count"},
                            hover_name='State',
                            hover_data={'State': False, 'District': True}
                            )

      trans_district_fig.update_layout(
                                 yaxis = dict(autorange="reversed"),
                                 width = 900, height = 500
                                 )


#4

      st.subheader(':blue[Registered User Count by State]')

      user_state = Map_user.groupby('State')['Registered_users'].sum().reset_index()
 
      with open(r"C:\Users\VENKA\Desktop\Data Science\Python Anaconda\Project\india_states.json") as f:
        geojson = json.load(f)

      if 'geojson' not in st.session_state:
       st.session_state["geojson"] = geojson

      user_state_fig = px.choropleth(
                                user_state, geojson = geojson,
                                locations = 'State',
                                featureidkey = 'properties.ST_NM',
                                color='Registered_users', projection = 'orthographic',
                                labels = {'Registered_users': "Registered Users"},
                                color_continuous_scale = 'reds'
                                )
    
      user_state_fig.update_geos(fitbounds='locations', visible=False)
      user_state_fig.update_layout(height=600, width=900)
    
      st.plotly_chart(user_state_fig, use_container_width = True)