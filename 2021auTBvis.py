import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st
import plotly.express as px


@st.cache
def import_tb_dataset(dataset):
	df = pd.read_csv(r'{}'.format(dataset), encoding='cp932')
	df = df.drop(index=0, axis=0)
	return df

df = import_tb_dataset("SIR51015.csv")

st.write(df.head(3))