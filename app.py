import streamlit as st
import pandas as pd
from datetime import datetime

from email_generator import generate_email
from logger import save_log

# Streamlit page config
st.set_page_config(page_title="Finance Credit Email Agent",
                   layout="wide")

st.title("📧 Finance Credit Follow-Up Email Agent")

# Load CSV
df = pd.read_csv("data/invoices.csv")

# Convert dates
df["due_date"] = pd.to_datetime(df["due_date"])

today = datetime.today()

# Escalation logic
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

# Main processing
for index, row in df.iterrows():

    days_overdue = (today - row["due_date"]).days

    stage = get_stage(days_overdue)

    st.divider()

    st.subheader(f"Invoice: {row['invoice_no']}")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Client:** {row['client_name']}")
        st.write(f"**Amount Due:** ₹{row['amount_due']}")

    with col2:
        st.write(f"**Days Overdue:** {days_overdue}")
        st.write(f"**Reminder Stage:** {stage}")

    # Escalation handling
    if stage == "Escalate to Finance Team":

        st.error("⚠ Escalated for manual finance review")

        save_log(
            row["invoice_no"],
            row["client_name"],
            days_overdue,
            stage,
            "Escalated"
        )

        continue

    # Generate email button
    if st.button(f"Generate Email for {row['invoice_no']}"):

        email = generate_email(
            row["client_name"],
            row["invoice_no"],
            row["amount_due"],
            row["due_date"].date(),
            days_overdue,
            stage
        )

        st.text_area(
            "Generated Email",
            email,
            height=300
        )

        save_log(
            row["invoice_no"],
            row["client_name"],
            days_overdue,
            stage,
            "Email Generated"
        )

        st.success("✅ Email generated and logged successfully")