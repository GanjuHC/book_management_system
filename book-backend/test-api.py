import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_get_books():
    """测试获取图书列表接口"""
    res = requests.get(f'{BASE_URL}/books')
    assert res.status_code == 200
    assert res.json()['status'] == 'success'

def test_add_book():
    """测试添加图书接口"""
    payload = {
        'book_number': 'TEST-01',
        'book_name': '测试驱动开发',
        'book_type': '技术',
        'book_prize': 59.9,
        'author': 'Kent Beck',
        'book_publisher': '测试出版社'
    }
    res = requests.post(f'{BASE_URL}/books', json=payload)
    assert res.json()['status'] == 'success'