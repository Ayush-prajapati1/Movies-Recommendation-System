import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <h1 className="header-title">🎬 Movie Recommendation System</h1>
        <p className="header-subtitle">
          Discover your next favorite movie from Netflix, Prime Video, Hotstar, and more!
        </p>
      </div>
    </header>
  );
};

export default Header;

