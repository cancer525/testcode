import cgi,sys,cgitb,time,os,sys
import md5
import hashlib

cgitb.enable()
import _mysqlTest

print "Content-type:text/html\n"
print ''
print '''
    <html>
        <head>            
        </head>
        <body>
        The present time is %s
        <form action="%s" method="post">
            用户名: <input type="text" name="user" size="12" />
            密码: <input type="password" name="passwd" size="12" />
            <INPUT TYPE="submit" NAME="login" VALUE="Submit">
        </FORM>
        </BODY>
    </HTML>
      '''% (time.strftime(" %Z [ %I:%M:%S %P ] "),os.environ['SCRIPT_NAME'])


def checkUserToBe (sql):
    db = _mysqlTest.DBbase()
    res= db.querySQL(sql)
    if res:
        print("<script>alert('登陆成功');</script>")
        return True
    else:
        print("<script>alert('登陆失败');</script>")
        return False
   
def saveUserInfo ():
    print('in..')
   

def createQuerySQL(username,passwd):
    m = md5.new()
    m.update(passwd)
    passwd = m.hexdigest()
    sql = "select * from `workuser` where `w_Phone`='%s' and `w_Pwd`='%s'"%(username,passwd)
    return sql
   
form = cgi.FieldStorage()
if form.getfirst('user') and  form.getfirst('passwd'):
    if checkUserToBe(createQuerySQL(form.getfirst('user'),form.getfirst('passwd'))):
        saveUserInfo()
    else:
        print('运行错误返回')
