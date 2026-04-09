# FastAPI Blog API with AI Features

A modern, AI-powered blog API built with FastAPI, featuring user authentication, note management, and intelligent AI capabilities including note summarization, title generation, and conversational search.

## Features

### User Management
- User registration and authentication
- JWT-based login system
- Protected routes with user authorization
- User profile access

### Note Management
- Create, read, update, and delete notes
- Pagination support for note listings
- Full-text search functionality
- User-specific note ownership

### AI-Powered Features
- **Note Summarization**: Automatically generate concise summaries of notes using local AI models
- **Title Generation**: AI-powered title suggestions for new notes
- **Conversational Search**: Chat with your notes using natural language queries, powered by vector embeddings and semantic search

### Technical Features
- RESTful API design
- PostgreSQL database with SQLAlchemy ORM
- Vector embeddings for semantic search using FAISS
- Local AI inference with Ollama (Gemma model)
- Asynchronous request handling
- Comprehensive error handling and validation

## Technology Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with python-jose
- **Password Hashing**: bcrypt
- **Vector Search**: FAISS (Facebook AI Similarity Search)
- **AI Model**: Ollama with Gemma 2B model
- **HTTP Client**: httpx for async requests
- **Environment Management**: python-dotenv

## Project Structure

```
fastapi-blog-api/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # Database configuration and session management
│   ├── models/
│   │   ├── user_model.py       # User database model
│   │   └── note_model.py       # Note database model
│   ├── routers/
│   │   ├── user_router.py      # User-related API endpoints
│   │   └── note_router.py      # Note-related API endpoints
│   ├── schemas/
│   │   ├── user_schema.py      # Pydantic schemas for user data
│   │   └── note_schema.py      # Pydantic schemas for note data
│   ├── services/
│   │   ├── user_service.py     # User business logic
│   │   ├── note_service.py     # Note business logic
│   │   ├── ai_service.py       # AI text processing (summarization, title generation)
│   │   ├── chat_service.py     # Conversational AI with notes
│   │   ├── embedding_service.py # Text embedding generation
│   │   ├── vector_loader.py    # Vector index initialization
│   │   └── vector_store.py     # FAISS vector search operations
│   └── utils/
│       ├── dependencies.py     # Dependency injection utilities
│       ├── security.py         # Password hashing utilities
│       └── token.py            # JWT token management
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd fastapi-blog-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**:
   - Create a PostgreSQL database named `fastapi_blog`
   - Update database connection details in `app/database.py` if needed

5. **Install and run Ollama**:
   - Download and install Ollama from [ollama.ai](https://ollama.ai)
   - Pull the Gemma model:
     ```bash
     ollama pull gemma:2b
     ```
   - Start Ollama server (runs on localhost:11434 by default)

6. **Configure environment variables**:
   - Create a `.env` file in the root directory
   - Add necessary environment variables (database URL, JWT secret, etc.)

## Running the Application

1. **Start the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API documentation**:
   - Open your browser and go to `http://localhost:8000/docs`
   - Interactive Swagger UI will be available for testing endpoints

## API Endpoints

### User Endpoints
- `POST /users` - Register a new user
- `GET /users` - Get all users (admin functionality)
- `POST /login` - User login (returns JWT token)
- `GET /profile` - Get current user profile (protected)

### Note Endpoints
- `POST /notes` - Create a new note (protected)
- `GET /notes` - Get user's notes with pagination and search (protected)
- `PUT /notes/{note_id}` - Update a note (protected)
- `DELETE /notes/{note_id}` - Delete a note (protected)
- `POST /notes/{note_id}/summarize` - Summarize a note using AI (protected)
- `POST /notes/generate-title` - Generate title for note content
- `POST /notes/chat` - Chat with notes using natural language

## Usage Examples

### Register a User
```bash
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "password": "securepassword"}'
```

### Login
```bash
curl -X POST "http://localhost:8000/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=john@example.com&password=securepassword"
```

### Create a Note
```bash
curl -X POST "http://localhost:8000/notes" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"title": "My First Note", "content": "This is the content of my note."}'
```

### Chat with Notes
```bash
curl -X POST "http://localhost:8000/notes/chat" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are my thoughts on AI?"}'
```

## AI Features in Detail

### Note Summarization
Uses the Gemma model to create concise 1-2 sentence summaries of note content, helping users quickly understand the essence of their notes.

### Title Generation
Automatically suggests appropriate titles for notes based on their content, ensuring consistent and meaningful note organization.

### Conversational Search
- Converts user questions into vector embeddings
- Searches through note embeddings using FAISS for semantic similarity
- Provides AI-generated answers based on the most relevant notes
- Supports natural language queries about note content


## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Acknowledgments

- FastAPI for the excellent web framework
- Ollama for local AI model serving
- FAISS for efficient vector similarity search
- The open-source community for the amazing tools and libraries