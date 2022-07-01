import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st
import plotly.express as px
from modules import dataset_function as ds_func

df = ds_func.import_tb_dataset("SIR51015.csv")

st.write(df.head(3))