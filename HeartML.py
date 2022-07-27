#Import Statements
import pandas as pd
import statsmodels.api as sm
import scipy.stats as st
import joblib
from sklearn import metrics
import matplotlib as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

#Input
gender = input("What is your gender? ")
if gender == "Male" or gender == "male":
    gender = True
else:
    gender = False
age = int(input("What is your age? "))
cigarettes = int(input("How many cigarettes do you smoke per day? "))
cholestrol = float(input("What is your total Cholestrol? "))
bp = float(input("What is your systolic blood pressure? "))
gl = float(input("What is your glucose level? "))
input_arr = [age, gender, cigarettes,cholestrol,bp,gl]
input = pd.DataFrame([input_arr], columns = ['age','male','cigsPerDay','totChol','sysBP','glucose'])

#Reading the csv file with all the data
df = pd.read_csv("framingham.csv")
#print(df.head())
starting_size = df.size
df.dropna(axis = 0, inplace = True)
#print(starting_size - df.size) #total number of rows with missing data

print(df['TenYearCHD'].value_counts())
noncovid= df[df['TenYearCHD'] == 0]
yescovid= df[df['TenYearCHD'] == 1]
nonvoidbal = noncovid.sample(len(yescovid), replace=True)
yescovid = yescovid.sample(len(yescovid), replace=True)
df = pd.concat([yescovid,noncovid], axis=0)
#Removes variables that do not positively contribute to the outcome
from statsmodels.tools import add_constant as add_constant
heart_df_constant = add_constant(df)


remove_arr = ["heartRate", "currentSmoker", "prevalentStroke", "prevalentHyp", "diabetes", "diaBP", "BMI"]
for i in remove_arr:
   heart_df_constant.drop([i],axis=1,inplace=True)

st.chisqprob = lambda chisq, df: st.chi2.sf(chisq, df)
cols=heart_df_constant.columns[:-1]
model=sm.Logit(df.TenYearCHD,heart_df_constant[cols])
result=model.fit()
result.summary()

#Creating the dataframe to put into the logistic regression
import sklearn
new_features=df[['age','male','cigsPerDay','totChol','sysBP','glucose','TenYearCHD']]

new_features.describe()
x=new_features.iloc[:,:-1]
y=new_features.iloc[:,-1]

#Final Output
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=(0.12))
reg = LogisticRegression()
reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)
max_accuracy = max(0,sklearn.metrics.accuracy_score(y_test,y_pred))
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['Disease', 'No Disease'])
print(max_accuracy)
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
print(confusion_matrix)

# cm_display.plot()
# plt.show()
joblib.dump(reg, 'heart_model.pkl')
