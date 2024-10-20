// components/NavList.js

import React from 'react';
import './NavList.css';

function NavList() {
  return (
    <nav>
      <ul className="nav-list">
        <li><a href="#home">Home</a></li>
        <li><a href="#story">Story</a></li>
        <li><a href="#quiz">Quiz</a></li>
      </ul>
    </nav>
  );
}

export default NavList;
