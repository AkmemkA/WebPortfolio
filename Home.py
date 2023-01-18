import streamlit as st
import pandas

st.set_page_config(layout='centered')


col0 = st.columns(1)
col1, empty_col, col2 = st.columns([1.5, 0.5, 2])
row1 = st.text("Contact Info Check")

with col1:
    st.image("images/Ava.png", width=300)

with col2:
    st.title("Sponge Bob")
    content = """
    Hello, my name is Bob, Sponge Bob. I am a creator of this super awesome
    website with 20 different projects written in python. As you see I am wearing shorts
    and the reason for that is that I cannot afford buying pants cause I am 
    out of job:( That is very sad and I am sure you feel pretty sorry. So what are
    you waiting for dear HR representative??? Go ahead and check out my projects and
    make me a job offer I won't be able to refuse!
    """
    st.write(content)

with row1:
    content2 = """
        Below you can see some applications I have made.
        """
    st.write(content2)


col3, col4 = st.columns(2)
df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
