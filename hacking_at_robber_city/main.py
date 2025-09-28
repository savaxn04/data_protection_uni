def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

if __name__ == "__main__":
    message_1 = input("message1: ")
    message_2 = input("message2: ")
    message_3 = input("message3: ")

    message_1_bytes = bytes.fromhex(message_1)
    message_2_bytes = bytes.fromhex(message_2)
    message_3_bytes = bytes.fromhex(message_3)

    key_2 = xor_bytes(message_1_bytes, message_2_bytes)
    main_message = xor_bytes(message_3_bytes, key_2)
    print(main_message.decode("ascii"))