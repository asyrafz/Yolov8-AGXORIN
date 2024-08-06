import cv2
import torch
import numpy as np
from ultralytics import YOLO
from multiprocessing import Process, Queue, Event, set_start_method
import signal
import sys


def process_frame(frame, model, device, camera_index):
    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    with torch.no_grad():  # Disable gradient calculation
        # Perform inference
        results = model(frame_rgb, device=device)

    # Extract bounding boxes, scores, and class IDs
    boxes = results[0].boxes.xyxy.cpu().numpy()
    scores = results[0].boxes.conf.cpu().numpy()
    class_ids = results[0].boxes.cls.cpu().numpy()

    # Draw bounding boxes and print class labels
    annotated_frame = frame.copy()
    for box, score, class_id in zip(boxes, scores, class_ids):
        if score > 0.5:  # Confidence threshold
            x1, y1, x2, y2 = box.astype(int)  # Ensure coordinates are integers
            label = f'{model.names[int(class_id)]} {score:.2f}'
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Print class label and confidence
            print(f'{camera_index}, Class: {model.names[int(class_id)]}, Conf: {score:.2f}')

    return annotated_frame

def camera_worker(camera_index, queue, stop_event):
    # Initialize YOLO model and device inside the worker process
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model = YOLO('yolov8n.pt')  # Adjust the model path as needed
    model.to(device)

    cap = cv2.VideoCapture(camera_index)
    while cap.isOpened() and not stop_event.is_set():
        success, frame = cap.read()
        if success:
            annotated_frame = process_frame(frame, model, device, camera_index)
            queue.put((camera_index, annotated_frame))
        else:
            break
    cap.release()

def signal_handler(sig, frame):
    print('Signal received, shutting down...')
    stop_event.set()

def main():
    set_start_method('spawn', force=True)  # Set start method to 'spawn'

    global stop_event
    stop_event = Event()  # Create an event for stopping processes

    # Handle termination signals
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    # Create a queue for inter-process communication
    queue = Queue()

    # Create and start camera worker processes
    p1 = Process(target=camera_worker, args=(0, queue, stop_event))
    p2 = Process(target=camera_worker, args=(2, queue, stop_event))
    p1.start()
    p2.start()

    while not stop_event.is_set():
        if not queue.empty():
            camera_index, annotated_frame = queue.get()
            window_name = f"YOLOv8 Detection - Camera {camera_index + 1}"
            cv2.imshow(window_name, annotated_frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()
            break

    p1.join()
    p2.join()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
