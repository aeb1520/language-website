import React from 'react';
import Header from './components/Header';
import MainContent from './components/MainContent';
import './App.css';
import NavList from './components/NavList';
import TextBox from './components/TextBox';
import Dropdown from './components/Dropdown';

function App() {
  return (
    <div className="App">
      <Header />
      <NavList />
      <MainContent />
      <Dropdown />
      <TextBox />
    </div>
  );
}

export default App;
