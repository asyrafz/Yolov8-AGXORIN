import torch
import torch.nn as nn
import cv2
import numpy as np
import tensorrt as trt

# Load the TensorRT model
trt_logger = trt.Logger(trt.Logger.INFO)
trt_runtime = trt.Runtime(trt_logger)
with open("yolov8.trt", "rb") as f:
    trt_model = trt_runtime.deserialize_cuda_model(f.read())

# Create a TensorRT engine
trt_engine = trt_runtime.new_execution_context(trt_model)

# Set up the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    frame = cv2.resize(frame, (640, 480))  # resize to match the model's input size
    frame = frame / 255.0  # normalize to [0, 1] range
    frame = np.transpose(frame, (2, 0, 1))  # HWC to CHW format

    # Convert the frame to a PyTorch tensor
    frame_tensor = torch.from_numpy(frame).float()

    # Create a batch of size 1
    batch = frame_tensor.unsqueeze(0)

    # Run the inference
    outputs = trt_engine.execute(batch)

    # Parse the outputs
    boxes = outputs[0].numpy()
    scores = outputs[1].numpy()
    classes = outputs[2].numpy()

    # Draw the bounding boxes
    for i in range(len(boxes)):
        x, y, w, h = boxes[i]
        cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0, 255, 0), 2)
        cv2.putText(frame, f"{classes[i]}: {scores[i]:.2f}", (int(x), int(y-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the output
    cv2.imshow("YOLOv8", frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
