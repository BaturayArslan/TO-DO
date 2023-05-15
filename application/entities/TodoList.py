from datetime import date
from typing import Optional, List

from application.entities.BaseList import BaseList
from application.entities.TodoItem import TodoItem
from application.entities.ItemStatus import ItemStatus


class TodoList(BaseList):
	def __init__(self,name: str, creation_date: date, id: int = 0, deletion_time: Optional[date] = None,
	       		update_date: Optional[date] = None, item_list: List[TodoItem]=[], comp_perc: Optional[int]=0):
		super().__init__(id=id, name=name, creation_date=creation_date,item_list=item_list)
		self.update_date = None
		self.deletion_time = deletion_time
		self.completion_percentage = comp_perc
		
	def add_item(self, item: TodoItem) -> None:
		super().add_item(item)
		self.calculate_completion_perc()
		self.set_update_date(date.today())
	
	def update_item(self, id: int, values: dict) -> None:
		super().update_item(id, values)
		self.calculate_completion_perc()
		self.set_update_date(date.today())
	
	def delete_item(self, id: int) -> None:
		super().delete_item(id)
		self.calculate_completion_perc()
		self.set_update_date(date.today())

	def update_list(self, values: dict) -> None:
		for key, value in values.items():
			setattr(self, key, value)
		self.set_update_date(date.today())
	
	def set_update_date(self, update_time: date) -> None:
		self.update_date = update_time
	
	def set_item_list(self, item_list: List[TodoItem]) -> None:
		self.item_list = item_list
	
	def calculate_completion_perc(self):
		total_item = len(self.item_list)
		done_item = 0
		for item in self.item_list:
			if(item.status.value == ItemStatus.DONE.value):
				print(total_item)
				done_item = done_item + 1
		
		self.completion_percentage = round((done_item / total_item) * 100 )
	
	def __repr__(self) -> str:
		return f"TodoList(id={self.ID}, name={self.name}, creation_date={self.creation_date}, update_date={self.update_date},\
            deletion_date={self.deletion_time}, complition={self.completion_percentage}, item_list: {self.item_list})"

