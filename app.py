import streamlit as st
import pandas as pd
import duckdb

st.title("SQL SRS")
# Création du DataFrame
data = {
    "Colonne_A": [1, 2, 3, 4, 5],
    "Colonne_B": ["A", "B", "C", "D", "E"],
    "Colonne_C": [10.5, 20.3, 30.1, 40.8, 50.2]
}

df = pd.DataFrame(data)
with st.sidebar:
    option = st.selectbox("What would you like to review ?", ['Joins', 'Group By', 'Windows Functions'],
                          placeholder="select a value ...", index=None)
    if option:
        st.write('You selected ', option)
tab1, tab2 = st.tabs(['SQL', 'Other'])
with tab1:
    input_text = st.text_area('Entrez votre input')
    processed_dataframe = duckdb.sql(input_text)
    if input_text:
        st.dataframe(processed_dataframe)