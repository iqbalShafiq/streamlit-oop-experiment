import streamlit as st
from libs import Coffee, Producer

if "coffees" not in st.session_state:
    st.session_state.coffees = []

def clear_form():
    st.session_state.taste = ""
    st.session_state.price = 0
    st.session_state.producer_name = ""
    st.session_state.producer_location = ""

def submit():
    producer = Producer(producer_name, producer_location)
    coffee = Coffee(st.session_state.taste, price)
    coffee.set_producer(producer)

    st.session_state.coffees.append(coffee)
    clear_form()

st.title("Coffee Shop")

# create pages
page = st.sidebar.selectbox("Choose a page", ["Add Coffee", "View Coffee"])

if page == "Add Coffee":
    st.write("Add Coffee")
    taste = st.text_input("Taste", key="taste")
    price = st.number_input("Price", key="price")
    producer_name = st.text_input("Producer Name", key="producer_name")
    producer_location = st.text_input("Producer Location", key="producer_location")
    btn_add = st.button("Add Coffee", on_click=submit)

elif page == "View Coffee":
    if len(st.session_state.coffees) == 0:
        st.write("No coffee available")
    else:
        for index, coffee in enumerate(st.session_state.coffees):
            st.write(coffee.taste)
            st.write(coffee.price)
            st.write(coffee.producer)
            st.write(coffee.check_sold_out())
            
            if not coffee.sold_out:
                btn_sold_out = st.button("Sold Out", key=f"btn_sold_out_{index}")

                if btn_sold_out:
                    coffee.set_sold_out()
                    st.rerun()
