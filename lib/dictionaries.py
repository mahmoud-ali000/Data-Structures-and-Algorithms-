def word_frequency(sentence):
    words = sentence.lower().split()
    freq_dict = {}
    
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
    
    return freq_dict

sentence = "This is a test sentence. This sentence is a test."
print(word_frequency(sentence))
