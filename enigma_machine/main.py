from typing import Iterable

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_shift(encode: bool, text: str, start: int) -> str:
    result = ""
    for i, ch in enumerate(text):
        idx = ord(ch) - ord('A')
        new_idx = (idx + start + i) % 26 if encode else (idx - start - i) % 26
        result += chr(new_idx + ord('A'))
    return result

def rotor_substitution(encode: bool, text: str, mapping: str) -> str:
    result = ""
    for ch in text:
        idx = ALPHABET.index(ch) if encode else mapping.index(ch)
        result += mapping[idx] if encode else ALPHABET[idx]
    return result

def enigma_machine(encode: bool, start: int, rotors: Iterable[str], text: str) -> str:
    if encode:
        result = caesar_shift(encode=encode, text=text, start=start)
        for rotor in rotors:
            result = rotor_substitution(encode=encode, text=result, mapping=rotor)
    else:
        for rotor in reversed(rotors):
            text = rotor_substitution(encode=encode, text=text, mapping=rotor)
        result = caesar_shift(encode=encode, text=text, start=start)
    return result

if __name__ == "__main__":
    operation = input("operation: ")
    pseudo_random_number = int(input("pseudo random number: "))

    rotor_1 = input("rotor_1: ")
    rotor_2 = input("rotor_2: ")
    rotor_3 = input("rotor_3: ")
    message = input("message: ").strip().upper()

    result = enigma_machine(
        encode=(operation == "ENCODE"),
        start=pseudo_random_number,
        rotors=[rotor_1, rotor_2, rotor_3],
        text=message
    )

    print(result)