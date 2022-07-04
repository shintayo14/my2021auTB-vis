import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st
import plotly.express as px
from modules import dataset_function as ds_func

df = ds_func.import_tb_dataset("SIR51015.csv")

# st.write(df.head(3))

df = df[~df['受渡日'].isnull()]
df['案件ID'] = df['案件ID'].apply(lambda x : str(x) if type(x) != str else x)
df['購入・予約管理ID'] = df['購入・予約管理ID'].apply(lambda x: str(x) if type(x) != str else x)
df['案件ID_案件名'] = df['案件ID'].str.cat(df['案件名'], sep='_')


df['受渡日'] = df['受渡日'].apply(lambda x: str(x) if type(x) != str else x)

from pandas.api.types import infer_dtype
st.write(df.apply(infer_dtype))

st.write(df.head(3))

