# 🐍 Python Basics to Projects

A structured, hands-on Python learning journey progressing from programming fundamentals to practical applications and AI-powered projects.

## 🚀 About This Repository

**Python Basics to Projects** documents my progression from Python fundamentals to building real-world applications.

The repository covers:

* Python fundamentals
* Problem solving
* Object-Oriented Programming
* File handling
* Advanced Python
* Mini projects
* AI-powered applications

The goal is to develop strong foundations for **Artificial Intelligence, Machine Learning, and Software Development** through consistent practice and project-based development.

---

## 📚 Learning Path

```text
Python Fundamentals
        ↓
Problem Solving
        ↓
Object-Oriented Programming
        ↓
File Handling
        ↓
Advanced Python
        ↓
Mini Projects
        ↓
AI-Powered Applications
```

---

## 📂 Repository Structure

| Folder                | Description                          |
| --------------------- | ------------------------------------ |
| 🟦 `exercises`        | Python practice and problem solving  |
| 🟩 `file_handling`    | File reading, writing and management |
| 🟨 `object_oriented`  | Classes, objects and OOP             |
| 🟧 `oops-inheritance` | Inheritance concepts                 |
| 🟥 `ADVANCED_PYTHON1` | Advanced Python concepts             |
| 🟪 `python-projects`  | Mini Python projects                 |
| 🤖 `Mega Project 1`   | AI-powered voice assistant           |

---

# 🤖 Mega Project 1 — AI Voice Assistant

A Python-based AI voice assistant combining **voice interaction, AI responses, automation, system utilities and a graphical interface**.

### ✨ Features

* 🎙️ Voice command recognition
* ⌨️ Typed command input
* 🤖 AI responses using Groq
* 🖥️ Pygame graphical interface
* 🔊 Text-to-speech responses
* 🌐 Browser automation
* 📰 News retrieval
* 🎵 Music commands
* 🕐 Time information
* 💻 System monitoring
* ⚡ Real-time command processing

### 🧠 Architecture

```text
                 ┌─────────────────┐
                 │      User       │
                 └────────┬────────┘
                          ↓
              ┌───────────────────────┐
              │ Pygame GUI / Voice    │
              │      Input            │
              └───────────┬───────────┘
                          ↓
              ┌───────────────────────┐
              │   Command Processor   │
              └───────────┬───────────┘
                          ↓
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
   ┌─────────┐       ┌─────────┐      ┌─────────┐
   │  Groq   │       │  APIs   │      │ System  │
   │   AI    │       │  News   │      │ Utility │
   └────┬────┘       └────┬────┘      └────┬────┘
        └─────────────────┼─────────────────┘
                          ↓
              ┌───────────────────────┐
              │ Text + Voice Response │
              └───────────────────────┘
```

---

## 🛠️ Technology Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core application          |
| Pygame            | Graphical interface       |
| Groq API          | AI responses              |
| SpeechRecognition | Voice input               |
| pyttsx3           | Text-to-speech            |
| Requests          | API communication         |
| python-dotenv     | Environment configuration |
| Git & GitHub      | Version control           |

---

## 📁 Mega Project 1

```text
Mega Project 1/
│
├── main.py
├── jarvis_backend.py
├── jarvis_gui.py
├── musicLibrary.py
├── requirements.txt
├── .env.example
└── README.md
```

### 🔐 Security

API credentials are stored locally using environment variables.

```text
.env
```

is intentionally excluded from version control.

Never commit real API keys to GitHub.

---

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/bhoomijn/Python-Basics-to-Projects.git
```

### 2. Open the project

```bash
cd Python-Basics-to-Projects
cd "Mega Project 1"
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate it on Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file and add the required API credentials.

### 7. Run Jarvis

```bash
python jarvis_gui.py
```

---

## 🛠️ Concepts Demonstrated

* Python programming
* Functions and modules
* Exception handling
* API integration
* Environment variables
* Voice recognition
* Text-to-speech
* GUI development
* Event-driven programming
* System monitoring
* Web automation
* AI integration
* Modular project architecture

---

## 🎯 Learning Outcome

This project represents the transition from writing individual Python programs to designing a **multi-component application** involving APIs, external libraries, user interaction, voice processing and graphical interfaces.

---

# 📈 Future Learning Goals

The next stages of this journey include:

* Machine Learning
* Deep Learning
* Computer Vision
* Generative AI
* Data Science
* Advanced AI Applications

---

# 👩‍💻 About Me

**Bhoomi Jain**

Integrated M.Tech — Artificial Intelligence & Machine Learning
**VIT Bhopal University**

Interested in:

* 🤖 Artificial Intelligence
* 🧠 Machine Learning
* 🐍 Python
* 💻 Software Development
* 🚀 Building practical technology solutions

---

## 🔗 Connect

📧 **Email:** [bhoomijn4@gmail.com](mailto:bhoomijn4@gmail.com)

🔗 **LinkedIn:**
https://www.linkedin.com/in/bhoomi-jain-3287803b5

---

⭐ If you find this repository useful, consider giving it a star.
