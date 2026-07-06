from flask import Flask, render_template, request
import pandas as pd
import joblib
import sqlite3
import os

app = Flask(__name__)

# -----------------------------
# Load Model and Label Encoders
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "credit_model.joblib"))
label_encoders = joblib.load(os.path.join(BASE_DIR, "label_encoders.joblib"))


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction
# -----------------------------

@app.route("/predict", methods=["POST"])
def predict():

    data = {

        "Month": request.form["Month"],
        "Age": int(request.form["Age"]),
        "Occupation": request.form["Occupation"],
        "Annual_Income": float(request.form["Annual_Income"]),
        "Monthly_Inhand_Salary": float(request.form["Monthly_Inhand_Salary"]),
        "Num_Bank_Accounts": int(request.form["Num_Bank_Accounts"]),
        "Num_Credit_Card": int(request.form["Num_Credit_Card"]),
        "Interest_Rate": float(request.form["Interest_Rate"]),
        "Num_of_Loan": int(request.form["Num_of_Loan"]),
        "Type_of_Loan": request.form["Type_of_Loan"],
        "Delay_from_due_date": int(request.form["Delay_from_due_date"]),
        "Num_of_Delayed_Payment": int(request.form["Num_of_Delayed_Payment"]),
        "Changed_Credit_Limit": float(request.form["Changed_Credit_Limit"]),
        "Num_Credit_Inquiries": int(request.form["Num_Credit_Inquiries"]),
        "Credit_Mix": request.form["Credit_Mix"],
        "Outstanding_Debt": float(request.form["Outstanding_Debt"]),
        "Credit_Utilization_Ratio": float(request.form["Credit_Utilization_Ratio"]),
        "Credit_History_Age": int(request.form["Credit_History_Age"]),
        "Payment_of_Min_Amount": request.form["Payment_of_Min_Amount"],
        "Total_EMI_per_month": float(request.form["Total_EMI_per_month"]),
        "Amount_invested_monthly": float(request.form["Amount_invested_monthly"]),
        "Payment_Behaviour": request.form["Payment_Behaviour"],
        "Monthly_Balance": float(request.form["Monthly_Balance"])
    }

    # -----------------------------
    # Handle unseen loan types
    # -----------------------------

    if data["Type_of_Loan"] not in label_encoders["Type_of_Loan"].classes_:
        data["Type_of_Loan"] = "Not Specified"

    # -----------------------------
    # Create DataFrame
    # -----------------------------

    df = pd.DataFrame([data])

    categorical_cols = [
        "Month",
        "Occupation",
        "Type_of_Loan",
        "Credit_Mix",
        "Payment_of_Min_Amount",
        "Payment_Behaviour"
    ]

    for col in categorical_cols:
        df[col] = label_encoders[col].transform(df[col])

    # -----------------------------
    # Prediction
    # -----------------------------

    pred = model.predict(df)[0]

    prediction = label_encoders["Credit_Score"].inverse_transform([pred])[0]

    # -----------------------------
    # Save into Database
    # -----------------------------

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions(

        month,
        age,
        occupation,
        annual_income,
        monthly_inhand_salary,
        num_bank_accounts,
        num_credit_card,
        interest_rate,
        num_of_loan,
        type_of_loan,
        delay_from_due_date,
        num_of_delayed_payment,
        changed_credit_limit,
        num_credit_inquiries,
        credit_mix,
        outstanding_debt,
        credit_utilization_ratio,
        credit_history_age,
        payment_of_min_amount,
        total_emi_per_month,
        amount_invested_monthly,
        payment_behaviour,
        monthly_balance,
        predicted_credit_score

    )

    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    """,

    (

        data["Month"],
        data["Age"],
        data["Occupation"],
        data["Annual_Income"],
        data["Monthly_Inhand_Salary"],
        data["Num_Bank_Accounts"],
        data["Num_Credit_Card"],
        data["Interest_Rate"],
        data["Num_of_Loan"],
        data["Type_of_Loan"],
        data["Delay_from_due_date"],
        data["Num_of_Delayed_Payment"],
        data["Changed_Credit_Limit"],
        data["Num_Credit_Inquiries"],
        data["Credit_Mix"],
        data["Outstanding_Debt"],
        data["Credit_Utilization_Ratio"],
        data["Credit_History_Age"],
        data["Payment_of_Min_Amount"],
        data["Total_EMI_per_month"],
        data["Amount_invested_monthly"],
        data["Payment_Behaviour"],
        data["Monthly_Balance"],
        prediction

    ))

    conn.commit()
    conn.close()

    # -----------------------------
    # Result Page
    # -----------------------------

    return render_template(

        "predict.html",

        prediction=prediction,
        age=data["Age"],
        annual_income=data["Annual_Income"],
        outstanding_debt=data["Outstanding_Debt"],
        utilization=data["Credit_Utilization_Ratio"],
        loans=data["Num_of_Loan"]

    )


# -----------------------------
# Database Page
# -----------------------------

@app.route("/database")
def database():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions")

    rows = cursor.fetchall()

    conn.close()

    return render_template("database.html", rows=rows)


# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)