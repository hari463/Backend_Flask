from flask import Flask, jsonify, request
import sample

app =Flask(__name__)

@app.get('/')
def getmethod():
    data=sample.getdetail();
    details_list=[]
    for details in data:
        contest={}
        contest={'id':details[0],'name':details[1],'department':details[2]};
        details_list.append(contest);
    return jsonify(details_list);

@app.post("/post")
def postmethod():
    data =request.get_json();
    sample.insertdetails(data)
    return("we have got your data")

@app.patch("/upd")
def updateFunc():
    data = request.get_json();
    print("--data--");
    sample.upd(data);
    return("Got Updated");

@app.delete("/del/<id>")
def delfunc(id):
    sample.deleteStu(id);
    return("Deleted");

if __name__=='__main__':
    app.run(debug=True,port=1000)
