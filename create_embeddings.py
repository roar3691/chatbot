import os
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss

# Directory to save files
project_dir = '/Users/yanalaraghuvamshireddy/Downloads/Chatbot'
os.makedirs(project_dir, exist_ok=True)

# Load course texts from the previous step
course_texts = [
    "Introduction to Python Programming",
    "Advanced Machine Learning Techniques",
    "Data Science with R"
    # Add more texts if available from your extraction step
]

# Create embeddings using TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(course_texts).toarray()

# Save the embeddings and vectorizer for later use
np.save(os.path.join(project_dir, 'embeddings.npy'), embeddings)
with open(os.path.join(project_dir, 'vectorizer.pkl'), 'wb') as f:
    pickle.dump(vectorizer, f)

# Create a FAISS index and add embeddings
d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)
faiss.write_index(index, os.path.join(project_dir, 'course_index.faiss'))

print("Embeddings and vectorizer saved successfully.")