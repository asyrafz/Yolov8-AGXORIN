import cv2
import torch
from ultralytics import YOLO

if __name__ == '__main__':
    
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    
    print(f"Using device: {device}")

    cap = cv2.VideoCapture(0)

    model = YOLO('yolov8n.pt')
    #model = YOLO('yolov8x04072024.pt')
    model.to(device)

    while cap.isOpened():
        success, frame = cap.read()
        if success:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = model(frame_rgb, device=device)

            annotated_frame = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)

            cv2.imshow("Y8", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()
