import cv2
import numpy as np
import glob
import time

# Configurable tile size variable
TILE_SIZE = 480  # Change this to adjust tile size (e.g., 32, 64, etc.)
SCALE_FACTOR = 10  # Adjust display scaling

# Define the folder containing frames
FRAME_FOLDER = "frames"

# Get all frame paths sorted
frame_paths = sorted(glob.glob(f"{FRAME_FOLDER}/*.png"))
print(f"Total frames loaded: {len(frame_paths)}")

# Create a window for display
cv2.namedWindow(f"Bad Apple - {TILE_SIZE}x{TILE_SIZE} Tiles", cv2.WINDOW_NORMAL)

# Play frames in sequence
for frame_path in frame_paths:
    # Load frame in grayscale
    frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)

    # Resize to TILE_SIZE x TILE_SIZE tiles
    frame_resized = cv2.resize(frame, (TILE_SIZE, TILE_SIZE), interpolation=cv2.INTER_NEAREST)

    # Convert to black-and-white (thresholding)
    _, frame_bw = cv2.threshold(frame_resized, 128, 255, cv2.THRESH_BINARY)

    # Enlarge display for better visibility
    display_frame = cv2.resize(frame_bw, (TILE_SIZE * SCALE_FACTOR, TILE_SIZE * SCALE_FACTOR), interpolation=cv2.INTER_NEAREST)

    # Show frame
    cv2.imshow(f"Bad Apple - {TILE_SIZE}x{TILE_SIZE} Tiles", display_frame)

    # Wait 33ms for smooth animation (~30 FPS)
    if cv2.waitKey(33) & 0xFF == ord('q'):  # Press 'q' to quit
        break

while True:
    if cv2.waitKey(33) & 0xFF == ord('q'):  # Press 'q' to close manually
        break

cv2.destroyAllWindows()