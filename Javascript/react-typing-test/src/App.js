import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Tester from './Tester';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Tester sentence="The quick brown fox jumps over the lazy dog"/>
      </div>
    );
  }
}

export default App;
