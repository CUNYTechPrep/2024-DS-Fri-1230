import streamlit as st

st.markdown('# Streamlit is soo easy.')

st.markdown('### Cheat Sheet Stuff')
text_dropdown = st.expander("View Text Examples", icon=":material/info:")
print(text_dropdown)
with text_dropdown:
    st.write("Inside the expander.")
    st.text("Fixed width text")
    st.markdown("_Markdown_") # see *
    st.latex(r""" e^{i\pi} + 1 = 0 """)
    st.title("My title")
    st.header("My header")
    st.subheader("My sub")
    st.code("for i in range(8): foo()")
    st.html("<p>Hi!</p>")
    

image_dropdown = st.expander("View Image Examples", icon=":material/image:")
with image_dropdown:
    image_url = 'https://whalebonemag.com/wp-content/uploads/2015/04/IMG_3133-1050x788.jpg'
    caption = 'Displaying in image that is online. (Thanks to whalebone magazine.)'
    st.image(image_url, caption)

# callbacks_dropdown = st.expander("View Callbacks Examples", icon="📲")
callbacks_dropdown = st.expander("View Callbacks Examples")
with callbacks_dropdown:
    st.markdown('# Callbacks')
    
    st.markdown('---')
    button_result = st.button("Click me")
    if button_result:
        st.write('Your button_result variable = ', button_result)
    
    # # st.download_button("Download file", data)
    st.markdown('---')
    feedback_result = st.feedback("thumbs")
    if feedback_result:
        st.write("feedback_result", feedback_result)
    
    st.markdown('---')
    st.link_button("Go to a website", 'https://www.boredpanda.com/shiba-inu-stuck-in-bush-japan/')

    st.markdown('---')
    checkbox_result = st.checkbox("I agree")
    if checkbox_result:
        st.write('Checkbox Result', checkbox_result)


    st.markdown('---')
    toggle_result = st.toggle("Enable")
    if toggle_result:
        st.write("toggle_result", toggle_result)

    st.markdown('---')
    radio_result = st.radio("Pick one", ["cats", "dogs"])
    if radio_result:
        st.write("radio_result", radio_result)
    
    st.markdown('---')
    selectbox = st.selectbox("Pick one", ["cats", "dogs"])
    if selectbox:
        st.write(selectbox)

    st.markdown('---')
    multiselect = st.multiselect("Buy", ["milk", "apples", "potatoes"])
    if multiselect:
        st.write(multiselect)

    st.markdown('---')
    slider = st.slider("Pick a number", 0, 100)
    if slider:
        st.write(slider)
    
    st.markdown('---')
    user_text_input = st.text_input("Type your input here")
    if user_text_input:
        st.write("Your user text input:", user_text_input)

    st.markdown('---')
    date_input = st.date_input("Your birthday")
    if date_input:
        st.write("date_input", date_input)
