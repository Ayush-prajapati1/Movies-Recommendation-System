import React, { useState, useEffect } from 'react';
import { movieAPI } from '../services/api';
import MovieCard from './MovieCard';
import './Recommendations.css';

const Recommendations = () => {
  const [recommendationType, setRecommendationType] = useState('content');
  const [movieTitle, setMovieTitle] = useState('');
  const [numRecommendations, setNumRecommendations] = useState(10);
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [movieTitles, setMovieTitles] = useState([]);
  
  // For hybrid recommendations
  const [userRatings, setUserRatings] = useState([{ movie: '', rating: 7.0 }]);

  useEffect(() => {
    movieAPI.getMovieTitles().then(res => setMovieTitles(res.data.titles));
  }, []);

  const handleContentBased = async (e) => {
    e.preventDefault();
    if (!movieTitle) {
      alert('Please select a movie');
      return;
    }

    setLoading(true);
    try {
      const response = await movieAPI.getContentBasedRecommendations(movieTitle, numRecommendations);
      setMovies(response.data.movies || []);
    } catch (error) {
      console.error('Recommendation error:', error);
      alert('Error getting recommendations. Make sure the API server is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleHybrid = async (e) => {
    e.preventDefault();
    const ratings = {};
    let hasValidRating = false;

    userRatings.forEach(({ movie, rating }) => {
      if (movie) {
        ratings[movie] = parseFloat(rating);
        hasValidRating = true;
      }
    });

    if (!hasValidRating) {
      alert('Please rate at least one movie');
      return;
    }

    setLoading(true);
    try {
      const response = await movieAPI.getHybridRecommendations({
        user_ratings: ratings,
        n_recommendations: numRecommendations,
      });
      setMovies(response.data.movies || []);
    } catch (error) {
      console.error('Recommendation error:', error);
      alert('Error getting recommendations. Make sure the API server is running.');
    } finally {
      setLoading(false);
    }
  };

  const addRatingField = () => {
    setUserRatings([...userRatings, { movie: '', rating: 7.0 }]);
  };

  const updateRating = (index, field, value) => {
    const updated = [...userRatings];
    updated[index][field] = value;
    setUserRatings(updated);
  };

  const removeRating = (index) => {
    if (userRatings.length > 1) {
      setUserRatings(userRatings.filter((_, i) => i !== index));
    }
  };

  return (
    <div className="recommendations">
      <h2>💡 Get Movie Recommendations</h2>
      <p className="section-description">
        Get personalized movie recommendations based on your preferences
      </p>

      <div className="recommendation-tabs">
        <button
          className={recommendationType === 'content' ? 'rec-tab active' : 'rec-tab'}
          onClick={() => setRecommendationType('content')}
        >
          Content-Based
        </button>
        <button
          className={recommendationType === 'hybrid' ? 'rec-tab active' : 'rec-tab'}
          onClick={() => setRecommendationType('hybrid')}
        >
          Hybrid (Best Results)
        </button>
      </div>

      {recommendationType === 'content' && (
        <form onSubmit={handleContentBased} className="recommendation-form">
          <div className="form-group">
            <label>Select a movie you like</label>
            <select
              value={movieTitle}
              onChange={(e) => setMovieTitle(e.target.value)}
              className="form-select"
              required
            >
              <option value="">Choose a movie...</option>
              {movieTitles.map(title => (
                <option key={title} value={title}>{title}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Number of recommendations: {numRecommendations}</label>
            <input
              type="range"
              min="5"
              max="20"
              value={numRecommendations}
              onChange={(e) => setNumRecommendations(parseInt(e.target.value))}
              className="form-range"
            />
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Finding recommendations...' : 'Get Recommendations'}
          </button>
        </form>
      )}

      {recommendationType === 'hybrid' && (
        <form onSubmit={handleHybrid} className="recommendation-form">
          <div className="form-group">
            <label>Rate movies you've watched (1-10)</label>
            {userRatings.map((rating, index) => (
              <div key={index} className="rating-row">
                <select
                  value={rating.movie}
                  onChange={(e) => updateRating(index, 'movie', e.target.value)}
                  className="form-select"
                  style={{ flex: 2 }}
                >
                  <option value="">Select movie...</option>
                  {movieTitles.map(title => (
                    <option key={title} value={title}>{title}</option>
                  ))}
                </select>
                <input
                  type="number"
                  min="1"
                  max="10"
                  step="0.1"
                  value={rating.rating}
                  onChange={(e) => updateRating(index, 'rating', e.target.value)}
                  className="form-input"
                  style={{ flex: 1, maxWidth: '100px' }}
                />
                {userRatings.length > 1 && (
                  <button
                    type="button"
                    onClick={() => removeRating(index)}
                    className="btn-remove"
                  >
                    ✕
                  </button>
                )}
              </div>
            ))}
            <button type="button" onClick={addRatingField} className="btn-secondary">
              + Add Another Movie
            </button>
          </div>

          <div className="form-group">
            <label>Number of recommendations: {numRecommendations}</label>
            <input
              type="range"
              min="5"
              max="20"
              value={numRecommendations}
              onChange={(e) => setNumRecommendations(parseInt(e.target.value))}
              className="form-range"
            />
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Generating recommendations...' : 'Get Hybrid Recommendations'}
          </button>
        </form>
      )}

      {movies.length > 0 && (
        <div className="results-section">
          <h3>Recommended Movies ({movies.length})</h3>
          <div className="movies-grid">
            {movies.map((movie, index) => (
              <MovieCard
                key={index}
                movie={movie}
                showSimilarity={recommendationType === 'content'}
              />
            ))}
          </div>
        </div>
      )}

      {movies.length === 0 && !loading && (
        <div className="empty-state">
          <p>Fill in the form above and click the button to get recommendations</p>
        </div>
      )}
    </div>
  );
};

export default Recommendations;

