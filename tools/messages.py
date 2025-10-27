import subprocess
from .constants import SCRIPTS_PREFIX


def send_message(phone_number: str, message: str) -> str:
    send_message_script_path = SCRIPTS_PREFIX / "send-message.applescript"

    try:
        result = subprocess.run(
            ["osascript", send_message_script_path, phone_number, message],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode == 0:
            return f"Successfully sent the message to {phone_number}"
        else:
            error_msg = result.stderr.strip() if result.stderr else "Unknown error"
            return f"Error: failed to send message: {error_msg}"

    except subprocess.TimeoutExpired:
        return "Error: Failed to send message: Operation timed out"
    except Exception as e:
        return f"Error: Failed to send message: {str(e)}"
