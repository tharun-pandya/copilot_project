from langchain.document_loaders import PyPDFLoader
from llms import LLMS

class Summerize:
    def __init__(self):
        None

    


    def process(self,file_name):
        loader = PyPDFLoader(file_name)
        pages = []
        for page in loader.load_and_split():
            pages.append(page.page_content)

        prompt="Please summarise this document:"+ " ".join(pages)
        model=LLMS("GEMINI")
        result= model.run(prompt)
        return result.text
    
        
       