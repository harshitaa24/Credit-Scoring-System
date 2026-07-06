import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    month TEXT,
    age INTEGER,
    occupation TEXT,

    annual_income REAL,
    monthly_inhand_salary REAL,

    num_bank_accounts INTEGER,
    num_credit_card INTEGER,
    interest_rate REAL,
    num_of_loan INTEGER,
    type_of_loan TEXT,

    delay_from_due_date INTEGER,
    num_of_delayed_payment INTEGER,

    changed_credit_limit REAL,
    num_credit_inquiries INTEGER,

    credit_mix TEXT,

    outstanding_debt REAL,

    credit_utilization_ratio REAL,

    credit_history_age INTEGER,

    payment_of_min_amount TEXT,

    total_emi_per_month REAL,

    amount_invested_monthly REAL,

    payment_behaviour TEXT,

    monthly_balance REAL,

    predicted_credit_score TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()
conn.close()

print("Database created successfully!")