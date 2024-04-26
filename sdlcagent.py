from llms import LLMS
from IPython.display import display
from IPython.display import Markdown
import textwrap


class SDLC:
    def __init__(self):
        None
    def to_markdown(self,text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    def generate_code(self,query):
        prompt_used = """
            Infer the programming language  from user input, otherwise use python, to Write efficient and well documented code

            with the following considerations:
            - include or import required libraries
            - Identify the expected input format and data types
            - Identify the expected output format and data types
            - consider any time or space complexity constraints that are implied or explicitly stated
            - Handle all extreme possible cases of errors
            - Handle exceptions whenever there is possibility
         
           
   
        """+"\n based on user input: "+query
        model=LLMS("GEMINI")
        result=model.run(prompt_used)
        return self.to_markdown(result.text).data          
    
    def optimize_code(self,query):
        prompt_used = """
            Identify programming language and optimize code interms of it time complexity and space complexity along with proper documentation

            with the following considerations:
            - include or import required libraries
                      

            """+"\n input: "+query
        model=LLMS("GEMINI")
        result=model.run(prompt_used)
        return result.text 
    
    def find_bugs(self,query):
        prompt_used = """
            Identify programming language and Point out the bugs in the code

            """+"\n input: "+query
        
        model=LLMS("GEMINI")
        result=model.run(prompt_used)
        return result.text 
    
    def generate_testcases(self,query):
        prompt_used = """
            Identify programming language and generate 10 sample inputs and expected outputs in the following format
            Inputs:
             provide input data from Infered input data type like
             1.
             2.
                        
            Outputs:
             provide corresponding output in infered output data type like
             1.
             2.

            for the following code

            """+"\n input: "+query

        
        model=LLMS("GEMINI")
        result=model.run(prompt_used)
        return result.text  
    def add_comments(self,query):
        prompt_used = """
            Identify programming language and add comments to the code line by line

            """+"\n input: "+query         
        model=LLMS("GEMINI")
        result=model.run(prompt_used)
        return result.text  
    def explain_code(self,query):
        prompt_used = """
            Identify programming language and explain each line of code like
            //explaination
            code line

            for the below\n input: """+query
         
        model=LLMS("GEMINI")
        result=model.run(prompt_used)
        return result.text  
    