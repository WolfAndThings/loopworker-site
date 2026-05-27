#!/usr/bin/env python3
"""Test SMTP login + send sample to self via alex@loopworker.com.

MX confirms Google Workspace. Uses smtp.gmail.com:587 STARTTLS.
If regular password fails, you need an APP PASSWORD:
  https://myaccount.google.com/apppasswords (must have 2FA on)
"""
import os
import smtplib
import ssl
import sys
from email.message import EmailMessage

EMAIL = os.environ.get("LOOPWORKER_EMAIL")
PW = os.environ.get("LOOPWORKER_EMAIL_PW")

if not EMAIL or not PW:
    sys.exit("ERROR: LOOPWORKER_EMAIL + LOOPWORKER_EMAIL_PW must be in env")

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = EMAIL
msg["Subject"] = "[SMTP test] LoopWorker pipeline"
msg.set_content("Connection works. Stripe → email pipeline ready.\n\n— Automated test")

try:
    print(f"Connecting to smtp.gmail.com:587 as {EMAIL}...")
    ctx = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as srv:
        srv.ehlo()
        srv.starttls(context=ctx)
        srv.ehlo()
        srv.login(EMAIL, PW)
        srv.send_message(msg)
    print("✓ Sent successfully")
except smtplib.SMTPAuthenticationError as e:
    print(f"✗ AUTH FAILED: {e.smtp_code} {e.smtp_error.decode() if isinstance(e.smtp_error, bytes) else e.smtp_error}")
    print("\nGoogle Workspace requires an APP PASSWORD, not your regular password.")
    print("Steps:")
    print("  1. Enable 2-Step Verification: https://myaccount.google.com/security")
    print("  2. Generate app password: https://myaccount.google.com/apppasswords")
    print("  3. Replace LOOPWORKER_EMAIL_PW in .env with the 16-char app password")
    sys.exit(1)
except Exception as e:
    print(f"✗ ERROR: {type(e).__name__}: {e}")
    sys.exit(2)
