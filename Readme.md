# 🌱 AI-Based Carbon Footprint Estimator

## 📌 Project Overview
The **Carbon Footprint Estimator** is an AI-based web application that estimates an individual’s **monthly carbon emissions** based on daily lifestyle activities such as electricity usage, fuel consumption, transportation habits, and diet type.  
The application also provides **eco-friendly suggestions** to encourage sustainable living.

This project promotes **green skills** and supports the **UN Sustainable Development Goals (SDGs)**.

---

## 🎯 Objectives
- Estimate individual carbon footprint using Machine Learning  
- Raise awareness about carbon emissions  
- Encourage sustainable and eco-friendly lifestyle choices  
- Provide visual insights using charts and graphs  

---

## 🧠 Technologies Used
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn (Linear Regression)  
- **Web Framework:** Streamlit  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib  
- **Model Storage:** Joblib  

---

## 📊 Features
- Interactive web interface  
- AI-based carbon footprint prediction  
- Color-coded bar charts  
- Carbon footprint classification (Low / Medium / High)  
- Eco-friendly lifestyle recommendations  

---

## 🗂️ Project Structure

```

carbon_footprint_estimator/
│
├── carbon_footprint.csv     # Dataset
├── train_model.py           # Model training script
├── app.py                   # Streamlit web application
├── carbon_model.pkl         # Trained ML model
├── diet_encoder.pkl         # Diet label encoder
└── README.md                # Project documentation

```

---

## ⚙️ Installation

### Step 1: Clone the Repository
```

git clone [https://github.com/your-username/carbon-footprint-estimator.git](https://github.com/your-username/carbon-footprint-estimator.git)
cd carbon-footprint-estimator

```

### Step 2: Install Required Libraries
```

pip install pandas scikit-learn streamlit matplotlib joblib

```

---

## How to Run the Project

### Step 1: Train the Machine Learning Model
```

python train_model.py

```

### Step 2: Run the Streamlit Application
```

streamlit run app.py

```

The application will automatically open in your default web browser.

---

## Output

The application provides:
- Estimated **monthly carbon footprint** (kg CO₂)
- **Carbon footprint category** (Low / Medium / High)
- **Bar charts** comparing emissions and usage
- **Personalized green lifestyle recommendations**

---

## Sustainable Development Goals (SDGs)

This project aligns with the following UN Sustainable Development Goals:

- **SDG 13**: Climate Action
- **SDG 7**: Affordable and Clean Energy
- **SDG 11**: Sustainable Cities and Communities
- **SDG 12**: Responsible Consumption and Production

---

## Future Enhancements

- Use real-world datasets for improved accuracy
- Add downloadable PDF reports
- Develop a mobile application
- Integrate IoT-based energy consumption data
- Use advanced ML models for better predictions

---

## Authors

- **Name(s):** Add your name
- **Institution:** Add your college name

---

## License

This project is developed for **educational purposes only**.


