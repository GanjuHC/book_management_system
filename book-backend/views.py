from flask import request
from flask.views import MethodView
from extension import db
from models import Book


class BookApi(MethodView):

    def get(self, book_id):
        if not book_id:
            books = Book.query.all()
            results = [{
                'id': book.id,
                'book_number': book.book_number,
                'book_name': book.book_name,
                'book_type': book.book_type,
                'book_prize': book.book_prize,
                'author': book.author,
                'book_publisher': book.book_publisher,
            } for book in books]
            return {'status': 'success', 'message': '数据查询成功', 'results': results}

        book = Book.query.get(book_id)
        if book is None:
            return {'status': 'fail', 'message': '图书不存在'}, 404

        return {'status': 'success', 'message': '数据查询成功', 'result': {
            'id': book.id,
            'book_number': book.book_number,
            'book_name': book.book_name,
            'book_type': book.book_type,
            'book_prize': book.book_prize,
            'author': book.author,
            'book_publisher': book.book_publisher,
        }}

    def post(self):
        form = request.json
        book = Book(
            book_number=form.get('book_number'),
            book_name=form.get('book_name'),
            book_type=form.get('book_type'),
            book_prize=form.get('book_prize'),
            author=form.get('author'),
            book_publisher=form.get('book_publisher'),
        )
        db.session.add(book)
        db.session.commit()
        return {'status': 'success', 'message': '数据添加成功'}

    def delete(self, book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return {'status': 'success', 'message': '数据删除成功'}

    def put(self, book_id):
        book = Book.query.get(book_id)
        form = request.json
        book.book_number = form.get('book_number')
        book.book_name = form.get('book_name')
        book.book_type = form.get('book_type')
        book.book_prize = form.get('book_prize')
        book.author = form.get('author')
        book.book_publisher = form.get('book_publisher')
        db.session.commit()
        return {'status': 'success', 'message': '数据修改成功'}