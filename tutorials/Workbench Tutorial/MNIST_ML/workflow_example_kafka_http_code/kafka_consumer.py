import argparse

import numpy as np

from kafka import KafkaConsumer
import json

import cv2

import logging

logging.basicConfig(level=logging.INFO)


def main(args):
    url = '%s:%d'%(args.ip, args.port)
    print(url)
    consumer = KafkaConsumer(args.topic,
                             group_id=args.groupid,
                             bootstrap_servers=[url])

    print('[begin] get consumer list')

    for message in consumer:

        # print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" %
        #       ( message.topic, message.partition, message.offset, message.key, message.value ))

        data = message.value
        data = data.decode()
        data = json.loads(data)

        print(data)
        # if len(data.keys()) != 2:
        #     print(data)
        #     continue
        #
        # for key in data.keys():
        #     if key == "images":
        #         image_array = data[key]
        #     else:
        #         label = data[key]
        #
        # image_array = np.reshape(image_array, (28,28))
        # image_array = cv2.resize(image_array, (500,500))
        #
        # label = np.argmax(label)
        #
        # cv2.putText(image_array, "label : %d" % (label),
        #             org=(370, 20),
        #             fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        #             fontScale=.8,
        #             color=(255, 255, 255),
        #             thickness=1,
        #             lineType=cv2.LINE_8,
        #             )
        # cv2.imshow("kafka_consumer", image_array)
        # c = cv2.waitKey(1)
        # # if c & 0xFF == ord('q'):
        # #     break

    print('[end] get consumer list')


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
                        default="mnist_output")
    parser.add_argument("--groupid",
                        type=str,
                        default="mnist_output")

    args = parser.parse_args()

    main(args)
