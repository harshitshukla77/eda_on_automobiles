import pandas as pd 
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/harshit/Downloads/train.csv")
sns.histplot(x=df["PassengerId"])
st.pyplot(plt.gcf())

st.sidebar.title("harshit")
x= st.slider("enter your value")
st.write(x)
st.write("harshit hukle")
st.write ("gupchup")
st.write ("hello")
st.write("hello sunai nhi de rha")
