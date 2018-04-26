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
        imgObj = dataBox.find("figure", class_="thumbnail")
        sinopseObj = dataBox.find("div", class_="synopsis")
        dataObj = dataBox.find("div", class_="meta-body").find("div", class_="meta-body-item meta-body-info")\
            .find("span", class_="date")


        #PARTE3
        data.append({'nome': nomeObj.text.strip(),
                     'poster': imgObj.img['data-src'].strip(),
                     'sinopse': sinopseObj.text.strip(),
                     'data': dataObj.text.strip()})

    return jsonify({'filmes': data})


#PARTE4
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # app.run(host='127.0.0.1', port=port)

    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='0.0.0.0', port=port)
