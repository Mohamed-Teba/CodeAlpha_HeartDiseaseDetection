import streamlit as st
import pandas as pd
import os
from experta import *
import matplotlib.pyplot as plt
import seaborn as sns
class HealthRiskExpert(KnowledgeEngine):
    result = "No Risk Detected"
    @Rule(Fact(cp_1=True) & Fact(thal_3=True))
    def high_risk(self):
        self.result = "High Risk detected!"
    @Rule(Fact(oldpeak=P(lambda x: x > 2.5)))
    def high_oldpeak(self):
        self.result = "Warning: High oldpeak value detected!"
    @Rule(Fact(exang=1) & Fact(thalach=P(lambda x: x < 100)))
    def exang_thalach_risk(self):
        self.result = "Moderate Risk: Exang and low thalach detected!"
file_path = r"C:\Users\mrahm\Documents\heart_disease_data.csv"
def load_data():
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return pd.DataFrame()
def plot_data(df, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df[column], bins=20, kde=True, ax=ax, color='skyblue')
    ax.set_title(f"Distribution of {column}")
    st.pyplot(fig)
def main():
    st.title("🩺 Heart Disease Risk Prediction")
    st.sidebar.header("User Input")
    cp_1 = st.sidebar.selectbox("cp_1", [True, False])
    thal_3 = st.sidebar.selectbox("thal_3", [True, False])
    oldpeak = st.sidebar.slider("oldpeak", -3.0, 3.0, 0.0)
    exang = st.sidebar.selectbox("exang", [0, 1])
    thalach = st.sidebar.slider("thalach", 60, 220, 150)
    slope_2 = st.sidebar.selectbox("slope_2", [True, False])
    target = st.sidebar.selectbox("target", [0, 1])
    if st.sidebar.button("Predict Risk"):
        engine = HealthRiskExpert()
        engine.reset()
        engine.declare(Fact(cp_1=cp_1), Fact(thal_3=thal_3), Fact(oldpeak=oldpeak), Fact(exang=exang),
                       Fact(thalach=thalach), Fact(slope_2=slope_2), Fact(target=target))
        engine.run()
        st.success(f"🚨 {engine.result}")
        new_data = pd.DataFrame([{"cp_1": cp_1, "thal_3": thal_3, "oldpeak": oldpeak,
                                  "exang": exang, "thalach": thalach, "slope_2": slope_2, "target": target}])
        if os.path.exists(file_path):
            new_data.to_csv(file_path, mode='a', header=False, index=False)
        else:
            new_data.to_csv(file_path, index=False)
        st.sidebar.success("✅ Data Saved!")
    st.subheader("📊 Dynamic Data Visualization")
    df = load_data()
    if not df.empty:
        st.dataframe(df.tail())
        column_to_plot = st.selectbox("Select Column to Visualize", df.columns)
        plot_data(df, column_to_plot)
    else:
        st.warning("No data available yet. Enter some inputs to populate the dataset.")
if __name__ == "__main__":
    main()
