from flask import Flask,request

from controllers.dishes import DishesInCategory, DishAll, DishOne
from controllers.categories import CategoryAll
from flask_restful import Api

from config import DBUSER,DBPASS,DBHOST


from flask_cors import CORS
from db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = "rggnrkbn454mgfje3"
CORS(app)
db.init_app(app)
api = Api(app)


with app.app_context():
    db.create_all()

api.add_resource(DishAll,'/dishes')
api.add_resource(DishOne,'/dishes/<int:id>')
api.add_resource(CategoryAll,'/categories')
api.add_resource(DishesInCategory, '/dishes/category/<int:category_id_id>')
#api.add_resource(RecipeFilter,'/dishes?category_id=<int:id>')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
