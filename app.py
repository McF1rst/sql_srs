# pylint: disable=missing-module-docstring
import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

st.title("SQL SRS")



with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ["cross_joins", "Group By", "Windows Functions"],
        placeholder="select a value ...",
        index=None,
    )
    if theme:
        st.write("You selected ", theme)
        exercise=con.execute(f"SELECT * FROM memory_state WHERE theme='{theme}'")
        st.write(exercise)
        st.write(con.execute("SELECT * FROM memory_state"))
input_text = st.text_area("Entrez votre input")
col1, col2 = st.columns(2)
"""
ANSWER = """
#SELECT * FROM beverages
#CROSS JOIN food_items
"""
solution = duckdb.sql(ANSWER).df()
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
"""
