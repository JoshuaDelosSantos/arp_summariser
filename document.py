from langchain_community.document_loaders import DirectoryLoader, TextLoader
import config

def get_documents(context_dir: str):
    loader = DirectoryLoader(context_dir, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents from {context_dir}")
    
    return documents

def curate_context(documents):
    combined_text = "\n\n--- NEXT DOCUMENT ---\n\n".join(
        [doc.page_content for doc in documents]
    )
    return combined_text

if __name__ == "__main__":
    print(curate_context(get_documents(config.CONTEXT_DIR)))