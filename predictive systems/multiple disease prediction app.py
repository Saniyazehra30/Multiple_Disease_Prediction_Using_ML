# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 07:38:49 2025

@author: rizvi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#changing name and logo
st.set_page_config(page_title="Disease Prediction" , page_icon="⌂")


#set background
background_image_url = "https://cdn.cta.tech/cta/media/media/events/ai-digital-health_500x500.jpg"

# loading the saved model
diabetes_model = pickle.load(open(r'C:/Users/rizvi/OneDrive/Desktop/aicte internship/predictive systems/saved models/diabetes_model.sav', 'rb'))

parkinsons_model = pickle.load(open(r'C:/Users/rizvi/OneDrive/Desktop/aicte internship/predictive systems/saved models/Parkinson_model.sav' , 'rb'))

heart_disease_model = pickle.load(open(r'C:/Users/rizvi/OneDrive/Desktop/aicte internship/predictive systems/saved models/heart_disease_model.sav' , 'rb'))

lung_cancer_model = pickle.load(open(r'C:/Users/rizvi/OneDrive/Desktop/aicte internship/predictive systems/saved models/lungs_disease_model.sav' , 'rb'))

thyroid_model = pickle.load(open(r'C:/Users/rizvi/OneDrive/Desktop/aicte internship/predictive systems/saved models/Thyroid_model.sav' , 'rb'))


# sidebar for navigate
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Parkinsons Prediction',
                            'Heart Disease Prediction',
                            'Lungs Cancer Prediction',
                            'Thyroid Prediction'], 
                           icons=['activity' , 'person', 'heart', 'lungs', 'caret-right-fill'],
                             default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user 
    #columns for input fields
    coll, col2, col3 = st.columns (3) 
    with coll: 
         Pregnancies = st.text_input('Number of Pregnancies') 
    with col2: 
         Glucose = st.text_input('Glucose Level') 
    with col3: 
         BloodPressure = st.text_input('Blood Pressure value') 
    with coll: 
         SkinThickness = st.text_input('Skin Thickness value') 
    with col2: 
         Insulin = st.text_input('Insulin Level') 
    with col3: 
         BMI = st.text_input('BMI value') 
    with coll: 
         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value') 
    with col2: 
         Age = st.text_input('Age') 

    
    
    #code for prediction
    diab_diagnosis =''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is diabetic'
        else :
            diab_diagnosis = 'The person is not diabetic'
      
    st.success(diab_diagnosis)       
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    coll, col2, col3 = st.columns(3) 
    with coll: 
       age = st.text_input('Age') 
    with col2: 
       sex = st.text_input('Sex') 
    with col3: 
       cp =st.text_input('Chest Pain types') 
    with coll: 
       trestops = st.text_input('Resting Blood Pressure') 
    with col2: 
       chol = st.text_input('Serum Cholestoral in mg/dL') 
    with col3: 
       fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL') 
    with coll: 
       restecg = st.text_input('Resting Electrocardiographic results') 
    with col2: 
       thalach = st.text_input('Naximum Heart Rate achieved') 
    with col3: 
       exang = st.text_input('Exercise Induced Angina')
       
    #code for Prediction 
    heart_diagnosis =''
  
    #creating a button for Prediction 
    if st.button('Heart Disease Test Result'): 
       heart_prediction = heart_disease_model.predict([[age, sex, cp, trestops, chol, fbs, restecg, thalach, exang]])
                                                      
       if (heart_prediction[0] == 1): 
            heart_diagnosis = 'The person is having heart disease'
       else: 
            heart_diagnosis = 'The person does not have any heart disease' 
    st.success(heart_diagnosis) 
   
            
    # Parkinsons Prediction Page
