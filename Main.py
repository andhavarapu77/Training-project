from gensim.summarization import summarize

# Example text data
text = """
John Tukey, a pioneering figure in data analysis, once remarked that the best thing about being a statistician is that you get to play in everyone’s backyard.
Indeed, Tukey’s work has had a profound impact on the field of data analysis and statistics. His contributions to exploratory data analysis, in particular, have paved the way for modern data scientists to uncover insights from data in ways that were not previously possible.
From developing the Fast Fourier Transform algorithm to coining the term “bit” for binary digit, Tukey’s legacy is deeply embedded in the fabric of data analysis and computational statistics.
As we continue to explore and develop new methodologies for understanding data, the principles and techniques pioneered by Tukey remain as relevant and influential as ever.
"""

# Step 3: Summarize the Text
summary = summarize(text, ratio=0.3)  # The ratio parameter defines the proportion of the original text to include in the summary

print("Original Text:\n", text)
print("\nSummary:\n", summary)

