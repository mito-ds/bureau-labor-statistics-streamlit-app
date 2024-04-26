import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import pandas as pd

st.set_page_config(layout="wide")
st.title('Bureau of Labor Statistics Analysis')


df = pd.read_csv('./Bureau of Labor Statistics Part 1.csv')
new_dfs, code = spreadsheet(
    df, 
    df_names=['Bureau_of_Labor_Statistics_Part_1'],
    import_folder='./data'
)

st.code(code)
