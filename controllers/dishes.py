from flask import request
from flask_restful import Resource
from db import db
from models.dish import Dish
class DishAll(Resource):
    def get(self):
        dishes = Dish.query.filter_by().all()
        return [dish.serialize() for dish in dishes]
    def post(self):
        data = request.get_json()
        try:
            dish = Dish(**data)
            # recipe = Recipe(
            #     title=data['title'],
            #     content=data['content'],
            #     imageUrl=data['imageUrl'],
            #     category_id=data['category_id']
            # )
            db.session.add(dish)
            db.session.commit()
            return {'message':f'{dish.dish_name} נוסף!'}, 201
        except:
            return {'message':'בקשה לא תקינה'},400

class DishOne(Resource):
    def get(self,id):
        dish = Dish.query.get(id)
        return dish.serialize()
    def delete(self,id):
        dish = Dish.query.get(id)
        db.session.delete(dish)
        db.session.commit()
        return {'message':'נמחק מנה'},400

    
class DishesInCategory(Resource):
    def get(self, category_id_id):
        dishes = Dish.query.filter_by(category_id_id=category_id_id).order_by(Dish.category_id_id).all()
        return [dish.serialize() for dish in dishes]