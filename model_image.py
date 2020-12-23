import pickle
import cv2
import dlib
import numpy as np

FACE_DESC, FACE_NAME = pickle.load(open('log/trainset.pk', 'rb'))
face_detector = cv2.CascadeClassifier('model_image/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("model_image/haarcascade_eye.xml")
detector = dlib.get_frontal_face_detector()  # dlib(bettle), openCV
sp = dlib.shape_predictor('model_image/shape_predictor_68_face_landmarks.dat')  # shape_landmark Detection
model = dlib.face_recognition_model_v1('model_image/dlib_face_recognition_resnet_model_v1.dat')  # buil model
smile_cascade = cv2.CascadeClassifier("model_image/haarcascade_smile.xml")

path_yolo = 'yolo-coco/yolov3-tiny.weights'
path_cfg = 'yolo-coco/yolov3-tiny.cfg'
net = cv2.dnn.readNet(path_yolo, path_cfg)
classes = []
with open("yolo-coco/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


def webdlib(cap):
    ret, img = cap.read()
    scale = 0.5
    img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    height, width, channels = img.shape
    name_app = []
    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, .7, color, 2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    for d in dets:
        xy = d.left(), d.top()
        wh = d.right(), d.bottom()
        shape = sp(img, d)
        face_desc0 = model.compute_face_descriptor(img, shape, 1)  # output deeplearning
        d = []
        for face_desc in FACE_DESC:
            d.append(np.linalg.norm(np.array(face_desc) - np.array(face_desc0)))
        d = np.array(d)  # compare picture
        idx = np.argmin(d)  # ระบุลาเบล
        # print(d[idx])
        if d[idx] <= 0.49:
            name = FACE_NAME[idx]
            name = str(name)
            # print(name)
            # print(name_api)
            name_app.append(name)
            cv2.putText(img, name, (xy[0], xy[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.rectangle(img, xy, wh, (0, 255, 0), 2)
        else:
            name = 'Unknown'
            # print(name)
            name_app.append(name)
            cv2.putText(img, name, (xy[0], xy[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.rectangle(img, xy, wh, (0, 0, 255), 2)
    ret, jpeg = cv2.imencode('.jpg', img)
    return jpeg.tobytes()
