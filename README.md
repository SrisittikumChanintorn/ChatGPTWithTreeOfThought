# ChatGPT with Tree of Thought (ToT) Implementation

A Python implementation that leverages ChatGPT's language capabilities combined with the Tree of Thought technique to solve complex analytical problems. This project demonstrates how GenAI can analyze multi-faceted questions by breaking them down into branches and sub-branches for comprehensive evaluation.

## 📋 Project Overview

This program implements the Tree of Thought technique with ChatGPT to solve complex problems requiring critical thinking and consideration of multiple factors. The current implementation analyzes the potential impact of a Chinese price war on Thailand's economy through multiple analytical branches.

## 🧠 Understanding Tree of Thought

The Tree of Thought (ToT) methodology follows these key steps:

1. **Root Question**: Submit a complex problem to the LLM
2. **Branch Identification**: Break down the problem into relevant branches/factors
3. **Sub-branch Analysis**: Explore each branch with specialized prompting
4. **Integration**: Combine insights from all branches
5. **Conclusion**: Generate a comprehensive solution

## 📁 Project Structure

```bash
.
├── main.py                  # Main execution script
├── requirements.txt         # Dependencies
├── tree_of_thought.py       # Core ToT implementation
└── README.md                # Project documentation
```

## 💻 Implementation Details

The implementation consists of:

1. **Main Script** (`main.py`):
   - Sets up API authentication with OpenAI
   - Defines the root question about Chinese price war impacts
   - Configures model parameters
   - Creates branch and sub-branch structure
   - Processes and assembles the final response

2. **Branch Structure**:
   - **Domestic Market Competition**
     - Price Undercutting
     - Market Share Losses
     - Innovation and Quality Improvement
   - **Consumer Behavior**
     - Demand for Cheaper Goods
     - Disposable Income and Spending Patterns
     - Brand Loyalty and Perception

3. **Processing Flow**:
   - Each branch has specialized system instructions to analyze from specific perspectives
   - Sub-branches examine focused aspects within each branch domain
   - Branches are analyzed independently and then combined
   - Developer can manually remove sub-branches with unsatisfactory responses
   - Final conclusion synthesizes all insights into a comprehensive analysis

## 🚀 Installation & Usage

### Prerequisites
- Python 3.11.6
- OpenAI API Key

## Installation and Usage 🚀

### Setup 🛠️ 

1. Clone this project to your repository:

### Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
```

2. Activate Virtual Environment (venv) 📦 
   
```bash
source venv/bin/activate  # On MacOS use this
venv\Scripts\activate     # On Windows use this 
```

3. Install dependencies ⬇️
```bash
pip install -r requirements.txt
```


4. Configure API key 🔑
   
#### Edit `main.py` with your API key

5. Run the analysis ▶️

```bash
python main.py
```
    
## 📊 How It Works

The implementation uses a structured approach where:

1. Each perspective function (like `domestic_market_competition`, `price_undercutting`, etc.) creates specific prompts for ChatGPT
2. Each function includes custom system content to guide ChatGPT's analysis from that particular perspective
3. The main script assembles all branch outputs into a final query
4. The `make_conclusion` function synthesizes all branches into a comprehensive analysis

## 🔄 Customization

The project is designed for easy adaptation to other complex analytical questions:

1. Modify the root question in `main.py`
2. Adjust branch functions in `tree_of_thought.py` to match your new question
3. Configure branch-specific prompts to guide ChatGPT's specialized analysis
4. Adjust the final query assembly to include all relevant perspectives

## 📝 Example Usage

#### This implementation analyzes Chinese price war impacts through perspectives like:

##### Domestic Market Competition
- Price undercutting
- Market share losses
- Innovation and quality improvement

##### Consumer Behavior
- Demand for cheaper goods
- Disposable income and spending patterns
- Brand loyalty and perception

### Implementation Process:

1. **Root Question Exploration**: First, we submit our root question to an LLM with instructions to identify only the most relevant issues (branches) related to the impact of a Chinese price war on Thailand's economy.

2. **Branch-Specific Analysis**: Each identified branch (e.g., Domestic Market Competition, Consumer Behavior) is then analyzed by an LLM with customized instructions specific to that perspective, producing detailed explanations (sub-branches) for each aspect.

3. **Synthesis and Conclusion**: Finally, all sub-branch insights are compiled and processed by an LLM with summarization instructions to produce a comprehensive, integrated analysis that addresses the root question from multiple perspectives.
   

## 🔍 Optimization Techniques

1. **Prompt Engineering**: Each branch uses carefully crafted system content
2. **Selective Branches**: Developer can manually include/exclude branches
3. **Parameter Tuning**: Configurable model name and token limits
4. **Structural Organization**: Clear separation of concerns between branches
