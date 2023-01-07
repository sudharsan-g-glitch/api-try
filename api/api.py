from flask import Flask,jsonify,request
app=Flask(__name__)

outputs=[{'Output':{''}}]

@app.route('/ocr',methods=['POST'])
def images():
    data=request.get_json()
    uid=data['uid']
    b64=data['b64']
    return jsonify({'Messageee':'Okayy','uid':uid,'b64':b64})

@app.route('/',methods=['GET'])
def returnTwo():
    
    return jsonify({'Message':'Works'})


if __name__=='__main__':
    app.run(debug=True,port=8080)