if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    coll, col2, col3, col4, col5 = st.columns(5) 
    with coll: 
        fo = st.text_input('MDVP: Fo(Hz)') 
    with col2:
        fhi = st.text_input('NDVP:Fhi (Hz)') 
    with col3: 
        flo = st.text_input('MDVP:FLo(Hz)') 
    with col4: 
        Jitter_percent = st.text_input('MDVP:Jitter(%)') 
    with col5: 
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)') 
    with coll: 
        RAP = st.text_input('MDVP: RAP') 
    with col2: 
        PPQ = st.text_input('MDVP: PPQ') 
    with col3: 
        DDP = st.text_input('Jitter:DDP') 
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer') 
    with col5: 
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)') 
    with coll: 
        APQ3 = st.text_input('Shimmer: APQ3') 
    with col2: 
        APQ5 = st.text_input('Shimmer: APQ5') 
    with col3: 
        APQ = st.text_input('MDVP: APQ') 
    with col4: 
        DDA = st.text_input('Shimmer:DDA') 
    with col5: 
        NHR = st.text_input('NHR')
    with coll: 
        HNR = st.text_input('HNR') 
    with col2: 
        RPDE = st.text_input('RPDE') 
    with col3: 
        DFA = st.text_input('DFA') 
    with col4: 
       spread1 = st.text_input('spread1') 
    with col5: 
       spread2 = st.text_input('spread2') 
    with coll: 
       D2 = st.text_input('D2') 
    with col2: 
       PPE = st.text_input('PPE')
      
    # code for Prediction 
    parkinsons_diagnosis = ''
   
    #creating a button for Prediction 
    if st.button("Parkinson's Test Result"): 
         parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,APQ3, APQ5, APQ, DDA, NHR, HNR,RPDE,DFA, spread1,spread2, D2, PPE]])
         if (parkinsons_prediction [0] == 1): 
             parkinsons_diagnosis = "The person has Parkinson's disease" 
         else: 
             parkinsons_diagnosis = "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)
    
# Lung Cancer Prediction Page
if (selected == "Lungs Cancer Prediction"):
    st.title('Lung Cancer')
    
    col1, col2 = st.columns(2)
    
    with col1:
     GENDER = st.text_input('Gender (1 = Male; 0 = Female)')
     AGE = st.text_input('Age')
     SMOKING = st.text_input('Smoking (1 = Yes; 0 = No)')
     YELLOW_FINGERS = st.text_input('Yellow Fingers (1 = Yes; 0 = No)')
     ANXIETY = st.text_input('Anxiety (1 = Yes; 0 = No)')
     PEER_PRESSURE = st.text_input('Peer Pressure (1 = Yes; 0 = No)')
     CHRONIC_DISEASE = st.text_input('Chronic Disease (1 = Yes; 0 = No)')
     FATIGUE = st.text_input('Fatigue (1 = Yes; 0 = No)')

    with col2:
     
     ALLERGY = st.text_input('Allergy (1 = Yes; 0 = No)')
     WHEEZING = st.text_input('Wheezing (1 = Yes; 0 = No)')
     ALCOHOL_CONSUMING = st.text_input('Alcohol Consuming (1 = Yes; 0 = No)')
     COUGHING = st.text_input('Coughing (1 = Yes; 0 = No)')
     SHORTNESS_OF_BREATH = st.text_input('Shortness Of Breath (1 = Yes; 0 = No)')
     SWALLOWING_DIFFICULTY = st.text_input('Swallowing Difficulty (1 = Yes; 0 = No)')
     CHEST_PAIN = st.text_input('Chest Pain (1 = Yes; 0 = No)')

    # code for Prediction 
    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = lung_cancer_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        if (lungs_prediction[0] == 1):
            lungs_diagnosis = "The person has lung cancer disease"
        else :
            lungs_diagnosis = "The person has not lung cancer disease"
    st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Thyroid Prediction":
    st.title("Thyroid")
    
    col1, col2 = st.columns(2)
    
    with col1:
      age = st.text_input('Age')
      sex = st.text_input('Sex (1 = Male; 0 = Female)')
      on_thyroxine = st.text_input('On Thyroxine (1 = Yes; 0 = No)')
      tsh = st.text_input('TSH Level')
     
    with col2:
      t3_measured = st.text_input('T3 Measured (1 = Yes; 0 = No)')
      t3 = st.text_input('T3 Level')
      tt4 = st.text_input('TT4 Level')
    
    # code for Prediction 
    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = thyroid_model.predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        if (thyroid_prediction[0] == 1):
            thyroid_diagnosis = "The person has lung cancer disease"
        else :
            thyroid_diagnosis = "The person has not lung cancer disease"
    st.success(thyroid_diagnosis)
    


