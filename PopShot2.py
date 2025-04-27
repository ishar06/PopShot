import cv2
import random
import numpy as np
import mediapipe as mp
import pygame
import os
import time

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


bomb_path = os.path.join(img_folder, "bomb.png")
bomb_img = cv2.imread(bomb_path, cv2.IMREAD_UNCHANGED)
if bomb_img is not None:
    bomb_img = cv2.resize(bomb_img, (80, 80))

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


score = 0
high_score = 0
difficulty = 1
MAX_BALLS = 5
paused = False
game_over = False
balls = []


NORMAL_MODE = "normal"
POWER_MODE = "power"
current_mode = NORMAL_MODE
game_start_time = 0
time_limit = 60 


INSTRUCTIONS_STATE = "instructions"
PLAYING_STATE = "playing"
GAME_OVER_STATE = "game_over"
CONFIRM_QUIT_STATE = "confirm_quit"  
game_state = INSTRUCTIONS_STATE


button_height = 50
button_width = 200
button_padding = 20

button_names = ["Quit", "Pause", "Restart", "Normal Mode", "Power Mode"]

buttons = {}


start_x = 10
start_y = 5

for index, name in enumerate(button_names):
    x = start_x + index * (button_width + button_padding)
    y = start_y
    buttons[name] = (x, y)


confirm_buttons = {
    "Yes": (None, None),  
    "No": (None, None)    
}


instruction_buttons = {}


width, height = 1280, 720


game_over_buttons = {}


font = cv2.FONT_HERSHEY_DUPLEX
try:
    pygame.font.init()
    font_poppins = pygame.font.Font("Poppins-SemiBold.ttf", 28)
    poppins_available = True
except:
    poppins_available = False
    font_poppins = None

def generate_ball(speed=2, include_bombs=False, force_normal=False):
    x = random.randint(150, 500)
    y = random.randint(150, 400)
    radius = 40
    dx = random.choice([-1, 1]) * speed
    dy = random.choice([-1, 1]) * speed
    
    
    is_bomb = False
    if include_bombs and not force_normal and random.random() < 0.15 and bomb_img is not None:  
        img = bomb_img
        is_bomb = True
    else:
        
        if ball_images:
            img = random.choice(ball_images)
        else:
            
            img = None
            print("Warning: No ball images loaded")
        
    return [x, y, radius, dx, dy, img, is_bomb]

def detect_hand_gesture(hand_landmarks):
    
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]
    ring_tip = hand_landmarks.landmark[16]
    pinky_tip = hand_landmarks.landmark[20]
    
    index_pip = hand_landmarks.landmark[6]
    middle_pip = hand_landmarks.landmark[10]
    ring_pip = hand_landmarks.landmark[14]
    pinky_pip = hand_landmarks.landmark[18]
    
    # Peace sign (Normal mode) - index and middle finger up, ring and pinky down
    if (index_tip.y < index_pip.y and middle_tip.y < middle_pip.y and 
        ring_tip.y > ring_pip.y and pinky_tip.y > pinky_pip.y):
        return "peace"
    
    # Yo sign (Power mode) - index and pinky finger up, middle and ring down
    if (index_tip.y < index_pip.y and middle_tip.y > middle_pip.y and 
        ring_tip.y > ring_pip.y and pinky_tip.y < pinky_pip.y):
        return "yo"
    
    return None

