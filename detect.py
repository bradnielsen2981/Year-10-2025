import cv2
from ultralytics import YOLO

# Load the YOLOv8 model (Nano version for speed)
model = YOLO("yolov8n.pt")  

# Open webcam
cap = cv2.VideoCapture(0)  # Change to 1 if you have an external webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO object detection
    results = model(frame)
    print(results)

    # Draw bounding boxes on the frame
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get box coordinates
            conf = box.conf[0]  # Confidence score
            cls = int(box.cls[0])  # Class ID
            label = f"{model.names[cls]} {conf:.2f}"  # Label with confidence

            # Draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)  # Green box
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.6, (0, 255, 0), 2)

    # Show the output frame
    cv2.imshow("YOLO Webcam", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
