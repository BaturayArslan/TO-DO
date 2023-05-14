from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

from application.entities.BaseList import BaseList


class BaseItem:
	
	def __init__(self, id: int, creation_date: date, content: str, list: Optional[BaseList] = None) -> None:
		self.ID = id
		self.list = list
		self.creation_date = creation_date
		self.content = content

	@abstractmethod
	def update(self, values: dict) -> None:
		...
	
	def set_list(self, list: BaseList) -> None:
		self.list = list