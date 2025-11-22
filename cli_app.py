"""
Command Line Interface for Movie Recommendation System
"""
import pandas as pd
from movie_data import generate_movie_dataset, generate_user_ratings
from recommendation_engine import MovieRecommendationEngine

def print_movie(movie, show_similarity=False, show_predicted=False):
    """Pretty print a movie"""
    print(f"\n{'='*60}")
    print(f"Title: {movie['title']} ({movie['year']})")
    print(f"Platform: {movie['platform']}")
    print(f"Genre: {movie['genre']}")
    print(f"Director: {movie['director']}")
    print(f"Rating: ⭐ {movie['rating']}/10")
    if show_similarity and 'similarity_score' in movie:
        print(f"Similarity: {movie['similarity_score']:.2%}")
    if show_predicted and 'predicted_rating' in movie:
        print(f"Predicted Rating: {movie['predicted_rating']:.1f}/10")
    print(f"{'='*60}")

def main():
    print("="*60)
    print("🎬 MOVIE RECOMMENDATION SYSTEM")
    print("="*60)
    print("\nLoading movie database...")
    
    # Initialize engine
    movies_df = generate_movie_dataset()
    user_ratings_df = generate_user_ratings(movies_df, num_users=50)
    engine = MovieRecommendationEngine(movies_df, user_ratings_df)
    
    print(f"✓ Loaded {len(movies_df)} movies from various platforms")
    print(f"✓ Loaded ratings from {len(user_ratings_df['user_id'].unique())} users\n")
    
    while True:
        print("\n" + "="*60)
        print("MAIN MENU")
        print("="*60)
        print("1. Search Movies")
        print("2. Get Content-Based Recommendations")
        print("3. Get Collaborative Filtering Recommendations")
        print("4. Get Hybrid Recommendations")
        print("5. Browse All Movies")
        print("6. Exit")
        print("="*60)
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n--- SEARCH MOVIES ---")
            query = input("Enter movie title (or press Enter to skip): ").strip()
            platform = input("Enter platform (Netflix/Prime Video/Hotstar) or press Enter: ").strip()
            genre = input("Enter genre or press Enter: ").strip()
            
            platform = None if not platform else platform
            genre = None if not genre else genre
            query = None if not query else query
            
            results = engine.search_movies(query=query, platform=platform, genre=genre)
            
            if not results.empty:
                print(f"\n✓ Found {len(results)} movies:")
                for idx, movie in results.iterrows():
                    print_movie(movie)
            else:
                print("\n✗ No movies found matching your criteria.")
        
        elif choice == "2":
            print("\n--- CONTENT-BASED RECOMMENDATIONS ---")
            print("\nAvailable movies:")
            movie_titles = sorted(movies_df['title'].tolist())
            for i, title in enumerate(movie_titles[:20], 1):
                print(f"{i}. {title}")
            if len(movie_titles) > 20:
                print(f"... and {len(movie_titles) - 20} more")
            
            movie_title = input("\nEnter a movie title you like: ").strip()
            num_recs = input("Number of recommendations (default 10): ").strip()
            num_recs = int(num_recs) if num_recs.isdigit() else 10
            
            if movie_title in movie_titles:
                print(f"\n✓ Finding movies similar to '{movie_title}'...")
                recommendations = engine.content_based_recommendations(movie_title, n_recommendations=num_recs)
                
                if not recommendations.empty:
                    print(f"\n✓ Here are {len(recommendations)} recommendations:")
                    for idx, movie in recommendations.iterrows():
                        print_movie(movie, show_similarity=True)
                else:
                    print("\n✗ Could not generate recommendations.")
            else:
                print(f"\n✗ Movie '{movie_title}' not found in database.")
        
        elif choice == "3":
            print("\n--- COLLABORATIVE FILTERING RECOMMENDATIONS ---")
            user_ids = sorted(user_ratings_df['user_id'].unique().tolist())
            print(f"\nAvailable users: {', '.join(user_ids[:10])}")
            if len(user_ids) > 10:
                print(f"... and {len(user_ids) - 10} more")
            
            user_id = input("\nEnter user ID: ").strip()
            num_recs = input("Number of recommendations (default 10): ").strip()
            num_recs = int(num_recs) if num_recs.isdigit() else 10
            
            if user_id in user_ids:
                print(f"\n✓ Generating recommendations for {user_id}...")
                recommendations = engine.collaborative_filtering_recommendations(user_id, n_recommendations=num_recs)
                
                if not recommendations.empty:
                    print(f"\n✓ Here are {len(recommendations)} recommendations:")
                    for idx, movie in recommendations.iterrows():
                        print_movie(movie, show_predicted=True)
                else:
                    print("\n✗ Could not generate recommendations.")
            else:
                print(f"\n✗ User '{user_id}' not found.")
        
        elif choice == "4":
            print("\n--- HYBRID RECOMMENDATIONS ---")
            print("\nRate some movies you've watched (1-10):")
            
            rated_movies = {}
            num_ratings = input("How many movies would you like to rate? (default 3): ").strip()
            num_ratings = int(num_ratings) if num_ratings.isdigit() else 3
            
            movie_titles = sorted(movies_df['title'].tolist())
            for i in range(num_ratings):
                print(f"\nMovie {i+1}:")
                movie = input("  Enter movie title: ").strip()
                if movie in movie_titles:
                    rating = input("  Enter your rating (1-10): ").strip()
                    try:
                        rating = float(rating)
                        if 1.0 <= rating <= 10.0:
                            rated_movies[movie] = rating
                        else:
                            print("  ✗ Rating must be between 1 and 10")
                    except ValueError:
                        print("  ✗ Invalid rating")
                else:
                    print(f"  ✗ Movie '{movie}' not found")
            
            if rated_movies:
                num_recs = input("\nNumber of recommendations (default 10): ").strip()
                num_recs = int(num_recs) if num_recs.isdigit() else 10
                
                print("\n✓ Generating hybrid recommendations...")
                recommendations = engine.hybrid_recommendations(
                    user_ratings=rated_movies,
                    n_recommendations=num_recs
                )
                
                if not recommendations.empty:
                    print(f"\n✓ Here are {len(recommendations)} personalized recommendations:")
                    for idx, movie in recommendations.iterrows():
                        print_movie(movie)
                else:
                    print("\n✗ Could not generate recommendations.")
            else:
                print("\n✗ No valid ratings provided.")
        
        elif choice == "5":
            print("\n--- BROWSE ALL MOVIES ---")
            sort_by = input("Sort by (rating/year/title, default: rating): ").strip().lower()
            
            display_df = movies_df.copy()
            
            if sort_by == "year":
                display_df = display_df.sort_values('year', ascending=False)
            elif sort_by == "title":
                display_df = display_df.sort_values('title')
            else:
                display_df = display_df.sort_values('rating', ascending=False)
            
            print(f"\n✓ Showing {len(display_df)} movies:\n")
            for idx, movie in display_df.iterrows():
                print_movie(movie)
            
            if len(display_df) > 10:
                show_all = input("\nShow all? (y/n): ").strip().lower()
                if show_all != 'y':
                    print(f"\nShowing first 10 of {len(display_df)} movies")
        
        elif choice == "6":
            print("\n👋 Thank you for using Movie Recommendation System!")
            break
        
        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n✗ An error occurred: {e}")

