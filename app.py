from flask import Flask, render_template, request, Response, redirect, abort, url_for, json

app=Flask(__name__)


@app.route('/display')
def lane():
    with open('button_info.json','r') as button_info:
        info=json.load(button_info)
        button_info.close()
        return render_template('lane.html', value=info['bay'], lane=info['lane'])
    
@app.route('/commendPLC/<lane>/<bay>')
def commendPLC(lane,bay):
    with open("button_info.json", "w") as button_info:
        a_dict={"bay":bay,"lane":lane}
        button_info_json=json.dumps(a_dict)
        button_info.write(button_info_json)
        button_info.close()
        return Response('200')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
