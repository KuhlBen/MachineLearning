def main():
    sentence = "I am a teacher and I love to inspire and teach people"

    # Split the sentence into words
    words = sentence.split()

    # Use a set to get unique words
    unique_words = set(words)

    # Get the number of unique words
    num_unique_words = len(unique_words)

    # Display the results
    print("Original Sentence:", sentence)
    print("Unique Words:", unique_words)
    print("Number of Unique Words:", num_unique_words)


main()
