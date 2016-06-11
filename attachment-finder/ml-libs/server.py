from __future__ import print_function

import json

from flask import Flask
from flask import Response
from flask import request

import logic
import utils.nl_api as nl

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        sentence = str(request.args['q'])
        print('Received text = {}'.format(sentence))
        nl_api_element = nl.call_nl_api(sentence)
        print('[NL API] element = {}'.format(nl_api_element))
        predicted_query = logic.build_query(nl_api_element)
        print('[Logic] predicted query = {}'.format(predicted_query))

        out = {'query': predicted_query,
               'nl_api': nl_api_element}
        ret = json.dumps(out)
    except Exception:
        ret = 'Hit the endpoint like this http://127.0.0.1:5000?q=TEXT'

    resp = Response(ret)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0')
