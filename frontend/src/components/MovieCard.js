import React from 'react';
import './MovieCard.css';

const MovieCard = ({ movie, showSimilarity = false, showPredicted = false }) => {
  const getPlatformColor = (platform) => {
    const colors = {
      'Netflix': '#E50914',
      'Prime Video': '#00A8E1',
      'Hotstar': '#FF6B6B',
      'Disney+ Hotstar': '#113CCF',
    };
    return colors[platform] || '#667eea';
  };

  return (
    <div className="movie-card">
      <div className="movie-header">
        <h3 className="movie-title">{movie.title}</h3>
        <span className="movie-year">({movie.year})</span>
      </div>
      
      <div className="movie-platform" style={{ backgroundColor: getPlatformColor(movie.platform) }}>
        {movie.platform}
      </div>
      
      <div className="movie-details">
        <div className="movie-genre">
          <strong>Genre:</strong> {movie.genre}
        </div>
        <div className="movie-director">
          <strong>Director:</strong> {movie.director}
        </div>
        <div className="movie-rating">
          <span className="rating-star">⭐</span>
          <strong>{movie.rating}/10</strong>
        </div>
        {showSimilarity && movie.similarity_score !== undefined && (
          <div className="movie-similarity">
            <strong>Similarity:</strong> {(movie.similarity_score * 100).toFixed(1)}%
          </div>
        )}
        {showPredicted && movie.predicted_rating !== undefined && (
          <div className="movie-predicted">
            <strong>Predicted Rating:</strong> {movie.predicted_rating.toFixed(1)}/10
          </div>
        )}
      </div>
    </div>
  );
};

export default MovieCard;

