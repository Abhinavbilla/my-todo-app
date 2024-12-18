import streamlit as sl
import function

todos = function.get_todos()
def add_todo():
    new_todo = sl.session_state["new_todo"]+"\n"
    print(new_todo)
    todos.append(new_todo)
    function.write_todos(todos)
sl.title("Todo app")
sl.subheader("hi")
sl.write("this is my personal todo app")


for index,todo in enumerate(todos):
    checkbox = sl.checkbox(todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        sl.experimental_rerun()

sl.text_input(label="",placeholder="Add todo.....",
              on_change=add_todo,key="new_todo")
sl.session_state