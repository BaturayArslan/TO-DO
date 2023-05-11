from application.app import create_app 
from application.entities.TodoList import TodoList
from datetime import date

if __name__ == "__main__":
    app = create_app(False)
    test = TodoList(10,"hello.",date.today())
    #app.run()