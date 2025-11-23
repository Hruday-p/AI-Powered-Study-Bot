# AI-Powered Study Bot 🤖

An intelligent Streamlit-based study companion powered by Google's Gemini 2.5 Flash AI model. This bot helps students with various learning tasks including explanations, quiz generation, flashcard creation, study plans, and homework assistance.

## 📋 Overview

The AI-Powered Study Bot is designed to enhance your learning experience by providing instant, intelligent responses to study-related queries. Whether you need concept explanations, practice questions, or personalized study plans, this bot serves as your 24/7 study companion.

## ✨ Features

- **📚 Concept Explanations**: Get clear, detailed explanations of any topic or concept
- **🧪 Quiz Generator**: Generate custom quizzes with multiple-choice or open-ended questions
- **🗂️ Flashcard Creator**: Create study flashcards for memorization and quick review
- **📅 Study Plan Generator**: Receive personalized study schedules and plans
- **✏️ Homework Helper**: Get assistance with homework problems and assignments
- **💬 Interactive Chat**: Natural conversation interface for all study needs
- **⚡ Real-time Responses**: Streaming responses for fast, dynamic interactions
- **🎨 Modern UI**: Beautiful gradient design with custom styling

## 🔧 Requirements

### Python Libraries

```bash
streamlit
google-generativeai
```

### Installation

Install all dependencies using pip:

```bash
pip install streamlit google-generativeai
```

### API Key

You need a **Google Gemini API Key** to run this application:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create or sign in to your Google account
3. Generate a new API key
4. Add it to Streamlit secrets (see setup instructions below)

## 🚀 Quick Start

### 1. Set Up Streamlit Secrets

Create a `.streamlit/secrets.toml` file in your project directory:

```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```

### 2. Run the Application

```bash
streamlit run AI-powered-Study-Bot.py
```

The app will open in your browser at `http://localhost:8501`

## 🎮 How to Use

### Basic Usage

1. **Start the Application**: Run the Streamlit app using the command above
2. **Enter Your Question**: Type your study-related question in the text area
3. **Submit**: Click the "Ask Your Study Buddy 🚀" button
4. **View Response**: The AI will generate a response in real-time with a typewriter effect

### Example Prompts

#### 📚 Concept Explanation
```
"Explain photosynthesis in simple terms"
"What is Newton's third law of motion?"
"How does machine learning work?"
```

#### 🧪 Quiz Generation
```
"Generate a 5-question quiz on World War II"
"Create multiple choice questions about Python programming"
"Make a quiz on organic chemistry"
```

#### 🗂️ Flashcard Creation
```
"Create flashcards for Spanish vocabulary"
"Make flashcards for calculus formulas"
"Generate flashcards about the periodic table"
```

#### 📅 Study Plan
```
"Create a 2-week study plan for GATE exam preparation"
"Help me plan my studies for final exams"
"Make a study schedule for learning web development"
```

#### ✏️ Homework Help
```
"How do I solve this quadratic equation: x² + 5x + 6 = 0?"
"Explain how to write a persuasive essay"
"Help me understand this calculus problem"
```

## 🤖 AI Model

- **Model**: Google Gemini 2.5 Flash
- **Provider**: Google Generative AI
- **Capabilities**: 
  - Natural language understanding
  - Multi-domain knowledge
  - Context-aware responses
  - Fast inference speed
  - Streaming outputs

## 🎨 Features Breakdown

### 1. Streaming Response
The bot uses Gemini's streaming API to provide real-time, word-by-word responses for a more engaging user experience.

### 2. Custom Styling
- Modern gradient background (purple/lavender theme)
- Poppins font family for clean readability
- Responsive button design with hover effects
- Centered layout for focused interaction

### 3. Session State Management
Maintains conversation history using Streamlit's session state for context-aware responses.

### 4. Error Handling
Includes proper error handling for API calls and displays user-friendly error messages.

## 📊 Application Architecture

