import cv2
import numpy as np
import pyautogui
import mediapipe as mp
import time


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)


screen_width, screen_height = pyautogui.size()


english_keys = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'],
    ['Caps', 'Lang', ' ', ' ', ' ', ' ', ' ', ' ', '⌫']
]

arabic_keys = [
    ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح'],
    ['ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ك'],
    ['ظ', 'ط', 'ذ', 'د', 'ز', 'ر', 'و', 'ة', 'ى', 'ء'],
    ['Caps', 'Lang', ' ', ' ', ' ', ' ', ' ', ' ', '⌫']
]


current_keys = english_keys


caps_lock = False


key_width = 80
key_height = 80
key_spacing = 10


keyboard_x = 50
keyboard_y = 100


last_key_press_time = 0
cooldown_duration = 0.5  


def draw_rounded_rect(frame, x, y, w, h, color, corner_radius=10):
    cv2.rectangle(frame, (x + corner_radius, y), (x + w - corner_radius, y + h), color, -1)
    cv2.rectangle(frame, (x, y + corner_radius), (x + w, y + h - corner_radius), color, -1)
    cv2.circle(frame, (x + corner_radius, y + corner_radius), corner_radius, color, -1)
    cv2.circle(frame, (x + w - corner_radius, y + corner_radius), corner_radius, color, -1)
    cv2.circle(frame, (x + corner_radius, y + h - corner_radius), corner_radius, color, -1)
    cv2.circle(frame, (x + w - corner_radius, y + h - corner_radius), corner_radius, color, -1)


def draw_keyboard(frame):
    for i, row in enumerate(current_keys):
        for j, key in enumerate(row):
            x = keyboard_x + j * (key_width + key_spacing)
            y = keyboard_y + i * (key_height + key_spacing)
            draw_rounded_rect(frame, x, y, key_width, key_height, (200, 200, 200), 15)
            if caps_lock and key.isalpha():
                key = key.upper() if key.islower() else key.lower()
            cv2.putText(frame, key, (x + 20, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


def detect_key_press(frame, index_x, index_y):
    for i, row in enumerate(current_keys):
        for j, key in enumerate(row):
            x = keyboard_x + j * (key_width + key_spacing)
            y = keyboard_y + i * (key_height + key_spacing)
            if x < index_x < x + key_width and y < index_y < y + key_height:
                draw_rounded_rect(frame, x, y, key_width, key_height, (0, 255, 0), 15)
                if caps_lock and key.isalpha():
                    key = key.upper() if key.islower() else key.lower()
                cv2.putText(frame, key, (x + 20, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                return key
    return None


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    draw_keyboard(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            h, w, _ = frame.shape
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)

            key = detect_key_press(frame, index_x, index_y)

            distance = np.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)
            if distance < 30: 
                current_time = time.time()
                if key and (current_time - last_key_press_time) > cooldown_duration:
                    if key == 'Lang':
                        current_keys = arabic_keys if current_keys == english_keys else english_keys
                    elif key == 'Caps':
                        caps_lock = not caps_lock
                    elif key == '⌫':
                        pyautogui.press('backspace') 
                    else:
                        pyautogui.press(key)  
                    last_key_press_time = current_time 
                    cv2.putText(frame, f"Pressed: {key}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw circles at the fingertips
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)

    cv2.imshow("Virtual Keyboard", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
