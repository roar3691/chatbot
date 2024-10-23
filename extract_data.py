from langchain_community.document_loaders import UnstructuredURLLoader

# Initialize the URL loader with the target URL
url_loader = UnstructuredURLLoader(urls=["https://brainlox.com/courses/category/technical"], mode="elements")

# Load and extract data
documents = url_loader.load()

# Extract text content from documents
course_texts = [doc.page_content for doc in documents]  # Use .page_content or similar attribute

# Print extracted texts for verification
print(course_texts)