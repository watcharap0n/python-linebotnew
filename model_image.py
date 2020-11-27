import pickle
import cv2
import dlib
import numpy as np


FACE_DESC, FACE_NAME = pickle.load(open('log/trainset.pk', 'rb'))
face_detector = cv2.CascadeClassifier('model_image/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("model_image/haarcascade_eye.xml")
detector = dlib.get_frontal_face_detector() #dlib(bettle), openCV
sp = dlib.shape_predictor('model_image/shape_predictor_68_face_landmarks.dat') #shape_landmark Detection
model = dlib.face_recognition_model_v1('model_image/dlib_face_recognition_resnet_model_v1.dat') #buil model
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