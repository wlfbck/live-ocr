import cv2
from pytesseract import image_to_string
import threading

import imagecapture
import config

import tempfile
import os

import zmq

# https://stackoverflow.com/questions/65839969/how-can-i-extract-numbers-from-video-frames-using-tesseract-ocr
def get_text(path):
    img = cv2.imread(path)
    # hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # h, s, v = cv2.split(hsv_img)
    # v = cv2.GaussianBlur(v, (1, 1), 0)
    # thresh = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(1, 2))
    # thresh = cv2.dilate(thresh, kernel)
    # txt = image_to_string(thresh)
    txt = image_to_string(img)
    return txt


def scan():
    # need to it this way because python sucks
    filename = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
    imagecapture.getImage(config.upper_left_x,
                          config.upper_left_y,
                          config.lower_right_x - config.upper_left_x,
                          config.lower_right_y - config.upper_left_y,
                          filename)
    text = get_text(filename)
    print(text)

    # delete the tempfile, otherwise we fill our drive
    os.remove(filename)
    return text


# https://stackoverflow.com/questions/69017296/python-if-condition-with-while-true-infinite-loop-conflict
class AlwaysThread(threading.Thread):
    server_socket = None
    context = zmq.Context()

    def __init__(self):
        super(AlwaysThread, self).__init__()
        self.stopThread = False
        self.server_socket = self.context.socket(zmq.REQ)
        address = "tcp://" + config.host + ":" + str(config.port)
        print("connection to " + address)
        self.server_socket.connect("tcp://" + config.host + ":" + str(config.port))

    def run(self):
        self.stopThread = False
        while not self.stopThread:
            text = scan()
            if not text:
                continue
            print("sending text")
            self.server_socket.send(str.encode(text))
            # we dont care what we get, but the ack tells us everything is fine
            self.server_socket.recv()
            print("ack received, continuing")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("running")

    # where you previously have done the endless loop
    t = AlwaysThread()
    t.start()

    # stop it with t.stopThread = True
    print("always thread started")
