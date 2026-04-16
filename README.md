# Real-Time-Stress-Detection-Using-Facial-Expressions

# Project Overview

Mental stress has become a common issue in modern life, especially among students and working professionals. Detecting stress early can help individuals manage their mental well-being and improve productivity.

This project presents a real-time stress detection system that analyzes facial expressions using computer vision and deep learning techniques. The system captures facial images through a webcam, detects faces using OpenCV, and classifies emotions using a Convolutional Neural Network trained on the FER-2013 dataset. Based on the detected emotion, the system estimates the user's stress level and provides suggestions to help reduce stress.

# Objectives

The main objectives of this project are:

To detect human faces from a live webcam feed.

To classify facial expressions using a trained deep learning model.

To estimate stress levels based on emotional states.

To provide suggestions to help users manage stress.

# Technologies Used

Programming Language:
Python

Libraries and Frameworks:
OpenCV  
TensorFlow / Keras  
NumPy  
Flask  

Frontend:
HTML  
CSS  
JavaScript  

Dataset:
FER-2013 Facial Expression Dataset

# System Workflow

The system works through the following steps:

1. The webcam captures real-time video input.
2. OpenCV detects faces using the Haarcascade classifier.
3. The detected face is processed and fed into the trained CNN model.
4. The model predicts the emotion displayed on the face.
5. The predicted emotion is mapped to a stress level.
6. The system displays suggestions to help the user reduce stress.

# Project Structure

Real-Time-Stress-Detection/

app.py  
emotion_stress.py  
haarcascade_frontalface_default.xml  

templates/  
index.html  

# Dataset

This project uses the FER-2013 dataset for emotion recognition. The dataset contains thousands of labeled grayscale facial images categorized into different emotional expressions.

The emotion categories include:

Angry  
Disgust  
Fear  
Happy  
Sad  
Surprise  
Neutral

These emotions are used by the system to determine stress levels.

# Features

Real-time facial emotion detection  
Stress level estimation  
Interactive web interface  
Automatic stress reduction suggestions  
Live webcam analysis

# Applications

Mental health monitoring systems  
Student stress tracking tools  
Workplace well-being analysis  
Human-computer interaction research  
AI-based health monitoring systems

# Future Improvements

Improving model accuracy using advanced deep learning architectures.

Adding physiological data such as heart rate for better stress estimation.

Developing a mobile application version of the system.

Enhancing personalization of stress management recommendations.

# Author

Aasritha Devi Narra  
B.Tech Computer Science and Engineering (Artificial Intelligence and Machine Learning)  
SRK Institute of Technology

# Research Work

This project is currently being developed as part of undergraduate research and is in the process of being submitted to an academic conference.
