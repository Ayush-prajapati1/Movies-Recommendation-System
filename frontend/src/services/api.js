import axios from 'axios';

// Use proxy in development, or direct URL in production
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 second timeout
});

// Add request interceptor for debugging
api.interceptors.request.use(
  (config) => {
    console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('API Request Error:', error);
    return Promise.reject(error);
  }
);

// Add response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.code === 'ECONNABORTED') {
      console.error('API Request Timeout');
      alert('Request timeout. Please check if the backend server is running.');
    } else if (error.message === 'Network Error') {
      console.error('Network Error - Backend server may not be running');
      alert('Cannot connect to backend server. Please make sure the Flask server is running on port 5000.\n\nRun: python api_server.py');
    } else {
      console.error('API Error:', error.message);
    }
    return Promise.reject(error);
  }
);

export const movieAPI = {
  // Get all movies with filters
  getMovies: (params = {}) => {
    return api.get('/movies', { params });
  },

  // Search movies
  searchMovies: (params = {}) => {
    return api.get('/movies/search', { params });
  },

  // Get content-based recommendations
  getContentBasedRecommendations: (movieTitle, nRecommendations = 10) => {
    return api.post('/recommendations/content-based', {
      movie_title: movieTitle,
      n_recommendations: nRecommendations,
    });
  },

  // Get collaborative filtering recommendations
  getCollaborativeRecommendations: (userId, nRecommendations = 10) => {
    return api.post('/recommendations/collaborative', {
      user_id: userId,
      n_recommendations: nRecommendations,
    });
  },

  // Get hybrid recommendations
  getHybridRecommendations: (data) => {
    return api.post('/recommendations/hybrid', data);
  },

  // Get platforms
  getPlatforms: () => {
    return api.get('/platforms');
  },

  // Get genres
  getGenres: () => {
    return api.get('/genres');
  },

  // Get movie titles
  getMovieTitles: () => {
    return api.get('/movie-titles');
  },

  // Get users
  getUsers: () => {
    return api.get('/users');
  },
};

export default api;

