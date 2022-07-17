# 把model 設計成streamlit app (offline)
## reference: 
## https://github.com/dataprofessor/code/blob/master/streamlit/part3/penguins-app.py

### ['SERPINA7', 'KRT23', 'F9', 'ALDOB', 'SLC10A1', 'MT2A', 'SPP1', 'CYP1A1', 'S100P', 'PIGR', 'PGC', 'DLK1', 'AGXT', 'ACSL4', 'HGFAC', 'APOA4', 'DEFB1', 'S100A14', 'LGALS4', 'CES1']
# gene_ls = ['AKR1D1', 'TIPARP', 'CYP3A4', 'HSD17B10', 'HSD17B8', 'AKR1C4',
# 'PPARGC1A', 'CYP19A1', 'SPP1', 'HSD17B3', 'ADM', 'SGPL1', 'HSD17B6',
# 'CYP17A1', 'SCARB1', 'SRD5A1', 'HSD17B11', 'WNT4', 'ESR1', 'HSD17B4','HSD3B1', 
# 'DHRS9', 'SHH', 'HSD3B2', 'PLEKHA1', 'SRD5A2']


# import time
import streamlit as st
# import numpy as np
# import pandas as pd



# st.title('測試版(accuracy = 0.91')
st.markdown("# HCC subgroup classifier")
st.markdown("> This classifier allows you to identify HCC subgroups based on the expression of 26 genes involved in androgen metabolic process pathway. You can choose to upload a csv file for multiple samples or manually input values for single sample.")
st.markdown("---")

st.sidebar.markdown("# Data Input")
st.sidebar.subheader("Multiple samples")


# # 格式範例
# st.subheader("File format should look like this: ")
# exm_df = pd.read_csv("gse14520.count.csv")
# exm_df.iloc[1:5]



# # 提供上傳資料====
# uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
# if uploaded_file is not None:
#     input_df = pd.read_csv(uploaded_file)
# else:
#     def user_input_features():
        
#         st.sidebar.subheader("Single sample:")
#         pt_name = st.sidebar.text_input("sample names","sample_XXX")
#         AKR1D1 = st.sidebar.number_input("AKR1D1",8.6840)
#         TIPARP = st.sidebar.number_input("TIPARP",6.4020)
#         CYP3A4	= st.sidebar.number_input("CYP3A4",7.9020)
#         HSD17B10 = st.sidebar.number_input("HSD17B10",9.3860)
#         HSD17B8	= st.sidebar.number_input("HSD17B8",5.9360)
#         AKR1C4	= st.sidebar.number_input("AKR1C4",8.0070)
#         PPARGC1A=	st.sidebar.number_input("PPARGC1A",5.9060)
#         CYP19A1	= st.sidebar.number_input("CYP19A1",4.6660)
#         SPP1	= st.sidebar.number_input("SPP1",8.4550)
#         HSD17B3	= st.sidebar.number_input("HSD17B3",3.8490)
#         ADM	= st.sidebar.number_input("ADM",7.5550)
#         SGPL1=	 st.sidebar.number_input("SGPL1",3.8890)
#         HSD17B6=	st.sidebar.number_input("HSD17B6",10.8770)
#         CYP17A1	= st.sidebar.number_input("CYP17A1",10.4170)
#         SCARB1	= st.sidebar.number_input("SCARB1",8.6200)
#         SRD5A1	= st.sidebar.number_input("SRD5A1",6.5930)
#         HSD17B11=	st.sidebar.number_input("HSD17B11",8.8510)
#         WNT4	= st.sidebar.number_input("WNT4",3.3000)
#         ESR1	= st.sidebar.number_input("ESR1",4.4760)
#         HSD17B4	= st.sidebar.number_input("HSD17B4",10.7240)
#         HSD3B1	= st.sidebar.number_input("HSD3B1",3.4330)
#         DHRS9	= st.sidebar.number_input("DHRS9",3.9080)
#         SHH	= st.sidebar.number_input("SHH",3.3920)
#         HSD3B2=	st.sidebar.number_input("HSD3B2",3.2890)
#         PLEKHA1	= st.sidebar.number_input("PLEKHA1",7.2920)
#         SRD5A2= st.sidebar.number_input("SRD5A2",3.7630)




#         data = {
#             "pt_name": pt_name,
#             "AKR1D1": AKR1D1,
#             "TIPARP": TIPARP,
#         "CYP3A4"	:CYP3A4,
#         'HSD17B10'	:HSD17B10,
#         "HSD17B8"	:HSD17B8,
#         "AKR1C4":   AKR1C4,
#         "PPARGC1A":   PPARGC1A,
#         "CYP19A1"	:  CYP19A1,
#         "SPP1"	:SPP1,
#         "HSD17B3":	HSD17B3,
#         "ADM"	:ADM,
#         "SGPL1"	:SGPL1,
#         "HSD17B6":	HSD17B6,
#         "CYP17A1":	CYP17A1,
#         "SCARB1":	SCARB1,
#         "SRD5A1":	SRD5A1,
#         "HSD17B11":	HSD17B11,
#         "WNT4"	:WNT4,
#         "ESR1"	:ESR1,
#         "HSD17B4"	:HSD17B4,
#         "HSD3B1"	:HSD3B1,
#         "DHRS9"	:DHRS9,
#         "SHH"	:SHH,
#         "HSD3B2":	HSD3B2,
#         "PLEKHA1":	PLEKHA1,
#         "SRD5A2": SRD5A2  
#                 }
        
#         features = pd.DataFrame(data, index=[0])
#         return features

#     input_df = user_input_features()
# ====

# st.subheader("Here's your input data:")
# input_df
# df_for_process = input_df[input_df.columns[input_df.columns!=input_df.columns[0]]]
# st.text("> Warning: Make sure the format looks sample as example above \n (First column should be patient names or id. The order of genes doesn't matters.)")


# # ====排好基因順序
# df_for_process = df_for_process[gene_ls]
# # ====正規化

# from sklearn import preprocessing
# x = df_for_process
# scaler = preprocessing.StandardScaler()
# standardized_x = scaler.fit_transform(x.T)
# standardized_x = standardized_x.T


# standardized_dfe = pd.DataFrame(standardized_x)
# standardized_dfe.columns = df_for_process.columns
# standardized_dfe.index = input_df[input_df.columns[0]]
# st.subheader("Here's your input data after normalization:")
# standardized_dfe

# # standardized_dfe


# import joblib
# # load the model from disk
# filename = "classifier.pkl"
# # Load
# model = joblib.load(filename)

# model.predict(
#     np.array(standardized_dfe)
#     )

# df_pred = pd.DataFrame(
#     model.predict(
#     np.array(standardized_dfe)
#     )
# )
# df_pred.columns = ["subgroup"]
# df_pred.index = standardized_dfe.index



# st.markdown("---")
# st.markdown("## __Here's the predicted results:__")
# df_pred = df_pred.transpose()
# df_pred

# import base64
# def get_table_download_link(df):
#     """Generates a link allowing the data in a given panda dataframe to be downloaded
#     in:  dataframe
#     out: href string
#     """
#     csv = df.to_csv(index=True)
#     b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
#     href = f'<a href="data:file/csv;base64,{b64}" download="download.csv">Download csv file</a>'
#     st.markdown(href, unsafe_allow_html=True)

# get_table_download_link(df_pred)

