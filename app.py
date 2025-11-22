"""
Streamlit Web Application for Movie Recommendations
"""
import streamlit as st
import pandas as pd
from movie_data import generate_movie_dataset, generate_user_ratings
from recommendation_engine import MovieRecommendationEngine

# Page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Initialize session state
if 'engine' not in st.session_state:
    with st.spinner("Loading movie database..."):
        movies_df = generate_movie_dataset()
        user_ratings_df = generate_user_ratings(movies_df, num_users=50)
        st.session_state.engine = MovieRecommendationEngine(movies_df, user_ratings_df)
        st.session_state.movies_df = movies_df
        st.session_state.user_ratings_df = user_ratings_df

# Title and description
st.title("🎬 Movie Recommendation System")
st.markdown("""
Discover your next favorite movie! This system recommends movies from **Netflix**, **Prime Video**, **Hotstar**, and more 
based on your preferences using advanced AI algorithms.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a feature:",
    ["🔍 Search Movies", "💡 Get Recommendations", "📊 Browse All Movies", "👤 User Recommendations"]
)

# Search Movies Page
if page == "🔍 Search Movies":
    st.header("🔍 Search Movies")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_query = st.text_input("Search by title", placeholder="e.g., Inception")
    
    with col2:
        platform_filter = st.selectbox(
            "Filter by Platform",
            ["All"] + list(st.session_state.movies_df['platform'].unique())
        )
    
    with col3:
        genre_filter = st.selectbox(
            "Filter by Genre",
            ["All"] + sorted(set([g for genres in st.session_state.movies_df['genre'] for g in genres.split(',')]))
        )
    
    if st.button("Search", type="primary"):
        platform = None if platform_filter == "All" else platform_filter
        genre = None if genre_filter == "All" else genre_filter
        
        results = st.session_state.engine.search_movies(
            query=search_query if search_query else None,
            platform=platform,
            genre=genre
        )
        
        if not results.empty:
            st.success(f"Found {len(results)} movies!")
            st.dataframe(
                results,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("No movies found matching your criteria.")

# Get Recommendations Page
elif page == "💡 Get Recommendations":
    st.header("💡 Get Movie Recommendations")
    
    recommendation_type = st.radio(
        "Choose recommendation type:",
        ["Content-Based (Based on a movie you like)", "Hybrid (Best of both worlds)"],
        horizontal=True
    )
    
    if recommendation_type == "Content-Based (Based on a movie you like)":
        st.subheader("Tell us a movie you like, and we'll find similar ones!")
        
        movie_titles = sorted(st.session_state.movies_df['title'].tolist())
        selected_movie = st.selectbox("Select a movie you enjoyed:", movie_titles)
        
        num_recommendations = st.slider("Number of recommendations", 5, 20, 10)
        
        if st.button("Get Recommendations", type="primary"):
            with st.spinner("Finding similar movies..."):
                recommendations = st.session_state.engine.content_based_recommendations(
                    selected_movie,
                    n_recommendations=num_recommendations
                )
                
                if not recommendations.empty:
                    st.success(f"Here are {len(recommendations)} movies similar to '{selected_movie}':")
                    
                    # Display recommendations in a nice format
                    for idx, movie in recommendations.iterrows():
                        with st.container():
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.markdown(f"### {movie['title']} ({movie['year']})")
                                st.markdown(f"**Platform:** {movie['platform']} | **Genre:** {movie['genre']} | **Director:** {movie['director']}")
                                st.markdown(f"**Rating:** ⭐ {movie['rating']}/10 | **Similarity:** {movie['similarity_score']:.2%}")
                            with col2:
                                st.metric("Match", f"{movie['similarity_score']:.0%}")
                            st.divider()
                else:
                    st.error("Could not generate recommendations. Please try another movie.")
    
    else:  # Hybrid recommendations
        st.subheader("Get personalized recommendations based on your preferences")
        
        st.markdown("**Option 1: Rate some movies you've watched**")
        
        # Movie rating interface
        rated_movies = {}
        num_movies_to_rate = st.slider("How many movies would you like to rate?", 1, 5, 3)
        
        movie_titles = sorted(st.session_state.movies_df['title'].tolist())
        
        for i in range(num_movies_to_rate):
            col1, col2 = st.columns([3, 1])
            with col1:
                movie = st.selectbox(f"Movie {i+1}", movie_titles, key=f"movie_{i}")
            with col2:
                rating = st.slider("Rating", 1.0, 10.0, 7.0, 0.1, key=f"rating_{i}")
                rated_movies[movie] = rating
        
        num_recommendations = st.slider("Number of recommendations", 5, 20, 10, key="hybrid_num")
        
        if st.button("Get Hybrid Recommendations", type="primary"):
            with st.spinner("Generating personalized recommendations..."):
                recommendations = st.session_state.engine.hybrid_recommendations(
                    user_ratings=rated_movies,
                    n_recommendations=num_recommendations
                )
                
                if not recommendations.empty:
                    st.success(f"Here are {len(recommendations)} personalized recommendations for you:")
                    
                    for idx, movie in recommendations.iterrows():
                        with st.container():
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.markdown(f"### {movie['title']} ({movie['year']})")
                                st.markdown(f"**Platform:** {movie['platform']} | **Genre:** {movie['genre']} | **Director:** {movie['director']}")
                                st.markdown(f"**Rating:** ⭐ {movie['rating']}/10")
                            with col2:
                                st.metric("Rating", f"{movie['rating']}/10")
                            st.divider()
                else:
                    st.error("Could not generate recommendations. Please try again.")

# Browse All Movies Page
elif page == "📊 Browse All Movies":
    st.header("📊 Browse All Movies")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        sort_by = st.selectbox("Sort by", ["Rating (High to Low)", "Year (Newest)", "Year (Oldest)", "Title (A-Z)"])
    with col2:
        platform_filter = st.selectbox(
            "Platform",
            ["All"] + list(st.session_state.movies_df['platform'].unique()),
            key="browse_platform"
        )
    with col3:
        min_rating = st.slider("Minimum Rating", 0.0, 10.0, 0.0, 0.1)
    
    # Apply filters
    display_df = st.session_state.movies_df.copy()
    
    if platform_filter != "All":
        display_df = display_df[display_df['platform'] == platform_filter]
    
    display_df = display_df[display_df['rating'] >= min_rating]
    
    # Sort
    if sort_by == "Rating (High to Low)":
        display_df = display_df.sort_values('rating', ascending=False)
    elif sort_by == "Year (Newest)":
        display_df = display_df.sort_values('year', ascending=False)
    elif sort_by == "Year (Oldest)":
        display_df = display_df.sort_values('year', ascending=True)
    else:
        display_df = display_df.sort_values('title')
    
    st.dataframe(
        display_df[['title', 'platform', 'genre', 'year', 'rating', 'director']],
        use_container_width=True,
        hide_index=True
    )
    
    st.info(f"Showing {len(display_df)} movies")

# User Recommendations Page
elif page == "👤 User Recommendations":
    st.header("👤 Collaborative Filtering Recommendations")
    st.markdown("Get recommendations based on what similar users liked!")
    
    # Get list of existing users
    if st.session_state.user_ratings_df is not None:
        user_ids = sorted(st.session_state.user_ratings_df['user_id'].unique().tolist())
        selected_user = st.selectbox("Select a user ID:", user_ids)
        
        num_recommendations = st.slider("Number of recommendations", 5, 20, 10, key="user_num")
        
        if st.button("Get User Recommendations", type="primary"):
            with st.spinner("Analyzing user preferences..."):
                recommendations = st.session_state.engine.collaborative_filtering_recommendations(
                    selected_user,
                    n_recommendations=num_recommendations
                )
                
                if not recommendations.empty:
                    st.success(f"Here are personalized recommendations for {selected_user}:")
                    
                    for idx, movie in recommendations.iterrows():
                        with st.container():
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.markdown(f"### {movie['title']} ({movie['year']})")
                                st.markdown(f"**Platform:** {movie['platform']} | **Genre:** {movie['genre']} | **Director:** {movie['director']}")
                                if 'predicted_rating' in movie:
                                    st.markdown(f"**Rating:** ⭐ {movie['rating']}/10 | **Predicted Rating:** {movie['predicted_rating']:.1f}/10")
                                else:
                                    st.markdown(f"**Rating:** ⭐ {movie['rating']}/10")
                            with col2:
                                if 'predicted_rating' in movie:
                                    st.metric("Predicted", f"{movie['predicted_rating']:.1f}/10")
                                else:
                                    st.metric("Rating", f"{movie['rating']}/10")
                            st.divider()
                else:
                    st.error("Could not generate recommendations.")
    else:
        st.warning("User ratings data not available.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.markdown("""
This recommendation system uses:
- **Content-Based Filtering**: Recommends movies similar to ones you like
- **Collaborative Filtering**: Recommends based on similar users' preferences
- **Hybrid Approach**: Combines both methods for best results
""")

