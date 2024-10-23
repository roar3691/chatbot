Here's an updated README with a section for assignment submission notes:

---

# Chatbot Project

This project is a custom chatbot built using Langchain, designed to extract course information from a URL, create embeddings, and provide a RESTful API for searching courses.

## Features

- **Data Extraction**: Extracts course data from a specified URL using Langchain.
- **Embeddings Creation**: Utilizes TF-IDF to create embeddings and stores them in a FAISS vector store.
- **Flask RESTful API**: Provides an API to handle search queries and return relevant course information.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/roar3691/chatbot.git
   cd chatbot
   ```

2. **Set Up Environment**:
   Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Extract Data**:
   Run the script to extract course data:
   ```bash
   python extract_data.py
   ```

2. **Create Embeddings**:
   Generate and store embeddings:
   ```bash
   python create_embeddings.py
   ```

3. **Run the Flask API**:
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Test the API**:
   Use Postman or `curl` to send POST requests to `http://127.0.0.1:5000/search` with JSON data:
   ```json
   {
     "query": "Python"
   }
   ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any changes or suggestions.

## License

This project is licensed under the MIT License.

## Submission Notes

- Ensure all code is pushed to the public GitHub repository.
- Verify that the README file is complete and accurate.
- Share the GitHub repository URL as part of your assignment submission.
- Confirm that all required files are included and that instructions are clear for setting up and running the project.
