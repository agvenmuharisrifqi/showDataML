from django.shortcuts import render
from django.conf import settings
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import json


def index(request):
    df=pd.read_excel(settings.BASE_DIR / 'MachineLearning/FIX Data Minat Nasabah excel.xlsx')
    df['label'].replace({2:0},inplace=True)
    y = df.loc[:, ['label']]
    x1= df.loc[:, [ 'jenis_kelamin','status','pendapatan_pertahun']]
    X_train, X_test, y_train, y_test = train_test_split(x1,y,test_size = 0.1,random_state=30,train_size=None,shuffle=True,stratify=None)
    model_NB=GaussianNB()
    model_NB.fit(X_train,y_train)
    y_pediksi=model_NB.predict(X_test)#prediksi

    """
    Read Data
    """
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    
    """
    Result Data
    """
    result_X_train = len(X_train)
    result_Y_train = len(y_train)
    result_X_test = len(X_test)
    result_X_test = len(y_test)
    accuracy = accuracy_score(y_test,y_pediksi)

    
    context = {
        'title': 'SHOW DATA ML',
        'data': data,
        'result_X_train': result_X_train,
        'result_Y_train': result_Y_train,
        'result_X_test': result_X_test,
        'result_Y_test': result_X_test,
        'accuracy': accuracy,
    }
    return render(request, 'index.html', context)