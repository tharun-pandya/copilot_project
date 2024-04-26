import os

import streamlit as st
from sdlcagent import SDLC
from streamlit_extras.grid import grid
from io import StringIO
from ragagent import RAGagent
from tempfile import NamedTemporaryFile



def invoking_fitnesscoach(food_intake):
    from healthagent import HealthAgent
    health_agent=HealthAgent()
    st.write(health_agent.get_suggestions(food_intake.split(",")))

def invoking_researchagent(research_area):
    from  researchagent import ResearchAgent
    ra=ResearchAgent()
    st.write(ra.get_latest_paper(research_area))

def invoking_qa_agent(query):
    from question_and_answeragent import QAagent
    qa_agent=QAagent(st)
    st.write(qa_agent.get_latest_info(query,10))

def invoking_rag_agent(file_name):
    rag_agent=RAGagent(file_name)
    return rag_agent

def get_answer(rag_agent,question):
    st.write(rag_agent.get_answer(question))



    


st.title("Tharun Copilot")



options = ['Research Agent', 'Fitness Agent', 'Question and Answer Agent',"SDLC Agent","RAG agent"]

# Display the dropdownoptions
selected_option = st.selectbox( "How do you want me to assist you today?",
   options,
   index=None,
   placeholder="Select agent...", )

if selected_option=="Research Agent":
    research_area = st.text_input('Let me know which research area paper you would like')
    if st.button("Get paper summary"):
        invoking_researchagent(research_area)

    
elif selected_option=='Fitness Agent':
    food_intake = st.text_input('Hey,what is your diet today', '2 boiled eggs , 400 gm grilled chicken, 1 cup rice')
    if st.button("Get fitness suggestion"):
        invoking_fitnesscoach(food_intake)
      

elif selected_option=='Question and Answer Agent':

    query = st.text_input("Enter your search query:")

    
    if st.button("Search and Summarize"):
        if query:
            invoking_qa_agent(query)
        else:
            st.write("Please enter a search query.")


elif selected_option=="SDLC Agent":
    query = st.text_area("Enter your search query:")

    koundinya=SDLC()
    my_grid = grid([3, 3], [3, 3], [3, 3], vertical_align="bottom")

    if my_grid.button("Generate Code", use_container_width=True):
            
        st.write(koundinya.generate_code(query))
        
        
    if my_grid.button("Optimize", use_container_width=True):
         st.write(koundinya.optimize_code(query))


    if my_grid.button("Find bugs", use_container_width=True):
        st.write(koundinya.find_bugs(query))
        

    if my_grid.button("Generate Test cases", use_container_width=True):
       st.write(koundinya.generate_testcases(query))
   
    
    if my_grid.button("Add comments", use_container_width=True):
        st.write(koundinya.add_comments(query))

    if my_grid.button("Explain code", use_container_width=True):
        st.write(koundinya.explain_code(query))
        

elif selected_option=="RAG agent":
    
    uploaded_file = st.file_uploader("Choose a pdf file",type=['pdf'])
    if uploaded_file is not None:
        
        save_path = os.path.join(".", uploaded_file.name)
        with open(save_path, mode='wb') as w:
            w.write(uploaded_file.getvalue())
        
        rag_agent=invoking_rag_agent(save_path)
        
       
        question = st.text_input("Enter your question:")

        if st.button("Get Answer"):
            if question:
                get_answer(rag_agent,question)
            else:
                st.write("Please enter your question.")