# To-asciify
Creating ASCII Art "Asciify" is also widely used to describe the process of converting an image, video, or 3D render into visual art made up of ASCII characters. Process: Software analyzes the intensity or color of pixels in the source material and replaces them with corresponding characters (e.g., using . for light areas and # or @ for dark .
Asciify
Transform videos into mesmerizing ASCII art, right in your terminal.

Preview


Features
Real-time video playback as ASCII art
Adaptive FPS and terminal width control
Simple, lightweight Python implementation
No external players needed
Quick Start
# Clone and navigate

cd asciify

# Set up environment
python3 -m venv venv
source venv/bin/activate(linux,macOS)  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Usage
python main.py
Follow the prompts to:

Specify video path (default: video.mp4)
Set terminal width (optional)
Press Ctrl+C to stop playback.

Requirements
Python 3.9+
opencv-python
numpy