def detect_fingertip(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    gesture = None
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
            gesture = detect_hand_gesture(hand_landmarks)
            
            
            fingertip = hand_landmarks.landmark[8]
            x = int(fingertip.x * frame.shape[1])
            y = int(fingertip.y * frame.shape[0])
            return x, y, gesture
    
    return None, None, None

def is_touched(fx, fy, bx, by, br):
    if fx is None or fy is None:
        return False
    distance = ((fx - bx) ** 2 + (fy - by) ** 2) ** 0.5
    return distance < br

def is_button_area(x, y, button_dict):
    """Check if a point is in any button area with some padding"""
    if x is None or y is None:
        return False
    
    
    padding = 10
    
    for label, (bx, by) in button_dict.items():
        if (bx - padding <= x <= bx + button_width + padding and 
            by - padding <= y <= by + button_height + padding):
            return True
    return False

def draw_buttons(frame, button_dict):
    for label, (x, y) in button_dict.items():
        
        color = (30, 30, 30)
        
        
        if (label == "Normal Mode" and current_mode == NORMAL_MODE) or \
           (label == "Power Mode" and current_mode == POWER_MODE):
            color = (0, 100, 200)
            
        cv2.rectangle(frame, (x, y), (x + button_width, y + button_height), color, -1)
        text = label
        if poppins_available:
            text_surface = font_poppins.render(text, True, (255, 255, 255))
            try:
                frame[y + button_height//2 - text_surface.get_height()//2 : y + button_height//2 + text_surface.get_height()//2, 
                      x + 20 : x + 20 + text_surface.get_width()] = np.array(pygame.surfarray.pixels3d(text_surface))
            except:
                
                cv2.putText(frame, text, (x + 15, y + 30), font, 0.9, (255, 255, 255), 2)
        else:
            cv2.putText(frame, text, (x + 15, y + 30), font, 0.9, (255, 255, 255), 2)

def check_button_click(x, y, button_dict):
    if x is None or y is None:
        return None
    for label, (bx, by) in button_dict.items():
        if bx <= x <= bx + button_width and by <= y <= by + button_height:
            return label
    return None

def overlay_image(bg, overlay, x, y, radius):
    if overlay is None or overlay.shape[2] < 3:
        
        cv2.circle(bg, (x, y), radius, (0, 255, 255), -1)
        return
        
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
                pass  
    else:
        
        try:
            overlay_resized = cv2.resize(overlay, (radius*2, radius*2))
            y_start = max(0, y-radius)
            y_end = min(bg.shape[0], y+radius)
            x_start = max(0, x-radius)
            x_end = min(bg.shape[1], x+radius)
            
            
            overlay_y_start = max(0, radius - y)
            overlay_y_end = overlay_resized.shape[0] - max(0, y + radius - bg.shape[0])
            overlay_x_start = max(0, radius - x)
            overlay_x_end = overlay_resized.shape[1] - max(0, x + radius - bg.shape[1])
            
            bg[y_start:y_end, x_start:x_end] = overlay_resized[overlay_y_start:overlay_y_end, overlay_x_start:overlay_x_end]
        except:
            
            cv2.circle(bg, (x, y), radius, (0, 255, 255), -1)

def reset_game(mode=None):
    global score, difficulty, balls, paused, game_over, current_mode, game_start_time, time_limit, game_state
    
    score = 0
    difficulty = 1
    balls = []
    paused = False
    game_over = False
    game_start_time = time.time()
    game_state = PLAYING_STATE
    
    if mode:
        current_mode = mode
        
    
    if current_mode == NORMAL_MODE:
        time_limit = 60  
    else: 
        time_limit = 90  

def draw_game_over_screen(frame, width, height):
    # Darken the background
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (width, height), (0, 0, 0), -1)
    frame = cv2.addWeighted(overlay, 0.7, frame, 0.3, 0)
    
    # Game over text
    cv2.putText(frame, "GAME OVER", (width//2 - 200, height//2 - 100),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    
    # Score display
    cv2.putText(frame, f"Score: {score}", (width//2 - 100, height//2 - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 255), 2)
    
    # High score display
    cv2.putText(frame, f"High Score: {high_score}", (width//2 - 130, height//2 + 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2)
    
    # Draw buttons
    draw_buttons(frame, game_over_buttons)
    
    return frame

def draw_confirm_quit_screen(frame, width, height):
    # Darken the background
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (width, height), (0, 0, 0), -1)
    frame = cv2.addWeighted(overlay, 0.7, frame, 0.3, 0)
    
    # Confirmation text
    cv2.putText(frame, "Are you sure you want to quit?", (width//2 - 250, height//2 - 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)
    
    # Draw buttons
    draw_buttons(frame, confirm_buttons)
    
    return frame

def draw_instructions_screen(frame, width, height):
    # Create a semi-transparent overlay
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (width, height), (0, 0, 0), -1)
    frame = cv2.addWeighted(overlay, 0.7, frame, 0.3, 0)
    
    # Title
    cv2.putText(frame, "POPSHOT - INSTRUCTIONS", (width//2 - 300, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 200, 255), 3)
    
    # Instructions
    instructions = [
        "Pop the balls by touching them with your index finger!",
        "Avoid touching bombs in Power Mode!",
        "",
        "GAME MODES:",
        "Normal Mode: Show PEACE SIGN to activate",
        "- Regular balls only",
        "- 60 seconds time limit",
        "",
        "Power Mode: Show YO SIGN to activate",
        "- Includes bombs that end your game if touched",
        "- 90 seconds time limit",
        "- Faster balls and higher difficulty",
        "",
        "Make a gesture to select a mode and start the game!"
    ]
    
    y_pos = 150
    for line in instructions:
        cv2.putText(frame, line, (width//2 - 350, y_pos),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        y_pos += 40
    
    # Display current detected gesture
    if fingertip_x is not None:
        if gesture == "peace":
            cv2.putText(frame, "Detected: PEACE SIGN ✌️ (Normal Mode)", (width//2 - 250, height - 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif gesture == "yo":
            cv2.putText(frame, "Detected: YO SIGN 🤙 (Power Mode)", (width//2 - 250, height - 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    return frame

def is_ball_out_of_bounds(ball, width, height):
    """Check if a ball is completely out of the screen bounds"""
    x, y, radius = ball[0], ball[1], ball[2]
    return (x + radius < 0 or x - radius > width or 
            y + radius < 0 or y - radius > height)

def count_normal_balls(balls):
    """Count how many normal (non-bomb) balls are in play"""
    return sum(1 for ball in balls if not ball[6])

# Main game loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    
    # Update game over buttons with correct dimensions (only once)
    if not game_over_buttons:
        game_over_buttons = {
            "Play Again": (width//2 - 150, height//2 + 50),
            "Quit": (width//2 + 50, height//2 + 50)
        }
        
    # Update confirm buttons with correct dimensions (only once)
    if confirm_buttons["Yes"][0] is None:
        confirm_buttons = {
            "Yes": (width//2 - 150, height//2 + 50),
            "No": (width//2 + 50, height//2 + 50)
        }
    
    # Detect hand
    fingertip_x, fingertip_y, gesture = detect_fingertip(frame)
    
    # Handle different game states
    if game_state == INSTRUCTIONS_STATE:
        # Draw instructions screen
        frame = draw_instructions_screen(frame, width, height)
        
        # Handle mode selection via gestures
        if gesture == "peace":
            reset_game(NORMAL_MODE)
        elif gesture == "yo":
            reset_game(POWER_MODE)
            
    elif game_state == GAME_OVER_STATE:
        frame = draw_game_over_screen(frame, width, height)
        
        # Check for button clicks in game over screen
        trigger = check_button_click(fingertip_x, fingertip_y, game_over_buttons)
        if trigger == "Play Again":
            game_state = INSTRUCTIONS_STATE
        elif trigger == "Quit":
            game_state = CONFIRM_QUIT_STATE
            
    elif game_state == CONFIRM_QUIT_STATE:
        frame = draw_confirm_quit_screen(frame, width, height)
        
        # Check for button clicks in confirm screen
        trigger = check_button_click(fingertip_x, fingertip_y, confirm_buttons)
        if trigger == "Yes":
            break  # Exit the game
        elif trigger == "No":
            # Return to previous state
            if game_over:
                game_state = GAME_OVER_STATE
            else:
                game_state = PLAYING_STATE
                
    elif game_state == PLAYING_STATE:
        # Handle gestures for mode switching during gameplay
        if gesture == "peace" and current_mode != NORMAL_MODE:
            reset_game(NORMAL_MODE)
        elif gesture == "yo" and current_mode != POWER_MODE:
            reset_game(POWER_MODE)
        
        # Draw game UI
        draw_buttons(frame, buttons)
        
        # Simulated click
        click_x, click_y = None, None
        if cv2.waitKey(1) & 0xFF == ord('c'):
            click_x, click_y = width // 2, height // 2
    
        trigger = check_button_click(fingertip_x, fingertip_y, buttons) or check_button_click(click_x, click_y, buttons)
        if trigger == "Quit":
            game_state = CONFIRM_QUIT_STATE
        elif trigger == "Pause":
            paused = not paused
        elif trigger == "Restart":
            game_state = INSTRUCTIONS_STATE
        elif trigger == "Normal Mode":
            reset_game(NORMAL_MODE)
        elif trigger == "Power Mode":
            reset_game(POWER_MODE)
    
        if paused:
            cv2.putText(frame, "PAUSED", (width // 2 - 100, height // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 100, 255), 3)
            cv2.imshow("PopShot", frame)
            continue
            
        # Check time limit
        elapsed_time = time.time() - game_start_time
        remaining_time = max(0, time_limit - elapsed_time)
        
        if remaining_time <= 0:
            # Game over due to time limit
            if score > high_score:
                high_score = score
            game_state = GAME_OVER_STATE
            continue
            
        # Ball spawning logic
        desired_balls = min(1 + score // 30, MAX_BALLS)
        
        # Set speed based on mode and score
        if current_mode == NORMAL_MODE:
            speed = 2.5 + (score // 40) * 0.7
        else:  # POWER_MODE
            speed = 3.5 + (score // 30) * 0.8  # Faster in power mode
    
        # Track if we need to add a normal ball to replace an exited bomb
        need_normal_ball = False
        
        # Count normal balls before processing
        normal_balls_count = count_normal_balls(balls)
        
        # Process existing balls
        new_balls = []
        popped = 0
        game_ended_by_bomb = False
        bombs_exited = 0
    
        for ball in balls:
            ball[0] += ball[3]  # x position
            ball[1] += ball[4]  # y position
            
            is_bomb = ball[6]
            
            # Check if ball is out of bounds
            if is_ball_out_of_bounds(ball, width, height):
                if is_bomb:
                    # If a bomb exits, we'll add a normal ball later
                    bombs_exited += 1
                continue  # Skip this ball, it's out of bounds
    
            # Bounce off walls and buttons
            if current_mode == NORMAL_MODE or not is_bomb:
                # Bounce off walls
                if ball[0] - ball[2] <= 0 or ball[0] + ball[2] >= width:
                    ball[3] *= -1
                if ball[1] - ball[2] <= 0 or ball[1] + ball[2] >= height:
                    ball[4] *= -1
                    
                # Bounce off buttons - check if ball is near any button
                if is_button_area(ball[0], ball[1], buttons):
                    # Find the closest button edge and bounce accordingly
                    for _, (bx, by) in buttons.items():
                        # Check if ball is horizontally aligned with button
                        if bx - ball[2] <= ball[0] <= bx + button_width + ball[2]:
                            # Ball is hitting top or bottom of button
                            if abs(ball[1] - by) < ball[2] or abs(ball[1] - (by + button_height)) < ball[2]:
                                ball[4] *= -1  # Reverse vertical direction
                                
                        # Check if ball is vertically aligned with button
                        if by - ball[2] <= ball[1] <= by + button_height + ball[2]:
                            # Ball is hitting left or right of button
                            if abs(ball[0] - bx) < ball[2] or abs(ball[0] - (bx + button_width)) < ball[2]:
                                ball[3] *= -1  # Reverse horizontal direction
            
            # Check pop
            if is_touched(fingertip_x, fingertip_y, ball[0], ball[1], ball[2]):
                if is_bomb:  # It's a bomb
                    game_ended_by_bomb = True
                    if score > high_score:
                        high_score = score
                    break
                else:
                    popped += 1
                    pop_sound.play()
                    continue
            else:
                new_balls.append(ball)
    
            overlay_image(frame, ball[5], int(ball[0]), int(ball[1]), ball[2])
    
        if game_ended_by_bomb:
            game_state = GAME_OVER_STATE
            continue
            
        # Update balls list
        balls = new_balls
        
        # Add new balls if needed
        while len(balls) < desired_balls:
            # In Power Mode, ensure we always have at least one normal ball
            force_normal = False
            if current_mode == POWER_MODE:
                # If there are no normal balls, force the next one to be normal
                if count_normal_balls(balls) == 0:
                    force_normal = True
            
            include_bombs = (current_mode == POWER_MODE)
            balls.append(generate_ball(speed, include_bombs, force_normal))
        
        # Add replacement normal balls for exited bombs
        for _ in range(bombs_exited):
            if len(balls) < MAX_BALLS:
                # Always generate a normal ball to replace an exited bomb
                balls.append(generate_ball(speed, False, True))
            
        score += popped * 10
        difficulty = 1 + score // 30
    
        # Display score and time
        cv2.putText(frame, f"Score: {score}", (20, 100 + button_padding),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3)
        cv2.putText(frame, f"Time: {int(remaining_time)}s", (20, 150 + button_padding),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 200, 255), 3)
        
        # Display current mode
        mode_text = "NORMAL MODE ✌️" if current_mode == NORMAL_MODE else "POWER MODE 🤙"
        cv2.putText(frame, mode_text, (width - 300, 100 + button_padding),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 200, 0), 3)
    
    cv2.imshow("PopShot", frame)
    
    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        game_state = CONFIRM_QUIT_STATE
    elif key == ord('p') and game_state == PLAYING_STATE:
        paused = not paused
    elif key == ord('r') and game_state == PLAYING_STATE:
        game_state = INSTRUCTIONS_STATE
    elif key == ord('n') and game_state == PLAYING_STATE:
        reset_game(NORMAL_MODE)
    elif key == ord('w') and game_state == PLAYING_STATE:
        reset_game(POWER_MODE)
    elif key == ord('i'):
        game_state = INSTRUCTIONS_STATE

cap.release()
cv2.destroyAllWindows()