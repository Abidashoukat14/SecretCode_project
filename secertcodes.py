import string
import random  
message_key_store = {}  
def coding(message,codekey):
    code=message.split(" ")
    newword=[]
    try:
        for word in code:
            if (len(word)>=3):
                newMessage="".join(random.choices(string.ascii_letters+string.digits,k=3))+ word[1::] + word[0]+"".join(random.choices(string.punctuation+string.ascii_letters+string.digits,k=3))
                newword.append(newMessage)
            else:
                newword.append(word[::-1])
        coded_message=" ".join(newword)
        message_key_store[message] = codekey
        print(f"        Coded Message: {coded_message}\n")
    except Exception as e:
        print(f"Opps!Something Is Wrong.An Error Is Occured {e}") 
def decoding(Code,decodekey):
    code=Code.split(" ")
    newword=[]
    try: 
        original_message = None
        for msg, key in message_key_store.items():
            if key == decodekey:
                original_message = msg
                break

        if original_message is None:
            print("Error: Invalid decode key. The key doesn't match any stored message.")
            return
        for word in code:
              if(len(word)>=3):
                  newmessage=word[3:-3]
                  newmessage=newmessage[-1] + newmessage[:-1]
                  newword.append(newmessage)
              else:
                  newword.append(word[::-1])   
        decoded_message=" ".join(newword)
        message_key_store[message] = decodekey
        print(f"         Decoded Message: {decoded_message}\n") 
        if decoded_message == original_message:
            print("Decoded message successfully.")
        else:
            print("Warning: Decoded message might not match the original message.")      
    except Exception as e:
        print(f"Opps!Something Is Wrong.An Error Is Occured {e}\n")

def decodecode(Code,decodekey):
    code=Code.split(" ")
    newword=[]
    try: 
        for word in code:
              if(len(word)>=3):
                  newmessage=word[3:-3]
                  newmessage=newmessage[-1] + newmessage[:-1]
                  newword.append(newmessage)
              else:
                  newword.append(word[::-1])   
        decoded_code=" ".join(newword)
        message_key_store[message] = decodekey
        print(f"           Decoded Message: {decoded_code}\n") 
    except Exception as e:
        print(f"Opps!Something Is Wrong.An Error Is Occured {e}\n")            
def quit():
     print("--------You Quit It . -------\n")
     
while True:   
 choice=input("Enter 'code' to code the mesagae .'decode' to Decoded same coded message .\n\nOr 'decodecode' to decode any code or 'Quit' to Quit it :").lower()
 if choice=="code":
    message=input("       Enter your message : ")
    codekey=int(input("\nEnter the Pin key.Its for safety. Pin must be a numbers (0-9)\n"))
    coding(message,codekey)    
 elif choice=="decode":
    Code=input("          Enter your code message : ")
    decodekey=int(input("\nEnter the Pin key.Its for safety.Pin must be a numbers (0-9)\n"))
    decoding(Code,decodekey)
 elif choice=="decodecode":
    Code=input("          Enter your code message : ")
    decodecodekey=int(input("\nEnter the Pin key.Its for safety.Pin must be a numbers (0-9)\n"))
    decodecode(Code,decodecodekey)   
 elif choice == "quit":
        quit()
        break
 else:
        print("Invalid choice. Please enter 'code', 'decode', or 'quit'.\n")    