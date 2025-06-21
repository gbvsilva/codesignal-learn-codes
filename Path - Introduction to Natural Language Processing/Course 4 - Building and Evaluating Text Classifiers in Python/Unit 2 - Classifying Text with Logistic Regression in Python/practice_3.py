import pandas as pd
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load the SMS Spam Collection dataset
sms_spam = load_dataset('codesignal/sms-spam-collection')

# Convert to pandas DataFrame for convenient handling
df = pd.DataFrame(sms_spam['train'])

# Initialize a TF-IDF Vectorizer and transform the messages
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(df['message'])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, df['label'], test_size=0.25, random_state=42)


# Train the Logistic Regression classifier with the training data
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Predict the labels of testing data
y_pred = log_reg.predict(X_test)

# Print the accuracy of the classifier on the testing set
print("Accuracy:", accuracy_score(y_test, y_pred))

# Custom code
new_messages = ['You have won a prize! Click here to claim your reward.',
                'Hi Graco, I need your help with an issue in the project.']
new_message_vec = vectorizer.transform(new_messages)
new_message_pred = log_reg.predict(new_message_vec)
print('New message category:', new_message_pred)
