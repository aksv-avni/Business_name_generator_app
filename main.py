
import streamlit as st
import langchain_helper

st.title("NameSphere : Trend Explorer & Business Naming Guru 😎")
st.header("**Generate your Business Name and stay updated on the latest trends within your Industry. 🎯**")
st.write("_Your response is baking! Please hold on a bit longer...😊_")
domain = st.sidebar.selectbox("Choose your Domain", ("Technology 👨‍💻","Apparels 👕","Healthcare 🩺", "Finance 💰","Retail 📊"
                                            ,"Fashion and Beauty 💄","Hospitality 🏨", "Education 📚",
                                            "Sports 🏀"))

if domain :
    response = langchain_helper.gen_business_name(domain)
    if domain == "Technology 👨‍💻":
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0])
        st.write(response[1])
    if domain == "Apparels 👕":
        st.image("https://images.unsplash.com/photo-1523381294911-8d3cead13475?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
    if domain == "Healthcare 🩺":
        st.image("https://plus.unsplash.com/premium_photo-1674499074438-8f611a3569f6?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
    if domain == "Finance 💰":
        st.image("https://plus.unsplash.com/premium_photo-1681469490209-c2f9f8f5c0a2?q=80&w=1783&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
    if domain == "Retail 📊":
        st.image("https://plus.unsplash.com/premium_photo-1664202219714-7451573a4fa7?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
    if domain == "Fashion and Beauty 💄":
        st.image("https://images.unsplash.com/photo-1621797064712-2ed3a36fc009?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
    if domain == "Hospitality 🏨":
        st.image("https://images.unsplash.com/photo-1544986581-efac024faf62?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
    if domain == "Education 📚":
        st.image("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
    if domain == "Sports 🏀":
        st.image("https://images.unsplash.com/photo-1517649763962-0c623066013b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 width = 300)
        st.write(response[0]) 
        st.write(response[1])
        
