import React, { useState } from 'react';
import './App.css';
import Header from './components/Header';
import SearchMovies from './components/SearchMovies';
import Recommendations from './components/Recommendations';
import BrowseMovies from './components/BrowseMovies';
import UserRecommendations from './components/UserRecommendations';

function App() {
  const [activeTab, setActiveTab] = useState('search');

  return (
    <div className="App">
      <Header />
      <div className="container">
        <div className="tabs">
          <button 
            className={activeTab === 'search' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('search')}
          >
            🔍 Search Movies
          </button>
          <button 
            className={activeTab === 'recommendations' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('recommendations')}
          >
            💡 Recommendations
          </button>
          <button 
            className={activeTab === 'browse' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('browse')}
          >
            📊 Browse All
          </button>
          <button 
            className={activeTab === 'user' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('user')}
          >
            👤 User Recommendations
          </button>
        </div>

        <div className="content">
          {activeTab === 'search' && <SearchMovies />}
          {activeTab === 'recommendations' && <Recommendations />}
          {activeTab === 'browse' && <BrowseMovies />}
          {activeTab === 'user' && <UserRecommendations />}
        </div>
      </div>
    </div>
  );
}

export default App;

