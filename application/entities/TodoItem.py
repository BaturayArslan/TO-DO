from datetime import date
from typing import Optional

from application.entities.BaseItem import BaseItem
from application.entities.ItemStatus import ItemStatus

class TodoItem(BaseItem):
	def __init__(self, creation_date: date, status: int, content: str,deletion_time:Optional[date] = None,
	    		update_date:Optional[date]=None, list=None, id: int = 0):
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

	def __repr__(self) -> str:
         return f"TodoItem(id={self.ID}, creation_date={self.creation_date}, update_date={self.update_date},\
            deletion_date={self.deletion_time}, status={self.status.name}, content={self.content}, list={self.list})"
