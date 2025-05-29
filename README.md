# 🏐 Volleyball Team Generator

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)  
![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange)  
[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

An AI-powered Streamlit application that helps coaches and players create fair and balanced volleyball teams based on player positions and skill levels. Built using LangChain and OpenAI for intelligent team balancing and reasoning.

🌐 **[Live Demo](https://volleyball-team-generator-n9ny.onrender.com)**

---

## 📁 Project Structure

```
volleyball-team-generator/
├── prompts/
│   └── team_balance.txt
├── src/
│   ├── app.py
│   ├── form_logic.py
│   ├── player.py
│   └── player.py
├── tests/
│   ├── form_logic.py
│   ├── test_player.py
│   └── test_player_manager.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.in
├── requirements.txt
├── requirements-dev.in
└── requirements-dev.txt
└── setup-dev-env.sh
```

---

## 🔧 Features

- 🧑‍🤝‍🧑 Input player names, positions, and skill levels
- ⚖️ Generate balanced teams using AI logic
- 💬 Optional explanation output from LLM
- 📤 Export team lists *(coming soon)*
- 🧪 Extensible architecture for scoring systems
- 🧍 Player entity abstraction and validation logic

---

## 🚀 Tech Stack

- **Python 3.13**
- **Streamlit**
- **LangChain**
- **OpenAI API**
- **Docker**
- **GitHub Actions**

---

## 🛠️ Getting Started (Local)

### 1. Clone the repository

```bash
git clone https://github.com/JeiHyde25/volleyball-team-generator.git
cd volleyball-team-generator
```

### 2. Install dependencies
# Requires Python 3.13+ and pip-tools
```bash
# First, install pip-tools (if not already installed)
pip install pip-tools

# Compile both runtime and dev requirements
pip-compile requirements.in
pip-compile requirements-dev.in

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Alternatively, run:
./setup-dev-env.sh

### 3. Set up Git hooks (optional but recommended)
```bash
pre-commit install
```

### 4. Run the app
```bash
PYTHONPATH=. streamlit run src/app.py
```

---

## 📦 Docker

```bash
docker build -t volleyball-team-generator .
docker run -p 8080:8080 volleyball-team-generator
```

---

## 🧪 Future Improvements

- Position balancing weight system
- Export to CSV
- Player ranking logic
- Team history tracking

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

**Harold Tago**  
[GitHub: JeiHyde25](https://github.com/JeiHyde25)

---

## 📫 Contact

For inquiries or collaboration, reach out via GitHub or [LinkedIn](https://linkedin.com/in/your-profile)
