"""
Movie Data Generator - Creates sample movie dataset from Netflix, Prime Video, Hotstar, etc.
"""
import pandas as pd
import numpy as np

def generate_movie_dataset():
    """Generate a comprehensive movie dataset with movies from various platforms"""
    
    movies_data = [
        # Netflix Movies
        {"title": "The Dark Knight", "platform": "Netflix", "genre": "Action,Crime,Drama", "year": 2008, "rating": 9.0, "director": "Christopher Nolan"},
        {"title": "Inception", "platform": "Netflix", "genre": "Action,Sci-Fi,Thriller", "year": 2010, "rating": 8.8, "director": "Christopher Nolan"},
        {"title": "The Matrix", "platform": "Netflix", "genre": "Action,Sci-Fi", "year": 1999, "rating": 8.7, "director": "Wachowski Brothers"},
        {"title": "Pulp Fiction", "platform": "Netflix", "genre": "Crime,Drama", "year": 1994, "rating": 8.9, "director": "Quentin Tarantino"},
        {"title": "The Shawshank Redemption", "platform": "Netflix", "genre": "Drama", "year": 1994, "rating": 9.3, "director": "Frank Darabont"},
        {"title": "Forrest Gump", "platform": "Netflix", "genre": "Drama,Romance", "year": 1994, "rating": 8.8, "director": "Robert Zemeckis"},
        {"title": "The Godfather", "platform": "Netflix", "genre": "Crime,Drama", "year": 1972, "rating": 9.2, "director": "Francis Ford Coppola"},
        {"title": "Fight Club", "platform": "Netflix", "genre": "Drama,Thriller", "year": 1999, "rating": 8.8, "director": "David Fincher"},
        {"title": "Interstellar", "platform": "Netflix", "genre": "Adventure,Drama,Sci-Fi", "year": 2014, "rating": 8.6, "director": "Christopher Nolan"},
        {"title": "The Departed", "platform": "Netflix", "genre": "Crime,Drama,Thriller", "year": 2006, "rating": 8.5, "director": "Martin Scorsese"},
        
        # Prime Video Movies
        {"title": "The Lord of the Rings: The Fellowship", "platform": "Prime Video", "genre": "Action,Adventure,Drama", "year": 2001, "rating": 8.8, "director": "Peter Jackson"},
        {"title": "The Prestige", "platform": "Prime Video", "genre": "Drama,Mystery,Thriller", "year": 2006, "rating": 8.5, "director": "Christopher Nolan"},
        {"title": "Gladiator", "platform": "Prime Video", "genre": "Action,Adventure,Drama", "year": 2000, "rating": 8.5, "director": "Ridley Scott"},
        {"title": "The Green Mile", "platform": "Prime Video", "genre": "Crime,Drama,Fantasy", "year": 1999, "rating": 8.6, "director": "Frank Darabont"},
        {"title": "The Usual Suspects", "platform": "Prime Video", "genre": "Crime,Mystery,Thriller", "year": 1995, "rating": 8.5, "director": "Bryan Singer"},
        {"title": "Se7en", "platform": "Prime Video", "genre": "Crime,Drama,Mystery", "year": 1995, "rating": 8.6, "director": "David Fincher"},
        {"title": "The Silence of the Lambs", "platform": "Prime Video", "genre": "Crime,Drama,Thriller", "year": 1991, "rating": 8.6, "director": "Jonathan Demme"},
        {"title": "Saving Private Ryan", "platform": "Prime Video", "genre": "Drama,War", "year": 1998, "rating": 8.6, "director": "Steven Spielberg"},
        {"title": "The Lion King", "platform": "Prime Video", "genre": "Animation,Adventure,Drama", "year": 1994, "rating": 8.5, "director": "Roger Allers"},
        {"title": "Goodfellas", "platform": "Prime Video", "genre": "Biography,Crime,Drama", "year": 1990, "rating": 8.7, "director": "Martin Scorsese"},
        
        # Hotstar Movies
        {"title": "3 Idiots", "platform": "Hotstar", "genre": "Comedy,Drama", "year": 2009, "rating": 8.4, "director": "Rajkumar Hirani"},
        {"title": "Dangal", "platform": "Hotstar", "genre": "Action,Biography,Drama", "year": 2016, "rating": 8.4, "director": "Nitesh Tiwari"},
        {"title": "Lagaan", "platform": "Hotstar", "genre": "Adventure,Drama,Sport", "year": 2001, "rating": 8.1, "director": "Ashutosh Gowariker"},
        {"title": "Taare Zameen Par", "platform": "Hotstar", "genre": "Drama,Family", "year": 2007, "rating": 8.4, "director": "Aamir Khan"},
        {"title": "PK", "platform": "Hotstar", "genre": "Comedy,Drama,Sci-Fi", "year": 2014, "rating": 8.1, "director": "Rajkumar Hirani"},
        {"title": "Zindagi Na Milegi Dobara", "platform": "Hotstar", "genre": "Comedy,Drama", "year": 2011, "rating": 8.2, "director": "Zoya Akhtar"},
        {"title": "Gully Boy", "platform": "Hotstar", "genre": "Drama,Music", "year": 2019, "rating": 8.0, "director": "Zoya Akhtar"},
        {"title": "Queen", "platform": "Hotstar", "genre": "Adventure,Comedy,Drama", "year": 2013, "rating": 8.2, "director": "Vikas Bahl"},
        {"title": "Andhadhun", "platform": "Hotstar", "genre": "Comedy,Crime,Thriller", "year": 2018, "rating": 8.3, "director": "Sriram Raghavan"},
        {"title": "Barfi!", "platform": "Hotstar", "genre": "Comedy,Drama,Romance", "year": 2012, "rating": 8.1, "director": "Anurag Basu"},
        
        # More popular movies across platforms
        {"title": "The Avengers", "platform": "Disney+ Hotstar", "genre": "Action,Adventure,Sci-Fi", "year": 2012, "rating": 8.0, "director": "Joss Whedon"},
        {"title": "Avatar", "platform": "Disney+ Hotstar", "genre": "Action,Adventure,Fantasy", "year": 2009, "rating": 7.8, "director": "James Cameron"},
        {"title": "Titanic", "platform": "Prime Video", "genre": "Drama,Romance", "year": 1997, "rating": 7.8, "director": "James Cameron"},
        {"title": "Jurassic Park", "platform": "Netflix", "genre": "Action,Adventure,Sci-Fi", "year": 1993, "rating": 8.1, "director": "Steven Spielberg"},
        {"title": "The Terminator", "platform": "Prime Video", "genre": "Action,Sci-Fi,Thriller", "year": 1984, "rating": 8.0, "director": "James Cameron"},
        {"title": "Back to the Future", "platform": "Netflix", "genre": "Adventure,Comedy,Sci-Fi", "year": 1985, "rating": 8.5, "director": "Robert Zemeckis"},
        {"title": "The Sixth Sense", "platform": "Prime Video", "genre": "Drama,Mystery,Thriller", "year": 1999, "rating": 8.1, "director": "M. Night Shyamalan"},
        {"title": "The Truman Show", "platform": "Netflix", "genre": "Comedy,Drama,Sci-Fi", "year": 1998, "rating": 8.1, "director": "Peter Weir"},
        {"title": "The Social Network", "platform": "Netflix", "genre": "Biography,Drama", "year": 2010, "rating": 7.7, "director": "David Fincher"},
        {"title": "Whiplash", "platform": "Prime Video", "genre": "Drama,Music", "year": 2014, "rating": 8.5, "director": "Damien Chazelle"},
    ]
    
    df = pd.DataFrame(movies_data)
    return df

def generate_user_ratings(movies_df, num_users=50):
    """Generate sample user ratings for collaborative filtering"""
    np.random.seed(42)
    
    user_ratings = []
    user_ids = [f"user_{i+1}" for i in range(num_users)]
    
    for user_id in user_ids:
        # Each user rates 5-15 random movies
        num_ratings = np.random.randint(5, 16)
        rated_movies = np.random.choice(movies_df.index, num_ratings, replace=False)
        
        for movie_idx in rated_movies:
            movie = movies_df.iloc[movie_idx]
            # Ratings are influenced by movie's actual rating with some randomness
            base_rating = movie['rating']
            user_rating = np.clip(np.random.normal(base_rating, 1.0), 1.0, 10.0)
            user_rating = round(user_rating, 1)
            
            user_ratings.append({
                'user_id': user_id,
                'movie_title': movie['title'],
                'rating': user_rating
            })
    
    return pd.DataFrame(user_ratings)

