# Importing the hashlib module for cryptographic hashing #
import hashlib


def get_hash(message):
    # Convert the message string to bytes using UTF-8 encoding
    message_bytes = message.encode()
    
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256(message_bytes) 
    
    # Generate the hexadecimal representation of the hash value
    hash_result = hash_object.hexdigest()
    
    # Return the hexadecimal hash value
    return hash_result 

# Prompt the user to input a message
user_message = input("Enter your message: ")

# Calculate the SHA-256 hash of the input message
message_hash = get_hash(user_message)

# Display the calculated SHA-256 hash value
print("The SHA256 hash of the message is:", message_hash)