# Virtual Keyboard Using Hand Gesture Recognition
## Overview
This project implements a virtual keyboard that can be controlled using hand gestures. The system uses MediaPipe to detect the user's hand, specifically the index finger and thumb, to simulate key presses. This allows users to type without physically touching a keyboard by using hand movements, providing a hands-free typing experience.

The virtual keyboard can switch between English and Arabic layouts and supports basic keyboard functionalities, such as Caps Lock, Language Switching, and Backspace.

## Key Features:
Hand Gesture Recognition: Uses MediaPipe's hand tracking solution to detect the position of the index finger and thumb.
Dynamic Keyboard Layout: The keyboard dynamically switches between English and Arabic layouts using hand gestures.
Caps Lock: Allows users to toggle between uppercase and lowercase letters with the Caps Lock key.
Backspace Functionality: Users can simulate a backspace key press by performing a specific gesture.
Customizable Keyboard: The size and layout of the keyboard can be adjusted to fit the screen or user preferences.
![Hi Five 👋](https://drive.google.com/uc?export=view&id=1dJDthxIwhfBpaRmGPFpAfzGfyk7htRJU)
## Libraries Used:
### OpenCV (cv2): 
Used for video capture and image processing.
### PyAutoGUI: 
Simulates keyboard input based on the user's gestures.
### MediaPipe: 
Used for hand tracking and detecting hand landmarks.
### NumPy: 
Used for calculating the distance between fingertips to determine key presses.

## How It Works:
1. Hand Detection:
The script uses MediaPipe to detect the landmarks of the hand. Specifically, it tracks the index finger tip and the thumb tip, which are used to simulate key presses on the virtual keyboard.

2. Keyboard Drawing:
The virtual keyboard is drawn on the screen using OpenCV. The layout changes between English and Arabic when the Language key is pressed. The keys are drawn as rectangles with rounded corners, and their labels are displayed in the middle.

3. Key Press Detection:
When the index finger moves over a key, it is highlighted. When the distance between the index finger and thumb becomes small enough (simulating a "tap" gesture), the corresponding key press is simulated using PyAutoGUI.

4. Keyboard Features:
Language Switching: Switching between English and Arabic keyboards is triggered by pressing the Lang key.
Caps Lock: Toggling Caps Lock is handled by the Caps key, which changes the case of alphabetic characters.
Backspace: Pressing the ⌫ key simulates the backspace key action.
5. Cooldown for Key Presses:
A cooldown period (0.5 seconds) is enforced between key presses to avoid multiple unintended inputs due to fast hand movements.

## Functions:
### draw_rounded_rect(frame, x, y, w, h, color, corner_radius=10)
Draws a rounded rectangle on the screen for each key.
frame: The frame to draw on.
x, y: Coordinates of the rectangle's top-left corner.
w, h: Width and height of the rectangle.
color: The color of the rectangle.
corner_radius: The radius of the rounded corners.

### draw_keyboard(frame)
Draws the entire keyboard layout on the screen.
frame: The frame to draw on.
detect_key_press(frame, index_x, index_y)
Detects if a key is pressed based on the position of the index finger.
frame: The frame to detect key presses on.
index_x, index_y: Coordinates of the index finger tip.

### Main Loop:
- Captures video from the webcam.
- Converts the frame to RGB for processing with MediaPipe.
- Tracks the hand landmarks and calculates the positions of the fingertips.
- Detects key presses based on the position of the index finger and thumb.
- Simulates the key press if the thumb and index finger are close enough.
- Updates the keyboard on the screen in real-time.
  
### Usage Instructions:
Index Finger: Move your index finger over a key to highlight it.
Thumb: Bring your thumb close to your index finger to press the highlighted key.
Caps Lock: Toggle the Caps Lock with the Caps key.
Language Switch: Toggle between English and Arabic layouts with the Lang key.
Backspace: Simulate the backspace action with the ⌫ key.

### Exit:
To exit the program, press the 'q' key.

## Future Enhancements:
Support for more languages and keyboard layouts.
Add support for more advanced key combinations (e.g., Shift, Ctrl).
Implement hand gesture recognition for other keyboard controls (e.g., number keys, symbols).
Screenshots:
(Include images or GIFs of the virtual keyboard in action)

Contributing:
Feel free to fork the repository, make changes, and create pull requests. All contributions are welcome!

This README provides an in-depth overview of the virtual keyboard project, explaining its functionality, and usage in detail.
