import React, { useState } from 'react';
import './TextBox.css';

function TextBox() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');  // State to hold the result

  const handleChange = (event) => {
    setText(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://172.27.86.104:8080/api/endpoint', {  // Update with your Flask server's address
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data);
        setResult(data.result);  // Set the result from the response
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  return (
    <div className="textbox-container">
      <textarea
        className="input-box"
        placeholder="Enter your vocab list..."
        value={text}
        onChange={handleChange}
      />
      <button className="submit-btn" onClick={handleSubmit}>Submit</button> {/* onClick added */}
      <p>{result}</p>  {/* Display the result from the server */}
    </div>
  );
}

export default TextBox;
