# pylint: disable=missing-module-docstring
import io
import streamlit as st
import pandas as pd
import duckdb

st.title("SQL SRS")
# Création du DataFrame
CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))
CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))
ANSWER = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution = duckdb.sql(ANSWER).df()
with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ["Joins", "Group By", "Windows Functions"],
        placeholder="select a value ...",
        index=None,
    )
    if option:
        st.write("You selected ", option)
input_text = st.text_area("Entrez votre input")
col1, col2 = st.columns(2)
if input_text:
    processed_dataframe = duckdb.sql(input_text).df()
    if processed_dataframe.equals(solution):
        st.success("Correct !")
        st.dataframe(processed_dataframe)
    else:
        with col1:
            st.error("Incorrect ! Expected :")
            st.dataframe(solution)
        with col2:
            st.error("But your output is :")
            st.dataframe(processed_dataframe)

tab1, tab2 = st.tabs(["Tables", "Solution"])
with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)
with tab2:
    st.write(ANSWER)
