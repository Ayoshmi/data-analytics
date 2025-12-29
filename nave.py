import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df=pd.read_csv("data.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]


encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=CategoricalNB().fit(X_train,y_train)

y_pred=model.predict(X_test)
print("accuracy{:.2f}%".format(accuracy_score(y_test,y_pred)*100))
print("predictionpip:",y_pred)