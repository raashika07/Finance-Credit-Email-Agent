# CrediFlow AI
The system supports both AI-generated and template-based fallback email generation. Template fallback ensures uninterrupted workflow in case of API quota exhaustion or network/API failures.


## AI-Powered Automated Invoice Follow-Up & Escalation System

CrediFlow AI is an intelligent finance automation system designed to help organizations manage overdue invoice follow-ups efficiently.

The system automatically:
- Detects overdue invoices
- Assigns escalation stages
- Generates professional payment reminder emails
- Logs communication activity
- Escalates critical overdue cases for manual review

Built as part of an internship assignment focused on AI-driven business workflow automation.

---

# Features

- CSV-based invoice ingestion  
- Automated overdue detection  
- Multi-stage escalation workflow  
- Dynamic follow-up email generation  
- Audit trail logging system  
- Finance escalation handling  
- Interactive Streamlit dashboard  
- Secure environment variable handling  
- Modular Python architecture  

---

# Workflow

```text
Invoice Data
     ↓
Overdue Detection
     ↓
Escalation Stage Assignment
     ↓
Email Generation
     ↓
Audit Logging
     ↓
Dashboard Display
```

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core backend logic |
| Pandas | Invoice data processing |
| Streamlit | Dashboard UI |
| CSV | Data storage |
| dotenv | Secure API/environment handling |

---

# Project Structure

```text
crediflow-ai/
│
├── data/
│   └── invoices.csv
│
├── logs/
│   └── audit_log.csv
│
├── app.py
├── email_generator.py
├── logger.py
├── escalation.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/crediflow-ai.git
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows
```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
streamlit run app.py
```

---

# Escalation Logic

| Days Overdue | Stage |
|---|---|
| 1–7 Days | Warm Reminder |
| 8–14 Days | Polite Reminder |
| 15–21 Days | Formal Reminder |
| 22–30 Days | Final Warning |
| 30+ Days | Escalated to Finance Team |

---

# Security Considerations

CrediFlow AI includes several security-focused practices:

- API/environment variables stored securely using `.env`
- Sensitive files excluded using `.gitignore`
- Audit logging for workflow traceability
- Manual escalation for high-risk overdue accounts
- Controlled local execution environment

---

# Dashboard Preview

The Streamlit dashboard provides:
- Invoice monitoring
- Overdue tracking
- Escalation visibility
- Email generation interface
- Audit workflow support

---

# Future Improvements

- Real email sending integration
- Database integration
- AI-generated smart payment recommendations
- Admin authentication
- Cloud deployment
- Analytics dashboard

---

# Author

Developed by Raashika Bora  
Internship Project – 2026