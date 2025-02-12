from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO('yolov8-pose.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8s-pose.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='coco8-pose.yaml', epochs=3)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model('./bus.jpg')

# Export the model to ONNX format
# success = model.export(format='onnx')