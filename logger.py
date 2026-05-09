import csv
import os
from datetime import datetime

LOG_FILE = "logs/audit_log.csv"

# Create log file with headers if it doesn't exist
if not os.path.exists(LOG_FILE):

    with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Invoice Number",
            "Client Name",
            "Days Overdue",
            "Reminder Stage",
            "Status"
        ])

# Function to save logs
def save_log(invoice_no, client_name,
             days_overdue, stage, status):

    with open(LOG_FILE, mode="a",
              newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            invoice_no,
            client_name,
            days_overdue,
            stage,
            status
        ])