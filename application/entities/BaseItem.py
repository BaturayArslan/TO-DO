from abc import ABC, abstractmethod
from datetime import date


class BaseItem:
	
	def __init__(self, id: int, list_id: id, creation_date: date, content: str) -> None:
		self.ID = id
		self.list_id = list_id
		self.creation_date = creation_date
		self.content = content

	@abstractmethod
	def update(self, values: dict) -> None:
		...