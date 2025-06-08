# 📧 Python Email Automation Script

This is a simple Python script that sends plain-text emails with optional file attachments using Gmail's SMTP server. It's useful for automating notifications, sending reports, or sharing files directly from a script.

---

## 🔧 Features

- Send plain-text emails
- Attach multiple files (e.g., Excel, PDF, etc.)
- Uses environment variables for secure configuration
- SMTP with TLS via Gmail

---

## 📦 Requirements

- Python 3.x
- `python-dotenv` (to load environment variables)

Install dependencies:

```bash
pip install python-dotenv
```

Create an .env in root directory:

- SENDER_ADDRESS=your_email@gmail.com
- APP_PASSWORD=your_gmail_app_password
- RECEIVER_ADDRESS=receiver_email@example.com

Run the Script:

```bash
automated _email_sender_script.py
```

