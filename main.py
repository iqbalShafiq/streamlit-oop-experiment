import streamlit as st
import pandas as pd
from libs import Coffee, Barista

if "coffees" not in st.session_state:
    try:
        df = pd.read_csv("coffees.csv")
        st.session_state.coffees = [
            Coffee(
                row["name"],
                row["price"],
                row["available"],
                Barista(row["barista_name"], row["barista_experience"]),
            )
            for _, row in df.iterrows()
        ]
    except FileNotFoundError:
        st.session_state.coffees = []


def save_to_csv():
    data = []
    for coffee in st.session_state.coffees:
        data.append(
            {
                "name": coffee.name,
                "price": coffee.price,
                "available": coffee.available,
                "barista_name": coffee.barista.name,
                "barista_experience": coffee.barista.experience_level,
            }
        )
    df = pd.DataFrame(data)
    df.to_csv("coffees.csv", index=False)


def clear_form():
    st.session_state.name = ""
    st.session_state.price = 0
    st.session_state.barista_name = ""
    st.session_state.barista_experience = ""


def submit():
    barista = Barista(
        st.session_state.barista_name, st.session_state.barista_experience
    )
    coffee = Coffee(st.session_state.name, st.session_state.price)
    coffee.set_barista(barista)
    st.session_state.coffees.append(coffee)

    save_to_csv()
    clear_form()


def update_coffee_availability(index):
    coffee.set_unavailable()
    st.session_state.coffees[index] = coffee
    save_to_csv()


st.title("Coffee Shop")
page = st.sidebar.selectbox("Choose a page", ["Add Coffee", "View Coffee"])

if page == "Add Coffee":
    st.write("Add Coffee")
    name = st.text_input("Name", key="name")
    price = st.number_input("Price", key="price")
    barista_name = st.text_input("Barista Name", key="barista_name")
    barista_experience = st.text_input("Barista Experience", key="barista_experience")
    btn_add = st.button("Add Coffee", on_click=submit)

elif page == "View Coffee":
    if len(st.session_state.coffees) == 0:
        st.write("No coffee available")
    else:
        for index, coffee in enumerate(st.session_state.coffees):
            st.write(coffee.name)
            st.write(coffee.price)
            st.write(coffee.barista)
            st.write(coffee.check_availability())

            if coffee.available:
                btn_unavailable = st.button(
                    "Set Unavailable",
                    key=f"btn_unavailable_{index}",
                    on_click=update_coffee_availability,
                    args=(index,),
                )
