from flask import Flask
from flask_cors import CORS
from extension import db
from models import Book
from views import BookApi

app = Flask(__name__)

# 跨域配置：允许前端开发服务器访问
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
app.json.ensure_ascii = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.cli.command()
def create():
    """初始化数据库：flask create"""
    db.drop_all()
    db.create_all()
    Book.init_db()
    print('数据库初始化完成')


# 注册路由
book_api = BookApi.as_view('book_api')
app.add_url_rule('/books', view_func=book_api, methods=['GET'], defaults={'book_id': None})
app.add_url_rule('/books', view_func=book_api, methods=['POST'])
app.add_url_rule('/books/<int:book_id>', view_func=book_api, methods=['GET', 'PUT', 'DELETE'])


if __name__ == '__main__':
    app.run(debug=True)