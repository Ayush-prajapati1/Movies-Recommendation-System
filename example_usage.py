"""
Example usage of the Movie Recommendation System
This script demonstrates how to use the recommendation engine programmatically
"""
from movie_data import generate_movie_dataset, generate_user_ratings
from recommendation_engine import MovieRecommendationEngine

def main():
    print("="*70)
    print("MOVIE RECOMMENDATION SYSTEM - EXAMPLE USAGE")
    print("="*70)
    
    # Step 1: Generate movie dataset
    print("\n1. Loading movie database...")
    movies_df = generate_movie_dataset()
    print(f"   ✓ Loaded {len(movies_df)} movies")
    
    # Step 2: Generate user ratings for collaborative filtering
    print("\n2. Loading user ratings...")
    user_ratings_df = generate_user_ratings(movies_df, num_users=50)
    print(f"   ✓ Loaded ratings from {len(user_ratings_df['user_id'].unique())} users")
    
    # Step 3: Initialize recommendation engine
    print("\n3. Initializing recommendation engine...")
    engine = MovieRecommendationEngine(movies_df, user_ratings_df)
    print("   ✓ Engine ready!")
    
    # Example 1: Content-Based Recommendations
    print("\n" + "="*70)
    print("EXAMPLE 1: Content-Based Recommendations")
    print("="*70)
    print("\nFinding movies similar to 'Inception'...")
    recommendations = engine.content_based_recommendations("Inception", n_recommendations=5)
    
    if not recommendations.empty:
        print(f"\n✓ Found {len(recommendations)} similar movies:\n")
        for idx, movie in recommendations.iterrows():
            print(f"  • {movie['title']} ({movie['year']})")
            print(f"    Platform: {movie['platform']} | Genre: {movie['genre']}")
            print(f"    Rating: {movie['rating']}/10 | Similarity: {movie['similarity_score']:.2%}\n")
    
    # Example 2: Collaborative Filtering Recommendations
    print("\n" + "="*70)
    print("EXAMPLE 2: Collaborative Filtering Recommendations")
    print("="*70)
    print("\nGetting recommendations for 'user_1'...")
    recommendations = engine.collaborative_filtering_recommendations("user_1", n_recommendations=5)
    
    if not recommendations.empty:
        print(f"\n✓ Found {len(recommendations)} recommendations:\n")
        for idx, movie in recommendations.iterrows():
            print(f"  • {movie['title']} ({movie['year']})")
            print(f"    Platform: {movie['platform']} | Genre: {movie['genre']}")
            if 'predicted_rating' in movie:
                print(f"    Rating: {movie['rating']}/10 | Predicted: {movie['predicted_rating']:.1f}/10\n")
            else:
                print(f"    Rating: {movie['rating']}/10\n")
    
    # Example 3: Hybrid Recommendations
    print("\n" + "="*70)
    print("EXAMPLE 3: Hybrid Recommendations")
    print("="*70)
    print("\nGetting hybrid recommendations based on user ratings...")
    user_ratings = {
        "Inception": 9.0,
        "The Matrix": 8.5,
        "Interstellar": 9.2
    }
    recommendations = engine.hybrid_recommendations(
        user_ratings=user_ratings,
        n_recommendations=5
    )
    
    if not recommendations.empty:
        print(f"\n✓ Found {len(recommendations)} personalized recommendations:\n")
        for idx, movie in recommendations.iterrows():
            print(f"  • {movie['title']} ({movie['year']})")
            print(f"    Platform: {movie['platform']} | Genre: {movie['genre']}")
            print(f"    Rating: {movie['rating']}/10\n")
    
    # Example 4: Search Movies
    print("\n" + "="*70)
    print("EXAMPLE 4: Search Movies")
    print("="*70)
    print("\nSearching for 'Action' movies on 'Netflix'...")
    results = engine.search_movies(query=None, platform="Netflix", genre="Action")
    
    if not results.empty:
        print(f"\n✓ Found {len(results)} movies:\n")
        for idx, movie in results.head(5).iterrows():
            print(f"  • {movie['title']} ({movie['year']}) - {movie['rating']}/10")
    
    print("\n" + "="*70)
    print("Examples completed! Run 'streamlit run app.py' for the web interface")
    print("or 'python cli_app.py' for the command-line interface.")
    print("="*70)

if __name__ == "__main__":
    main()

