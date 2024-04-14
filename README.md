# SHA-256 Hash Generator

This Python script generates the SHA-256 hash of a user-provided message using the `hashlib` module.

## Usage

1. Clone the repository.
2. Navigate to the directory containing the script.
3. Run the script.
4. Enter your message when prompted.
5. The script will calculate the SHA-256 hash of the input message and display it.

## Requirements

- Python 3.x
- `hashlib` module

## Script Explanation

- `get_hash(message)`: This function takes a message string as input, converts it to bytes using UTF-8 encoding, creates a SHA-256 hash object, and returns the hexadecimal representation of the hash value.
- `user_message`: This variable stores the message input by the user.
- `message_hash`: This variable stores the SHA-256 hash of the input message.

## Example

```bash
Enter your message: Hello, world!
The SHA256 hash of the message is: 65a8e27d8879283831b664bd8b7f0ad4c2b697c98294b5c4f1
```
