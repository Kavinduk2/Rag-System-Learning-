"""
Document processing module for RAG system
"""

class DocumentProcessor:
    def __init__(self, data_dir='data/text_files'):
        self.data_dir = data_dir
        self.documents = []
    
    def load_documents(self):
        """Load all documents from the data directory."""
        import os
        
        if not os.path.exists(self.data_dir):
            raise ValueError(f"Directory not found: {self.data_dir}")
        
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.txt'):
                filepath = os.path.join(self.data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.documents.append({
                        'name': filename,
                        'content': content
                    })
        
        return self.documents
    
    def get_document_count(self):
        """Get the number of loaded documents."""
        return len(self.documents)
    
    def get_document_by_name(self, name):
        """Retrieve a specific document by name."""
        for doc in self.documents:
            if doc['name'] == name:
                return doc
        return None
