# 🧤 PopShot 🎯 – A Real-Time Hand Gesture Game

**PopShot** is a real-time interactive game built using Python and OpenCV where players use hand gestures to pop bouncing sports balls on their webcam feed. It uses MediaPipe for hand tracking and integrates audio-visual feedback for an immersive gaming experience. This project is endless, progressively challenging, and designed for fun and learning.

---

# 📜 Version Information

| Feature                     | PopShot (v1)                                      | PopShot2 (v2)                                             |
|------------------------------|---------------------------------------------------|-----------------------------------------------------------|
| Basic Gameplay              | Pop balls using finger poke                       | Pop balls with new gesture modes                         |
| Gesture Modes               | Single gesture (index finger poke)                | Two modes: Normal Mode (✌️ Peace sign) and Power Mode (🤟 Yo sign) |
| Mode Activation             | Always active                                    | Normal Mode activated with Peace ✌️ sign, Power Mode activated with Yo 🤟 sign |
| Power Mode Features         | Not available                                    | Power Mode allows bigger blast radius, faster popping    |
| Stability and Speed         | Basic frame handling                             | Optimized frame reading and FPS smoothing                |
| UI Enhancements             | Minimal                                           | Enhanced text and instruction overlays                  |
| Sound and Visual Effects    | Basic pop sound                                  | Upgraded effects with better response                   |
| Ball Images                 | Static 2-3 ball types                             | More polished ball types with different behaviors        |

---

# 🚀 How to Set Up and Run PopShot Locally

Follow these steps to download, install dependencies, and run the game on your local machine:

## 1. Install Python First (Important!)

If you don't have Python installed:
- Download Python from the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/)

**Windows Users:**
- Download the "Windows installer (64-bit)".
- During installation, **make sure to tick the box** that says "**Add Python to PATH**" before clicking Install Now.

**Mac Users:**
- MacOS usually comes with Python pre-installed, but it's often outdated.
- It's recommended to install the latest version via [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
- After installation, you may need to use `python3` and `pip3` instead of `python` and `pip`.

To verify Python installation:
```bash
python --version
# or for Mac
python3 --version
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/ishar06/popshot.git
cd popshot
```

## 3. Set Up a Virtual Environment

```bash
# Windows
python -m venv venv

# MacOS
python3 -m venv venv
```

## 4. Activate the Virtual Environment

- **Windows**:
```bash
venv\Scripts\activate
```

- **macOS/Linux**:
```bash
source venv/bin/activate
```

## 5. Install Required Dependencies

```bash
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

## 6. Add Sound and Image Assets

- Place your sound file `pop.wav` in the project root or appropriate `sounds` folder.
- Ensure ball images like `basketball.png`, `tennis.png`, `football.png` are inside the `images` folder.

## 7. Run the Game

```bash
python popshot.py
# or for Mac
python3 popshot.py
```

> 🎥 Make sure your webcam is enabled before running the game!

---

# 🎮 Gameplay Instructions

- **Normal Mode (✌️ Peace sign):**
  - Gesture with two fingers to enter normal popping mode.
- **Power Mode (🤙 Yo sign):**
  - Gesture with thumb and pinky extended to activate power mode (bigger pops, faster pops!)
- Use your index finger or hand to pop balls by touching them virtually on the screen.
- Score as much as you can!

---

# 🛠️ Technologies Used

- **Python 3.x**
- **OpenCV** – for computer vision and video feed handling
- **MediaPipe** – for real-time hand gesture detection
- **Pygame** – for audio playback
- **NumPy** – for numerical operations
- **Virtual Environments** – for clean Python environment setup

---

# 👨‍💻 About the Developer

Hey! I'm a passionate developer interested in real-time interactive applications and computer vision. I love building engaging projects that mix creativity with technical skills. PopShot is one of my favorite projects blending gaming with gesture-based control.

🔗 LinkedIn : [https://www.linkedin.com/in/ishardeep-singh-743789311/](https://www.linkedin.com/in/ishardeep-singh-743789311/)

> 💬 Feel free to connect or contribute to this project!

---

# 📄 License & Copyright

© 2025 Ishardeep Singh

This project is for educational and personal use. All media assets used (images and sounds) must be properly licensed or free to use. If you reuse this project, kindly give credit and do not distribute without permission.

---

🎯 **Enjoy popping!** 🎉

