import streamlit as st
import joblib
import pandas as pd
import imageio

st.set_page_config(
    page_title="Heart Disease", page_icon="💒",
)

image = imageio.imread('heart.jpg')
st.write("# Predicted Chance of Getting Cardiovascular Heart Disease in the Next Few Years")
st.write(
    """This is a machine learning based approcach to predict cardiovascular disease through data. Please keep in mind that this is in no way a substitution of a profession diagnosis by a doctor.""")
col1, col2 = st.columns(2)
age = col1.number_input("Enter your age")
gender = col1.selectbox("Enter your gender",["Male", "Female"])
cigsPerDay = col1.number_input("How many cigarettes do you smoke every day")
chol = col2.number_input("Enter your cholesterol level")
sys_bp = col2.number_input("Enter your systolic blood pressure")
glucose = col2.number_input("Enter your glucose level")
if gender=="Male":
    gender = 1
else:
    gender = 0
input_arr = [age, gender, cigsPerDay,chol,sys_bp,glucose]
input = pd.DataFrame([input_arr], columns = ['age','male','cigsPerDay','totChol','sysBP','glucose'])
model = joblib.load('heart_model.pkl')
prediction = model.predict(input)

if st.button('Predict'):
    if(prediction[0]==0):
        st.image(image)
        st.write('<h1 style="text-align: center;"><span style="font-size: xx-large; background-color: #99ccff;">You most likely DO NOT have heart and/or cardiovascular disease.</span></h1><p><strong>If concerned, there are several ways you can reduce your risk of developing heart and/or cardiovascular diseases, such as:</strong></p>\
                <p><span> 1. Lower your blood and cholesterol levels.</span></p>\
<p><span> 2. Eating a healthy, balanced diet.</span></p>\
<p><span> 3. Maintaining a healthy weight.</span></p>\
<p><span> 4. Giving up and/or avoiding smoking and tobacco.</span></p>\
<p><span> 5. Reducing alcohol consumption.</span></p>\
<p><span> 6. Keeping blood pressure under control.</span></p>\
<p><span> 7. Being consistently active and involved in physical activity.</span></p>\
<p>&nbsp;</p>\
<p><span "><strong>Cardiovascular diseases (CVDs) are the leading cause of death globally. An estimated 17.9 million people died from cardiovascular diseases per year, representing 32% of all global deaths.</strong></span></p>\
<p>&nbsp;</p>\
<p><em>Identifying those at the highest risk of CVDs early on, diagnosing as early as possible, and ensuring patients receive appropriate treatment at the correct time can prevent premature and consequential deaths. Access to noncommunicable disease medicines and basic health technologies is essential to ensure that those in need receive appropriate care.</em></p>',unsafe_allow_html=True)

    else:
        st.image(image)
        st.write('<div style="text-align: center;"><span style="font-size: x-large; color: #ff0000;">You have a HIGH chance of having cardiovascular disease in the next few years. Please see a doctor immediately.</span></div>\
<p>&nbsp;</p>\
<p>&nbsp;</p>\
<p style="text-align: center;"><strong>Cardiovascular diseases (CVDs) are the leading cause of death globally. An estimated 17.9 million people died from cardiovascular diseases per year, representing 32% of all global deaths.</strong></p>\
<p style="text-align: center;">&nbsp;</p>\
<p><em>Identifying those at the highest risk of CVDs, diagnosing as early as possible, and ensuring patients receive appropriate treatment at the correct time can prevent premature and consequential deaths. Access to noncommunicable disease medicines and basic health technologies is essential to ensure that those in need receive appropriate care.</em></p>',unsafe_allow_html=True)

