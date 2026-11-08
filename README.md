# 图书资源管理系统 (Book Management System)

一个基于 Flask + Vue3 的前后端分离全栈实战项目。实现了图书信息的完整增删改查（CRUD），并包含接口自动化测试。

## 技术栈

*   **后端**：Python 3, Flask, Flask-SQLAlchemy, SQLite
*   **前端**：Vue3 (Composition API), Element Plus, Axios, Vite
*   **测试**：Pytest, Requests
*   **工程化**：Git, CORS 跨域处理, RESTful API 设计

## 功能特性

*    **数据展示**：表格分页展示图书信息。
*    **图书新增**：弹窗表单输入，带前端基础校验。
*    **图书编辑**：回显数据并支持修改。
*    **图书删除**：二次确认弹窗防误触。
*    **前后端分离**：前端通过 Axios 请求后端 RESTful API，并使用 Flask-CORS 解决跨域问题。
*    **质量保障**：使用 Pytest 对后端接口进行自动化测试。

## 如何运行

### 1. 启动后端 (Flask)
```bash
cd book-backend
pip install -r requirements.txt # (pip install flask flask-sqlalchemy flask-cors)
flask --app app create          # 初始化数据库
python app.py                   # 运行在 http://127.0.0.1:5000
```
### 2.启动前端（Vue3)
```bash
cd book-frontend
npm install                     # 安装依赖
npm run dev                     # 运行在 http://localhost:5173
```
### 3.运行测试 (Pytest)
```bash
cd book-backend
pytest test_api.py -v
```
