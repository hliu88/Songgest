import logo from './logo.svg';
import './App.css';
import ButtonLoader from "./ButtonLoader/index"
import React from 'react';
// import {trackPromise} from 'react-promise-tracker';


// function App() {
//   return (
//     <div className="App">
//     </div>
//   );
// }

function fetchAPI(param) {
  // param is a highlighted word from the user before it clicked the button
  // return fetch("http://127.0.0.1:8000/importPlaylist/?param=" + param);
  return fetch("http://songgest.herokuapp.com/importPlaylist/https://open.spotify.com/playlist/37i9dQZF1DX3KoYiZJ8DD4?si=ec1f4d63c6bc49f5");
}

class App extends React.Component {
  state = { result: null };

  toggleButtonState = () => {
    let selectedWord = window.getSelection().toString();
    fetchAPI(selectedWord).then(result => {
      this.setState({ result });
    });
  };
  render() {
    return (
      <div>
        <button onClick={this.toggleButtonState}> Click me </button>
        <div>{this.state.result}</div>
      </div>
    );
  }
}


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }


export default App;
