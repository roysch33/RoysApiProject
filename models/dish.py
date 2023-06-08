from db import db
from datetime import datetime as dt
class Dish(db.Model):
    __tablename__ = "dish"
    id = db.Column(db.Integer,primary_key=True)
    dish_name = db.Column(db.String(200),nullable=False)
    price = db.Column(db.Float,nullable=False)
    description = db.Column(db.Text,nullable=False)
    image = db.Column(db.Text,nullable=False)
    category_id_id = db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "dish_name":self.dish_name,
            "price":self.price,
            "description":self.description,
            "image":self.image,
            "category_id_id":self.category_id_id
        }
    

