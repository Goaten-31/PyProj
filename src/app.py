import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

base_dataset = "../data/pyproj_data.csv"

st.title("Student Grade Dashboard")

uploaded_dataset = st.file_uploader(label="Upload a csv file upto 10 MBs in size.",
                type="csv", max_upload_size=10)

if not uploaded_dataset:
    df = pd.read_csv(base_dataset)
else:
    df = pd.read_csv(uploaded_dataset)

st.dataframe(df)