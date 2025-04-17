# PopShot  – A Real-Time Hand Gesture Game

**PopShot** is a real-time interactive game built using Python and OpenCV where players use hand gestures to pop bouncing sports balls like basketballs, tennis balls, and footballs on their webcam feed. It uses MediaPipe for hand tracking and integrates audio-visual feedback for an immersive gaming experience. This project is endless, progressively challenging, and designed for fun and learning.

-----

## How to Set Up and Run PopShot Locally

Follow these steps to download, install dependencies, and run the game on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/popshot.git
cd popshot
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- On **Windows**:

```bash
venv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source venv/bin/activate
```

### 4. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Sound and Image Assets

- Place your sound file `pop.wav` in the project root or appropriate `sounds` folder.
- Ensure ball images like `basketball.png`, `tennis.png`, `football.png` are inside the `images` folder.

### 6. Run the Game

```bash
python popshot.py
```

> Make sure your webcam is enabled before running the game.

-----

## Technologies Used

- **Python 3.x**
- **OpenCV** – for computer vision and video feed handling
- **MediaPipe** – for real-time hand gesture detection
- **Pygame** – for audio playback
- **NumPy** – for numerical operations
- **Virtual Environments** – for clean Python environment setup

-----

## About the Developer

Hey! I'm a passionate developer interested in real-time interactive applications and computer vision. I love building engaging projects that mix creativity with technical skills. PopShot is one of my favorite projects that blends gaming with gesture-based control.
Follow me via LinkedIn : https://www.linkedin.com/in/ishardeep-singh-743789311/

> Feel free to connect or contribute to this project!

-----

## 📄 License & Copyright

© 2025 Ishardeep Singh

This project is for educational and personal use. All media assets used (images and sounds) must be properly licensed or free to use. If you reuse this project, kindly give credit and do not distribute without permission.

-----

Enjoy popping! 
