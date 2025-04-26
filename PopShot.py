import cv2
import random
import numpy as np
import mediapipe as mp
import pygame
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

pygame.mixer.init()
pop_sound = pygame.mixer.Sound("pop.wav")

ball_images = []
img_folder = "img_folder"  
img_names = ["ball1.png", "ball2.png", "ball3.png", "ball4.png"]  
for name in img_names:
    path = os.path.join(img_folder, name)
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is not None:
        img = cv2.resize(img, (80, 80))
        ball_images.append(img)

cap = cv2.VideoCapture(0)

# Increase camera resolution for better view
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 1280x720 for better quality
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

score = 0
difficulty = 1
MAX_BALLS = 5
paused = False
balls = []

# Button positions and sizes
button_height = 50
button_width = 150
button_padding = 20  # Added padding between score and buttons
buttons = {
    "Quit": (10, 5),
    "Pause": (170, 5),
    "Restart": (330, 5)
}

# Font setup (Poppins Sans Serif if available)
font = cv2.FONT_HERSHEY_DUPLEX
try:
    pygame.font.init()  # Initialize Pygame font system
    font_poppins = pygame.font.Font("Poppins-SemiBold.ttf", 28)  # Path to Poppins font
    poppins_available = True
except:
    poppins_available = False
    font_poppins = None

def generate_ball(speed=2):
    x = random.randint(150, 500)
    y = random.randint(150, 400)
    radius = 40  # fixed for consistent display
    dx = random.choice([-1, 1]) * speed
    dy = random.choice([-1, 1]) * speed
    img = random.choice(ball_images)
    return [x, y, radius, dx, dy, img]

def detect_fingertip(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingertip = hand_landmarks.landmark[8]
            x = int(fingertip.x * frame.shape[1])
            y = int(fingertip.y * frame.shape[0])
            return x, y
    return None, None

def is_touched(fx, fy, bx, by, br):
    if fx is None or fy is None:
        return False
    distance = ((fx - bx) ** 2 + (fy - by) ** 2) ** 0.5
    return distance < br

def draw_buttons(frame):
    for label, (x, y) in buttons.items():
        # Create rounded rectangle button with padding
        color = (30, 30, 30)
        cv2.rectangle(frame, (x, y), (x + button_width, y + button_height), color, -1)
        text = label
        if poppins_available:
            text_surface = font_poppins.render(text, True, (255, 255, 255))
            frame[y + button_height//2 - text_surface.get_height()//2 : y + button_height//2 + text_surface.get_height()//2, x + 20 : x + 20 + text_surface.get_width()] = np.array(pygame.surfarray.pixels3d(text_surface))
        else:
            cv2.putText(frame, text, (x + 15, y + 30), font, 0.9, (255, 255, 255), 2)

def check_button_click(x, y):
    if x is None or y is None:
        return None
    for label, (bx, by) in buttons.items():
        if bx <= x <= bx + button_width and by <= y <= by + button_height:
            return label
    return None

def overlay_image(bg, overlay, x, y, radius):
    if overlay.shape[2] == 4:
        alpha = overlay[:, :, 3] / 255.0
        overlay_resized = cv2.resize(overlay, (radius*2, radius*2))
        for c in range(3):
            try:
                bg[y-radius:y+radius, x-radius:x+radius, c] = (
                    alpha * overlay_resized[:, :, c] +
                    (1 - alpha) * bg[y-radius:y+radius, x-radius:x+radius, c]
                )
            except:
                pass  # Skip drawing if size overflows

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape

    # Draw UI with increased padding
    draw_buttons(frame)

    # Detect hand
    fingertip_x, fingertip_y = detect_fingertip(frame)

    # Simulated click
    click_x, click_y = None, None
    if cv2.waitKey(1) & 0xFF == ord('c'):
        click_x, click_y = width // 2, height // 2

    trigger = check_button_click(fingertip_x, fingertip_y) or check_button_click(click_x, click_y)
    if trigger == "Quit" or cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('1'):
        break
    elif trigger == "Pause" or cv2.waitKey(1) & 0xFF == ord('p') or cv2.waitKey(1) & 0xFF == ord('2'):
        paused = not paused
    elif trigger == "Restart" or cv2.waitKey(1) & 0xFF == ord('r') or cv2.waitKey(1) & 0xFF == ord('3'):
        score = 0
        difficulty = 1
        balls = []
        paused = False

    if paused:
        cv2.putText(frame, "PAUSED", (width // 2 - 100, height // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 100, 255), 3)
        cv2.imshow("PopShot", frame)
        continue

    # Ball spawning logic
    desired_balls = min(1 + score // 30, MAX_BALLS)
    speed = 2.5 + (score // 40) * 0.7  # slight increase in difficulty

    while len(balls) < desired_balls:
        balls.append(generate_ball(speed))

    new_balls = []
    popped = 0

    for ball in balls:
        ball[0] += ball[3]
        ball[1] += ball[4]

        # Bounce off walls
        if ball[0] - ball[2] <= 0 or ball[0] + ball[2] >= width:
            ball[3] *= -1
        if ball[1] - ball[2] <= 0 or ball[1] + ball[2] >= height:
            ball[4] *= -1

        # Check pop
        if is_touched(fingertip_x, fingertip_y, ball[0], ball[1], ball[2]):
            popped += 1
            pop_sound.play()
            continue
        else:
            new_balls.append(ball)

        overlay_image(frame, ball[5], int(ball[0]), int(ball[1]), ball[2])

    score += popped * 10
    difficulty = 1 + score // 30
    balls = new_balls

    # Stylish score display with a glow effect
    cv2.putText(frame, f"Score: {score}", (20, 100 + button_padding),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3)
    cv2.putText(frame, f"Balls: {len(balls)}", (20, 150 + button_padding),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 200, 255), 3)

    cv2.imshow("PopShot", frame)

    # Avoid holding down the key for action, it now works on a single keypress
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('1'):
        break
    elif key == ord('p') or key == ord('2'):
        paused = not paused
    elif key == ord('r') or key == ord('3'):
        score = 0
        difficulty = 1
        balls = []
        paused = False

cap.release()
cv2.destroyAllWindows()
