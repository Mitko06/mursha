def convert_sentence(sentence):
    convert_sentence = ""
    for let in sentence:
        if let.islower():
            convert_sentence += let.upper()
        elif let.isupper():
            convert_sentence += let.lower()
        elif let =="?":
            convert_sentence += "."
        else: 
            convert_sentence += let
    return convert_sentence
    
input_sentence = input("Iskam izrechenie: ")
print(convert_sentence(input_sentence))