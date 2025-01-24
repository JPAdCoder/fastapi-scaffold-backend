# FastAPI Code Generator

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