# Hand Gesture Recognition with Text-to-Speech

## Overview
This project implements a real-time hand gesture recognition system using OpenCV and a pre-trained Keras model. The system detects gestures through a webcam, classifies them into letters (A-Z), and announces the detected gesture using a text-to-speech engine. The model was trained using [Teachable Machine](https://teachablemachine.withgoogle.com/), an easy-to-use tool for building machine learning models.

## Features
- Detect and classify hand gestures in real-time.
- Use a pre-trained Keras model for accurate classification.
- Output the classified gesture both visually and audibly.

## Requirements
To run the project, install the required Python libraries:
```bash
pip install cvzone 
pip install mediapipe
pip install tensorflow
pip install pyttsx3
```

## Setup
1. **Model and Labels**: Place `keras_model.h5` and `labels.txt` in the `Model` directory.
2. **Run Scripts**: 
   - `project data.py`: Save processed hand images for training.
   - `projectTesting.py`: Perform real-time gesture recognition and text-to-speech.
3. Execute the script:
   ```bash
   python3 projectTesting.py
   ```

## File Structure
```
├── project data.py         # Script for saving hand images
├── projectTesting.py       # Real-time gesture recognition script
├── Model
│   ├── keras_model.h5     # Pre-trained gesture recognition model
│   ├── labels.txt         # Labels for the model
├── Data                   # Directory for storing hand images (used in training)
```

## Labels
The gesture labels supported by the model are:
```
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
```

## Usage
1. Point the webcam at your hand.
2. The system will detect the hand, classify the gesture, and announce the corresponding letter.
3. Press `s` while running `project data.py` to save cropped hand images for training purposes.

## Acknowledgments
This project utilizes:
- [CVZone](https://github.com/cvzone/cvzone) for hand tracking and classification.
- TensorFlow/Keras for gesture recognition.
- Pyttsx3 for text-to-speech functionality.

