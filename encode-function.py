message = "SOS We have hit an iceberg and need help quickly"


# `morse` is a list which will eventually contain the 
# strings for each morse code letter in the message.

import morse

try:
    encoded_message = morse.encode(message)
    print(f"Incoming message: {message}")
    print(f"   Morse encoded: {encoded_message}")
except ValueError as e:
    print(f"Could not encode message: {e}")

