# pylint: disable=missing-module-docstring
import ast

import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

st.title("SQL SRS")


with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ["cross_join", "Group By", "Windows Functions"],
        placeholder="select a value ...",
        index=None,
    )
    if theme:
        st.write("You selected ", theme)
        exercise = con.execute(f"SELECT * FROM memory_state WHERE theme='{theme}'").df()
    else:
        st.warning("Please choose a theme to study.")
        st.stop()
input_text = st.text_area("Entrez votre input")
col1, col2 = st.columns(2)
with open(f"answers/{exercise.loc[0, 'exercise_name']}.sql") as f:
    answer = f.read()
solution = con.execute(answer).df()
if input_text:
    processed_dataframe = con.execute(input_text).df()
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
    for table in ast.literal_eval(exercise.loc[0, "tables"]):
        st.write(f"table: {table}")
        st.dataframe(con.execute(f"SELECT * FROM {table}").df())

with tab2:
    st.write(answer)
