# House Price Prediction Using Linear Regression 🏠

A machine learning project to predict house prices based on land area using a Linear Regression algorithm. The project includes a trained model, data visualization, and an interactive Streamlit web application for user-friendly predictions.

---

## 📌 Project Overview

This project leverages a single-variable Linear Regression model to predict house prices based on land area (in square feet). The dataset contains **1,460 entries** with land areas ranging from **1,300 to 215,245 sq.ft.** and corresponding house prices.

- The model was trained in **Google Colab**
- Visualized using **Matplotlib**
- Deployed as an interactive **Streamlit** app for real-time predictions

---

## 🚀 Features

- **Data Analysis**: Summarizes dataset statistics and visualizes the relationship between land area and price  
- **Machine Learning**: Implements Linear Regression using `scikit-learn` to predict house prices  
- **Interactive UI**: A Streamlit app allows users to input land area and view predicted prices  
- **Visualization**: Scatter plots to explore the dataset using `Matplotlib`  
- **Model Persistence**: Saves the trained model as `house_price_model.pkl` for deployment

---

## 🛠️ Technologies Used

- **Machine Learning**: Linear Regression algorithm (`scikit-learn`)
- **Programming Language**: Python  
- **Libraries**:
  - `scikit-learn`: For building and training the Linear Regression model
  - `pandas`: For data manipulation
  - `matplotlib`: For data visualization
  - `streamlit`: For creating the interactive user interface  
- **Development Environment**: Google Colab / Jupyter Notebook (model training), Anaconda Navigator  
- **Version Control**: GitHub

---

## 📂 Dataset

- **Filename**: `HPPdataset.csv`
- **Description**: Contains land area and price data used for training and evaluation.

---

## ▶️ How to Run the Project

```bash
streamlit run app.py
