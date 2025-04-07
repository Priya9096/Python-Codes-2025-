def add_movie(movie, movies):
    """Add a movie to the list if not already present."""
    return movies + [movie] if movie not in movies else movies

def search_movie(movie, movies):
    """Search for a movie and print its availability."""
    print(f"'{movie}' is {'available' if movie in movies else 'not available'} in the collection.")

def view_movies(movies):
    """Display all movies in the collection."""
    print(f"Available movies: {movies}")

# Initialize movie collection
movies = ['The Matrix', 'Interstellar', 'The Godfather']

# Demonstrate functionality
view_movies(movies)
movies = add_movie('Inception', movies)
view_movies(movies)

search_movie('The Matrix', movies)
search_movie('Inception', movies)Step-by-Step Breakdown: