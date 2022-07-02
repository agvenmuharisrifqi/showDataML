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
    data_excel = []
    data_excel = json.loads(json_records)
    
    """
    Result Data
    """
    result_X_train = len(X_train)
    result_Y_train = len(y_train)
    result_X_test = len(X_test)
    result_X_test = len(y_test)
    accuracy = accuracy_score(y_test,y_pediksi)

    """
    Input Data
    """
    have_data = False
    data_predik = {}
    if request.method == 'POST':
        input_data = {
            "jenis_kelamin": request.POST.get('jenis_kelamin'),
            "status": request.POST.get('status'),
            "pendapatan_pertahun": request.POST.get('pendapatan_pertahun')
        }
        data_predik = pd.DataFrame(input_data, index=[0])
        y_predik = model_NB.predict(data_predik)
        data_predik['label'] = y_predik
        have_data = True
        json_records = data_predik.reset_index().to_json(orient ='records')
        data_predik = []
        data_predik = json.loads(json_records)
    
    context = {
        'title': 'SHOW DATA ML',
        'data': data_excel,
        'result_X_train': result_X_train,
        'result_Y_train': result_Y_train,
        'result_X_test': result_X_test,
        'result_Y_test': result_X_test,
        'accuracy': accuracy,
        'data_predik': data_predik,
        'have_data': have_data,
    }
    return render(request, 'index.html', context)