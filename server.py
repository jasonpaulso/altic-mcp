from fastmcp import FastMCP
from tools import messages, contacts, app

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


if __name__ == "__main__":
    mcp.run()
