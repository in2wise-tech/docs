import argparse

import numpy as np
import random

from kafka import KafkaProducer # pip install kafka-python
import json

import cv2

import logging

logging.basicConfig(level=logging.INFO)


def main(args):
    data = np.load("mnist_test.npy")
    data_size = len(data)

    seed = 0
    random.seed(seed)

    kafka_servers = '%s:%d'%(args.ip, args.port)
    topic = args.topic
    producer = KafkaProducer(bootstrap_servers=kafka_servers, api_version=(0, 10, 1))
    # producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(0, 10, 1))
    while True:
        idx = random.randrange(0, data_size)
        image_array = data[idx,:]
        label = image_array[0]
        image_array = image_array[1:]

        item = {
            "images": list(image_array)
        }

        js = json.dumps(item)

        producer.send(topic, js.encode())
        image_array = np.reshape(image_array, (28,28))
        image_array = cv2.resize(image_array, (500,500))

        cv2.putText(image_array, "label : %d"%(label),
                    org=(370,20),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=.8,
                    color=(255,255,255),
                    thickness=1,
                    lineType=cv2.LINE_8,
                    )
        cv2.imshow("kafka_producer", image_array)
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
                        default=9092)
    parser.add_argument("--topic",
                        type=str,
                        default="mnist_input")
    parser.add_argument("--groupid",
                        type=str,
                        default="mnist_input")

    args = parser.parse_args()

    main(args)
