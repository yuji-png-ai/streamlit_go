import streamlit as st

st.title("Radio buttons, Checboxes and buttons")
page_names = ['Checkbox', 'Button']
page = st.radio('Navigation', page_names)
st.write("**The variable 'page' returns:**", page)

if page == 'Checkbox':
    st.subheader("Welcome to the Checkbox page!")
    st.write("Nice to see you! :wave:")
    check = st.checkbox("Click here")
    st.write("State of the checkbox:", check)
    
if check:
    nested_btn = st.button("Button nested in Checkbox")
    
    if nested_btn:
        st.write(":cake:" * 20)
        
else:
    st.subheader("Welcome to the button page!")
    st.write(':thumsup')
    result = st.button('Click Here')
    st.write("State of button:", result)

if result:
    nested_check = st.checkbox("Checkbox nested in BUtton")
    if nested_check:
        st.write(":heart:"*20)
        

    
