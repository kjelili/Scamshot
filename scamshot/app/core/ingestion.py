import os
from app.security.clamav_scanner import scan_file
from app.utils.alerts import send_slack_alert, send_email_alert

def handle_uploaded_attachment(file_path, email_address=None):
    scan_result = scan_file(file_path)

    if "Infected" in scan_result:
        msg = f"❌ Threat detected in file: {os.path.basename(file_path)}\nResult: {scan_result}"
        if email_address:
            msg += f"\nReported from: {email_address}"
        send_slack_alert(msg)
        send_email_alert("Scamshot Alert - Infected File", msg)

        # Optionally quarantine file (move to a separate directory)
        quarantine_dir = "quarantine"
        os.makedirs(quarantine_dir, exist_ok=True)
        os.rename(file_path, os.path.join(quarantine_dir, os.path.basename(file_path)))
        return "❌ Infected"

    return "✅ Clean"
