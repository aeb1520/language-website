// components/QuizPage.js

import React, { useState } from 'react';
import './QuizPage.css';

function QuizPage() {
  const [level, setLevel] = useState("beginner");

  const handleLevelChange = (event) => {
    setLevel(event.target.value);
  };

  return (


      <div className="level-select2">
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
  );
}

export default QuizPage;
