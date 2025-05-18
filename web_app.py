import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("Todo App")
#terminal: streamlit run C:\Users\maham\PycharmProjects\PythonProject\web_app1\web_app.py
st.subheader("This is the Todo app")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo") #or an empty string

#st.session_state
#pip freeze > requirements.txt
#https://pioneers-m85qskvk9vzfheanekjbcx.streamlit.app/