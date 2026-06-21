import streamlit as st
import base64

st.set_page_config(layout="wide")

# Background Image
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
img = get_base64("background.jpg")
st.markdown(
    f"""
    <style>
    .stApp {{
        background:
            linear-gradient(
                rgba(0,0,0,0.8),
                rgba(0,0,0,0.8)
            ),
            url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Title
st.markdown("""
<h1 style='
text-align:center;
color:white;
font-size:50px;
white-space:nowrap;
'>
🎓📝 Welcome to All the Basic Python Codes 🚀📖
</h1>
""", unsafe_allow_html=True)
# Logo and Login Form in Center
col1, col2, col3 = st.columns([3,2,3])

with col2:
    st.image("logo.jpg", width=200)

    t1 = st.text_input("USERNAME")
    t2 = st.text_input("PASSWORD", type="password")

    b1 = st.button("Sign In")
    #b2 = st.button("Forget Password")
if b1:
    if t1=="":
       st.error("Please enter a Username and try again")
    elif t2=="":
       st.error("Please enter your Password and try again")
    else:
       st.success(f"Welcome {t1}!")
       st.toast("Login Successful 🚀")
       st.balloons()
code='''
import streamlit as st
import base64

st.set_page_config(layout="wide")

# Background Image
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
img = get_base64("background.jpg")
st.markdown(
    f"""
    <style>
    .stApp {{
        background:
            linear-gradient(
                rgba(0,0,0,0.8),
                rgba(0,0,0,0.8)
            ),
            url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Title
st.markdown("""
<h1 style='
text-align:center;
color:white;
font-size:50px;
white-space:nowrap;
'>
🎓📝 Welcome to All the Basic Python Codes 🚀📖
</h1>
""", unsafe_allow_html=True)
# Logo and Login Form in Center
col1, col2, col3 = st.columns([3,2,3])

with col2:
    st.image("logo.jpg", width=200)

    t1 = st.text_input("USERNAME")
    t2 = st.text_input("PASSWORD", type="password")

    b1 = st.button("Sign In")
    #b2 = st.button("Forget Password")
if b1:
    st.toast("Login Successful 🚀")
    st.balloons()
    if t1=="":
       st.error("Please enter a Username and try again")
    elif t2=="":
       st.error("Please enter your Password and try again")
    else:
       st.success(f"Welcome {t1}!")
'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
