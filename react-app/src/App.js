import React from 'react';
import Header from './components/Header';
import MainContent from './components/MainContent';
import './App.css';
import NavList from './components/NavList';
import TextBox from './components/TextBox';
import Dropdown from './components/Dropdown';
import StoryPage from './components/StoryPage';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <NavList />
        <MainContent />
        <Routes>
          <Route path="/" element={
            <>
              <Dropdown />
              <TextBox />
            </>
          } />
          <Route path="/story" element={<StoryPage />} />
          {/* Add other routes like /quiz as needed */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
