from django.shortcuts import render

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import tuple_factory


def subset_dic(subset, superset):
    return len(set(subset.items()) & set(superset.items())) == len(subset)
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def help(request):
    cloud_config={
    'secure_connect_bundle': 'V:\Hackathon\Hackathon\secure-connect-unisupportdb.zip'
    }

    auth_provider=PlainTextAuthProvider('unisupportdb','supersecurepassword')
    cluster=Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session=cluster.connect()

    session.row_factory = tuple_factory
    try:
        row = session.execute("SELECT senderid, senderusername, messagecontent from unisupport.messages WHERE receiverid = 2 ALLOW FILTERING;")
    except:
        row=[]
    contacts=[]

    row=reversed(list(row))

    for user_row in row:
        inContacts=False
        addRow={'id':user_row[0], 'name':user_row[1], 'content':user_row[2]}
        for i in range(len(contacts)):
            if subset_dic({'id':user_row[0], 'name':user_row[1]}, contacts[i]):
                inContacts=True
        if inContacts==False:
            contacts.append(addRow)
        print(user_row)
    print(contacts)
    #print("dingdong")
    return render(request, 'help.html', {'users':contacts})


def login(request):
    return render(request, 'login.html')


def search(request):
    return render(request, 'search.html')


def signup(request):
    return render(request, 'signup.html')


def terms(request):
    return render(request, 'terms.html')
