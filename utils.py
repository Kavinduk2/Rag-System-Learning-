"""
Utility functions for RAG system
"""

def load_text_file(file_path):
    """Load text content from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")


def split_text_into_chunks(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks for processing."""
    chunks = []
    start = 0
    
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    
    return chunks


def clean_text(text):
    """Clean and normalize text content."""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Remove special characters but keep sentences
    return text.strip()
