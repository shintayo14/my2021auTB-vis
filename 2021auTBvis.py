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
	df = df[~df['購入・予約管理ID'].isnull()]
	return df

df = import_tb_dataset("SIR51015.csv")
df = df[['案件ID', '案件名', '年度ID', '期ID', '顧客CD', '顧客名', '担当者CD',
		 '決済方法', '配送方法', '購入・予約管理ID', '購入ステータス','受渡日', '配送伝票番号',
		 '販売単価', '販売単価（税抜）', '本体価格（税抜）','ISBNコード', '書名', '出版社', '商品口']]
st.write(df.head(3))