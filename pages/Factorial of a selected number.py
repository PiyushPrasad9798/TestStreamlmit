import streamlit as st
from background import set_bg
set_bg()
st.title("👨‍💻 Factorial python code 💻")
n=st.slider("➜ Pick a number 🔎",1,100)
f=1
for i in range(1,n+1):
    f=f*i
st.success(f"Factoral of {n} Is {f}")
st.subheader("👨‍💻 Python Code 💻")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("👨‍💻 Factorial python code 💻")
n=st.slider("➜ Pick a number 🔎",1,100)
f=1
for i in range(1,n+1):
    f=f*i
st.success(f"Factoral of {n} Is {f}")
st.subheader("👨‍💻 Python Code 💻")'''
with st.expander("</> Show Python Code </>"):
    st.code(code, language="python")
