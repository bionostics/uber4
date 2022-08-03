import pandas as pd
import joblib
import tensorflow as tf


from sklearn.utils import shuffle
covid = pd.read_csv("/Users/mvideet/PycharmProjects/CAC/Covid Dataset.csv")
covid=covid.drop('Running Nose',axis=1)
covid=covid.drop('Chronic Lung Disease',axis=1)
covid=covid.drop('Headache',axis=1)
covid=covid.drop('Heart Disease',axis=1)
covid=covid.drop('Diabetes',axis=1)
covid=covid.drop('Gastrointestinal ',axis=1)
covid=covid.drop('Wearing Masks',axis=1)
covid=covid.drop('Sanitization from Market',axis=1)
covid=covid.drop('Asthma',axis=1)
covid = covid.replace({"Yes":1, "No": 0})
covid['COVID-19'].value_counts()
noncovid= covid[covid['COVID-19'] == 0]
yescovid= covid[covid['COVID-19'] == 1]
print(noncovid.iloc[1])
nonvoidbal = noncovid.sample(len(noncovid), replace=True)
yescovid = yescovid.sample(len(noncovid), replace=True)
covid = pd.concat([yescovid,noncovid], axis=0)

print(covid['COVID-19'].value_counts())
x=covid.iloc[:,:-1]
y=covid.iloc[:,-1]
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20,shuffle=1, random_state=42)
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print((y_pred))
y_test = y_test.to_numpy()
for i in range(len(y_pred)):
    if(y_pred[i] != y_test[i]):
        print("At index " + str(i) + " the prediction is wrong. It is supposed to be " + str(y_test[i]) + " but it predicted " + str(y_pred[i]))
print(metrics.accuracy_score(y_test,y_pred))
joblib.dump(model, '../uber4/covid.pkl')
print((x.head()))
# acc_decisiontree=model.score(y_pred, y_test)*100
# print(acc_decisiontree)
# print()