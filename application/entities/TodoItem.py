from datetime import date
from typing import Optional

from application.entities.BaseItem import BaseItem
from application.entities.TodoList import TodoList
from application.entities.ItemStatus import ItemStatus

class TodoItem(BaseItem):
	def __init__(self, id: int, creation_date: date, status: int, content: str,deletion_time:Optional[date] = None,
	    		update_date:Optional[date]=None, list: Optional[TodoList]=None):
		super().__init__(id=id,creation_date=creation_date,content=content,list=list)
		self.status = ItemStatus(status)
		self.deletion_time = deletion_time
		self.update_date = update_date

	def update(self, values: dict) -> None:
		for key, value in values.items():
			setattr(self, key, value)
		self.update_date(date.today())
		
	def set_update_date(self, update_time: date) -> None:
		self.update_date = update_time
