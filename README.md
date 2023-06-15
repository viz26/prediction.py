# prediction.py
This code demonstrates a simple sentiment analysis task using the scikit-learn library in Python.

1) The code begins by importing the necessary modules: CountVectorizer for text vectorization and MultinomialNB for the Naive Bayes classifier.
2) The training data consists of a list of conversations, where each conversation is represented as a dictionary with a 'text' key and a 'sentiment' key.
   The 'text' key contains the text of the conversation, while the 'sentiment' key specifies the sentiment (positive or negative) associated with that conversation.
3) The 'texts' list is created by extracting the text from each conversation in the training data.
4) The 'outcomes' list is created by extracting the sentiment from each conversation in the training data.
5) A CountVectorizer object is instantiated to convert the text data into a matrix of token counts. It tokenizes the text and creates a feature vector representation.
6)  'X' variable is created by fitting the vectorizer to the 'texts' data and transforming it into a sparse matrix. It represents the vectorized text data.
7)  An instance of the MultinomialNB classifier is created.
8)  The classifier is trained using the vectorized training data ('X') and the corresponding sentiment labels ('outcomes').
9)  The 'new_conversations' list contains new conversation texts for which we want to predict the sentiment.
10)  The 'new_X' variable is created by transforming the 'new_conversations' data using the same vectorizer used for training. It represents the vectorized new conversation data.
11)  The trained classifier is then used to predict the sentiment ('positive' or 'negative') for each conversation in 'new_X'.
12)  Finally, the predicted sentiments for each new conversation are printed.



Finally, the predicted sentiments for each new conversation are printed.
