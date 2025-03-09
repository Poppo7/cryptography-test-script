def fragment_message(message, fragment_size):
    # splits a message into smaller fragments of given size
    fragments = [message[i:i+fragment_size] for i in range(0, len(message), fragment_size)]
    return fragments

def reassemble_fragments(fragments):
    # recombines fragments back into the original message
    return ''.join(fragments)

# Example Usage
if __name__ == "__main__":
    secret_message = "Your hidden message goes here"
    fragments = fragment_message(secret_message, 5)  # splitting into fragments of 5 chars
    print(f"Fragments: {fragments}")

    reconstructed_message = reassemble_fragments(fragments)
    print(f"Reconstructed Message: {reconstructed_message}")
