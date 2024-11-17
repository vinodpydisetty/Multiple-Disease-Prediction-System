# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/SHYAM/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/SHYAM/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/SHYAM/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Survey',
                           'SignIn',
                           'SignUp',
                           'About'],
                          icons=['activity','heart','person','pencil-square','person-square','person-bounding-box','link'],
                          default_index=0)
    

if (selected == 'About'):
    st.title("Multiple Disease Prediction System")
    st.subheader("This project aims to develop a comprehensive disease prediction system that focuses on predicting three prevalent medical conditions: Diabetes, Heart disease, and Parkinson's disease ")
    st.subheader("Many of the existing machine learning models for health care analysis are concentrating on one disease per analysis. For example first is for Diabetes analysis, one for Heart analysis, one for Lung diseases like that. If a user wants to predict more than one disease, he/she has to go through different sites. There is no common system where one analysis can perform more than one disease for prediction.This platform will give you that feasibility of make prediction for more than one disease.")
    st.header("Designers")
    col1, col2, col3 = st.columns(3)
    with col1:
         st.text("ShyamKumar Jada\nN180061\nn180061@rguktn.ac.in\n+918179175620")
    with col2:
        st.text("SubbaRao Mareboina\nN180505\nn18505@rguktn.ac.in\n+917032505187")
    with col3:
        st.text("HarshaRajesh Lanka\nN180854\nn180854@rguktn.ac.in\n+918790801589")

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age',0,100)
        
    with col2:
        sex = st.number_input('Sex',0,10)
        
    with col3:
        cp = st.number_input('Chest Pain types',0,3)
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure',0,200)
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',100,1000)
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',0,10)
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',0,10)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',0,200)
        
    with col3:
        exang = st.number_input('Exercise Induced Angina',0,10)
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',0,10)
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',0,10)
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',0,10)
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',0,10)
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

if (selected=="Survey"):
    st.title("Survey Form")
    form=st.form(key='form')
    name=form.text_input("Enter Your Name")
    gender=form.selectbox("pick your gender",("Male","Female","Others"))
    Dob=form.date_input("Date of Birth")
    age=form.number_input("Age",0,100)
    phone=form.text_input("Enter Your Phonenumber")
    address=form.text_input("Enter Your Address")
    disease=form.selectbox("Select your Disease",("Diabetes","Heart","Parkinsons"))
    doctor=form.text_input("Enter Hospital or Doctor Name if Consulted")
    file=form.file_uploader("Upload your Report")
    txtarea=form.text_area("Write Here")
    
    submit_button=form.form_submit_button('Submit')
    if submit_button:
        st.success("uploaded Successfully")
    
    

if (selected == "SignIn"):
    st.title("SignIn Here")
    form2=st.form(key='form2')
    username=form2.text_input("Username")
    password=form2.text_input("Password",type="password")

    submit_button=form2.form_submit_button('Login')
    if submit_button:
        st.success("Successfully Login")

if (selected=='SignUp'):
    st.title("Signup Here")
    form3=st.form(key='form3')
    firstname=form3.text_input("Firstname")
    lastname=form3.text_input("Lastname")
    Dob=form3.date_input("Date of Birth")
    Email=form3.text_input("Email")
    password=form3.text_input("Create Password",type="password")
    
    submit_button=form3.form_submit_button('Submit')
    if submit_button:
        st.success("Successfully completed SignUp")
    


    

            


