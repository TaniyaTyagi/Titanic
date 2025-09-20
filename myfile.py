import streamlit as st
import pandas as pd
import pickle

model=pickle.load(open("titanic_model.pkl","rb"))

st.title(" Titanic Survival Prediction (Simple Version)")

# Input fields 
pclass = st.selectbox("Class (1=1st, 2=2nd, 3=3rd)", [1, 2, 3])
sex = st.radio("Sex", ["male", "female"])
age = st.number_input("Age", 0, 100, 25)
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 600.0, 32.0)

if st.button("Predict Survival"):
    sex_val = 0 if sex == "male" else 1
    data = pd.DataFrame([[pclass, sex_val, age, sibsp, parch, fare]], columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"])
    pred = model.predict(data)[0]
    if pred == 1:
        st.success(" Passenger will SURVIVE")
    else:
        st.error(" Passenger will NOT SURVIVE")


