def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "decrypt":
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Keep punctuation, numbers, and spaces unchanged
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be a number.")
        return
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please type 'encrypt' or 'decrypt'.")
        return

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed message): {output}")

if __name__ == "__main__":
    main()
