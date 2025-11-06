import cv2
import os
import time
import numpy as np
from IPython.display import clear_output

def frame_to_ascii(frame, width=80):
    """Convert one video frame to ASCII art."""
    chars = " .:-=+*#%@"
    height = max(1, int(frame.shape[0] * width / frame.shape[1] / 2))
    small = cv2.resize(frame, (width, height))
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY) if len(small.shape) > 2 else small
    indices = (gray / 255.0 * (len(chars) - 1)).astype(int)
    ascii_frame = '\n'.join(''.join(chars[i] for i in row) for row in indices)
    return ascii_frame

def play_ascii_video(video_path, width=80):
    """Play a video file as ASCII art inside Jupyter Notebook."""
    if not os.path.exists(video_path):
        print(f"❌ Error: '{video_path}' not found")
        return
    
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = 1.0 / fps if fps > 0 else 1.0 / 30
    
    print("🎬 Starting ASCII video playback...\n")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("\n✅ End of video.")
                break
            
            ascii_art = frame_to_ascii(frame, width)
            clear_output(wait=True)
            print(ascii_art)
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("\n🛑 Playback stopped by user.")
    finally:
        cap.release()
play_ascii_video("video (2).mp4", width=80)
