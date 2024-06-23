import json
from flask import Flask
from flask_cors import cross_origin
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd

pca = PCA()
kmeans = KMeans(n_clusters=6)
app = Flask(__name__)


with open('testdata.json') as f:
    d = json.load(f)
jsondata=json.dumps(d)
print(pd.DataFrame(d["rerations"]))
relation_matrix=[[0 for i in d["profile_datas"]] for i in d["profile_datas"]]



@app.route("/")
# @cross_origin(origins=["http://localhost:5173"], methods=["GET"])
def index():
    """ ブラウザに「Hello World」と表示 """
    return "Hello World"

@app.route("/json")
@cross_origin(origins=["http://localhost:5173"], methods=["GET"])
def hello_world():
    with open('testdata.json') as f:
        d = json.load(f)
    jsondata=json.dumps(d)
    return jsondata

if __name__ == '__main__':
  app.run(port=8080, debug=True)