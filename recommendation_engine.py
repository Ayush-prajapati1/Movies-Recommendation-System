"""
Movie Recommendation Engine - Implements multiple recommendation algorithms
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds

class MovieRecommendationEngine:
    """Main recommendation engine with multiple algorithms"""
    
    def __init__(self, movies_df, user_ratings_df=None):
        """
        Initialize the recommendation engine
        
        Args:
            movies_df: DataFrame with movie information
            user_ratings_df: DataFrame with user ratings (optional, for collaborative filtering)
        """
        self.movies_df = movies_df.copy()
        self.user_ratings_df = user_ratings_df
        
        # Prepare content-based features
        self._prepare_content_features()
        
        # Prepare collaborative filtering matrix if ratings available
        if user_ratings_df is not None:
            self._prepare_collaborative_matrix()
    
    def _prepare_content_features(self):
        """Prepare features for content-based filtering"""
        # Combine genre, director, and year for content similarity
        self.movies_df['content'] = (
            self.movies_df['genre'].astype(str) + ' ' +
            self.movies_df['director'].astype(str) + ' ' +
            self.movies_df['year'].astype(str)
        )
        
        # Create TF-IDF matrix
        self.tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
        self.tfidf_matrix = self.tfidf.fit_transform(self.movies_df['content'])
        
        # Calculate cosine similarity matrix
        self.content_similarity = cosine_similarity(self.tfidf_matrix)
    
    def _prepare_collaborative_matrix(self):
        """Prepare user-item matrix for collaborative filtering"""
        # Create user-item matrix
        user_item_matrix = self.user_ratings_df.pivot_table(
            index='user_id',
            columns='movie_title',
            values='rating',
            fill_value=0
        )
        
        self.user_item_matrix = user_item_matrix
        self.movie_titles = user_item_matrix.columns.tolist()
        
        # Convert to sparse matrix for SVD
        self.sparse_matrix = csr_matrix(user_item_matrix.values)
        
        # Perform SVD for collaborative filtering
        self._perform_svd()
    
    def _perform_svd(self, n_components=50):
        """Perform Singular Value Decomposition for collaborative filtering"""
        # Normalize by subtracting user mean
        user_ratings_mean = np.mean(self.sparse_matrix, axis=1)
        self.sparse_matrix_normalized = self.sparse_matrix - user_ratings_mean.reshape(-1, 1)
        
        # Perform SVD
        U, sigma, Vt = svds(self.sparse_matrix_normalized, k=min(n_components, min(self.sparse_matrix.shape) - 1))
        sigma = np.diag(sigma)
        
        self.U = U
        self.sigma = sigma
        self.Vt = Vt
    
    def content_based_recommendations(self, movie_title, n_recommendations=10):
        """
        Get content-based recommendations for a movie
        
        Args:
            movie_title: Title of the movie
            n_recommendations: Number of recommendations to return
            
        Returns:
            DataFrame with recommended movies
        """
        if movie_title not in self.movies_df['title'].values:
            return pd.DataFrame()
        
        # Get index of the movie
        movie_idx = self.movies_df[self.movies_df['title'] == movie_title].index[0]
        
        # Get similarity scores
        similarity_scores = list(enumerate(self.content_similarity[movie_idx]))
        
        # Sort by similarity
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        # Get top recommendations (excluding the movie itself)
        top_movies = similarity_scores[1:n_recommendations+1]
        
        # Extract movie indices and scores
        movie_indices = [i[0] for i in top_movies]
        scores = [i[1] for i in top_movies]
        
        # Create recommendations dataframe
        recommendations = self.movies_df.iloc[movie_indices].copy()
        recommendations['similarity_score'] = scores
        
        return recommendations[['title', 'platform', 'genre', 'year', 'rating', 'director', 'similarity_score']]
    
    def collaborative_filtering_recommendations(self, user_id, n_recommendations=10):
        """
        Get collaborative filtering recommendations for a user
        
        Args:
            user_id: ID of the user
            n_recommendations: Number of recommendations to return
            
        Returns:
            DataFrame with recommended movies
        """
        if self.user_ratings_df is None:
            return pd.DataFrame()
        
        if user_id not in self.user_item_matrix.index:
            # If user doesn't exist, return popular movies
            return self._get_popular_movies(n_recommendations)
        
        # Get user index
        user_idx = self.user_item_matrix.index.get_loc(user_id)
        
        # Predict ratings using SVD
        predicted_ratings = np.dot(np.dot(self.U[user_idx, :], self.sigma), self.Vt)
        
        # Add back user mean
        user_mean = np.mean(self.sparse_matrix[user_idx, :].toarray())
        predicted_ratings = predicted_ratings + user_mean
        
        # Get already rated movies
        user_ratings = self.user_item_matrix.iloc[user_idx]
        rated_movies = user_ratings[user_ratings > 0].index.tolist()
        
        # Create recommendations dataframe
        recommendations = []
        for i, movie_title in enumerate(self.movie_titles):
            if movie_title not in rated_movies:
                recommendations.append({
                    'movie_title': movie_title,
                    'predicted_rating': predicted_ratings[i]
                })
        
        recommendations_df = pd.DataFrame(recommendations)
        recommendations_df = recommendations_df.sort_values('predicted_rating', ascending=False)
        recommendations_df = recommendations_df.head(n_recommendations)
        
        # Merge with movie details
        recommendations_df = recommendations_df.merge(
            self.movies_df,
            left_on='movie_title',
            right_on='title',
            how='left'
        )
        
        return recommendations_df[['title', 'platform', 'genre', 'year', 'rating', 'director', 'predicted_rating']]
    
    def hybrid_recommendations(self, movie_title=None, user_id=None, user_ratings=None, n_recommendations=10):
        """
        Get hybrid recommendations combining content-based and collaborative filtering
        
        Args:
            movie_title: Title of a movie the user likes (for content-based)
            user_id: ID of the user (for collaborative filtering)
            user_ratings: Dict of {movie_title: rating} for new users
            n_recommendations: Number of recommendations to return
            
        Returns:
            DataFrame with recommended movies
        """
        recommendations = []
        
        # Content-based recommendations
        if movie_title:
            content_recs = self.content_based_recommendations(movie_title, n_recommendations * 2)
            if not content_recs.empty:
                content_recs['rec_type'] = 'content'
                recommendations.append(content_recs)
        
        # Collaborative filtering recommendations
        if user_id and self.user_ratings_df is not None:
            collab_recs = self.collaborative_filtering_recommendations(user_id, n_recommendations * 2)
            if not collab_recs.empty:
                collab_recs['rec_type'] = 'collaborative'
                recommendations.append(collab_recs)
        
        # For new users with ratings
        if user_ratings:
            content_recs_list = []
            for movie, rating in user_ratings.items():
                if rating >= 7.0:  # Only consider highly rated movies
                    recs = self.content_based_recommendations(movie, n_recommendations)
                    if not recs.empty:
                        recs['weight'] = rating / 10.0  # Weight by user rating
                        content_recs_list.append(recs)
            
            if content_recs_list:
                combined_content = pd.concat(content_recs_list, ignore_index=True)
                # Aggregate by movie title, taking weighted average
                combined_content = combined_content.groupby('title').agg({
                    'platform': 'first',
                    'genre': 'first',
                    'year': 'first',
                    'rating': 'first',
                    'director': 'first',
                    'similarity_score': 'mean',
                    'weight': 'mean'
                }).reset_index()
                combined_content['final_score'] = combined_content['similarity_score'] * combined_content['weight']
                combined_content = combined_content.sort_values('final_score', ascending=False)
                combined_content['rec_type'] = 'hybrid'
                recommendations.append(combined_content)
        
        if not recommendations:
            return self._get_popular_movies(n_recommendations)
        
        # Combine and deduplicate
        all_recs = pd.concat(recommendations, ignore_index=True)
        all_recs = all_recs.drop_duplicates(subset=['title'], keep='first')
        
        # Sort by rating and similarity/predicted rating
        if 'similarity_score' in all_recs.columns:
            all_recs = all_recs.sort_values(['rating', 'similarity_score'], ascending=[False, False])
        elif 'predicted_rating' in all_recs.columns:
            all_recs = all_recs.sort_values(['rating', 'predicted_rating'], ascending=[False, False])
        else:
            all_recs = all_recs.sort_values('rating', ascending=False)
        
        return all_recs.head(n_recommendations)[['title', 'platform', 'genre', 'year', 'rating', 'director']]
    
    def _get_popular_movies(self, n_recommendations=10):
        """Get popular movies based on rating"""
        popular = self.movies_df.nlargest(n_recommendations, 'rating')
        return popular[['title', 'platform', 'genre', 'year', 'rating', 'director']]
    
    def search_movies(self, query, platform=None, genre=None, year=None):
        """
        Search movies by various criteria
        
        Args:
            query: Text query to search in title
            platform: Filter by platform (Netflix, Prime Video, Hotstar, etc.)
            genre: Filter by genre
            year: Filter by year
            
        Returns:
            DataFrame with matching movies
        """
        results = self.movies_df.copy()
        
        if query:
            results = results[results['title'].str.contains(query, case=False, na=False)]
        
        if platform:
            results = results[results['platform'].str.contains(platform, case=False, na=False)]
        
        if genre:
            results = results[results['genre'].str.contains(genre, case=False, na=False)]
        
        if year:
            results = results[results['year'] == year]
        
        return results[['title', 'platform', 'genre', 'year', 'rating', 'director']].sort_values('rating', ascending=False)

