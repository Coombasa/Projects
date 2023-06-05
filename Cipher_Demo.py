import Cipher_Project as ciph

print("This is a demo script that showcases the use of my Cipher Project class.")
print("To begin with, we generate two instances of the class, then encrypt and decrypt a string with them:")

first = ciph.Cipher("key", "shift")
second = ciph.Cipher("bismuth 12", "a particularly long phrase with spaces and 1 or 2 numbers")

test_string = "Make sure that Steven doesn't find out about his surprise party at 1 pm tomorrow!"
print(test_string)
print(first.encode(test_string) + " | " + first.decode(first.encode(test_string)))
print(second.encode(test_string) + " | " + first.decode(first.encode(test_string)))

print("Note that because the space is treated like any other character, the message is further obfuscated.")
print("This behaviour could be extended to all ASCII characters for even greater security, "
      "which would ultimately lead to simpler code, as well as preserve capitalization.")
print("However, any risk of Unicode characters would force the return of some complexity!")
print()
print("The generation of a new Cipher can also be completed in other ways..")
print("Here - follow the prompts to make your own...")
print()
user = ciph.Cipher()
print()
print("Now here is the original string as well as it's encoded and decoded version.")
print(user.encode(test_string) + " | " + user.decode(user.encode(test_string)))
print()
print("Here, the class method show() is used to display all three of the ciphers used so far. "
      "This method is mostly for educational purposes, or if one wanted to make a handwritten version.")
print()
first.show()
print()
second.show()
print()
user.show()
print()