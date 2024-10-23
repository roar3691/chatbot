from flask import Flask, request, jsonify
import numpy as np
import pickle
import faiss
import os

app = Flask(__name__)

# Directory where files are stored
project_dir = '/Users/yanalaraghuvamshireddy/Downloads/Chatbot'

# Load previously saved vectorizer and embeddings
with open(os.path.join(project_dir, 'vectorizer.pkl'), 'rb') as f:
    vectorizer = pickle.load(f)

embeddings = np.load(os.path.join(project_dir, 'embeddings.npy'))

# Create a FAISS index and add embeddings
d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)

# Simulated course texts for returning results (ensure these match your data)
course_texts = [
    "Introduction to Python Programming",
    "Advanced Machine Learning Techniques",
    "Data Science with R"
]

@app.route('/')
def home():
    return "Welcome to the Course Search API"

@app.route('/search', methods=['POST'])
def search_courses():
    query = request.json.get('query')
    if not query:
        return jsonify({'error': 'Query is required'}), 400

    # Convert query to embedding using the same vectorizer
    query_embedding = vectorizer.transform([query]).toarray()

    # Perform search in FAISS index for top-5 similar courses
    D, I = index.search(query_embedding, k=5)

    # Collect results (indices of similar courses) and remove duplicates using set
    results = [course_texts[i] for i in I[0]]
    unique_results = list(set(results))

    return jsonify({'results': unique_results})

@app.errorhandler(404)
def page_not_found(e):
    return "This page does not exist", 404

if __name__ == '__main__':
    app.run(debug=True)