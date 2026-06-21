import streamlit as st
from background import set_bg
set_bg()
st.title("Generate table of a number in streamlit")
t1=st.slider("Select a number",1,1000)
if st.button("Generate Table"):
    for i in range(1,11):
        st.write(i*t1)
st.subheader("Python Code")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("Generate table of a number in streamlit")
t1=st.slider("Select a number",1,1000)
if st.button("Generate Table"):
    for i in range(1,11):
        st.write(i*t1)
st.subheader("Python Code")'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
