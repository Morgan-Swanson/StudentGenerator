import React from 'react';
import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';

class App extends Component {

  state = {
    contacts: []
  }
  componentDidMount() {
    fetch('/api/10')
    .then(res => res.json())
    .then((data) => {
      this.setState({ contacts: data })
    })
    .catch(console.log)
  }
}

export default App;
