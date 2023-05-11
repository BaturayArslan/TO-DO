from datetime import date

from application.entities.BaseItem import BaseItem
from application.entities.ItemStatus import ItemStatus

class TodoItem(BaseItem):
	def __init__(self, id: int, list_id: id, creation_date: date, status: int, content: str, deletion_time = None):
		super().__init__(id, list_id, creation_date, content)
		self.status = ItemStatus(status)
		self.deletion_time = deletion_time
		self.update_date = None

	def update(self, values: dict) -> None:
		for key, value in values.items():
			setattr(self, key, value)
		self.update_date(date.today())
		
	def set_update_date(self, update_time: date) -> None:
		self.update_date = update_time
