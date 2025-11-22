import React, { useState, useEffect } from 'react';
import { movieAPI } from '../services/api';
import MovieCard from './MovieCard';
import './SearchMovies.css';

const SearchMovies = () => {
  const [query, setQuery] = useState('');
  const [platform, setPlatform] = useState('');
  const [genre, setGenre] = useState('');
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [platforms, setPlatforms] = useState([]);
  const [genres, setGenres] = useState([]);

  useEffect(() => {
    // Load platforms and genres
    movieAPI.getPlatforms().then(res => setPlatforms(res.data.platforms));
    movieAPI.getGenres().then(res => setGenres(res.data.genres));
  }, []);

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const params = {};
      if (query) params.q = query;
      if (platform) params.platform = platform;
      if (genre) params.genre = genre;
      
      const response = await movieAPI.searchMovies(params);
      setMovies(response.data.movies || []);
    } catch (error) {
      console.error('Search error:', error);
      alert('Error searching movies. Make sure the API server is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="search-movies">
      <h2>🔍 Search Movies</h2>
      <p className="section-description">
        Find movies by title, platform, or genre
      </p>

      <form onSubmit={handleSearch} className="search-form">
        <div className="form-row">
          <div className="form-group">
            <label>Movie Title</label>
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="e.g., Inception"
              className="form-input"
            />
          </div>

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
            <label>Genre</label>
            <select
              value={genre}
              onChange={(e) => setGenre(e.target.value)}
              className="form-select"
            >
              <option value="">All Genres</option>
              {genres.map(g => (
                <option key={g} value={g}>{g}</option>
              ))}
            </select>
          </div>
        </div>

        <button type="submit" className="btn-primary" disabled={loading}>
          {loading ? 'Searching...' : '🔍 Search'}
        </button>
      </form>

      {movies.length > 0 && (
        <div className="results-section">
          <h3>Found {movies.length} movies</h3>
          <div className="movies-grid">
            {movies.map((movie, index) => (
              <MovieCard key={index} movie={movie} />
            ))}
          </div>
        </div>
      )}

      {movies.length === 0 && !loading && (
        <div className="empty-state">
          <p>Enter search criteria and click Search to find movies</p>
        </div>
      )}
    </div>
  );
};

export default SearchMovies;

