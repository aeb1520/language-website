// components/StoryPage.js

import React, { useState } from 'react';
import './StoryPage.css';
import TextBox2 from './TextBox2';

function StoryPage() {
  const [level, setLevel] = useState("beginner");

  const handleLevelChange = (event) => {
    setLevel(event.target.value);
  };

  return (
    <div className="story-page-container">
      <div className="level-select">
        <label>
          <input
            type="radio"
            name="level"
            value="beginner"
            checked={level === "beginner"}
            onChange={handleLevelChange}
          />
          Beginner
        </label>

        <label>
          <input
            type="radio"
            name="level"
            value="intermediate"
            checked={level === "intermediate"}
            onChange={handleLevelChange}
          />
          Intermediate
        </label>

        <label>
          <input
            type="radio"
            name="level"
            value="advanced"
            checked={level === "advanced"}
            onChange={handleLevelChange}
          />
          Advanced
        </label>
      </div>

  <div className="story-textbox">
  <TextBox2 topic={topic} />  {}
  </div>
  </div>
  );
}

export default StoryPage;
