# 📚 ScholarAI: Predicting Citation Impact from Research Abstracts using NLP + Statistical Modeling

> Can we predict how much a research paper will be cited — just from its title and abstract?  
> **ScholarAI** uses NLP and machine learning to find out.

---

## 🎯 Project Goal

Predict the **citation count** of a paper using:
- 📝 Title
- 📄 Abstract
- 🔍 Metadata (year, authors, journal, venue, etc.)

And explore:  
**What makes a paper citable?**

---

## 🛠️ Technologies Used

- Python 3.8+
- Scikit-learn, XGBoost, LightGBM
- spaCy, BERT (Transformers)
- SHAP for explainability
- Streamlit (for interactive demo app)
- Pandas, NumPy, Matplotlib, Seaborn

---

## 📁 Project Structure

scholarai/

├── README.md # Project overview

├── requirements.txt # Dependencies

├── data/ # Raw & cleaned datasets

├── notebooks/ # Exploratory notebooks

├── src/ # Model training and utils

│ ├── train_model.py

│ └── preprocess.py

├── models/ # Saved ML models

└── app/ # Streamlit app


---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/AfsarJahan/scholarai.git
cd scholarai

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run training script
python src/train_model.py
