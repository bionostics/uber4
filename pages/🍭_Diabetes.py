import math
import streamlit as st
import joblib
import pandas as pd
st.set_page_config(page_title="Diabetes Predictor ", page_icon="🍭")
st.markdown("# Diabetes  Predictor")
st.write(
    """This is a machine learning based approcach to predict Diabetes through symptoms. Please keep in mind that this is in no way a substitution of a profession diagnosis by a doctor.""")
col1, col2,col3 = st.columns(3)
BP = col1.selectbox("Do you have a relatively high blood pressure?",["Yes", "No"])
cholestrol = col1.selectbox("Do you have a relatively high cholestrol level?",["Yes", "No"])
BMI = col1.number_input("What is your BMI(Body-Mass Index)?")
smoke = col1.selectbox("Have you smoked at least 100 cigarettes in your life?",["Yes", "No"])
stroke = col1.selectbox("Have you ever had a stroke?",["Yes", "No"])
CHD = col1.selectbox("Have you ever had a heart attack or myocardial infarction",["Yes", "No"])
phys = col2.selectbox("Do you maintain physical activity?",["Yes", "No"])
fruit = col2.selectbox("Do you regularly eat fruits?",["Yes", "No"])
veggies = col2.selectbox("Do you regularly eat veggies?",["Yes", "No"])
alc = col2.selectbox("Are you a heavy alcohol drinker?",["Yes", "No"])
healthcare = col2.selectbox("Do you have a healthcare provider?",["Yes", "No"])
nodoc = col2.selectbox("Was there a time where you needed to see the doctor but could not because of the cost?",["Yes", "No"])
genhealth = col3.number_input("On a scale of 1-5, how would you say your general health is?",min_value = 1,max_value=5)
menhealth = col3.number_input("In the last 30 days, approximately how many days have you had bad mental health?",min_value = 1,max_value=30)
stair = col3.selectbox("Do you have difficulty walking or climbing stairs?",["Yes", "No"])
gender = col3.selectbox("What is your gender?",["Male", 'Female'])
age = col3.number_input("What is your age?")
if gender=="Male":
    gender = 1
else:
    gender = 0
if age<24:
    age=1
else:
    age =  math.floor((float(age)/5.0)-3.0)
inp_arr = [BP,cholestrol,BMI,smoke,stroke,CHD,phys,fruit,veggies,alc,healthcare,nodoc,genhealth,menhealth,stair,gender,age]
for i in range(len(inp_arr)-2):
    if  i!=2 and i!=12 and i!=13:
        if inp_arr[i]=="Yes":
            inp_arr[i]=1.0
        else:
            inp_arr[i]=0.0
input = pd.DataFrame([inp_arr], columns = ['HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'DiffWalk', 'Sex', 'Age']
)
model = joblib.load('/Users/mvideet/PycharmProjects/uberfinal1/diabetes.pkl')
y_pred = model.predict(input)
if st.button('Predict'):
    if y_pred[0]==0:
        st.write('<p style="text-align: center;"><span style="font-size: x-large; color: #339966;">You have a very low chance of having diabetes</span>.</p>\
<p>If you feel like you are experiencing symptoms similar to:</p>\
<p>1. Urinate often</p>\
<p>2. Very thirsty</p>\
<p>3. Ability to lose weight without trying</p>\
<p>4. Have blurry vision</p>\
<p>5. Tiredness</p>\
<p><em>Source:&nbsp;https://www.cdc.gov/diabetes/basics/symptoms.html</em></p>\
<p style="text-align: center;"><span style="font-size: medium;"><strong>Please contact your doctor and immediately get a checkup.</strong></span></p>\
<p>&nbsp;</p>', unsafe_allow_html=True)
    elif y_pred[0]==1:
        st.write('<p style="text-align: center;"><span style="color: #ff9900;"><span style="font-size: x-large;">You have a chance of having pre-diabetes</span>.</span></p>\
<p style="text-align: center;"><span style="font-size: medium; color: #ff9900;">Pre-diabetes is the stage right before type-2 diabetes. Having pre-diabetes means that without any intervention, you are likely to get diabetes in the next ten years.</span></p>\
<p>If you feel like you are experiencing symptoms similar to:</p>\
<p>1. Urinate often</p>\
<p>2. Very thirsty</p>\
<p>3. Ability to lose weight without trying</p>\
<p>4. Have blurry vision</p>\
<p>5. Tiredness</p>\
<p><em>Source:&nbsp;https://www.cdc.gov/diabetes/basics/symptoms.html</em></p>\
<p style="text-align: center;"><span style="font-size: medium;"><strong>Please contact your doctor and immediately get a checkup.</strong></span></p>\
<p style="text-align: center;">&nbsp;</p>\
<p>&nbsp;</p>', unsafe_allow_html=True)
    else:
        st.write('''<p style="text-align: center;"><strong><span style="color: #ff0000; font-size: x-large;">You have a high chance of having diabetes.</span></strong></p>
<p style="text-align: left;">If you feel like you are experiencing symptoms similar to:</p>
<p>1. Urinate often</p>
<p>2. Very thirsty</p>
<p>3. Ability to lose weight without trying</p>
<p>4. Have blurry vision</p>
<p>5. Tiredness</p>
<p><em>Source:&nbsp;https://www.cdc.gov/diabetes/basics/symptoms.html</em></p>
<p style="text-align: center;"><span><strong>Please get a checkup immediately for an official diagnosis.</strong></span></p>''',unsafe_allow_html=True)

#finish up '2' later