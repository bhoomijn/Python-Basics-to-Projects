# 🐍 Python Basics to Projects

<p align="center">
  <strong>A hands-on journey from Python fundamentals to AI-powered applications.</strong>
</p>

<p align="center">
  <a href="https://github.com/bhoomijn/Python-Basics-to-Projects">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <img src="https://img.shields.io/badge/Focus-AI%20%2F%20ML-8A2BE2?style=for-the-badge" alt="AI/ML">
  <img src="https://img.shields.io/badge/Status-Active-2EA44F?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/github/license/bhoomijn/Python-Basics-to-Projects?style=for-the-badge" alt="License">
</p>

<p align="center">
  <a href="#-about">About</a> •
  <a href="#-learning-path">Learning Path</a> •
  <a href="#-featured-project">Featured Project</a> •
  <a href="#-repository-structure">Structure</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 👋 About

**Python Basics to Projects** is my hands-on Python learning repository.

Instead of stopping at syntax and theory, this repository follows a progression from **fundamentals → problem solving → software concepts → practical applications → AI-powered projects**.

The goal is simple:

> **Learn by building.**

Every stage of the repository represents a step toward becoming a stronger **AI/ML and software developer**.

---

## 🧭 Learning Path

```text
┌──────────────────────┐
│  Python Fundamentals │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Problem Solving      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ OOP & Inheritance    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ File Handling        │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Advanced Python      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Practical Projects   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ AI-Powered Projects  │
└──────────────────────┘
```

---

# ⭐ Featured Project

## 🤖 Mega Project 1 — AI Voice Assistant

The first major project in this repository is a **Python-based AI voice assistant** designed to combine conversational AI with everyday computer interaction.

It brings together multiple Python concepts and external services into one application.

### What it can do

| Capability           | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| 🎙️ Voice Input      | Accepts commands through the microphone                    |
| ⌨️ Text Input        | Allows commands to be typed                                |
| 🧠 AI Responses      | Uses Groq-powered AI for questions and explanations        |
| 🔊 Voice Output      | Converts responses into speech                             |
| 🖥️ GUI              | Interactive Pygame-based interface                         |
| 🌐 Web Automation    | Opens commonly used websites                               |
| 📰 News              | Retrieves current news through an API                      |
| 🎵 Music             | Handles predefined music commands                          |
| 🕐 Time              | Provides the current time                                  |
| 💻 System Info       | Reports system information such as CPU, RAM and battery    |
| ⚡ Command Processing | Routes different commands to the appropriate functionality |

---

## 🧠 How Mega Project 1 Works

```text
                         USER
                           │
              ┌────────────┴────────────┐
              │                         │
        🎙️ Voice Input             ⌨️ Text Input
              │                         │
              └────────────┬────────────┘
                           ↓
                  COMMAND PROCESSOR
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
      🤖 AI Engine      🌐 APIs         💻 System
          │                │                │
       Groq AI         News API        CPU / RAM /
                                        Battery
          └────────────────┼────────────────┘
                           ↓
                  RESPONSE GENERATION
                           │
                  ┌────────┴────────┐
                  ↓                 ↓
             🖥️ GUI Output     🔊 Voice Output
```

---

## 🖥️ Interface

The project includes a dedicated **Pygame interface** with:

* Animated AI orb
* Assistant status
* Voice interaction
* Text command input
* Send button
* Microphone button
* AI response display

> Add your actual project screenshot here:

```text
docs/
└── jarvis-dashboard.png
```

Then place it in the README:

```markdown
![Jarvis Interface](docs/jarvis-dashboard.png)
```

---

## 🛠️ Tech Stack

### Core

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pygame-1C1C1C?style=flat-square&logo=python&logoColor=white">
</p>

### AI & APIs

<p>
<img src="https://img.shields.io/badge/Groq%20API-F55036?style=flat-square">
<img src="https://img.shields.io/badge/REST%20APIs-02569B?style=flat-square">
</p>

### Python Libraries

