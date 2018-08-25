import os
from flask import Flask,render_template,request
from flask_uploads import UploadSet, configure_uploads,ALL

app=Flask(__name__)

videos= UploadSet('videos',ALL)

app.config['UPLOADED_VIDEOS_DEST']='static'
configure_uploads(app,videos)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST' and 'video' in request.files:
        filename=videos.save(request.files['video'])
        return render_template('test.html')


@app.route('/splitVideo',methods=['GET','POST'])
def send():
    if request.method=='POST':
        os.system('python vidToScreenshots.py')
        return "Done"

@app.route('/trackMovement',methods=['GET','POST'])
def sending():
    if request.method=='POST':
        os.system('python testscript.py')
        return "Done"

if __name__=="__main__":
    app.run()
