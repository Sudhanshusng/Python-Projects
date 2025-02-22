import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st



def main():
    st.title("Streamlit App for Data Analysis :")
    st.sidebar.title("Upload your File here")
    uploaded_file = st.sidebar.file_uploader("Upload your File" , type = [".csv",".xlsx"])
    try:
        if uploaded_file.name.endswith(".csv"):
         df = pd.read_csv(uploaded_file)
        else:
         df = pd.read_excel(uploaded_file)
  
        st.sidebar.success("File Uploaded Successfully")
        st.subheader("Data Overview - ")
        st.dataframe(df.head())
        st.subheader("Basic info of Data")
        st.write("Data Stats", df.shape)
        st.write("Column Names", df.columns)
        st.write("Describe Data", df.describe())
    except Exception as e:
        print (e)

if __name__ == "__main__":
    main()
