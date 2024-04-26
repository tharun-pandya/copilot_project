
import requests
from  llms import LLMS
from IPython.display import Markdown
import textwrap
class HealthAgent:
    def __init__(self):
        None
        
    def to_markdown(self,text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    
    def get_suggestions(self,food_intake):    

        url = 'https://api.edamam.com/api/nutrition-details'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        data = {
            "title": "string",
            "ingr":food_intake,
            "url": "https://api.edamam.com/api/nutrition-details",
            "summary": "string",
            "yield": "string",
            "time": "string",
            "img": "string",
            "prep": "string"
        }

        params = {
            'app_id': '6529f2a4',
            'app_key': '1184d0536c25efd8eefd1d260309aa64',
            'beta': 'true',
            'force': 'true',
        }

        response = requests.post(url, headers=headers, params=params, json=data)



        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            self.calories=data["calories"]
            # prompt="you are best fitness coach. you need to suggest dietary and fitness activities for 31 year old male with 176 cm  height , 75 kgs weight based on todays "+str(self.calories) +" calories consumption"
            prompt="""As a fitness coach for Me (Bharat), provide suggestions for me to maintain good health like 
                        1. Mention my personal details along with total amount of calories consumed today
                        2. suggest exercises or fitness activities needs to be done today to maintain optimal body mass index  for 31 year old male with 176 cm  height , 60 kgs weight based on todays "+str(self.calories) +" calories consumption"
                        """
            model=LLMS("GEMINI")
            result= model.run(prompt)
            
            return result.candidates[0].content.parts[0].text if result.candidates[0] else result.text
            
        else:
            print("Request failed with status code:", response.status_code)

  
       

        
        
        
