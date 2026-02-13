# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

本次作业将带领你使用 FastAPI 框架，构建一个简单的 RESTful API 服务，掌握现代 Web 后端开发的基本流程。

## 📝 Tasks

### 🛠️ 任务一：FastAPI 项目初始化

#### Description
搭建 FastAPI 项目环境，实现第一个 API 路由。

#### Requirements
Completed program should:

- 安装 fastapi 和 uvicorn
- 创建 main.py 文件，定义一个返回 "Hello, World!" 的 GET 路由
- 能通过 uvicorn 启动并访问该接口


### 🛠️ 任务二：实现基本的 CRUD API

#### Description
扩展你的 FastAPI 项目，实现对“学生”资源的增删查改（CRUD）接口。

#### Requirements
Completed program should:

- 定义学生（Student）数据模型（如 id, name, age）
- 实现添加、查询、修改、删除学生的 API 路由
- 所有数据暂存于内存（如 Python 列表）
- 每个接口返回清晰的 JSON 响应
