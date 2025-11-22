import React, { useState, useEffect } from 'react';
import { movieAPI } from '../services/api';
import MovieCard from './MovieCard';
import './BrowseMovies.css';

const BrowseMovies = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [platform, setPlatform] = useState('');
  const [sortBy, setSortBy] = useState('rating');
  const [minRating, setMinRating] = useState(0);
  const [platforms, setPlatforms] = useState([]);

  useEffect(() => {
    movieAPI.getPlatforms().then(res => setPlatforms(res.data.platforms));
    loadMovies();
  }, []);

  useEffect(() => {
    loadMovies();
  }, [platform, sortBy, minRating]);

  const loadMovies = async () => {
    setLoading(true);
    try {
      const params = {};
      if (platform) params.platform = platform;
      
      const response = await movieAPI.getMovies(params);
      let moviesList = response.data.movies || [];
      
      // Filter by minimum rating
      moviesList = moviesList.filter(m => m.rating >= minRating);
      
      // Sort
      moviesList.sort((a, b) => {
        switch (sortBy) {
          case 'rating':
            return b.rating - a.rating;
          case 'year':
            return b.year - a.year;
          case 'year_old':
            return a.year - b.year;
          case 'title':
            return a.title.localeCompare(b.title);
          default:
            return 0;
        }
      });
      
      setMovies(moviesList);
    } catch (error) {
      console.error('Error loading movies:', error);
      alert('Error loading movies. Make sure the API server is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="browse-movies">
      <h2>📊 Browse All Movies</h2>
      <p className="section-description">
        Explore all available movies with filters and sorting options
      </p>

      <div className="browse-filters">
        <div className="form-group">
          <label>Platform</label>
          <select
            value={platform}
            onChange={(e) => setPlatform(e.target.value)}
            className="form-select"
          >
            <option value="">All Platforms</option>
            {platforms.map(p => (
              <option key={p} value={p}>{p}</option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Sort By</label>
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            className="form-select"
          >
            <option value="rating">Rating (High to Low)</option>
            <option value="year">Year (Newest)</option>
            <option value="year_old">Year (Oldest)</option>
            <option value="title">Title (A-Z)</option>
          </select>
        </div>

        <div className="form-group">
          <label>Minimum Rating: {minRating.toFixed(1)}</label>
          <input
            type="range"
            min="0"
            max="10"
            step="0.1"
            value={minRating}
            onChange={(e) => setMinRating(parseFloat(e.target.value))}
            className="form-range"
          />
        </div>
      </div>

      {loading ? (
        <div className="loading-state">
          <p>Loading movies...</p>
        </div>
      ) : (
        <>
          <div className="movies-count">
            Showing {movies.length} movies
          </div>
          <div className="movies-grid">
            {movies.map((movie, index) => (
              <MovieCard key={index} movie={movie} />
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default BrowseMovies;

