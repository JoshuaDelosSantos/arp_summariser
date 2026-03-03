from langchain_core.prompts import ChatPromptTemplate
import config
import document
import llm

def main():
    document_context = document.curate_context(document.get_documents(config.CONTEXT_DIR))
    
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI researcher. Give key insights from the provided context. Limit insights to 1 point per paper. Ensure to provide paper tittles and authors for each insight.

    <context>
    {context}
    </context>

    Question: {question}
    """)
    
    model = llm.get_chat_model(config.CHAT_MODEL)
    
    chain = prompt | model
    
    response = chain.invoke({
        "context": document_context,
        "question": "Summarise the attached papers."
    })
    
    print(response.content)
    
if __name__ == "__main__":
    main()