```text
SpeechRecognition
pyttsx3
requests
python-dotenv
pygame
```

### Development

```text
Git
GitHub
VS Code
Virtual Environment
```

---

# 📂 Repository Structure

```text
Python-Basics-to-Projects/
│
├── exercises/
│   └── Python practice & problem solving
│
├── file_handling/
│   └── File-based Python programs
│
├── object_oriented/
│   └── OOP concepts and implementations
│
├── oops-inheritance/
│   └── Inheritance examples
│
├── ADVANCED_PYTHON1/
│   └── Advanced Python concepts
│
├── python-projects/
│   └── Mini Python projects
│
├── Mega Project 1/
│   ├── main.py
│   ├── jarvis_backend.py
│   ├── jarvis_gui.py
│   ├── musicLibrary.py
│   ├── requirements.txt
│   └── .env.example
│
├── tests/
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🧩 Concepts Practiced

### Python

* Variables & Data Types
* Conditional Logic
* Loops
* Functions
* Modules
* Exception Handling

### Software Development

* Modular programming
* Environment configuration
* API integration
* Event-driven programming
* GUI development
* Input validation
* Error handling
* Version control

### AI / Automation

* AI API integration
* Voice recognition
* Text-to-speech
* Natural-language commands
* Computer automation
* System monitoring

---

# 🔐 Security

API credentials are **never stored directly in source code**.

Local credentials are loaded through environment variables:

```env
GROQ_API_KEY=your_api_key
NEWS_API_KEY=your_api_key
```

The real `.env` file should remain local and must **not** be committed to GitHub.

A safe template can be provided as:

```text
.env.example
```

---

# 🚀 Running Mega Project 1

### 1. Clone the repository

```bash
git clone https://github.com/bhoomijn/Python-Basics-to-Projects.git
```

### 2. Enter the project

```bash
cd "Python-Basics-to-Projects/Mega Project 1"
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate it

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API keys

Create `.env`:

```env
GROQ_API_KEY=your_groq_key
NEWS_API_KEY=your_news_api_key
```

### 7. Launch the GUI

```bash
python jarvis_gui.py
```

---

# 📌 Current Status

| Area               | Status       |
| ------------------ | ------------ |
| Python Core        | ✅            |
| Voice Commands     | ✅            |
| Typed Commands     | ✅            |
| AI Integration     | ✅            |
| News API           | ✅            |
| System Information | ✅            |
| Text-to-Speech     | ✅            |
| Pygame GUI         | ✅            |
| GitHub Repository  | ✅            |
| Documentation      | 🔄 Improving |

---

# 🗺️ Roadmap

The repository will continue evolving toward more advanced applications.

```text
✅ Python Fundamentals
        ↓
✅ Practical Python Projects
        ↓
✅ AI Voice Assistant
        ↓
🔄 Machine Learning
        ↓
🔄 Computer Vision
        ↓
🔄 Generative AI
        ↓
🔄 Advanced AI Applications
```

---

# 🎯 Long-Term Goal

Build a portfolio demonstrating not only the ability to **write Python code**, but also the ability to:

* Understand problems
* Design solutions
* Integrate technologies
* Build usable applications
* Document projects
* Maintain clean code
* Continuously learn and improve

---

# 👩‍💻 About Me

### Bhoomi Jain

**Integrated M.Tech — Artificial Intelligence & Machine Learning**
**VIT Bhopal University**

Interested in:

**Artificial Intelligence · Machine Learning · Python · Software Development · Generative AI**

---

## 🔗 Connect

📧 **Email:** [bhoomijn4@gmail.com](mailto:bhoomijn4@gmail.com)

💼 **LinkedIn:**
[linkedin.com/in/bhoomi-jain-3287803b5](https://www.linkedin.com/in/bhoomi-jain-3287803b5)

---

## ⭐ Support

If you find this repository useful or interesting, consider giving it a ⭐.

---

<p align="center">
  <i>Learning Python. Building projects. Moving toward AI.</i>
</p>
