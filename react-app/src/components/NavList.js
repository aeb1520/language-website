// components/NavList.js

import React from 'react';
import { Link } from 'react-router-dom';
import './NavList.css';


function NavList() {
  return (
    <nav>
      <ul className="nav-list">
        <li className = "home"><Link to="/">Home</Link></li>
        <li className = "story"><Link to="/story">Story</Link></li>
      </ul>
    </nav>
  );
}

export default NavList;
