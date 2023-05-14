from application.app import create_app 

from application.entities.TodoList import TodoList
from datetime import date
from application.repositories.ListRepository import ListRepository
from application.providers.orm.models import ListModel, ItemModel
from application.dto.request.UpdateListRequest import UpdateListRequest

if __name__ == "__main__":
    app = create_app(False)
    test = ListRepository()
    item = ItemModel(creation_date = date.today(), update_date = None, deletion_date = None, content = "This Must Be Done", status="TODO")
    list = ListModel(name="Hello World", creation_date = date.today(), update_date = None, deletion_date = None, completion_percentage=0)
    update_list_req = UpdateListRequest(name="baturay",deletion_date_str="26/12/1998")
    #test.insert(list)
    print(test.get(4))
    # test.update(1, update_list_req)
    # print(test.get(1))

    #app.run()