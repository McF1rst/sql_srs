import io

import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
# --------------------------------------------------
# EXERCISES LIST
# --------------------------------------------------
data = {
    "theme": ["cross_join", "window_functions"],
    "exercise_name": ["beverages_and_food", "simple_window"],
    "tables": [["beverages", "food_items"], "simple_window"],
    "last_reviewed": ["1970-01-01", "1970-01-01"],
    "answer": ["SELECT * FROM beverages CROSS JOIN food_items", ""],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# --------------------------------------------------
# CROSS JOIN
# --------------------------------------------------

# Création du DataFrame
CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

ANSWER = """
 SELECT * FROM beverages
 CROSS JOIN food_items
"""
solution = duckdb.sql(ANSWER).df()

SIZE = """
size
XS
M
L
XL
"""

TRADEMARK = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""

size = pd.read_csv(io.StringIO(SIZE))
trademark = pd.read_csv(io.StringIO(TRADEMARK))
