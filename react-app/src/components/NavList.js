// components/NavList.js

import React from 'react';
import { Link } from 'react-router-dom';
import './NavList.css';


function NavList() {
  return (
    <nav>
      <ul className="nav-list">
        <li><Link to="/">Beginner</Link></li>
        <li><Link to="/story">Story</Link></li>
        <li><Link to="/quiz">Quiz</Link></li>
      </ul>
    </nav>
  );
}

export default NavList;
