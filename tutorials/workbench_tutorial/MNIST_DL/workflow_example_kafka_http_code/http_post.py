import argparse

import numpy as np
import random

import requests
import json

import cv2

import logging

logging.basicConfig(level=logging.INFO)


def main(args):

    data = np.load("mnist_test.npy")
    data_size = len(data)

    seed = 0
    random.seed(seed)

    url = "http://%s:%d"%(args.ip, args.port)

    while True:
        idx = random.randrange(0, data_size)
        image_array = data[idx,:]
        label = image_array[0]
        image_array = image_array[1:]

        item = {
            "images": list(image_array)
        }

        js = json.dumps(item)

        headers ={'Content-Type': 'application/json'}
        resp = requests.post(url, headers = headers, data=js)
        
        image_array = np.reshape(image_array, (28,28))
        image_array = cv2.resize(image_array, (500,500))
        cv2.putText(image_array, "resp : %s" % (resp.text),
                    org=(0, 480),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=.8,
                    color=(255, 255, 255),
                    thickness=1,
                    lineType=cv2.LINE_8,
                    )
        cv2.putText(image_array, "label : %d"%(label),
                    org=(370,20),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=.8,
                    color=(255,255,255),
                    thickness=1,
                    lineType=cv2.LINE_8,
                    )
        cv2.imshow("http_post", image_array)
        c = cv2.waitKey(0)
        if c & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        type=str,
                        default="39.119.108.174")
    parser.add_argument("--port",
                        type=int,
                        default=53012)
    args = parser.parse_args()

    main(args)
