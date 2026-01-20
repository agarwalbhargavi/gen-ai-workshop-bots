import streamlit as st
from groq import Groq

st.set_page_config("BHARGAVI-AI Content Generator", layout="wide")
st.title("📢 BHARGAVI-AI – Content Generator")
col_img, col_title = st.columns([1, 5])

st.image(
    "https://sp.yimg.com/ib/th/id/OIP.BPRwAy_Kmot1UHCnmYE5BQAAAA?pid=Api&w=148&h=148&c=7&dpr=2&rs=1",
    width=80
)


client = Groq(api_key=st.secrets["GROQ_API_KEY"])

col1, col2 = st.columns(2)

with col1:
    product = st.text_input("Product")
    audience = st.text_input("Audience")

    if st.button("Generate Content"):
        prompt = f"Write marketing content for {product} targeting {audience}."
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        st.session_state.text = response.choices[0].message.content

with col2:
    if "text" in st.session_state:
        content = st.text_area("Generated Content", st.session_state.text, height=300)

        st.download_button(
            label="⬇️ Download as TXT",
            data=content,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
    else:
        st.info("Generate content first")
