# word_counter.py

def count_word_frequency(file_name):
    try:
        with open(file_name, "r") as f:
            text = f.read().lower()
            words = text.split()
            
            word_count = {}
            for word in words:
                word = word.strip(".,!?")  # remove punctuation
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            
            return word_count
    except FileNotFoundError:
        print("File not found! Please check the file name.")

if __name__ == "__main__":
    file_name = "sample.txt"   # add a sample text file in this folder
    counts = count_word_frequency(file_name)
    if counts:
        for word, freq in counts.items():
            print(f"{word}: {freq}")

# word_counter.py

def count_word_frequency(file_name):
 
    try:
        with open(file_name,"r") as f:
            text = f.read().lower()
            words = text.split()
        
            word_count = {}
            for word in words:
                word = word.strip(".,?!")     # removes punctuation
                if word in word_count:
                    word_count[word] +=1
                else:
                    word_count[word] = 1

            return word_count

    except FileNotFoundError:
        print("File not Foun! Please check the file name.")


if __name__ == "__main__":
     file_name = "sample.txt"
     counts = count_word_frequency(file_name)
     if counts:
         for word, freq in counts.items():
             print(f"{word} : {freq}")
             
