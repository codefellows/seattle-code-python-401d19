import random


# chars = ['0'...'9']


def encrypt(plain, shift):
    encrypted = ""
    for char in plain:
        num = int(char)
        shifted_num = (num + shift) % 10 # must be 0-9
        encrypted += str(shifted_num)

        # LAB note - you can convert alpha characters (aka letters) into numeric form.
        # search for python "ord" function
        # and chr to go the other direction


    return encrypted


def decrypt(cipher, shift):
    # you can do own logic here, or notice that decrypting is same as encrypting with the number negated
    return encrypt(cipher, -shift)


if __name__ == "__main__":
    pins = [
        "1234",
        "9876",
        "0000",
        "9999",
    ]

    for pin in pins:
        key = random.randint(1, 9)
        print("plain pin", pin)
        encrypted_pin = encrypt(pin, key)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, key)
        print("decrypted_pin", decrypted_pin)
