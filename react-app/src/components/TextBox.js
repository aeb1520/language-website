// components/TextBox.js

import React from 'react';
import './TextBox.css';

function TextBox() {
  return (
    <textarea 
      className="input-box" 
      placeholder="Enter your vocab list..."
    />
  );
}

export default TextBox;
