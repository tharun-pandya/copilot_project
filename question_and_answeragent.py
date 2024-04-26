from googlesearch import search
from bs4 import BeautifulSoup
from llms import LLMS
import requests

class QAagent:
    def __init__(self,st):
        self.st=st
    
    def search_and_scrape(self,query,num_sites):
        search_results = search(query,num_results=num_sites )

        scraped_data = []
        for link in search_results:
            try:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = ""
                for paragraph in soup.find_all('p'):
                    text += paragraph.get_text() + " "
                scraped_data.append(text)
            except Exception as e:
                return f"Error scraping {link}: {e}"
        
        return scraped_data
   
    def generate_summary(self,data, query,max_len):
        # prompt=r"extract  information relevant to query: "+str(query)+r"in the following data:"+" ".join(data)
        #prompt=r"Summarize the following data within "+str(max_len)+" words \ninput:"+" ".join(data)
        prompt="summarize the following data in "+ str(max_len)+" words. data:"+" ".join(data)
      
        model=LLMS("GEMINI")
        result= model.run(prompt)
        return result.text
    
    def get_latest_info(self,query,output_len=150,num_sites=10):
        self.st.write("Searching Google...")
        search_results = self.search_and_scrape(query,num_sites)
        self.st.write("Generating Summary...")
        summary = self.generate_summary(search_results,query,output_len)
        return summary