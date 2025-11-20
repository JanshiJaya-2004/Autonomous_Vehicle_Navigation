import streamlit as st
import cv2
import numpy as np
from detection.yolo_detection import detect_objects

st.set_page_config(page_title="Autonomous Vehicle Dashboard", layout="wide")

st.markdown("""
    <h2 style='text-align:center; color:#00a3ff;'>Autonomous Vehicle Navigation System</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

# CAMERA COLUMN 
with col1:
    st.subheader(" Live Camera Feed with Obstacle Detection")
    frame_window = st.empty()

    camera = cv2.VideoCapture(0)

    # Streamlit loop
    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            st.error("Camera not found!")
            break

        # Detect objects (must return processed image!)
        output_frame = detect_objects(frame)

        # Display output image
        frame_window.image(output_frame, channels="BGR")

# STATUS PANEL
with col2:
    st.subheader("Vehicle Status")
    st.metric("Speed", "35 km/h")
    st.metric("Steering Angle", "0.12 rad")
    st.metric("Reward", "+0.83", delta="0.05")

    st.subheader(" Navigation Controls")
    st.button("Start Vehicle")
    st.button("Stop Vehicle")
    st.button("Emergency Brake")

    st.subheader("⚙ Settings")
    confidence = st.slider("Detection Confidence", 0.1, 1.0, 0.5)
    st.write("FPS:", 30)
