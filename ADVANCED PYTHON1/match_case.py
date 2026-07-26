def http_status(status: int) -> str:
    """
    Return the HTTP status message for a given status code.

    Args:
        status (int): HTTP status code

    Returns:
        str: Corresponding status message
    """
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"


if __name__ == "__main__":
    # Example usage
    print(http_status(200))  # Output: OK
    print(http_status(404))  # Output: Not Found
    print(http_status(500))  # Output: Internal Server Error
    print(http_status(403))  # Output: Unknown status
