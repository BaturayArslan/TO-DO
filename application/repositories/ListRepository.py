from sqlalchemy import select

from application.repositories.BaseRepository import BaseRepository
from application.providers.orm.models import ListModel, ItemModel

class ListRepository(BaseRepository):

    def get(self, id: int):
        stmt = select(ListModel).where(ListModel.id.in_([id]))
        for user in self.session.scalars(stmt):
            print(user)
    
    def insert(self, item):
        with self.session:
            self.session.add_all([item])
            self.session.commit()