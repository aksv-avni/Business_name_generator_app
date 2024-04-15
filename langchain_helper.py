from langchain_cohere import ChatCohere
from langchain_core.messages import AIMessage
from langchain.prompts.chat import ChatPromptTemplate



chat_model = ChatCohere(cohere_api_key="i2g6h90Q6ouBBph6VPNMqpTxImkbj5vJSu1tyA0H", model = "command-r", max_tokens = 50, temperature = 0.6 )

def gen_business_name(domain):
    
    template = "You are a helpful assistant that generates a Business name for a given product."
    human_template = "give a company name for products of type : {product}, please don't include words like 'sure!' at the start."

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])


    chain = chat_prompt | chat_model
    
    name_output = chain.invoke({"product" : domain}).content
    
    template_command = "You are a helpful assistant that generates all the latest trends for a given Business domain."
    human_command = "give the latest trends for business domain : {domain}, please don't include words like 'sure!' at the start."
    
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



