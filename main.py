import cv2
from camera.camera_stream import get_frame
from detection.yolo_detection import detect_objects, classes
from navigation.simple_controller import control_vehicle
from navigation.avoid_obstacle import avoid
from utils.image_processing import preprocess

for frame in get_frame():

    processed = preprocess(frame)

    boxes, class_ids, confs = detect_objects(processed)

    obstacle = False

    for i, box in enumerate(boxes):
        x, y, w, h = box
        label = classes[class_ids[i]]

        if label in ["person", "car", "truck", "bus", "motorbike"]:
            obstacle = True

        cv2.rectangle(processed, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(processed, label, (x, y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    action = control_vehicle(obstacle)
    avoid_dir = avoid(obstacle)

    cv2.putText(processed, f"Action: {action}", (10, 420),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.putText(processed, f"Avoid: {avoid_dir}", (10, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow("Autonomous Vehicle System", processed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
