alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
             't','u','v','w','x','y','z']

def caesar(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1

    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted = alphabets.index(letter) + shift_amount
            shifted = shifted % len(alphabets)
            output_text += alphabets[shifted]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

want_to_continue = True
while want_to_continue:

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n").lower()
    text = input("Type you message: \n").lower()
    shift = int(input("Type the shift number : \n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if restart == 'no':
        want_to_continue = False
        print("Goodbye")

#code of encode
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted = alphabets.index(letter) + shift_amount
#         shifted = shifted % len(alphabets)
#         cipher_text += alphabets[shifted]

#     print(cipher_text)
# encrypt(original_text=text,shift_amount=shift)

#code of decode
# def decrypt(original_text,shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted = alphabets.index(letter) - shift_amount
#         shifted = shifted % len(alphabets)
#         output_text += alphabets[shifted]
#     print(output_text)
# decrypt(original_text=text,shift_amount=shift)



