def main():
    name = input("\nInput your name:")
    age = int(input("\nInput you age:"))

    # print("Your name is " + name + " and you are " + str(age) + " years old.")
    print("Your name is", name, "and you are" , age, "years old.")

    sentence = input("\nInput a sentence:")
    print("The sentence is:", sentence)

    word_to_be_replaced = input("\nEnter the word to be replaced in the sentence above:")
    new_word = input("Enter the new word to replace the one right above:")

    new_sentence = sentence.replace(word_to_be_replaced, new_word)
    print("\nThe new sentence is:", new_sentence)

if __name__ == "__main__":
    main()