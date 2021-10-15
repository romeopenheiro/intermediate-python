message = "... . -.-. .-. . - / -- . ... ... .- --. ."

# `morse` is a list which will eventually contain the 
# strings for each morse code letter in the message.

import morse

decoded_message = morse.decode(message)

print(f"Incoming message: {message}")
print(f"   Morse decoded: {decoded_message}")

