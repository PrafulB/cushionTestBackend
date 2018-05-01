import React, { Component } from 'react';
import './App.css';
import TextHighlight from './TextHighlight';
import SearchBar from './SearchBar';
import { ButtonGroup, Button } from 'react-bootstrap';

const env = process.env.NODE_ENV || "development";
const config = require('./env.json')[env];

class App extends Component {

  constructor(props) {
    super(props);
    this.handleURL = this.handleURL.bind(this);

    this.state = {
      text: '',
      freqWords: [],
      highlightWord: ''
    }
  }

  handleURL(url) {
    const options = {
      method: 'POST',
      headers: 
      { 
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ 
        "url": url 
      })
    };
    
    fetch(config.apiBasePath + config.getDataEndpoint, options)
    .then((response) =>{
      return response.json()
    }).then((data) => {
      // console.log(data)
      this.setState({
        text: data.text,
        freqWords: data.wordFreqs,
      })
    }).catch((err) => {
      console.log(err);
    });
  }

  highlightWord(word) {
    this.setState({
      highlightWord: word
    });
  }

  render() {
    return (
      <div className="App">
        <div>
          <SearchBar
          handler={this.handleURL}
          />
        </div>
        <div>
          <ButtonGroup>
            {this.state.freqWords.map((word, i) => {
              console.log(word)
              return (
              <Button onClick={() => this.highlightWord(word.word)} key={i}>{word.word} : {word.freq}</Button>
              );
            })}
          </ButtonGroup>
        </div>
        <div className="text">
          <TextHighlight
          text={this.state.text}
          highlightWord={this.state.highlightWord}
          />
        </div>
      </div>
    );
  }
}

export default App;
