# 📚 ScholarAI: Predicting Citation Impact from Research Abstracts using NLP & Statistical Modeling

**Can we predict how often a research paper will be cited — using just its title, abstract, and metadata?**

**ScholarAI** is an academic machine learning project that explores this question using NLP, explainable AI, and gradient boosting. Built by a Master’s student in Statistics & Data Analytics, it aims to model what makes scientific work *citable*.

---

## 🎯 Project Goal

To predict the **future citation count** of a paper using:

- 📝 Title
- 📄 Abstract
- 🔍 Metadata (year, authors, journal, venue, etc.)

And explore:

> **What makes some papers more cited than others?**

---

## 🛠️ Technologies Used

- Python 3.8+
- Scikit-learn, XGBoost, LightGBM
- spaCy, BERT (Transformers)
- SHAP (for interpretability)
- Pandas, NumPy, Matplotlib, Seaborn
- Streamlit (for interactive UI)

---

## 📁 Project Structure



scholarai/

├── README.md # Project overview

├── requirements.txt # Dependencies

├── data/ # Raw and cleaned datasets

├── notebooks/ # EDA and experiments

├── src/ # Preprocessing and training scripts

│ ├── train_model.py

│ └── preprocess.py

├── models/ # Saved ML models

└── app/ # Streamlit app

---


---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/AfsarJahan/scholarai.git
cd scholarai

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate   # on macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the model
python src/train_model.py

# 5. Launch the app
streamlit run app/app.py

---


---
## 📈 Demo Coming Soon

An interactive web app will let you input a paper's title and abstract — and get a predicted citation count, plus SHAP visualizations for interpretability.

## 👩‍💻 Author

**Afsar Jahan**  
🎓 MSc Statistics & Data Analytics | UG Gold Medalist  
🔗 [GitHub](https://github.com/AfsarJahan) | [LinkedIn](#)

## ⭐ Show Some Love

If you find this project helpful or interesting, consider giving it a ⭐ on GitHub or sharing it with others!
