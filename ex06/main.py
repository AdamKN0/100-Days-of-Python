print("Welcome to the Caesar Cipher")
text = input("Enter the text you want to encode or decode: ")
shift = int(input("Enter the number of shifts: "))
direction =  input("Enter 'encode' to encode or 'decode' to decode: ").lower()

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(text, shift):
    encoded_text = ""
    for i in text:
        if i in alphabet_lower:
            encoded_text += alphabet_lower[(alphabet_lower.index(i) + shift) % 26]
        elif i in alphabet_upper:
            encoded_text += alphabet_upper[(alphabet_upper.index(i) + shift) % 26]
        else:
            encoded_text += i
    print(f"The encoded text is {encoded_text}")

def decode(text, shift):
    decoded_text = ""
    for i in text:
        if i in alphabet_lower:
            decoded_text += alphabet_lower[(alphabet_lower.index(i) - shift) % 26]
        elif i in alphabet_upper:
            decoded_text += alphabet_upper[(alphabet_upper.index(i) - shift) % 26]
        else:
            decoded_text += i
    print(f"The decoded text is {decoded_text}")

if direction == "encode":
    encode(text, shift)
elif direction == "decode":
    decode(text, shift)
else:
    print("Invalid input")
