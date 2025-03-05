#user_input = int(input("How old are you?"))

#def life_in_weeks(age):
#   lifed_weeks = age * 52
#   rest_weeks = 4680 - lifed_weeks
#   print(f"You have {rest_weeks} weeks left.")
    
    
#life_in_weeks(user_input)

alaphabet = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    for letter in original_text:
        shifted_position = alphabet.index(letter)


