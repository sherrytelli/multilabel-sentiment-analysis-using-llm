# 🧠 Multi-Label Semantic Analyzer using LLM

A robust, local-run Python application that performs multi-label sentiment and topic classification using Large Language Models (LLMs) powered by [Ollama](https://ollama.com/). 

This project allows you to input news headlines, paragraphs, or mixed content, and receive structured feedback categorizing the text into up to seven distinct domains with a confidence score.

## ✨ Features

*   **Multi-Label Classification**: Identifies multiple relevant categories within a single input (e.g., tagging a text as both `Technology` and `Business`).
*   **Confidence Scoring**: Returns a relevance score (0–100%) for each assigned label.
*   **Local Execution**: Runs entirely on your machine using `phi3:3.8b` via Ollama. No API keys required; completely private.
*   **Robust JSON Parsing**: Utilizes a custom stack-based brace-matching algorithm to extract clean JSON from noisy LLM outputs.
*   **Strict Validation**: Automatically filters out hallucinations or invalid tags that do not match the predefined schema.

## 📂 Project Structure

```text
multilabel-sentiment-analysis-using-llm/
|
├── classifier.py          # Main execution script (CLI interface)
└── semantic_analyzer.py   # Core logic class (Prompt handling, LLM calling, Parsing)
```

## 🚀 Getting Started

### Prerequisites
Before running this project, ensure you have the following installed:
1.  **Python 3.12+**
2.  **[Ollama](https://ollama.com/download)** (Running locally)

### Installation

#### 1. Setup Virtual Environment
It is recommended to isolate dependencies using a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 2. Install Dependencies
```bash
pip install ollama
```

#### 3. Download the AI Model
The analyzer relies on the **Phi-3-mini** model optimized for 3.8B parameters. Download it by running:

```bash
ollama pull phi3:3.8b
```

## 💻 Usage

Run the main classifier script:

```bash
python classifier.py
```

**Interactive Mode:**
You will be prompted to enter text. You can provide news snippets, short sentences, or paragraphs.

**Example Session:**
```text
enter text: Apple just announced a new AI chip that improves battery life while lowering energy costs globally.

Bot: label: Technology, confidence: 92%
Bot: label: Business, confidence: 78%
Bot: label: Health, confidence: 25%

enter text:
```

**Exit:** Type `exit` to stop the bot.

## ⚙️ Under the Hood

### System Prompt & Constraints
The system utilizes a highly restrictive System Prompt to force the LLM into behaving like a deterministic data engine rather than a conversational assistant. Key rules include:
*   **Schema Adherence**: Strict JSON structure (`{"labels": [], "confidence": []}`).
*   **Single vs. Multi**: Instructed to prefer single labels unless multiple are strongly supported by the text.
*   **Output Hygiene**: Explicit commands to avoid markdown or explanations.

### Custom JSON Extraction
Large Language Models often append conversational filler (e.g., *"Here is the JSON:"*). To prevent parsing errors, `semantic_analyzer.py` implements a **stack-based parser**:
1.  It finds the first `{` character.
2.  It iterates through the string, incrementing/decrementing a counter for every `{` or `}` found.
3.  When the counter returns to zero, it isolates the valid JSON object, ignoring all trailing garbage text.

### Data Sanitization
To ensure data integrity, the results are passed through a validation layer. If the model returns an unknown category (e.g., `"SportsNews"` instead of `"Sports"`), it is discarded to maintain database cleanliness.

## 🏷️ Supported Categories

| Category | Description |
|----------|-------------|
| **Technology** | Gadgets, Software, AI, Internet |
| **Sports** | Athletes, Leagues, Matches |
| **Education** | Schools, Universities, Learning |
| **Business** | Markets, Stocks, Corporate |
| **Health** | Medicine, Wellness, Biology |
| **Politics** | Government, Laws, Policy |
| **Entertainment** | Movies, Music, Celebrities |

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.