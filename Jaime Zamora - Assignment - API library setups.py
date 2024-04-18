import tkinter as tk
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to tokenize and summarize the text
def process_text():
    input_text = text_input.get("1.0", "end-1c")
    words = word_tokenize(input_text)
    sentences = sent_tokenize(input_text)
    blob = TextBlob(input_text)
    summary = blob.noun_phrases

    # Update GUI with results
    word_count_var.set(f"Word Count: {len(words)}")
    sentence_count_var.set(f"Sentence Count: {len(sentences)}")
    summary_var.set(f"Key Phrases: {', '.join(summary[:5])}")

    # Generate a word cloud
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(input_text)
    plt.figure(figsize=(8, 4), dpi=100)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# Set up the GUI
root = tk.Tk()
root.title("Text Manipulation Tool")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

analyze_button = tk.Button(root, text="Analyze Text", command=process_text)
analyze_button.pack()

word_count_var = tk.StringVar()
word_count_label = tk.Label(root, textvariable=word_count_var)
word_count_label.pack()

sentence_count_var = tk.StringVar()
sentence_count_label = tk.Label(root, textvariable=sentence_count_var)
sentence_count_label.pack()

summary_var = tk.StringVar()
summary_label = tk.Label(root, textvariable=summary_var)
summary_label.pack()

root.mainloop()
