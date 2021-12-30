from flask import Flask, render_template, request
import jsonify
import requests
import pickle
app = Flask(__name__)
model = pickle.load(open('random_forest.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    inp = request.form["link"]
    new_url = urlparse(inp)
    if not new_url.netloc:
        return None
    query_dict = parse_qs(new_url[4])
    query_dict['tag'] = "krishnaventur-21"
    new_url = new_url[:4] + (urlencode(query_dict, True), ) + new_url[5:]
    return redirect(prediction)
if __name__=="__main__":
    app.run(debug=True)
