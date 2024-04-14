from langchain_cohere import ChatCohere
from langchain_core.messages import AIMessage
from langchain.prompts.chat import ChatPromptTemplate



chat_model = ChatCohere(cohere_api_key="7vuRcifreUcrTmd7BhawUHKDpRgTFhKx89mRI51J", temperature = 0.6 )

# os.environ["SERPAPI_API_KEY"] = "d6315857583bc9a0810143011f8a996a1b3f83324560162667cf7996ff266273"

def gen_business_name(domain):
    
    template = "You are a helpful assistant that generates a Business name for a given product."
    human_template = "give a company name for products of type : {product}, please don't include words like 'sure!' at the start, also don't ask any further question in the results."

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])


    chain = chat_prompt | chat_model
    
    name_output = chain.invoke({"product" : domain}).content
    
    template_command = "You are a helpful assistant that generates all the latest trends for a given Business domain."
    human_command = "give the latest trends for business domain : {domain}, please don't include words like 'sure!' at the start, also don't ask any further question in the results."
    
    trend_prompt = ChatPromptTemplate.from_messages([
        ("system",template_command),
        ("human", human_command)
        ])
    
    trend_chain = trend_prompt | chat_model
    
    trend_output = trend_chain.invoke({"domain" : domain}).content
    
    output = (name_output, trend_output)
    
    return output

if __name__ == "__main__":
    print(gen_business_name("Technology"))
    
 #   tool = GoogleTrendsQueryRun(api_wrapper=GoogleTrendsAPIWrapper())
 #   tool.run(domain)



