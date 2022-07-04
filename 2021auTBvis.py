import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st
import plotly.express as px
from modules import dataset_function as ds_func

df = ds_func.import_tb_dataset("SIR51015.csv")

# st.write(df.head(3))

df = df[~df['delivery_date'].isnull()]
df['project_id'] = df['project_id'].apply(lambda x : str(x) if type(x) != str else x)
df['order_id'] = df['order_id'].apply(lambda x: str(x) if type(x) != str else x)
df['projectNameID'] = df['project_id'].str.cat(df['project_name'], sep='_')


# df['受渡日'] = df['受渡日'].apply(lambda x: str(x) if type(x) != str else x)

from pandas.api.types import infer_dtype
st.write(df.apply(infer_dtype))

st.write(df.head(3))

