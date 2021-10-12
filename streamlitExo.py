###############
### Imports ###
###############

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

###############
### Options ###
###############

st.set_page_config(page_title="Entrainement sur Streamlit",
                   page_icon="🚗",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   )
############
### Data ###
############

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

################
### Slidebar ###
################
st.sidebar.title('Data Set Cars')

choix_slidebar = st.sidebar.radio("Menu", ("Présentation de l'exercice", 
                                           "Analyse de la distribution du Data Set", 
                                           "Analyse de la corrélation du Data Set"))

############
### Main ###
############

################################################################################################
### Page 1 ### Présentation de l'exercice
################################################################################################

if choix_slidebar == "Présentation de l'exercice":
    st.title('Corrélation et de Distribution du Data Set Cars')
    
    img = Image.open("pdv1.jpg")  
    st.image(img, width=620)
    st.subheader("Sujet:") 

    st.markdown("""Dans cet **exercice** nous verrons différentes applications de **Streamlit** et comment ajouter:
* des titres
* des Photos
* du texte
* des boutons interactifs
* des listes de sélections
* et enfins des graphiques""")

################################################################################################
### Page 2 ### Analyse de la distribution du Data Set
################################################################################################

if choix_slidebar == "Analyse de la distribution du Data Set":
    st.header("Distribution de 'cars'")
    col1, col2 = st.columns([1, 5]) 
    ########################################################
    ### GRAPH 1 ### histogramme répartition de "country" ###
    ########################################################
    with col1:
        st.markdown("""<br/><br/><br/><br/><br/>
        Ici nous pouvons observer le nombre total de **voitures** par **région** :red_car: """, unsafe_allow_html=True)

    with col2:    
        fig= px.histogram(df_cars, x='continent',
                        title="Répartition des voitures par Régions")
        fig.update_xaxes(title= 'Régions')
        fig.update_yaxes(title= 'Nombre de Voitures')
        st.plotly_chart(fig)


    ##########################################################
    ### GRAPH 2 ### histogramme répartition de "cylinders" ###
    ##########################################################
    with col1:
        st.markdown("""<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
        Là le nombre de **voiture** en fonction du nombre de **cylindres**:blue_car:""", unsafe_allow_html=True)

    with col2:
        fig1= px.histogram(df_cars, x='cylinders',
                        title="Répartition des voitures par cylindres")
        fig1.update_xaxes(title= 'Nombre de cylindres"')
        fig1.update_yaxes(title= 'Nombre de Voitures')
        st.plotly_chart(fig1)

    ###########################################################
    ### GRAPH 3 ### histogramme répartition de "time-to-60" ###
    ###########################################################
    with col1:
        st.markdown("""<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
        Et enfin le nombre de **voitures** en fonction de l'**accélération** (secondes pour atteindre 60 milles/h):police_car:""", unsafe_allow_html=True)
    with col2:
        fig2= px.histogram(df_cars, x='time-to-60',
                        title="Répartition des voitures par Accélération")
        fig2.update_xaxes(title= 'Temps pour atteindre 60 milles/h', autorange="reversed")
        fig2.update_yaxes(title= 'Nombre de Voitures')
        st.plotly_chart(fig2)

    ###########################
    ### GRAPH 4 ### boxplot ###
    ###########################
    
    st.markdown("""---""")

    st.markdown("""Pour ce graphique **boîte à moustache**, sélectionnons d'abord une **région** pour
     afficher ensuite la **répartition des voitures** en fonction de leur **consomation**, du **cm3**, des
      **chevaux** ou encore de leur **année**. """)

    continent = st.selectbox("Region: ", 
                     [' US.', ' Europe.', ' Japan.'])
    dfCont = df_cars.loc[df_cars['continent'] == continent]
    fig3 = make_subplots(4, 1)

    fig3.add_trace(go.Box(
        x=dfCont.mpg, 
        name='distance/galon'), 1, 1)

    fig3.add_trace(go.Box(
        x=dfCont.cubicinches, 
        name='cm3'), 2, 1)

    fig3.add_trace(go.Box(
        x=dfCont.hp, 
        name='Cheveaux'), 3, 1)

    fig3.add_trace(go.Box(
        x=dfCont.year, 
        name='Années'), 4, 1)

    fig3.update_layout(height=600, width=900, title_text=f"Répartitions en Boxplots pour la région {continent}",
                    legend=dict(orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="left"),
                    )
    st.plotly_chart(fig3)

################################################################################################
### Page 3 ### Analyse de la corrélation du Data Set
################################################################################################

if choix_slidebar == "Analyse de la corrélation du Data Set":
    st.header("Corrélations dans 'cars'")
    ###########################
    ### GRAPH 5 ### heatmap ###
    ###########################
    st.markdown("""Ce premier graphique dit **"Heatmap"** met en avant les corrélations entre les différents
     champs en affichant le pourcentage de corrélation et en colorant plus fortement lorsque celui ci est plus élevé.""")
    fig4, ax = plt.subplots(figsize= (15, 8))
    sns.heatmap(df_cars.corr(), cmap='coolwarm', center= 0.00, linewidths=0.5, linecolor= 'black', annot=True, fmt ='.0%', vmax=1, vmin= -1)
    plt.title('Heatmap des variables df_cars')
    st.pyplot(fig4)

    #######################################################
    ### GRAPH 6 ### 'Corrélation consomation/poids/cm3' ###
    #######################################################
    st.markdown("""<br/>""", unsafe_allow_html=True)
    st.markdown("""---""", unsafe_allow_html=True)
    st.markdown("""<br/>
        Les deux graphiques ci-dessous mettent en avant des corrélations via un nuage de point coloré par 'cm3' """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 5]) 
    with col1:
        st.markdown("""<br/><br/><br/><br/><br/><br/>
        Nous pouvons voir ici une corrélation négative, plus le poids de la voiture est important et moins la distance parcourue
        avec un galon d'essence est grande""", unsafe_allow_html=True)
    with col2:
        fig5= px.scatter(df_cars,
                        x= 'weightlbs',
                        y= 'mpg',
                        color= 'cubicinches',
                        title= 'Corrélation consomation/poids/cm3',
                        trendline= 'ols',
                        labels={
                            "weightlbs": "Poids en Livre",
                            "mpg": "distance en miles avec un galon d'essence",
                            "cubicinches": "cm3"
                        })
        fig5.update_layout(height=600, width=900)

        st.plotly_chart(fig5)

    ##########################################################################
    ### GRAPH 7 ### 'Corrélation Chevaux/temps pour atteindre 60mPerH/cm3' ###
    ##########################################################################
    with col1:
        st.markdown("""<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
        Une nouvelle fois, nous observons une corrélation négative,
         plus la voiture possèdes de chevaux et moins il faut de secondes pour atteindre 60 miles par heure""", unsafe_allow_html=True)

    with col2:
        fig6= px.scatter(df_cars,
                        x= 'hp',
                        y= 'time-to-60',
                        color= 'cubicinches',
                        title= 'Corrélation Chevaux/temps pour atteindre 60mPerH/cm3',
                        trendline= 'ols',
                        labels={
                            "hp": "Chevaux",
                            "time-to-60": "Secondes pour atteindre 60miles/heure",
                            "cubicinches": "cm3"
                        })
        fig6.update_layout(height=600, width=900)

        st.plotly_chart(fig6)