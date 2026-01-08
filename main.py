from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

def main():
    print("Hello from langchain-course!")
    information ="""
    Jeffrey Preston Bezos (/ˈbeɪzoʊs/ BAY-zohss;[2] né Jorgensen; born January 12, 1964) 
    is an American businessman best known as the founder, executive chairman, 
    and former president and CEO of Amazon, the world's largest e-commerce and cloud computing company. 
    According to Forbes, as of December 2025, Bezos's estimated net worth is US$239.4 billion, 
    making him the fourth richest person in the world.[3] He was the wealthiest person from 2017 to 2021,
    according to Forbes and the Bloomberg Billionaires Index.[4].
    Bezos was born in Albuquerque and raised in Houston and Miami. 
    He graduated from Princeton University in 1986 with a degree in engineering. 
    He worked on Wall Street in a variety of related fields from 1986 to early 1994.
    Bezos founded Amazon in mid-1994 on a road trip from New York City to Seattle. 
    The company began as an online bookstore and has since expanded to a variety of other e-commerce products and services, including video and audio streaming, cloud computing, and artificial intelligence. It is the world's largest online sales company, the largest Internet company by revenue, and the largest provider of virtual assistants and cloud infrastructure services through its Amazon Web Services branch.
    """
    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    llm = ChatOpenAI(model_name="gpt-5", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)
if __name__ == "__main__":
    main()
