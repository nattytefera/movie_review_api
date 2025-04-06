```markdown
# Movie Review API

A Django REST Framework API for managing movies and user reviews.

## Features

- User authentication (JWT tokens)
- Create, read, update, and delete movies
- Post and manage movie reviews
- Search functionality for movies

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nattytefera/movie_review_api.git
   cd movie_review_api
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/token/` - Get JWT tokens
- `POST /api/token/refresh/` - Refresh access token

### Movies
- `GET /api/movies/` - List all movies
- `POST /api/movies/` - Create a new movie
- `GET /api/movies/{id}/` - Get movie details
- `PUT /api/movies/{id}/` - Update a movie
- `DELETE /api/movies/{id}/` - Delete a movie

### Reviews
- `GET /api/reviews/` - List all reviews (user's only)
- `POST /api/reviews/` - Create a new review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update a review
- `DELETE /api/reviews/{id}/` - Delete a review



## TMDB Integration

This project uses TMDB API **only for searching movies**.  
No TMDB data is stored in the database - users must manually create movies locally before reviewing.
