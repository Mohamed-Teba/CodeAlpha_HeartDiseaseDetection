# ❤️ Heart Disease Detection

This project detects heart disease using both **Machine Learning models** and a **Rule-Based Expert System**. It includes data preprocessing, model training, accuracy comparison, and an interactive UI for predictions.

## 🚀 How to Run

1. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model**
   ```bash
   python ml_model/train_model.py
   ```

3. **Predict**
   ```bash
   python ml_model/predict.py
   ```

4. **Run the Expert System**
   ```bash
   python rule_based_system/expert_system.py
   ```

5. **Launch the UI**
   ```bash
   streamlit run ui/app.py
   ```

## 📁 Project Structure

```
heart-disease-detection/
├── data/                  # Datasets
├── ml_model/              # Machine Learning scripts
├── rule_based_system/     # Expert system code
├── notebooks/             # Data analysis and training
├── reports/               # Accuracy comparison and visuals
├── ui/                    # User Interface
├── utils/                 # Helper functions
└── requirements.txt
```

## 📊 Accuracy

See [`reports/accuracy_comparison.md`](reports/accuracy_comparison.md) for detailed model performance.
