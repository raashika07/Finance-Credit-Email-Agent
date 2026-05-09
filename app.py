import pandas as pd
from datetime import datetime

# Read invoice data
df = pd.read_csv("data/invoices.csv")

# Convert due_date column to datetime
df["due_date"] = pd.to_datetime(df["due_date"])

# Get today's date
today = datetime.today()

# Function to determine escalation stage
def get_stage(days_overdue):
    if 1 <= days_overdue <= 7:
        return "Stage 1 - Warm Reminder"
    elif 8 <= days_overdue <= 14:
        return "Stage 2 - Polite Reminder"
    elif 15 <= days_overdue <= 21:
        return "Stage 3 - Formal Reminder"
    elif 22 <= days_overdue <= 30:
        return "Stage 4 - Final Warning"
    elif days_overdue > 30:
        return "Escalate to Finance Team"
    else:
        return "Not Overdue"

# Calculate overdue days and stages
for index, row in df.iterrows():
    days_overdue = (today - row["due_date"]).days
    stage = get_stage(days_overdue)

    print("\n-----------------------------------")
    print(f"Invoice Number : {row['invoice_no']}")
    print(f"Client Name    : {row['client_name']}")
    print(f"Days Overdue   : {days_overdue}")
    print(f"Reminder Stage : {stage}")