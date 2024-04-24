import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

# set the path to the file
file_path = "random_paragraphs.txt"

# load the stop words
stop_words = set(stopwords.words('english'))

# read the contents of the file
with open(file_path, "r") as file:
    contents = file.read()

# tokenize the text
tokens = nltk.word_tokenize(contents)

# remove stop words
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# join the filtered tokens back into a string
filtered_text = ' '.join(filtered_tokens)

# count the frequency of each word
word_frequency = Counter(filtered_tokens)

# sort the word frequency in descending order
sorted_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

# show the top 100 most frequent words
for word, frequency in sorted_frequency[:100]:
    print(f"{word}: {frequency}")
