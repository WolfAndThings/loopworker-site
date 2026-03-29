"""
LoopWorker Audit Form Webhook — Modal
Receives form submissions, sends auto-reply via Gmail SMTP, notifies Alex.

Deploy: python3 -m modal deploy audit_webhook.py
Test:   python3 -m modal run audit_webhook.py
"""

import modal
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app_image = modal.Image.debian_slim(python_version="3.11").pip_install("fastapi[standard]")
app = modal.App("loopworker-audit", image=app_image)


AUTO_REPLY_SUBJECT = "Got your audit request — here's what happens next"

AUTO_REPLY_HTML = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 560px; margin: 0 auto; color: #333;">
  <p>Hey {name},</p>

  <p>Thanks for submitting your content audit request. I'm on it.</p>

  <p><strong>Here's what happens next:</strong></p>

  <ol style="line-height: 2;">
    <li>I review your social media and website</li>
    <li>I put together a custom breakdown of what's costing you customers</li>
    <li>I send it to your inbox within 24 hours</li>
  </ol>

  <p>No fluff, no generic advice — just a clear look at what's not working and what I'd fix first.</p>

  <p>Talk soon,<br><strong>Alex Lamb</strong><br>LoopWorker<br><a href="https://www.loopworker.com" style="color: #555;">loopworker.com</a></p>
</div>
"""

NOTIFY_SUBJECT = "New Audit Request: {business}"

NOTIFY_HTML = """
<div style="font-family: monospace; font-size: 14px;">
  <h2>New Content Audit Request</h2>
  <table style="border-collapse: collapse;">
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Name</td><td>{name}</td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Email</td><td>{email}</td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Business</td><td>{business}</td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Website/IG</td><td>{website}</td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Type</td><td>{business_type}</td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Challenge</td><td>{challenge}</td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Active?</td><td>{actively_seeking_customers}</td></tr>
  </table>
</div>
"""

ALEX_EMAIL = "hello@wolvescreative.com"


def send_email(smtp_user, smtp_pass, to_email, subject, html_body, from_name="Alex Lamb"):
    """Send email via Gmail SMTP."""
    msg = MIMEMultipart("alternative")
    msg["From"] = f"{from_name} <{smtp_user}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


@app.function(
    secrets=[modal.Secret.from_name("loopworker-keys")],
)
@modal.fastapi_endpoint(method="POST")
def audit_webhook(data: dict):
    """Receive form submission, send auto-reply + notification."""
    import os

    smtp_user = os.environ.get("GMAIL_USER", ALEX_EMAIL)
    smtp_pass = os.environ.get("GMAIL_APP_PASSWORD", "")

    name = data.get("name", "there")
    email = data.get("email", "")
    business = data.get("business", "")
    website = data.get("website", "")
    business_type = data.get("business_type", "")
    challenge = data.get("challenge", "")
    actively = data.get("actively_seeking_customers", "")

    fmt = {
        "name": name,
        "email": email,
        "business": business,
        "website": website,
        "business_type": business_type,
        "challenge": challenge,
        "actively_seeking_customers": actively,
    }

    results = {"auto_reply": "skipped", "notification": "skipped"}

    if not smtp_pass:
        return {"error": "GMAIL_APP_PASSWORD not set in Modal secrets", **fmt}

    # 1. Send auto-reply to submitter
    if email:
        try:
            send_email(
                smtp_user,
                smtp_pass,
                email,
                AUTO_REPLY_SUBJECT,
                AUTO_REPLY_HTML.format(**fmt),
            )
            results["auto_reply"] = "sent"
        except Exception as e:
            results["auto_reply"] = f"error: {e}"

    # 2. Notify Alex
    try:
        send_email(
            smtp_user,
            smtp_pass,
            ALEX_EMAIL,
            NOTIFY_SUBJECT.format(**fmt),
            NOTIFY_HTML.format(**fmt),
            from_name="LoopWorker Bot",
        )
        results["notification"] = "sent"
    except Exception as e:
        results["notification"] = f"error: {e}"

    return {"status": "ok", **results, "name": name, "business": business}
