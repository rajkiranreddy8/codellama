import React, { useState } from 'react';
import axios from 'axios';
import './app.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [timeComplexity, setTimeComplexity] = useState('');
  const [language, setLanguage] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');

  const handleGenerateCode = async () => {
    try {
      const result = await axios.post('http://localhost:5000/generate', {
        input_text: inputText,
        timeComplexity: timeComplexity,
        language: language,
      });
      setResponse(result.data.response);
    } catch (error) {
      setError('Failed to generate code. Please try again.');
    }
  };

  return (
    <div className="container">
      <h1>Code Generator</h1>

      <div className="input-group">
        <label>Description</label>
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Enter the task description"
        />
      </div>

      <div className="input-group">
        <label>Time Complexity</label>
        <input
          type="text"
          value={timeComplexity}
          onChange={(e) => setTimeComplexity(e.target.value)}
          placeholder="Enter time complexity"
        />
      </div>

      <div className="input-group">
        <label>Programming Language</label>
        <input
          type="text"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
          placeholder="Enter programming language"
        />
      </div>

      <button onClick={handleGenerateCode}>Generate Code</button>

      {error && <p className="error">{error}</p>}

      <div className="output">
        <h2>Generated Code</h2>
        <pre>{response}</pre>
      </div>
    </div>
  );
}

export default App;