import cv2
import torch
from ultralytics import YOLO

def init_model(model_path):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    model = YOLO(model_path)
    model.to(device)
    return model, device

def process_frame(frame, model, device):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame_rgb, device=device)
    return results

def print_detected_classes(results):
    detected_classes = results[0].boxes.cls
    class_names = results[0].names
    
    if len(detected_classes) > 0:
        print("\nDetected classes:")
        for cls in detected_classes:
            class_name = class_names[int(cls)]
            print(f"- {class_name}")
    else:
        print("\nNo objects detected")

def annotate_frame(results):
    return results[0].plot()

def main():
    model, device = init_model('yolov8n.pt')
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = process_frame(frame, model, device)
        print_detected_classes(results)
        annotated_frame = cv2.cvtColor(annotate_frame(results), cv2.COLOR_BGR2RGB)
        cv2.imshow("Y8", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
