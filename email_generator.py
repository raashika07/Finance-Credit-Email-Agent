from dotenv import load_dotenv
import os

load_dotenv()

def generate_email(client_name, invoice_no, amount_due,
                   due_date, days_overdue, stage):

    if "Stage 1" in stage:

        email = f"""
Subject: Friendly Reminder - Invoice {invoice_no}

Dear {client_name},

I hope you are doing well.

This is a friendly reminder that Invoice {invoice_no} for ₹{amount_due}
was due on {due_date} and is currently {days_overdue} days overdue.

If you have already made the payment, please ignore this email.

Otherwise, kindly process the payment at your earliest convenience.

Best Regards,
Finance Team
"""

    elif "Stage 2" in stage:

        email = f"""
Subject: Payment Reminder - Invoice {invoice_no}

Dear {client_name},

This is a polite reminder regarding Invoice {invoice_no} amounting to ₹{amount_due}.

The payment is currently {days_overdue} days overdue.
Please confirm the payment status and expected payment date.

We appreciate your prompt attention.

Regards,
Finance Team
"""

    elif "Stage 3" in stage:

        email = f"""
Subject: Urgent Outstanding Payment - Invoice {invoice_no}

Dear {client_name},

Despite previous reminders, Invoice {invoice_no} for ₹{amount_due}
remains unpaid and is now {days_overdue} days overdue.

We request immediate attention to this matter.

Please respond within 48 hours.

Regards,
Finance Department
"""

    elif "Stage 4" in stage:

        email = f"""
Subject: FINAL NOTICE - Invoice {invoice_no}

Dear {client_name},

This is the final reminder regarding Invoice {invoice_no}
for ₹{amount_due}, currently overdue by {days_overdue} days.

Failure to make payment immediately may result in escalation
to our legal and recovery team.

Please take urgent action.

Regards,
Finance Recovery Team
"""

    else:

        email = "Escalated for manual finance review."

    return email