import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st
import plotly.express as px

df = pd.read_csv(r'SIR51015.csv', encoding='cp932')
df = df.drop(index=0, axis=0)
df = df[~df['購入・予約管理ID'].isnull()]

# df = df[['案件ID', '案件名', '年度ID', '期ID', '顧客CD', '顧客名', '担当者CD', '決済方法', '配送方法', '購入・予約管理ID', '決済方法', '購入ステータス', '受渡日', '配送伝票番号', '販売単価', '販売単価（税抜）', '本体価格（税抜）', 'ISBNコード', '書名', '出版社', '商品口']]
df = df[['案件ID', '案件名','受渡日']]