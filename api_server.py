"""
Flask API Server for Movie Recommendation System
Provides REST API endpoints for the React frontend
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from movie_data import generate_movie_dataset, generate_user_ratings
from recommendation_engine import MovieRecommendationEngine

app = Flask(__name__)
# Enable CORS for React frontend with specific origins
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize the recommendation engine
print("Initializing movie recommendation engine...")
movies_df = generate_movie_dataset()
user_ratings_df = generate_user_ratings(movies_df, num_users=50)
engine = MovieRecommendationEngine(movies_df, user_ratings_df)
print("✓ Engine ready!")

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "Movie Recommendation API is running"})

@app.route('/api/movies', methods=['GET'])
def get_all_movies():
    """Get all movies with optional filters"""
    query = request.args.get('query', '').strip() or None
    platform = request.args.get('platform', '').strip() or None
    genre = request.args.get('genre', '').strip() or None
    year = request.args.get('year', type=int)
    
    results = engine.search_movies(query=query, platform=platform, genre=genre, year=year)
    
    if results.empty:
        return jsonify({"movies": [], "count": 0})
    
    movies_list = results.to_dict('records')
    return jsonify({"movies": movies_list, "count": len(movies_list)})

@app.route('/api/movies/search', methods=['GET'])
def search_movies():
    """Search movies endpoint"""
    query = request.args.get('q', '').strip() or None
    platform = request.args.get('platform', '').strip() or None
    genre = request.args.get('genre', '').strip() or None
    year = request.args.get('year', type=int)
    
    results = engine.search_movies(query=query, platform=platform, genre=genre, year=year)
    
    if results.empty:
        return jsonify({"movies": [], "count": 0})
    
    movies_list = results.to_dict('records')
    return jsonify({"movies": movies_list, "count": len(movies_list)})

@app.route('/api/recommendations/content-based', methods=['POST'])
def get_content_based_recommendations():
    """Get content-based recommendations"""
    data = request.get_json()
    movie_title = data.get('movie_title')
    n_recommendations = data.get('n_recommendations', 10)
    
    if not movie_title:
        return jsonify({"error": "movie_title is required"}), 400
    
    try:
        recommendations = engine.content_based_recommendations(movie_title, n_recommendations)
        
        if recommendations.empty:
            return jsonify({"movies": [], "count": 0, "message": "No recommendations found"})
        
        movies_list = recommendations.to_dict('records')
        return jsonify({"movies": movies_list, "count": len(movies_list)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/recommendations/collaborative', methods=['POST'])
def get_collaborative_recommendations():
    """Get collaborative filtering recommendations"""
    data = request.get_json()
    user_id = data.get('user_id')
    n_recommendations = data.get('n_recommendations', 10)
    
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    try:
        recommendations = engine.collaborative_filtering_recommendations(user_id, n_recommendations)
        
        if recommendations.empty:
            return jsonify({"movies": [], "count": 0, "message": "No recommendations found"})
        
        movies_list = recommendations.to_dict('records')
        return jsonify({"movies": movies_list, "count": len(movies_list)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/recommendations/hybrid', methods=['POST'])
def get_hybrid_recommendations():
    """Get hybrid recommendations"""
    data = request.get_json()
    movie_title = data.get('movie_title')
    user_id = data.get('user_id')
    user_ratings = data.get('user_ratings')  # Dict of {movie_title: rating}
    n_recommendations = data.get('n_recommendations', 10)
    
    try:
        recommendations = engine.hybrid_recommendations(
            movie_title=movie_title,
            user_id=user_id,
            user_ratings=user_ratings,
            n_recommendations=n_recommendations
        )
        
        if recommendations.empty:
            return jsonify({"movies": [], "count": 0, "message": "No recommendations found"})
        
        movies_list = recommendations.to_dict('records')
        return jsonify({"movies": movies_list, "count": len(movies_list)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/platforms', methods=['GET'])
def get_platforms():
    """Get list of all available platforms"""
    platforms = sorted(movies_df['platform'].unique().tolist())
    return jsonify({"platforms": platforms})

@app.route('/api/genres', methods=['GET'])
def get_genres():
    """Get list of all available genres"""
    all_genres = set()
    for genres in movies_df['genre']:
        all_genres.update([g.strip() for g in genres.split(',')])
    genres_list = sorted(list(all_genres))
    return jsonify({"genres": genres_list})

@app.route('/api/movie-titles', methods=['GET'])
def get_movie_titles():
    """Get list of all movie titles"""
    titles = sorted(movies_df['title'].tolist())
    return jsonify({"titles": titles})

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get list of all user IDs"""
    if user_ratings_df is not None:
        users = sorted(user_ratings_df['user_id'].unique().tolist())
        return jsonify({"users": users})
    return jsonify({"users": []})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🎬 Movie Recommendation API Server")
    print("="*60)
    print("Server starting on http://localhost:5000")
    print("API endpoints available at http://localhost:5000/api/")
    print("="*60 + "\n")
    app.run(debug=True, port=5000)

