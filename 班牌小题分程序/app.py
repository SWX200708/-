from flask import *
from flask_bootstrap import Bootstrap
import sqlite3
import time
from werkzeug.utils import secure_filename
from datetime import *
from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from sqlite3 import *
import pandas as pd
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)
app.config['UPLOAD_FOLDER'] = 'upload/'


Bootstrap(app)
Accordion_dic={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six'}
Rate_dic={'0':'Administrator','1':"年级组长","2":"班主任",'3':'学生'}
username = ""
conn_Test=sqlite3.connect("test.sqlite",check_same_thread=False)
cur_Test=conn_Test.cursor()

def changefile(path,Grade):
    pd.read_excel()


@app.route('/')
def index():
    return redirect(url_for('score'))

# ------------------------------------------------------------

@app.route('/EA',methods=['GET','POST'])
def EA():
    return render_template("Nav.html")


# ------------------------------------------------------------

@app.route('/EA/upload',methods=['GET','POST'])
def upload():
    if request.method=='GET':
        return render_template("Upload.html")
    if request.method=='POST':
        File_upload = request.files['File']
        Subject = request.values.get("考试科目")
        Grade = request.values.get("年级")
        
        Filename=secure_filename(File_upload.filename)
        File_upload.save(os.path.join('/upload',Filename))

# ------------------------------------------------------------
@app.route('/score',methods=['GET','POST'])
def score():
    Name=session.get('Name')
    Grade=session.get('Grade')

    TestTime=[]
    TestName=[]
    cur_Test.execute(f'SELECT * FROM Test Where Grade = 1')
    res = cur_Test.fetchall()
    for i in res:
        TestTime.append(i[1])
        TestName.append(i[2])
    group=[i for  i in range(len(TestName))]

    

    if request.method=='GET':
        return render_template('score.html',TestTime=TestTime[::-1],TestName=TestName[::-1],group=group)

    if request.method=='POST':
        for i in TestName:
            RequestSubject=request.values.get(i)
            if RequestSubject != None:
                RequestTest = i 
                break
        




# ------------------------------------------------------------
if __name__ == '__main__':
    app.run("0.0.0.0", 12564, debug=True)
