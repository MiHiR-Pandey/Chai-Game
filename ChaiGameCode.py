import streamlit as st

st.set_page_config(
page_icon=("chai.png")
)

st.header("Chai Maker")
st.subheader("A Simple Chai Making Game")

base = st.radio('Select your chai base:', ['Milk', 'Water', 'Almond Milk'])
st.text(f'Your selected base for chai is {base}')

flavour = st.selectbox('Select Your Flavour', ['Adrak', 'Masala', 'Honey', 'Herbs'])
st.text(f'Your Selected Flavour is {flavour}')

items = st.multiselect('Select Ingredents', ['Sugar', 'Lemon', 'Adrak', 'Elachi'])

if 'Sugar' in items:
    sugar = st.slider('Select number of spoons', 1, 10)
    st.text(f'You Choose {sugar} spoon(s) of sugar')

    if sugar >= 7:
        st.warning('Chai will become very sweet!')

if 'Adrak' in items:
    adrak = st.number_input('Select How Much Picese of Adrak You Want: ', 1, 10)
    st.write(f'You Choose {adrak} Pisces of Adrak')

    if adrak >= 5:
        st.warning('Chai will become very bitter!')

if 'Elachi' in items:
    elachi = st.number_input('Select How Much Picese of Adrak You Want: ', 1, 10)
    st.write(f'You Choose {elachi} Pisces of Elachi')

