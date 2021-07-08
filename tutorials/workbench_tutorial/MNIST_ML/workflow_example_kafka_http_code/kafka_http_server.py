import argparse
import json
import numpy as np

from flask import Flask, request, make_response, jsonify

import logging
logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--ip",
                    type=str,
                    default="192.168.0.108")
parser.add_argument("--port",
                    type=int,
                    default=8088)
parser.add_argument("--path",
                    type=str,
                    default="/mnist_kafka_http/output")
args = parser.parse_args()

app = Flask(__name__)


@app.route(args.path, methods=['GET', 'POST', 'PUT', 'DELETE'])
def mnist():
    if request.method == 'POST':
        # print('POST')
        data = request.data
        data = data.decode()
        data = json.loads(data)
        print(data)
        # if len(data.keys()) != 2:
        #     print(data)
        #     return
        #
        # for key in data.keys():
        #     if key == "images":
        #         pass
        #     else:
        #         label = data[key]
        #
        # label = np.argmax(label)
        # print("Result : ", label)

    else:
        print(request.method)

    return make_response(jsonify({'status': True}), 200)


if __name__ == '__main__':
    app.run(host=args.ip, port=args.port, debug=True)
