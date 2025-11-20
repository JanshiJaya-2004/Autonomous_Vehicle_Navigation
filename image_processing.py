import cv2

def preprocess(frame):
    frame = cv2.resize(frame, (416,416))
    return frame
