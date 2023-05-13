from application.app import create_app 

from application.entities.TodoList import TodoList
from datetime import date
from application.repositories.ListRepository import ListRepository
from application.providers.orm.models import ListModel, ItemModel

if __name__ == "__main__":
    app = create_app(False)
    test = ListRepository()
    item = ItemModel(creation_date = date.today(), update_date = None, deletion_date = None, content = "This Must Be Done", status="TODO")
    list = ListModel(name="Hello World", creation_date = date.today(), update_date = None, deletion_date = None, completion_percentage=0,item_list=[item] )
    test.get(3)

    #app.run()