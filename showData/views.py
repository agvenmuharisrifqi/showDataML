from django.shortcuts import render
from django.conf import settings
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import json
from sklearn import feature_selection as fs
from sklearn.linear_model import LogisticRegression


def index(request):
    df=pd.read_excel(settings.BASE_DIR / 'MachineLearning/FIX Data Minat Nasabah excel.xlsx')
    df['label'].replace({2:0},inplace=True)
    y = df.loc[:, ['label']]
    
    # Not selection
    x = df.loc[:, ['jenis_kelamin', 'status','usia','pekerjaan','pendapatan_pertahun','produk']]
    
    # Selection
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
    

    """


result_X_train = len(X_train2)
result_Y_train = len(y_train2)
result_X_test = len(X_test2)
result_X_test = len(y_test2)
accuracy = accuracy_score(y_test2,y_pediksi2)
    

    """
    Result Data
    """
    model_ls = LogisticRegression(max_iter=15)
    rfe = fs.RFE(model_ls)
    rfe.fit(x,y)
    print(f'Support = {rfe.support_}')#tampilkan 
    print(f'Ranking = {rfe.ranking_}') #ampilkan 
    result_X_train = len(X_train)
    result_Y_train = len(y_train)
    result_X_test = len(X_test)
    result_X_test = len(y_test)
    accuracy = accuracy_score(y_test,y_pediksi)



    """
    Selection Fiture
    """
    have_data = False
    selection = None
    data_predik = {}
    if request.method == 'POST':
        selection = True
        check_selection = request.POST.get('selection')
        input_data = {
            "jenis_kelamin": request.POST.get('jenis_kelamin'),
            "status": request.POST.get('status'),
            "pendapatan_pertahun": request.POST.get('pendapatan_pertahun')
        }
        if check_selection == 'not_selection':
            """
            Saya ganti dari x1 menjadi x
            """
            X_train, X_test, y_train, y_test = train_test_split(x,y,test_size = 0.1,random_state=30,train_size=None,shuffle=True,stratify=None)
            #X_train2, X_test2, y_train2, y_test2 = train_test_split(x,y,test_size = 0.1,random_state=30,train_size=None,shuffle=True,stratify=None)
            model_NB=GaussianNB()
            model_NB.fit(X_train,y_train)
            input_data['usia'] = request.POST.get('usia')
            input_data['pekerjaan'] = request.POST.get('pekerjaan')
            input_data['produk'] = request.POST.get('produk')
            selection = False
        data_predik = pd.DataFrame(input_data, index=[0])
        y_predik = model_NB.predict(data_predik)
        data_predik['label'] = y_predik
        json_records = data_predik.reset_index().to_json(orient ='records')
        data_predik = []
        data_predik = json.loads(json_records)
        have_data = True
    
    
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
        'selection': selection
    }
    return render(request, 'index.html', context)