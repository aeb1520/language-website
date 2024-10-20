import React from 'react';
import Header from './components/Header';
import MainContent from './components/MainContent';
import './App.css';
import NavList from './components/NavList';
import TextBox from './components/TextBox';
import Dropdown from './components/Dropdown';
import StoryPage from './components/StoryPage';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MyComponent from './components/MyComponent';
import LevelSelect from './components/LevelSelect';
import StoryGenerator from './components/StoryGenerator';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <MainContent />
        <LevelSelect />
        <Dropdown />
        <TextBox />  {/* Move this outside the Routes if needed on all pages */}
        <Routes>
        </Routes>
        <MyComponent />
        <StoryGenerator />
      </div>
    </Router>
  );
}

export default App;

/*
function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <MainContent />
        <Routes>
          <Route path="/" element={
            <>
              <Dropdown />
              <TextBox />
            </>
          } />
          <Route path="/story" element={<StoryPage />} />
        </Routes>
        <MyComponent />
        <StoryGenerator />
      </div>
    </Router>
  );
}
  */

//export default App;
