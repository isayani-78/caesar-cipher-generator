import string


chars = string.ascii_letters + string.digits + string.punctuation + " " 


common_words = ["the", "and", "you", "that", "for", "with", "this", "have",
                "not", "are", "from", "your", "just", "like", "they", "what",
                "when", "there", "can", "about", "hello", "world", "test"]

def caesar_encrypt(plaintext, shift):
    return ''.join(
        chars[(chars.index(c) + shift) % len(chars)] if c in chars else c
        for c in plaintext
    )

def caesar_decrypt(ciphertext, shift):
    return ''.join(
        chars[(chars.index(c) - shift) % len(chars)] if c in chars else c
        for c in ciphertext
    )

def auto_decrypt(ciphertext):
    best_guess = None
    max_matches = 0

    for key in range(len(chars)):
        decrypted = caesar_decrypt(ciphertext, key)
        
        matches = sum(word in decrypted.lower() for word in common_words)

        if matches > max_matches:
            max_matches = matches
            best_guess = (key, decrypted)

    if best_guess:
        print(f"\n[+] Best key guess: {best_guess[0]}")
        print(f"[+] Decrypted text: {best_guess[1]}")
    else:
        print("\n[-] No good match found. Try checking brute-force results.")
        brute_force(ciphertext)

def brute_force(ciphertext):
    print("\n[+] Brute-forcing all possible keys:\n")
    for key in range(len(chars)):
        print(f"Key {key}: {caesar_decrypt(ciphertext, key)}")

if __name__ == "__main__":
    choice = input("Encrypt (E) or Decrypt (D): ").strip().upper()

    if choice == "E":
        msg = input("Enter message: ")
        key = int(input("Enter key: "))
        enc = caesar_encrypt(msg, key)
        print("\nEncrypted:", enc)

    elif choice == "D":
        cipher = input("Enter encrypted text: ")
        auto_decrypt(cipher)

    else:
        print("Invalid choice!")
