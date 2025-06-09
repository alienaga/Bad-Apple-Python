import cv2
import os

video_path = "badapple.mp4"
output_dir = "frames"

# Create directory to store frames
os.makedirs(output_dir, exist_ok=True)

# Load video
cap = cv2.VideoCapture(video_path)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Resize to 16×16 tiles
    resized_frame = cv2.resize(gray_frame, (640, 480), interpolation=cv2.INTER_NEAREST)
    
    # Save frame as image
    cv2.imwrite(f"{output_dir}/frame_{frame_count:04d}.png", resized_frame)
    frame_count += 1

cap.release()