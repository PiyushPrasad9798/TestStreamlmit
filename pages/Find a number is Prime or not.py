import streamlit as st
from background import set_bg
set_bg()
st.title("Prime python code")
t1=st.slider("Pick a number",1,100)
count=0
for i in range(1,t1+1):
    if t1%i==0:
        count=count+1
if count==2:
    st.success("Number is Prime")
else:
    st.success("Number is not Prime")
st.subheader("Python Code")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("Prime python code")
t1=st.slider("Pick a number",1,100)
count=0
for i in range(1,t1+1):
    if t1%i==0:
        count=count+1
if count==2:
    st.success("Number is Prime")
else:
    st.success("Number is not Prime")
st.subheader("Python Code")'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
