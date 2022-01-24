import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

def profit_prediction(Research,Admin,Market,State_N,State_C):
    df = pd.read_csv('/mnt/c/Users/Sourabh Singh/Desktop/model_deploy/files/50_Startups.csv')
    encoder = OneHotEncoder(sparse=False,drop='first')
    df_onehot = encoder.fit_transform(df['State'].values.reshape(-1,1))
    dfonehot = pd.DataFrame(df_onehot)#,columns=['State_NewYork','State_California'])#,columns = ["FuelType_"+str(int(i)) for i in range(3)])
    df = pd.concat([df, dfonehot], axis=1)
    df= df.drop(['State'], axis=1)

    df_train = df.drop(columns='Profit',axis =1)
    df_test = df['Profit']


    X = df_train.values
    y = df_test.values

    reg = LinearRegression()
    reg.fit(X,y)
    
    X_test = np.array([Research,Admin,Market,State_N,State_C])
    X_test = X_test.reshape((-1,5))
    
    return reg.predict(X_test)

# df = pd.read_csv('/mnt/c/Users/Sourabh Singh/Desktop/model_deploy/files/50startup_train.csv')
# df_train = df.drop(columns='Profit',axis =1)
# df_test = df['Profit']
# X = df_train.values
# y = df_test.values
# reg = LinearRegression()
# reg.fit(X,y)

# print(df.info())

