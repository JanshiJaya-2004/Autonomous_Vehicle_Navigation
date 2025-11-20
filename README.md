# 🚗 Autonomous Vehicle Navigation System  
### Real-Time Obstacle Detection & Navigation Using YOLO + OpenCV + Reinforcement Learning + Streamlit Dashboard

This project implements an **Autonomous Vehicle Navigation System** capable of detecting obstacles and making navigation decisions using **AI and Computer Vision**.

The system uses:

- **YOLO Object Detection** – Detects pedestrians, vehicles, obstacles, mobile phones, etc.  
- **OpenCV** – Real-time camera processing  
- **Reinforcement Learning (RL)** – Decision-making model to navigate safely  
- **Streamlit Dashboard** – Live display of camera feed + detections + vehicle status  
- **Python** – Core development language  

---

##  Demo Output

### **Live Camera Feed with Obstacle Detection**
The dashboard visualizes real-time detection:

- Bounding boxes around detected objects  
- Class label (e.g., person, cell phone, vehicle)  
- Confidence score (e.g., 1.00, 0.98)

> **Confidence Score** = How sure YOLO is about the detection (NOT object size).

---

##  Features

- Real-time obstacle detection from camera feed  
- Detects person, vehicles, cell phones, objects  
- Displays confidence levels and bounding boxes  
- Reinforcement Learning–based navigation logic  
- Live dashboard view using Streamlit  
- Speed, Steering Angle, Reward visualization  
- Emergency stop & vehicle control buttons  

---

##  Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3.11 |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8 |
| UI / Dashboard | Streamlit |
| ML / AI | Reinforcement Learning (DQN / PPO) |
| Libraries | NumPy, cv2, torch, protobuf |
| Optional Simulator | CARLA |

---

##  Project Structure
clg_project/
│── autonomous_vehicle_rl/
│   │── av_env/
│   │── camera/
│   │── detection/
│   │   ├── yolo_detection.py
│   │   └── __pycache__/
│   │── yolo_weights/
│   │   ├── coco.names
│   │   ├── yolov3.cfg
│   │   ├── yolov3.weights
│   │── env/
│   │── navigation/
│   │── rl_training/
│   │   ├── model/
│   │   ├── train.py
│   │── utils/
│   │   ├── image_processing.py
│   │   ├── reward_function.py
│   │   └── __pycache__/
│
│── dashboard.py
│── main.py
│── requirements.txt
│── *.zip (backup folders)

INSTALLATION -

1️⃣ Create a virtual environment
python -m venv av_env

2️⃣ Activate it
av_env\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run the Project
1. Run Object Detection
python autonomous_vehicle_rl/detection/yolo_detection.py

2. Run Training
python autonomous_vehicle_rl/rl_training/train.py

3. Run Dashboard
streamlit run dashboard.py

4. Run Main Auto Navigation
python main.py

