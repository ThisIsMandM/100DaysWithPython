from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print (logo)
program_open = True

def caesar_cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode in ("encode", "decode"):
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position = shifted_position % len(alphabet)
                output_text = output_text + alphabet[shifted_position]
            else:
                output_text = output_text + letter
        print(f"This is your word '{output_text}'")
    else:
        print("Wrong request! Only type 'encode' to encrypt, type 'decode' to decrypt.")

    
while program_open:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

   
    
    caesar_cipher(original_text = text, shift_amount = shift, encode_or_decode = direction)
    run_again = str(input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")).lower()
    if run_again == 'yes':
        program_open = True
    else:
        program_open = False


    
