import streamlit as st
import functions


result = functions.get_read_lines()

def add_todo():
    item = st.session_state["new_todo"] + "\n"
    # call the key to store new todos items
    result.append(item)
    functions.get_write_lines(result)

st.title("My Todo App")
st.subheader("This is SubHead of Todo App ")
st.write("This is a simple text")

for index, item in enumerate(result) :
    check = st.checkbox(item, key=item)
    if check:
        result.pop(index)
        functions.get_write_lines(result)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add New Todo's",
               on_change=add_todo, key='new_todo')           #on_change return custom key word
