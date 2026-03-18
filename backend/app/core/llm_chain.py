from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from typing import List, Dict

class LLMGenerator:
    def __init__(self, model_name: str = "llama3.2"):
        # Connect to your local Ollama engine
        # We use a low temperature (0.1) to make the model analytical and strict, rather than creative.
        self.llm = Ollama(
            model=model_name,
            base_url="http://host.docker.internal:11434",
            temperature=0.1 
        )
        
        # The strict instruction manual for the AI
        self.prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="""You are Lumen, a precise AI teaching assistant for engineering students. 
            Answer the question based STRICTLY on the provided context below. 
            If the answer is not contained in the context, you must reply exactly with: "I cannot answer this based on the provided documents." 
            Do not make up formulas, facts, or external information.
            
            Context:
            {context}
            
            Question:
            {question}
            
            Answer:"""
        )

    def generate_answer(self, query: str, retrieved_chunks: List[Dict]) -> str:
        """
        Takes the user's question and the vector database chunks, 
        combines them into a prompt, and generates an answer.
        """
        # 1. Stitch the retrieved chunks together into one large text block
        context_text = "\n\n---\n\n".join([chunk["text"] for chunk in retrieved_chunks])
        
        # 2. Inject the context and the user's question into the template
        prompt = self.prompt_template.format(context=context_text, question=query)
        
        # 3. Ask the local LLM to generate the response
        response = self.llm.invoke(prompt)
        
        return response