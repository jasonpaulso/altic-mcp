import subprocess
from .constants import SCRIPTS_PREFIX
from rapidfuzz import fuzz, process
import logging

logger = logging.getLogger(__name__)


def search_contacts(name: str) -> str:
    script_path = SCRIPTS_PREFIX / "fetch-all-contacts.applescript"
    match_threshold = 70
    try:
        result = subprocess.run(
            ["osascript", script_path],
            capture_output=True,
            text=True,
            timeout=300,
        )

        if result.returncode != 0:
            return f"Unable to execute script to fetch contacts: {result.stderr}"

        contacts = result.stdout.strip().split("\n")

        contact_map = {}
        for contact in contacts:
            if "|" in contact:
                contact_name = contact.split("|")[0]
                contact_map[contact_name] = contact

        search_term = name.lower()

        exact_matches = [
            contact_name
            for contact_name in contact_map.keys()
            if search_term in contact_name.lower()
        ]

        if exact_matches:
            output = ""
            for idx, matched_name in enumerate(exact_matches[:5]):  # Limit to 5
                full_contact = contact_map[matched_name]
                output += f"Option {idx + 1}: {full_contact}\n"
            return output

        matches = process.extract(
            name, list(contact_map.keys()), scorer=fuzz.token_sort_ratio, limit=5
        )

        output = ""
        for idx, match in enumerate(matches):
            matched_name = match[0]
            match_score = match[1]

            if match_score >= match_threshold:
                full_contact = contact_map[matched_name]
                output += f"Option {idx + 1}: {full_contact} (score: {match_score})\n"

        if not output:
            return f"No contacts found matching '{name}'"

        return output

    except Exception as e:
        error_msg = f"Failed to retrieve contacts: {str(e)}"
        return error_msg
