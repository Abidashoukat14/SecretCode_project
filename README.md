# SecretCode_project
# Secret Code Project

This project is a Python-based tool that allows users to encode and decode messages using a custom encryption process. It provides a simple, user-friendly interface for encoding secret messages with a pin key and decoding them. It also includes a unique feature that allows users to decode any message without using the original key, updating the key for future use.

# Features

**1. Encode a Message (With Pin Key):**

Users can encode any message into a secret code by providing a custom numerical pin key (0-9). This secret key is used to encrypt the message, which is then stored securely.

**2. Decode a Message (With Pin Key):**

Once a message is encoded, it can be decoded back into its original form using the same pin key that was used during the encoding process.

**3. Decode Any Code (Without Pin Key):**

The program also allows users to decode any secret code **without** using the original key. This feature updates the stored pin key for that specific message after decoding.

**4. Quit the Program Anytime:**

Users can exit the program at any time by selecting the "Quit" option.

# How It Works

**1. Encoding Process**
The program scrambles the message using random letters, digits, and symbols. The first character of each word is shifted to the end, and random characters are added to the front and back. This obfuscation ensures the message is unreadable without decoding.

**2. Decoding Process**
When decoding, the program strips away the random characters and reverses the transformation to recover the original message, but only if the correct pin key is provided. The special "decode any message" feature allows for decoding without the key, updating the key in the process.

# How to Use the Program

**Clone the Repository:**

`git clone https://github.com/your-username/secret-code-project.git
cd secret-code-project`

**Run the Program:**

`python secret_code.py`

**Follow the Menu:**

Enter `'code'` to encode a message.
Enter `'decode'` to decode a message using the same pin key.
Enter `'decodecode'` to decode any message without the key.
Enter `'quit'` to exit the program.

# Example Usage

# Encoding:

`Enter 'code' to code the message, 'decode' to decode the message, or 'decodecode' to decode without a key.
Or 'Quit' to quit: code`

**Enter your message:** Hello World  <br>

**Enter the Pin key:** 1234   <br>

**Coded Message:** aBc elloH?Ld+ 

# Decoding:

`Enter 'code' to code the message, 'decode' to decode the message, or 'decodecode' to decode without a key.
Or 'Quit' to quit: decode

**Enter your code message:** aBc elloH?Ld+    <br>

**Enter the Pin key:** 1234    <br>

**Decoded Message:** Hello World    <br>

# Decoding Without Pin Key:

`Enter 'decodecode' to decode any message without a key.`

**Enter your code message:** aBc elloH?Ld+ <br>

**Enter a new Pin key:** 5678   <br>

**Decoded Message**: Hello World 

# Error Handling

**1.** The program detects invalid pin keys during decoding and alerts the user.

**2.** If any unexpected errors occur during encoding or decoding, the program will catch and display the error message.

# Future Enhancements

**1. Graphical User Interface (GUI):**


I plan to add a GUI to make the program more interactive and accessible, using frameworks such as Tkinter or PyQt.

**2. Advanced Encryption:**

I will explore adding more advanced encryption algorithms, such as AES or RSA, to increase security.

**3. Complex Encoding Schemes:**

Future versions may support multiple layers of encoding, allowing users to apply more complex transformations to their messages.

# Contact

If you have any questions or suggestions, feel free to reach out via GitHub or LinkedIn.0 <br>

**linkedin:** https://www.linkedin.com/in/abida-shoukat-a5518831b/
