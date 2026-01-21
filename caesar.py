def caesar(text, shift, encrypt=True):
    # Validación
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# --- Inputs del usuario ---
text = input("Introduce el texto: ")

# Asegurarse de que shift sea un número entero
while True:
    try:
        shift = int(input("Introduce el desplazamiento (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("El desplazamiento debe estar entre 1 y 25.")
    except ValueError:
        print("Debes ingresar un número entero.")

# Preguntar si el usuario quiere cifrar o descifrar
accion = input("¿Quieres cifrar o descifrar? (c/d): ").lower()
if accion == 'c':
    encryptar = True
elif accion == 'd':
    encryptar = False
else:
    print("Opción no válida, se asumirá cifrado.")
    encryptar = True

# Ejecutar la función
resultado = caesar(text, shift, encrypt=encryptar)
print("Resultado:", resultado)
