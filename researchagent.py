import arxiv
from  summarize import Summerize

class ResearchAgent:
    def __init__(self):
        None
        
  
    def get_latest_paper(self,research_area):
        client = arxiv.Client()
        search = arxiv.Search(
                query = research_area,
                max_results = 1,
                sort_by = arxiv.SortCriterion.SubmittedDate
            )

        paper = client.results(search)
        paper=next(paper)
        if paper.pdf_url:
            filename=str(paper.title)+".pdf"  
            paper.download_pdf(filename=filename)         
         
            summarizer=Summerize()
            return summarizer.process(filename)
        else:
            print("PDF not available for this paper.")
        
