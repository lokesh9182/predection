from django.shortcuts import render,HttpResponse
from cropapp import models

# Create your views here.
 
def home(request):
    context={"crops":1, 'status':False}
    if request.method=='POST':
        n=int(request.POST.get('n'))
        pho=int(request.POST.get('pho'))
        pot=int(request.POST.get('pot'))
        t=int(request.POST.get('t'))
        h=int(request.POST.get('h'))
        ph=int(request.POST.get('ph'))
        r=float(request.POST.get('r'))
        print('!!!!!!----------------!!!!!!!!--------',n,pho,pot,t,h,ph,r)
        ud=[n,pho,pot,t,h,ph,r]
        #print(ud)
 
        # Machine Learning alogorithm---------------------------
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt


        dataset=pd.read_excel('crop.xlsx')
        data=dataset.iloc[:,:-1].values
        crops=set(dataset.iloc[:,-1].values)

        from sklearn.cluster import KMeans

        # elbow=[]
        # for i in range(1,11):    
        #     cluster=KMeans(n_clusters=i,init='k-means++', max_iter=300, random_state=0,n_init=10 )
        #     cluster.fit(data)
        #     elbow.append(cluster.inertia_)

        # plt.plot(range(1,11),elbow)


        cluster=KMeans(n_clusters=4,init='k-means++',max_iter=300,n_init=10,random_state=0)
        y=cluster.fit_predict(data)
        #ud=[3,72,24,36.5,57.9,6,122]
        userdata=[ud,]
        #userdata=[[3,72,24,36.5,57.9,6,122],]
        test=np.array(userdata)
        k=cluster.predict(test)
        recom_crops=list(set(dataset.iloc[:,:].values[y==k,-1]))
        print(recom_crops)
        context={"crops":recom_crops, 'status':True}

    return render(request,'home.html',context)



def contact(request):
    status=False
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        disc=request.POST.get('desc')
        print('---------------------------------------------', request.method,name,age,phone,disc)
        instnce=models.farmer(e_name=name,e_age=age,e_phone=phone,e_desc=disc)
        instnce.save()
        dic={'success':True}
        return render(request,'contact.html',dic)
    return render(request,'contact.html')