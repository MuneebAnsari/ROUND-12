import os
from flask import Flask,render_template,request,url_for
from flask_uploads import UploadSet, configure_uploads,ALL

app=Flask(__name__)

videos= UploadSet('videos',ALL)

app.config['UPLOADED_VIDEOS_DEST']='./'
configure_uploads(app,videos)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST' and 'video' in request.files:
        filename=videos.save(request.files['video'])
        os.system('python vidToScreenshots.py --vidName='+filename)
        return render_template('uploadComplete.html')


@app.route('/splitVideo',methods=['GET','POST'])
def send():
    if request.method=='POST':
        os.system('python vidToScreenshots.py --vidName=')
        return "Done"

@app.route('/trackMovement',methods=['GET','POST'])
def sending():
    if request.method=='POST':
        os.system('python testscript.py')
        os.system('python guard_hand_feedback.py')
        guard_hand_file = open("./feedback_guard_hand.txt", "r")
        var =guard_hand_file.readline()
        os.system('python neck_torso_feedback.py')
        guard_hand_file = open("./feedback_neck_torso.txt", "r")
        var2 =guard_hand_file.readline()
        return render_template('finalPage.html',variable=var,variable2=var2)

@app.route('/getGuardInfo',methods=['GET','POST'])
def getGuardStatus():
    if request.method=='POST':
        os.system('python guard_hand_feedback.py')
        guard_hand_file = open("./feedback_guard_hand.txt", "r")
        var =guard_hand_file.readline()
        return render_template('finalPage.html',variable=var)

if __name__=="__main__":
    app.run()
