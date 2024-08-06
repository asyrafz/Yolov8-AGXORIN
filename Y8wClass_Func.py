import cv2
import torch
import numpy as np
from ultralytics import YOLO

def process_frame(frame, model, device):
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
            print(f'Class: {model.names[int(class_id)]}, Confidence: {score:.2f}')

    return annotated_frame

def main():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    # Initialize video capture for two cameras
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(2)
    model = YOLO('yolov8n.pt')  # Adjust the model path as needed
    model.to(device)

    while cap1.isOpened() and cap2.isOpened():
        success1, frame1 = cap1.read()
        success2, frame2 = cap2.read()

        if success1 and success2:
            # Process both frames
            annotated_frame1 = process_frame(frame1, model, device)
            annotated_frame2 = process_frame(frame2, model, device)

            # Display the frames
            cv2.imshow("YOLOv8 Detection - Camera 1", annotated_frame1)
            cv2.imshow("YOLOv8 Detection - Camera 2", annotated_frame2)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
