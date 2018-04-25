#PARTE1
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

#PARTE2
app = Flask(__name__)


#PARTE3
@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    #PARTE1
    html_doc = urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    #PARTE2
    data = []

    for dataBox in soup.find_all("div",class_="card card-entity card-entity-list cf"):
        nomeObj = dataBox.find("h2", class_="meta-title").find("a", class_="meta-title-link")
        # imgObj = dataBox.find(class_="img_side_content")
        # sinopseObj = dataBox.find("div", class_="content").find("p")
        # dataObj = dataBox.find("ul", class_="list_item_p2v tab_col_first").find("div", class_="oflow_a")


        #PARTE3
        # data.append({'nome': nomeObj.text.strip(),
        #              'poster': imgObj.img['src'].strip(),
        #              'sinopse': sinopseObj.text.strip(),
        #              'data': dataObj.text.strip()})
        data.append({'nome': nomeObj.text.strip()})

    return jsonify({'filmes': data})


#PARTE4
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
