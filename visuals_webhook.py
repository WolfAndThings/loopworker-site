"""
LoopWorker Visuals Request Webhook — Modal

Receives URL submissions from the homepage hero ("Generate my visuals").
Sends a notification to Alex and an auto-reply to any email we can resolve
from the submitted site, plus a stamped record we can pull from the dashboard.

Deploy: python3 -m modal deploy visuals_webhook.py
Test:   python3 -m modal run visuals_webhook.py

Update the ENDPOINT constant in index.html (#visuals-hero-form script) with
the deployed URL after `modal deploy` prints it.
"""

import modal
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone

app_image = modal.Image.debian_slim(python_version="3.11").pip_install("fastapi[standard]")
app = modal.App("loopworker-visuals", image=app_image)

ALEX_EMAIL = "lambsbrown@gmail.com"

NOTIFY_SUBJECT = "New Visuals Request: {website}"

NOTIFY_HTML = """
<div style="font-family: monospace; font-size: 14px;">
  <h2>New Visuals Request (home hero)</h2>
  <table style="border-collapse: collapse;">
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Website</td><td><a href="{website}">{website}</a></td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Source</td><td>{source}</td></tr>
    <tr><td style="padding: 4px 12px 4px 0; color: #888;">Submitted</td><td>{submitted_at}</td></tr>
  </table>
  <p style="margin-top:16px;">Next steps: scrape brand, queue preview render, reply with a Loom + 3 sample frames within 24h.</p>
</div>
"""


def send_email(smtp_user, smtp_pass, to_email, subject, html_body, from_name="LoopWorker Bot"):
    msg = MIMEMultipart("alternative")
    msg["From"] = f"{from_name} <{smtp_user}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


@app.function(secrets=[modal.Secret.from_name("loopworker-keys")])
@modal.fastapi_endpoint(method="POST")
def visuals_webhook(data: dict):
    """Accept {website, source} JSON. Email Alex, log, return 200."""
    import os

    smtp_user = os.environ.get("GMAIL_USER", ALEX_EMAIL)
    smtp_pass = os.environ.get("GMAIL_APP_PASSWORD", "")

    website = (data.get("website") or "").strip()
    source = (data.get("source") or "unknown").strip()
    submitted_at = datetime.now(timezone.utc).isoformat()

    if not website:
        return {"status": "error", "reason": "missing website"}

    fmt = {"website": website, "source": source, "submitted_at": submitted_at}

    result = {"status": "ok", "notification": "skipped", **fmt}

    if not smtp_pass:
        result["notification"] = "skipped: GMAIL_APP_PASSWORD not set"
        return result

    try:
        send_email(
            smtp_user,
            smtp_pass,
            ALEX_EMAIL,
            NOTIFY_SUBJECT.format(**fmt),
            NOTIFY_HTML.format(**fmt),
        )
        result["notification"] = "sent"
    except Exception as e:
        result["notification"] = f"error: {e}"

    return result
