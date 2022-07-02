from django.shortcuts import redirect, render
from django.conf import settings
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import feature_selection as fs
import pandas as pd
import json


def index(request):
    df=pd.read_excel(settings.BASE_DIR / 'MachineLearning/FIX Data Minat Nasabah excel.xlsx')
    df['label'].replace({2:0},inplace=True)
    y = df.loc[:, ['label']]
    
    # Selection x1
    x1= df.loc[:, [ 'jenis_kelamin','status','pendapatan_pertahun']]
    
    # Not selection x2
    x2 = df.loc[:, ['jenis_kelamin', 'status','usia','pekerjaan','pendapatan_pertahun','produk']]
    
    # Selection x1
    X1_train, X1_test, y1_train, y1_test = train_test_split(x1,y,test_size = 0.1,random_state=30,train_size=None,shuffle=True,stratify=None)
    model_NB1=GaussianNB()
    model_NB1.fit(X1_train,y1_train)
    y1_pediksi=model_NB1.predict(X1_test)

    # Not selection x2
    X2_train, X2_test, y2_train, y2_test = train_test_split(x2,y,test_size = 0.1,random_state=30,train_size=None,shuffle=True,stratify=None)
    model_NB2=GaussianNB()
    model_NB2.fit(X2_train,y2_train)
    y2_pediksi=model_NB2.predict(X2_test)


    # Feature Selection
    model_ls = LogisticRegression(max_iter=15)
    rfe = fs.RFE(model_ls)
    rfe.fit(x2,y)
    support = rfe.support_
    ranking = rfe.ranking_

    """
    Read Data
    """
    json_records = df.reset_index().to_json(orient ='records')
    data_excel = []
    data_excel = json.loads(json_records)
    
    """
    Result Data
    """
    # Selection x1
    result1 = {
        'result_X_train': len(X1_train),
        'result_Y_train': len(y1_train),
        'result_X_test': len(X1_test),
        'result_Y_test': len(y1_test),
        'accuracy': accuracy_score(y1_test,y1_pediksi),
    }

    # Not selection x2
    result2 = {
        'result_X_train': len(X2_train),
        'result_Y_train': len(y2_train),
        'result_X_test': len(X2_test),
        'result_Y_test': len(y2_test),
        'accuracy': accuracy_score(y2_test,y2_pediksi),
    }
    
    """
    Selection Feature
    """
    have_data = False
    selection = None
    data_predik = {}
    if request.method == 'POST':
        check_selection = request.POST.get('selection')
        if check_selection == 'selection':
            input_data = {
                "jenis_kelamin": request.POST.get('jenis_kelamin'),
                "status": request.POST.get('status'),
                "pendapatan_pertahun": request.POST.get('pendapatan_pertahun')
            }
            data_predik = pd.DataFrame(input_data, index=[0])
            y_predik = model_NB1.predict(data_predik)
            selection = True
        else:
            input_data = {
                "jenis_kelamin": request.POST.get('jenis_kelamin'),
                "status": request.POST.get('status'),
                "pendapatan_pertahun": request.POST.get('pendapatan_pertahun'),
                'usia': request.POST.get('usia'),
                'pekerjaan': request.POST.get('pekerjaan'),
                'produk': request.POST.get('produk'),
            }
            data_predik = pd.DataFrame(input_data, index=[0])
            y_predik = model_NB2.predict(data_predik)
            selection = False
        data_predik['label'] = y_predik
        json_records = data_predik.reset_index().to_json(orient ='records')
        data_predik = []
        data_predik = json.loads(json_records)
        have_data = True
    context = {
        'title': 'SHOW DATA ML',
        'data': data_excel,
        'support': support,
        'ranking': ranking,
        'result1': result1,
        'result2': result2,
        'data_predik': data_predik,
        'have_data': have_data,
        'selection': selection,
    }
    return render(request, 'index.html', context)