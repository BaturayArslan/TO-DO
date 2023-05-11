from datetime import date
from typing import Optional

from application.entities.BaseList import BaseList
from application.entities.TodoItem import TodoItem


class TodoList(BaseList):
	def __init__(self, id: int, name: str, creation_date: date, deletion_time: Optional[date] = None):
		super().__init__(id=id, name=name, creation_date=creation_date)
		self.update_date = None
		self.deletion_time = deletion_time
		self.completion_percentage = 0
		
	def add_item(self, item: TodoItem) -> None:
		super().add_item(item)
		self.set_update_date(date.today())
	
	def update_item(self, id: int, values: dict) -> None:
		super().update_item(id, values)
		self.set_update_date(date.today())
	
	def delete_item(self, id: int) -> None:
		super().delete_item(id)
		self.set_update_date(date.today())

	def update_list(self, values: dict) -> None:
		for key, value in values.items():
			setattr(self, key, value)
		self.set_update_date(date.today())
	
	def set_update_date(self, update_time: date):
		self.update_date = update_time

