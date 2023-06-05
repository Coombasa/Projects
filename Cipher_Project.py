import string
class Cipher:
    # Static variable containing a string with the lowercase latin alphabet to be used by class methods.
    # TODO include spaces.
    alpha = string.ascii_lowercase + " " + string.digits
    def __init__(self, key = None, shift = None):
        # Changes the global cipher alphabets. Empty arg prompts for key from user input.
        self.beta = Cipher.alpha
        self.gamma = []
        if key is None:
            # Gets user input for a key and/or a shift if they didn't include an argument.
            # Contained in loop to ensure an appropriate key is provided.
            while True:
                key = input("Enter a key which contains only one instance of each letter: ").lower()
                # Since a set can only contain one instance of each value, casting the key to a set
                # and comparing its length to that of the key length suffices to assure uniqueness of characters.
                if len(set(key)) == len(key):
                    break
            shift = input("If you'd like to include a shift, enter it here; if not, hit enter: ").lower()
        else:
            if len(set(key)) != len(key):
                while True:
                    input("Please use a key which contains only one instance of each character.")
                    if len(set(key)) == len(key):
                        break
            key = key.lower()
        for k in key:
            # Slice the alphabet in two places - on either side of each letter in the key.
            self.beta = self.beta[:self.beta.find(k)] + self.beta[self.beta.find(k) + 1:]
        # Brings the key to the front.
        self.beta = key + self.beta
        if shift is not None:
            for s in shift:
                # Generates shifted versions of the keyed alphabet for better encoding.
                self.gamma.append(self.beta[self.beta.find(s):] + self.beta[:self.beta.find(s)])
        print("New Cipher object has been generated.")

    def encode(self, mess=None, file=False, path=None):
        # Initial code to determine whether the call is being used to encode from a text file.
        if file:
            if path is None:
                path = input("Enter the name of the file to be encoded; if it is not in the script directory, "
                             "include the full path: ")
            with open(path, 'r') as f:
                mess = f.read()
        if mess is None or "":
            mess = input("Enter a string of text to encode: ")
        mess = mess.lower()
        # Initialize the string to be returned.
        rmess = ""
        # Encoding for simple ciphertext.
        if self.gamma == []:
            for m in mess:
                if m.isalnum() or m.isspace():
                    rmess += self.beta[Cipher.alpha.find(m)]
                else:
                    rmess += m
        # Encoding in two-key ciphertext.
        else:
            count = 0
            for m in mess:
                # This check avoids issues with spaces, and other characters outside the substitution.
                if m.isalnum() or m.isspace():
                    count %= (len(self.gamma) - 1)
                    rmess += self.gamma[count][Cipher.alpha.find(m)]
                    count += 1
                else:
                    rmess += m
        # Handle return or output based on arguments.
        if file:
            with open(path.replace(".txt", "") + '_encoded.txt', 'w') as f:
                f.write(rmess)
            print(f"Encoding complete. The output file can be found in the script directory, with "
                  f"path {path.replace('.txt', '')}_encoded.txt")
        else:
            return rmess

    # Leverage the encode method to run multiple passes of the same encoding.
    def m_encode(self, n, mess=None, file=False, path=None):
        if file:
            if path is None:
                path = input("Enter the name of the file to be encoded; if it is not in the script directory, "
                             "include the full path: ")
            with open(path, 'r') as f:
                mess = f.read()
        for k in range(n):
            mess = self.encode(mess)
        if file:
            with open(path.replace(".txt", "") + '_encoded.txt', 'w') as f:
                f.write(mess)
            print(f"Encoding complete. The output file can be found in the script directory, with "
                  f"path {path.replace('.txt', '')}_encoded.txt")
        else:
            return mess

    # Works the algorithm in reverse to decode encoded text.
    def decode(self, mess=None, file=False, path=None):
        if file:
            if path is None:
                path = input("Enter the name of the file to be decoded; if it is not in the script directory, "
                             "include the full path: ")
            with open(path, 'r') as f:
                mess = f.read().lower()
        if mess is None or "":
            mess = input("Enter a string of text to decode: ")
        mess = mess.lower()
        rmess = ""
        # Decoding from simple keyed ciphertext.
        if self.gamma == []:
            for m in mess:
                if m.isalnum() or m.isspace():
                    rmess += Cipher.alpha[self.beta.find(m)]
                else:
                    rmess += m
        # Decoding from two-key ciphertext.
        else:
            count = 0
            for m in mess:
                if m.isalnum() or m.isspace():
                    # Modulus assures that the count remains within the index of gamma.
                    # Count cycles through the list of shifted alphabets to further obscure the text.
                    count %= (len(self.gamma) - 1)
                    rmess += Cipher.alpha[self.gamma[count].find(m)]
                    count += 1
                else:
                    rmess += m
        if file:
            with open(path.replace(".txt", "") + '_decoded.txt', 'w') as f:
                f.write(rmess)
            print(f"Decoding complete. The output file can be found in the script directory, with "
                  f"path {path.replace('.txt', '')}_decoded.txt")
        else:
            return rmess

    # Decodes through multiple passes; inverse of m_encode.
    def m_decode(self, n, mess=None, file=False, path=None):
        if file:
            if path is None:
                path = input("Enter the name of the file to be decoded; if it is not in the script directory, "
                             "include the full path: ")
            with open(path, 'r') as f:
                mess = f.read()
        for k in range(n):
            mess = self.decode(mess)
        if file:
            with open(path.replace(".txt", "") + '_decoded.txt', 'w') as f:
                f.write(mess)
            print(f"Decoding complete. The output file can be found in the script directory, with "
                  f"path {path.replace('.txt', '')}_decoded.txt")
        else:
            return mess

    def show(self):
        print("This is the alphabet and numerals followed by the alphabet "
              "generated by substituting with the key argument.")
        print(" ".join(Cipher.alpha))
        print(" ".join(self.beta) + '\n|')
        if self.gamma is not []:
            for g in self.gamma:
                print(" ".join(g))
            print("The above alphabets are generated by starting the substituted "
                  "alphabet at the characters defined by the 'shift' argument.")

    # A static method for determining character frequency. Useful for decoding ciphertext in general cryptography.
    @staticmethod
    def char_freq(text=None, prt=True, file=True, path=None):
        freq = []
        if file:
            if path is None:
                path = input("Enter the name of the file to be analysed; if it is not in the script directory, "
                             "include the full path: ")
            with open(path, 'r') as f:
                text = f.read().lower()
        for a in Cipher.alpha:
            freq.append((a, text.count(a)))
        if prt:
            for f in freq:
                print(f)
        else:
            return freq