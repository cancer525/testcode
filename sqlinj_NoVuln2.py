from django.db import connection

def user_contacts(request):
    user = request.GET['username']
    sql = "SELECT * FROM user_contacts WHERE username = %s;"
    cursor = connection.cursor()
    
    user = test_func(untainted);
    cursor.execute(sql, user)
    # ... do something with the results

user_contacts(a);
