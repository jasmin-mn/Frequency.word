import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Text to analyze
text = "Artificial Intelligence (AI) is a branch of computer science that focuses on creating machines that can think and learn like humans. AI systems can analyze data, recognize patterns, and make decisions without being explicitly programmed for every task. AI is used in many areas such as healthcare, education, finance, and transportation. For example, AI helps doctors detect diseases, supports students in learning, and powers virtual assistants like chatbots. As technology continues to grow, AI is becoming more important in improving efficiency, solving complex problems, and shaping the future of work and society."

# Make text lowercase and split into words
words = text.lower().split()

# (words we ignore)
stop_words = {
    "is", "a", "the", "of", "and", "to", "in", "that", "from", "on"
}

# Remove stopwords
filtered_words = []
for word in words:
    if word.isalpha() and word not in stop_words:
        filtered_words.append(word)

# Count word frequency using NLTK
frequency = FreqDist(filtered_words)

# Take top 10 words
common_words = frequency.most_common(10)

# Separate words and counts
words_list = []
counts = []

for word, count in common_words:
    words_list.append(word)
    counts.append(count)

# Draw bar chart using matplotlib
plt.figure()
plt.bar(words_list, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency (NLTK + Matplotlib)")
plt.show()
