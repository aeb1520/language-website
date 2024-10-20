import React, { useState } from 'react';
import './TextBox.css';
 
function TextBox() {
  const [text, setText] = useState('');
  // for putting the output text in the same text field:
  const [result, setResult] = useState('');  // State to hold the result

  const handleChange = (event) => {
    setText(event.target.value);
  };

  const handleSubmit = async () => {
    const response = await fetch('http://localhost:5000/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    console.log(data);
    // also for outputting python text to the website:
    setResult(data.result);  // Set the result from the response
  };

  return (
    <div>
      <textarea 
        className="input-box" 
        placeholder="Enter your vocab list..."
        value={text}
        onChange={handleChange}
      />
      <button onClick={handleSubmit}>Submit</button>
      {result && <p>Result: {result}</p>}  {/* Display the result */} 
    </div>
    // last piece (line 3 of 3) for outputting python text is the {result} line under the button stuff (I can't comment there)
  );
}

export default TextBox;



// extra comment so I can commit the changes