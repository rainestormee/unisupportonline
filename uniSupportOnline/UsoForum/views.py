import hashlib
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.query import tuple_factory
import re
import os
from django.shortcuts import render

cloud_config = {
    'secure_connect_bundle': os.path.join(os.path.realpath(os.path.dirname(__file__)),
                                          'secure-connect-unisupportdb.zip')
}

auth_provider = PlainTextAuthProvider('unisupportdb', 'supersecurepassword')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.row_factory = tuple_factory


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
    try:
        otherPerson = request.GET['foo']
        otherPerson = int(otherPerson)
    except BaseException:
        otherPerson = 3
    try:
        row = session.execute("SELECT senderid, senderusername, messagecontent, sent_at from unisupport.messages WHERE receiverid = 2 ALLOW FILTERING;")
        row = sorted(row, key=lambda x: x[3])
    except BaseException:
        row = []
    contacts = []

    row = reversed(list(row))

    for user_row in row:
        inContacts = False
        addRow = {'id': user_row[0], 'name': user_row[1], 'content': user_row[2], 'timestamp': user_row[3]}
        for i in range(len(contacts)):
            if subset_dic({'id': user_row[0], 'name': user_row[1]}, contacts[i]):
                inContacts = True
        if not inContacts:
            contacts.append(addRow)
        print(user_row)

    loggedInUser = session.execute(
        "select * from unisupport.messages WHERE receiverid = 2 and senderid = %s ALLOW FILTERING;", [otherPerson])

    otherUser = session.execute(
        "select * from unisupport.messages WHERE receiverid = %s and senderid = 2 ALLOW FILTERING;", [otherPerson])

    displayUser = session.execute("SELECT username FROM unisupport.users WHERE userid = %s ALLOW FILTERING;", [otherPerson])


    # sender #receiver #time #message

    messages = []
    for i in loggedInUser:
        messages.append({"sender": i[4], "receiver": i[6],
                         "time": i[1], "message": i[2]})

    for i in otherUser:
        messages.append({"sender": i[4], "receiver": i[6],
                         "time": i[1], "message": i[2]})

    messages = reversed(sorted(messages, key=lambda x: x['time']))
    return render(request, 'help.html', {'users': contacts, 'messages': messages, 'displayUser': displayUser})


def login(request):
    return render(request, 'login.html')


def loginCode(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password = hashlib.sha512(password.encode()).hexdigest()

    row = session.execute(
        "SELECT username, password FROM unisupport.users where username = %s AND password = %s ALLOW FILTERING;",
        [username, password])
    if not row:
        response = {"bool": False, "user": "", "message": "You are not logged in."}

    else:
        response = {"bool": True, "user": username, "message": "You are logged in as " + username}

    request.session['member_id'] = username

    return render(request, 'login.html', {'response': response})

    # DO LOGIN STUFF HERE OR PARSE VALUES WHERE YOU WANT


def search(request):
    return render(request, 'search.html')


def signup(request):
    return render(request, 'signup.html')

def validateEmail(email):
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(regex, email):
        return False
    else:
        return True

def validateUsername(username):
    try:
        username = username.encode('ascii', 'strict').decode()
    except:
        return False
    row = session.execute("SELECT username FROM unisupport.users where username = %s ALLOW FILTERING;",[username])
    if not row:
        return True
    else:
        return False

def validatePassword(password):
    try:
        return password.encode("ascii", 'strict')
    except:
        return None

def signupCode(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    email=request.POST.get('email')
    
    if(validateEmail(email) and validatePassword(password) is not None and validateUsername(username) is True):
        username = username.encode('ascii', 'strict').decode()
        password = validatePassword(password)
        password=hashlib.sha512(password).hexdigest()
        row = session.execute('SELECT MAX(userid) AS max FROM unisupport.users')
        userid = row[0][0] + 1
        row = session.execute("INSERT INTO unisupport.users (userid, accounttype, email, password, username) VALUES (%s, %s, %s, %s, %s);",[userid, 'User', email, password, username])
        response={"bool": True, "user": username, "message": "Succesfully signed up as "+username}
    else:
        response = {"bool": False, "user": "", "message": "Unsuccesfully signed up."}

    return render(request, 'signup.html', {'response': response})

def terms(request):
    return render(request, 'terms.html')

def discussions(request):
    return render(request, 'discussions.html')
