from flask import Flask, render_template, jsonify, request, json
app = Flask(__name__)

from pymongo import MongoClient
import certifi

client = MongoClient('mongodb+srv://sparta:test@sparta.mw5zmbb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())

db = client.dbsparta

@app.route('/')
def home():
    getInfo = list(db.info.find({}, {'_id':False}))
    return render_template('index.html', info=getInfo)

@app.route('/sendEmail')
def contact():
    return render_template('sendEmail.html')

@app.route('/comment')
def comment():
    return render_template('comment.html')

# comment
@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    group_receive = request.form['group_give']
    doc={
        'name':name_receive,
        'comment':comment_receive,
        'group':group_receive
    }
    db.fanm.insert_one(doc)

    return jsonify({'msg': '응원 저장 완료'})

@app.route('/guestbook', methods=['GET'])
def guestbook_get():
    all_fan = list(db.fanm.find({}, {'_id':False}))
    return jsonify({'result': all_fan})

@app.route('/guestbook', methods=['DELETE'])
def guestbook_delete():

    
    all_fan = list(db.fanm.find({}, {'_id':False}))
    return jsonify({'result': all_fan})


@app.route('/detail')
def detail():
    query = request.args.get('query')
    getInfo = list(db.info.find({'name':query}, {'_id':False}))

    return render_template('detail.html', info=getInfo)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5501, debug=True)