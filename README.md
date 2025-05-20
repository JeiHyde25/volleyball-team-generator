
# 🏐 Volleyball Team Generator

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange)

An AI-powered Streamlit application that helps coaches and players create fair and balanced volleyball teams based on player positions and skill levels. Built using LangChain and OpenAI for intelligent team balancing and reasoning.

🚀 [Live Demo](https://your-app-url.onrender.com) <!-- Replace with actual Render URL -->

---

## 📁 Project Structure

```
volleyball-team-generator/
├── prompts/
│   └── team_balance.txt
├── src/
│   ├── app.py
│   ├── generator.py
│   ├── utils.py
│   ├── player.py
│   └── config.py
├── tests/
│   └── test_generator.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🔧 Features

- 🧑‍🤝‍🧑 Input player names, positions, and skill levels
- ⚖️ Generate balanced teams using AI logic
- 💬 Optional explanation output from LLM
- 📤 Export team lists (future)
- 🧪 Extensible architecture for scoring systems

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
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run src/app.py
```

---

## 📦 Docker

```bash
docker build -t volleyball-generator .
docker run -p 8080:8080 volleyball-generator
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
