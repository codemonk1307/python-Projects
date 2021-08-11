
# Packages needed to be installed

# pip install tensorFlow == 2.4.0

# pip install keras == 2.4.3 numpy == 1.19.3 pillow == 7.0.0 scipy == 1.4.1
# h5py == 2.10.0 matplotlib == 3.3.2 opencv-python keras-resnet == 0.2.0

# pip install imageai --upgrade

# Download the     RetinaNet model file 
# Google  the  retinanet  model file   --> download it and place it to your current working directory(cwd) i.e. where this code file is written



from imageai.Detection import ObjectDetection
import os 

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.Path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()

detections = detector.detectObjectFromImage(input_image = os.path.join(execution_path, "image.jpg"), output_image_path = os.path.join(execution_path, "imagenew.jpg"))

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"])




