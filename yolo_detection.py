import cv2
import numpy as np
import os

# ---- AUTO PATH FIX (no more errors) ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_CFG = os.path.join(BASE_DIR, "yolo_weights/yolov3.cfg")
MODEL_WEIGHTS = os.path.join(BASE_DIR, "yolo_weights/yolov3.weights")
COCO_NAMES = os.path.join(BASE_DIR, "yolo_weights/coco.names")

# Load YOLO model
net = cv2.dnn.readNetFromDarknet(MODEL_CFG, MODEL_WEIGHTS)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1][0] if isinstance(i, np.ndarray) else layer_names[i - 1]
                 for i in net.getUnconnectedOutLayers()]
classes = open(COCO_NAMES).read().strip().split("\n")


def detect_objects(frame):
    """Returns the processed frame with drawn YOLO detections"""
    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    boxes = []
    class_ids = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]

            if conf > 0.5:
                cx, cy, bw, bh = det[0:4] * np.array([w, h, w, h])
                x = int(cx - bw/2)
                y = int(cy - bh/2)

                boxes.append([x, y, int(bw), int(bh)])
                class_ids.append(class_id)
                confs.append(float(conf))

    # APPLY NON-MAX SUPPRESSION
    indices = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)

    # DRAW DETECTIONS ON FRAME
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, bw, bh = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confs[i]

            cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

    return frame   #  return image only (numpy array)
