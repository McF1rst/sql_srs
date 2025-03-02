import streamlit as st
import pandas as pd
import duckdb

# Création du DataFrame
data = {
    "Colonne_A": [1, 2, 3, 4, 5],
    "Colonne_B": ["A", "B", "C", "D", "E"],
    "Colonne_C": [10.5, 20.3, 30.1, 40.8, 50.2]
}

df = pd.DataFrame(data)
tab1, tab2 = st.tabs(['SQL', 'Other'])
with tab1:
    input_text = st.text_area('Entrez votre input')
    processed_dataframe = duckdb.sql(input_text)
    if input_text:
        st.dataframe(processed_dataframe)