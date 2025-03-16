# pylint: disable=missing-module-docstring
import logging
import os
from datetime import date, timedelta
import duckdb
import streamlit as st


#################
# Functions part
#################
def check_answer(text_to_check: str):
    """
    Checks the answer filled by the user
    In
        text_to_check
            str
            text filled by the user that will be checked
    Out
     -
    """
    processed_dataframe = con.execute(text_to_check).df()
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


#################

if "data" not in os.listdir():
    logging.error(os.listdir)
    logging.error("creating folder data")
    os.mkdir("data")
if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

st.title("SQL SRS")

all_data = con.execute("SELECT * FROM memory_state").df()
with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        all_data["theme"].unique(),
        placeholder="select a value ...",
        index=None,
    )
    if theme:
        st.write("You selected ", theme)
        exercise = con.execute(f"SELECT * FROM memory_state WHERE theme='{theme}'").df()
        st.write(exercise)
        exercise_to_practice = st.selectbox(
            "Which exercise do you want to practice ?",
            exercise["exercise_name"].values,
            placeholder="select a value ...",
            index=None,
        )
        if exercise_to_practice:
            st.write("You selected ", exercise_to_practice)
        else:
            st.warning("Please choose an exercise to practice.")
            st.stop()
    else:
        st.warning("Please choose a theme to study.")
        st.stop()

with open(f"answers/{exercise_to_practice}.sql") as f:
    answer = f.read()
solution = con.execute(answer).df()
input_text = st.text_area("Entrez votre input")
col1, col2 = st.columns(2)

if input_text:
    check_answer(input_text)

for n_days in [2, 7, 21]:
    if st.button(f"Revoir dans {n_days} jours"):
        next_review=date.today() + timedelta(days=n_days)
        con.execute(f"UPDATE memory_state SET last_reviewed = '{next_review}' WHERE exercise_name='{exercise_to_practice}'")
        st.rerun()
if st.button('Reset'):
    con.execute(f"UPDATE memory_state SET last_reviewed='1970-01-01'")
    st.rerun()
tab1, tab2 = st.tabs(["Tables", "Solution"])
with tab1:
    for table in exercise.loc[
        exercise.exercise_name.eq(exercise_to_practice), "tables"
    ].values[0]:
        st.write(f"table: {table}")
        st.dataframe(con.execute(f"SELECT * FROM {table}").df())

with tab2:
    st.write(answer)
