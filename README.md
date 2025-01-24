# FastAPI Code Generator

[English](#fastapi-code-generator) | [中文](#fastapi-代码生成器)

A powerful FastAPI code generator that helps developers quickly scaffold FastAPI projects with best practices.

## Features

- 🚀 Quick project scaffolding
- 🔐 Built-in authentication and authorization
- 📝 Auto-generated CRUD operations
- 🎯 Best practices out of the box
- 🔄 Database migrations support
- 📚 Auto-generated API documentation

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/generate-fastapi-be.git
cd generate-fastapi-be

# Install dependencies using Poetry
poetry install
```

## Quick Start

1. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. Initialize the database:
   ```bash
   poetry run alembic upgrade head
   ```

3. Start the development server:
   ```bash
   poetry run uvicorn main:app --reload
   ```

4. Visit the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Generation

### Generate a New Project

```bash
# Example command to generate a new project
poetry run python -m app.cli generate-project --name myproject
```

### Generate API Components

```bash
# Generate CRUD operations
poetry run python -m app.cli generate-crud --model User

# Generate Schemas
poetry run python -m app.cli generate-schema --model User

# Generate API endpoints
poetry run python -m app.cli generate-api --model User
```

## Project Structure

```
.
├── alembic/            # Database migrations
├── app/
│   ├── api/           # API endpoints
│   ├── core/          # Core functionality
│   ├── crud/          # CRUD operations
│   ├── db/            # Database configuration
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic models
│   └── utils/         # Utility functions
├── tests/             # Test suite
└── main.py            # Application entry point
```

## Configuration

The project uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:

```env
# Server Configuration
SERVER_HOST=localhost
SERVER_PORT=8000

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Security
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# FastAPI 代码生成器

一个强大的FastAPI代码生成器，帮助开发者快速搭建具有最佳实践的FastAPI项目。

## 功能特点

- 🚀 快速项目脚手架
- 🔐 内置认证和授权
- 📝 自动生成CRUD操作
- 🎯 开箱即用的最佳实践
- 🔄 数据库迁移支持
- 📚 自动生成API文档

## 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/generate-fastapi-be.git
cd generate-fastapi-be

# 使用Poetry安装依赖
poetry install
```

## 快速开始

1. 设置环境变量：
   ```bash
   cp .env.example .env
   # 编辑.env文件配置你的环境变量
   ```

2. 初始化数据库：
   ```bash
   poetry run alembic upgrade head
   ```

3. 启动开发服务器：
   ```bash
   poetry run uvicorn main:app --reload
   ```

4. 访问API文档：
   - Swagger UI界面: http://localhost:8000/docs
   - ReDoc界面: http://localhost:8000/redoc

## 项目生成

### 生成新项目

```bash
# 生成新项目的示例命令
poetry run python -m app.cli generate-project --name myproject
```

### 生成API组件

```bash
# 生成CRUD操作
poetry run python -m app.cli generate-crud --model User

# 生成数据模型
poetry run python -m app.cli generate-schema --model User

# 生成API端点
poetry run python -m app.cli generate-api --model User
```

## 项目结构

```
.
├── alembic/            # 数据库迁移
├── app/
│   ├── api/           # API端点
│   ├── core/          # 核心功能
│   ├── crud/          # CRUD操作
│   ├── db/            # 数据库配置
│   ├── models/        # SQLAlchemy模型
│   ├── schemas/       # Pydantic模型
│   └── utils/         # 工具函数
├── tests/             # 测试套件
└── main.py            # 应用入口点
```

## 配置

项目使用环境变量进行配置。在根目录创建`.env`文件，包含以下变量：

```env
# 服务器配置
SERVER_HOST=localhost
SERVER_PORT=8000

# 数据库配置
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# 安全配置
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 贡献

欢迎提交Pull Request来贡献代码！

## 许可证

本项目采用MIT许可证 - 详见LICENSE文件。