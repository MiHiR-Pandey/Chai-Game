import streamlit as st
import time

st.set_page_config(
    page_icon=("chai.png")
)

st.header("Chai Maker")
st.subheader("A Simple Chai Making Game")

#Base Selection 
base = st.radio('Select your chai base:', ['Milk', 'Water', 'Almond Milk'])
st.text(f'Your selected base for chai is {base}')

# Flavour SelectioN
flavour = st.selectbox('Select Your Flavour', ['Adrak', 'Masala', 'Honey', 'Herbs'])
st.text(f'Your Selected Flavour is {flavour}')

#Ingredients Selection 
items = st.multiselect('Select Ingredients', ['Sugar', 'Lemon', 'Adrak', 'Elachi'])

# Sugar Logic 
if 'Sugar' in items:
    sugar = st.slider('Select number of spoons', 1, 10)
    st.text(f'You chose {sugar} spoon(s) of sugar')

    if sugar >= 7:
        st.warning('Chai will become very sweet!')

#Adrak Logic
if 'Adrak' in items:
    adrak = st.number_input('Select how many pieces of Adrak you want:', 1, 10)
    st.write(f'You chose {adrak} pieces of Adrak')

    if adrak >= 5:
        st.warning('Chai will become very bitter!')

#Elachi Logic
if 'Elachi' in items:
    elachi = st.number_input('Select how many pieces of Elachi you want:', 1, 10)
    st.write(f'You chose {elachi} pieces of Elachi')

# Show Stove Button ONLY If All Ingredients Are Selected #
required_ingredients = {'Sugar', 'Adrak', 'Elachi'}
if required_ingredients.issubset(set(items)) and base and flavour:
    st.success("All ingredients selected! Ready to cook.")

    if 'start_cooking' not in st.session_state:
        st.session_state.start_cooking = False

    if not st.session_state.start_cooking:
        if st.button('🔥 Turn On Stove'):
            st.session_state.start_cooking = True
            st.rerun()

# Stove Logic: Timer, Image #
if st.session_state.get('start_cooking', False):
    st.info("🍵 Making your chai... Please wait 10 seconds")

    # Progress Bar for 10 seconds
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i + 1)

    # Chai Ready Message
    st.success("🎉 Your Chai is Ready! Enjoy! ☕")

    # Show Chai Image #
    st.image('chai.png', caption='Hot Chai Ready!', width=400)  # Use your image

    #Reset Btton
    if st.button('🔄 Make Again'):
        st.session_state.start_cooking = False
        st.rerun()
