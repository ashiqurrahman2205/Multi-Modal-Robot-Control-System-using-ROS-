# 🐢 Voice-Controlled Turtlesim Simulator in ROS 2 Jazzy Jaliso 🎙️

Welcome to the **Voice-Controlled Turtlesim Simulator**! This project allows you to control the movements of a turtle in the classic `turtlesim` simulator using voice commands. It leverages **speech recognition** and **pyaudio** libraries to provide an engaging experience. 🐢✨

---

## 🚀 Features

- 🎙️ **Voice Commands**: Control the turtle using simple commands like `forward`, `backward`, `left`, and `right`.
- ⚙️ **ROS 2 Integration**: Built on the robust ROS 2 Jazzy Jaliso framework.
- 🖥️ **Python Powered**: Utilizes Python's `speechrecognition` and `pyaudio` for real-time speech-to-text functionality.

---

## 🛠️ Setup and Usage

Follow these steps to set up and run the Voice-Controlled Turtlesim Simulator:

### Step 1: Prerequisites
- Install **ROS 2 Jazzy Jaliso** on your system.
- Ensure Python 3 is installed with `pip`.

---

### Step 2: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Koushik-04KK/speechreco_turtle.git
cd speechreco_turtle
```

### Step 3: Install Required Python Packages
Install the necessary Python dependencies:
```bash
pip install speechrecognition pyaudio --break-system-packages
```

### Step 4: Run the Turtlesim Simulator
Open a terminal and start the turtlesim simulator node:
```bash
ros2 run turtlesim turtlesim_node
```

###Step 5: Run the Speech Recognition Script
In another terminal, execute the Python script for voice control:
```bash
python3 speech.py
```

### Step 6: Give Voice Commands
Speak the following commands to control the turtle:

forward: Move the turtle forward.

backward: Move the turtle backward.

left: Turn the turtle left.

right: Turn the turtle right.

Enjoy controlling the turtle hands-free with your voice! 🎉

🎉 Happy Learning!
This project is designed to be a fun and educational tool. I hope you enjoy the experience of controlling the turtle with your voice. 🐢✨

🖤 Contributing
Feel free to fork this repository, submit issues, or make pull requests to enhance this project.
