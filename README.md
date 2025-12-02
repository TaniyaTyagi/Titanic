 Titanic Survival Prediction – Machine Learning Web App

This is a simple and interactive Streamlit web application that predicts whether a passenger would have survived the Titanic disaster based on certain input features.
The model used in this app is trained on the Titanic dataset (commonly used in Kaggle ML competitions).

 Features

User-friendly UI built using Streamlit

Takes passenger inputs such as:
  * Passenger Class
  * Sex
  * Age
  * Number of Siblings/Spouses
  * Number of Parents/Children
  * Ticket Fare

Uses a pre-trained Machine Learning model (titanic_model.pkl) to predict survival

Displays result clearly:
```
   Survived
   Not Survived
```

###  Technologies Used

| Component            | Technology                                                                      |
|---------------------|----------------------------------------------------------------------------------|
| Programming Language | Python                                                                          |
| Web App Framework    | Streamlit                                                                       |
| Data Handling        | Pandas                                                                          |
| Model Storage        | Pickle                                                                          |
| ML Algorithm         | (Depends on your trained model, e.g., Logistic Regression / Random Forest etc.) |


 Project Structure
```
  │-- titanic_model.pkl       # Saved ML model
  │-- app.py (or your .py file)   # Streamlit application script
  │-- README.md                # Project documentation
```

 How to Run the App
1. Install Required Libraries
 ```
pip install streamlit pandas pickle-mixin
```

2. Run the Streamlit App
```
streamlit run app.py
```

 Usage Instructions
 1. Open the app in your browser after running Streamlit.
 2. Select or enter passenger details.
 3. Click the Predict Survival button.
 4. View your prediction instantly.
