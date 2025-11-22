import React, { useState, useEffect } from 'react';
import { movieAPI } from '../services/api';
import MovieCard from './MovieCard';
import './UserRecommendations.css';

const UserRecommendations = () => {
  const [userId, setUserId] = useState('');
  const [numRecommendations, setNumRecommendations] = useState(10);
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    movieAPI.getUsers().then(res => {
      const userList = res.data.users || [];
      setUsers(userList);
      if (userList.length > 0) {
        setUserId(userList[0]);
      }
    });
  }, []);

  const handleGetRecommendations = async (e) => {
    e.preventDefault();
    if (!userId) {
      alert('Please select a user');
      return;
    }

    setLoading(true);
    try {
      const response = await movieAPI.getCollaborativeRecommendations(userId, numRecommendations);
      setMovies(response.data.movies || []);
    } catch (error) {
      console.error('Recommendation error:', error);
      alert('Error getting recommendations. Make sure the API server is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="user-recommendations">
      <h2>👤 Collaborative Filtering Recommendations</h2>
      <p className="section-description">
        Get recommendations based on what similar users enjoyed using collaborative filtering
      </p>

      <form onSubmit={handleGetRecommendations} className="recommendation-form">
        <div className="form-group">
          <label>Select User ID</label>
          <select
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            className="form-select"
            required
          >
            <option value="">Choose a user...</option>
            {users.map(user => (
              <option key={user} value={user}>{user}</option>
            ))}
          </select>
          <small className="form-help">
            {users.length > 0 
              ? `Available users: ${users.length}` 
              : 'No users available'}
          </small>
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

        <button type="submit" className="btn-primary" disabled={loading || users.length === 0}>
          {loading ? 'Analyzing preferences...' : 'Get User Recommendations'}
        </button>
      </form>

      {movies.length > 0 && (
        <div className="results-section">
          <h3>Recommended Movies for {userId} ({movies.length})</h3>
          <div className="movies-grid">
            {movies.map((movie, index) => (
              <MovieCard
                key={index}
                movie={movie}
                showPredicted={true}
              />
            ))}
          </div>
        </div>
      )}

      {movies.length === 0 && !loading && (
        <div className="empty-state">
          <p>Select a user and click the button to get personalized recommendations</p>
        </div>
      )}
    </div>
  );
};

export default UserRecommendations;

