from decimal import DefaultContext
from fastmcp import FastMCP
from tools import messages, contacts, app, reminders, notes
from pydantic import Field

mcp = FastMCP("Altic-MCP")


@mcp.tool()
def open_app(name: str) -> str:
    """
    Open any mac application by specifying its name. Use this tool
    if you encounter any error or issue mentioning that the app is not
    open

    Args:
        name: Name of the mac app. e.g. "Mail", "Contacts", "Messages" etc.

    Returns:
        A success or failure message
    """
    return app.open_app(name)


@mcp.tool()
def send_imessage(phone_number: str, message: str) -> str:
    """
    Send an imessage to someone in your contacts

    Args:
        phone_number: The phone number of the recipient
        message: The message text to send

    Returns:
        Success or error message
    """
    return messages.send_message(phone_number=phone_number, message=message)


@mcp.tool()
async def search_contacts(name: str) -> str:
    """
    Search for a phone number from contacts by name. Returns multiple
    options if more than one contact is found or more than one number is found.
    Ask clarifying questions on which number if any following actions are required

    Args:
        name: The name of contact to search for
        ctx: FastMCP context for logging

    Returns:
        A list of matching contacts
    """
    return contacts.search_contacts(name)


@mcp.tool()
async def read_recent_messages(
    phone_number: str, recent_message_count: int = Field(default=25, ge=1, le=200)
) -> str:
    """
    Read the recent X messages from the iMessage app between the user and the
    person with the phone number. X is defined based on the value of recent_message_count

    Args:
        phone_number: The phone number of the person you want to retrieve the chat from
        recent_message_count: The recent messages to retrieve, can be a maximum of 200

    Returns:
        A list of recent messages in the chat
    """
    return messages.read_recent_messages(phone_number, recent_message_count)


@mcp.tool()
async def set_reminder(name: str, datetime: str, list_name: str = "Reminders") -> str:
    """
    Set a reminder

    Args:
        name: The reminder text
        datetime: The time to set the reminder for, must in the following format "YYYY-MM-DD HH:MM"
        list_name: Reminder list, e.g. Work, Personal etc. Defaults to "Reminders"

    Returns:
        A success or error message
    """
    return reminders.set_reminder(name, datetime, list_name)


@mcp.tool()
async def create_note(name: str, body: str, folder: str = Field(default="")) -> str:
    """
    Create a note

    Args:
        name: Title of the note
        body: Content of the note
        folder: Use this if the note has to be created in a specific folder. Uses
        default folder if none is specified

    Returns:
        A success or error message
    """
    return notes.create_note(name, body, folder)


@mcp.tool()
async def search_notes(
    query: str, max_results: int = Field(default=10, ge=1, le=20)
) -> str:
    """
    Search Apple notes based on a query

    Args:
        query: The query string
        max_results: The maximum number of results returned from the tool, defaults to 10

    Returns:
        A list of notes based on search
    """
    return notes.search_notes(query, max_results)


if __name__ == "__main__":
    mcp.run()
