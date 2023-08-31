import streamlit as st
from PIL import Image
import pickle
from warnings import catch_warnings
import numpy as np

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


# ---- LOAD ASSETS ----

img = Image.open("loan.jpg")


st.set_page_config(page_title="Fore-Loan", page_icon=":tada:", layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>Welcome to Fore-Loan</h1>",
            unsafe_allow_html=True)
# st.title('Welcome to ActoVision')

with st.container():
    st.header("Fore-Loan")
    st.image(img)
    st.subheader(
        "We can predict whether your loan application is gone be rejected or accepted by the banks or other finicial institutions."
    )

model = pickle.load(open('Loan.pickle', 'rb'))


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")

        st.markdown("<h3 style='text-align: center; color: white; margin:0'>Loan Prediction</h3>",
            unsafe_allow_html=True)
        
        Age = st.text_input("Enter your Age")
        Income = st.text_input("Enter your Income")
        Ownership = st.selectbox("Ownership: ",['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
        Intent = st.selectbox("Intent: ",['PERSONAL', 'EDUCATION', 'MEDICAL','VENTURE','HOMEIMPROVEMENT','DEBTCONSOLIDATION'])
        Amount = st.text_input("Enter your Loan Amount")

        if(st.button('Submit')):

            Ownership = Ownership

            mapping = {'RENT': 0, 'OWN': 1, 'MORTGAGE': 2, 'OTHER': 3}

            if Ownership in mapping:
                Ownership = mapping[Ownership]

            mapp = {'PERSONAL':0,'EDUCATION':1,'MEDICAL':2,'VENTURE':3,'HOMEIMPROVEMENT':4,'DEBTCONSOLIDATION':5}

            if Intent in Intent:
                Intent = mapp[Intent]

            data=np.array([[Age,Income,Ownership,Intent,Amount]])

            price =  model.predict(data)

            if(price==1):
                st.success("Loan will be Approved")
            else:
                st.warning("Loan will be Dismissed")

    with right_column:
        st.write('\n')
        st.image(img)



# ---- footer ----
with st.container():
    st.write("---")
    st.markdown("<p style='text-align: center; color: white;'>Copyrights 2023: Mayur Pimpude</p>",
                unsafe_allow_html=True)


hide_default_format = """
       <style>
       # MainMenu {visibility: hidden; }
       footer {visibility: hidden; }
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