```
┌─────────────────────────────────────────────┐
│         Streamlit Web Interface             │
│  ┌───────────────────────────────────────┐  │
│  │     User Input Text Area              │  │
│  │  "Enter your study question here..."  │  │
│  └─────────────────┬─────────────────────┘  │
│                    │                         │
│                    ▼                         │
│  ┌─────────────────────────────────────┐    │
│  │    Google Gemini 2.5 Flash API      │    │
│  │  • Natural Language Processing      │    │
│  │  • Knowledge Retrieval              │    │
│  │  • Response Generation              │    │
│  └─────────────────┬─────────────────────┘  │
│                    │                         │
│                    ▼                         │
│  ┌─────────────────────────────────────┐    │
│  │    Streaming Response Display       │    │
│  │  • Real-time text generation        │    │
│  │  • Markdown formatting              │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

## 🔄 Customization

### Change AI Model
Modify the model initialization to use different Gemini models:
```python
model = genai.GenerativeModel("gemini-pro")  # Alternative model
```

### Adjust Styling
Edit the CSS in the `st.markdown()` section to customize colors, fonts, and layout:
```python
st.markdown("""
    <style>
        .header h1 { color: #your-color; }
        body { background: linear-gradient(135deg, #color1, #color2); }
    </style>
""", unsafe_allow_html=True)
```

### Add System Prompt
Configure the model with a system instruction for specialized behavior:
```python
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are a helpful tutor specializing in mathematics..."
)
```

## 💡 Use Cases

- **Students**: Quick homework help and concept clarification
- **Teachers**: Generate quiz questions and study materials
- **Self-Learners**: Create personalized study plans and flashcards
- **Exam Preparation**: Practice questions and topic reviews
- **Language Learning**: Vocabulary practice and grammar explanations

## 🛠️ Troubleshooting

### API Key Errors
- Verify your API key is correctly added to `secrets.toml`
- Ensure no extra spaces or quotes around the key
- Check that your API key is active in Google AI Studio

### Import Errors
- Install required packages: `pip install streamlit google-generativeai`
- Ensure you're using Python 3.8 or higher

### Streaming Issues
- Check your internet connection
- Verify Gemini API service status
- Try refreshing the page if responses freeze

### No Response Generated
- Ensure your query is clear and study-related
- Check API rate limits haven't been exceeded
- Verify the model name is correct (`gemini-2.5-flash`)

## 🔐 Security Notes

- **Never commit `secrets.toml`** to version control
- Add `.streamlit/` to your `.gitignore` file
- Use environment variables for production deployments
- Monitor API usage to avoid unexpected charges

### Example .gitignore
```
.streamlit/
secrets.toml
__pycache__/
*.pyc
```

## 📚 Technical Details

- **Framework**: Streamlit 1.x
- **AI Provider**: Google Generative AI
- **Model**: Gemini 2.5 Flash
- **Language**: Python 3.8+
- **Response Mode**: Streaming
- **UI Style**: Custom CSS with gradient themes

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub (without secrets)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add `GEMINI_API_KEY` to Streamlit Cloud secrets
5. Deploy!

### Local Development

```bash
# Clone repository
git clone <your-repo-url>
cd <your-repo>

# Install dependencies
pip install -r requirements.txt

# Add API key to secrets.toml
echo 'GEMINI_API_KEY = "your-key"' > .streamlit/secrets.toml

# Run app
streamlit run AI-powered-Study-Bot.py
```

## 📝 Requirements.txt

Create a `requirements.txt` file for easy dependency management:

```
streamlit>=1.28.0
google-generativeai>=0.3.0
```

## 👨‍💻 Author

Developed to demonstrate AI-powered educational assistance using Google's Gemini API and Streamlit framework.

## 📄 License

This project is available for educational and personal use.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 🙏 Acknowledgments

- **Google Gemini AI**: For providing the powerful language model
- **Streamlit**: For the amazing web app framework
- **Community**: For feedback and suggestions

---

**Note**: Ensure you comply with Google's AI usage policies and rate limits when using the Gemini API. This application is for educational purposes and demonstrates basic integration of generative AI with web applications.