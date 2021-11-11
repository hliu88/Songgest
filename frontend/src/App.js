import React from 'react';
import ReactDOM from 'react-dom';
import logo from './logo.svg';
import './App.css';
const state = 0;
let page;
page = <p>hi</p>

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
// function App(){
//   if(state === 0){
//     page = <p>...</p>
//   }
// }
// return = this.App

// ReactDOM.render(
//   {App},
//   document.getElementById('root')
// );
class App extends React.Component {

  constructor(props) {
     super(props);

     this.state = {
        playlistURL: null,
        playlistURL_coded: null,
        submitted: null,
     }
     this.handleChange = this.handleChange.bind(this);
     this.handleSubmit = this.handleSubmit.bind(this);
     this.updateState = this.updateState.bind(this);
  };
  getURL(){
    return this.state.playlistURL
  }
  updateState() {
     this.setState({data: 'Data updated...'})
  }
  handleChange(event) {    this.setState({playlistURL: event.target.value});  }
  handleSubmit(event) {
    this.setState({playlistURL: event.target.value})
    this.setState({submitted: true})
  }

  //encodeURIComponent(this.state.playlistURL).replace(':', '%3A').replace('/', '%2F')

  // useEffect(url){
  //   fetch("http://127.0.0.1:8000/importPlaylist/" + url)
  //   .then(response => response.json()
  //   .then(data => {
  //     console.log(data)
  //   })
  // )}

  renderFunc(){
    if(this.state.submitted === null){
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            Import Playlist:
            <input type="text" value={this.state.playlistURL} onChange={this.handleChange} />        
          </label>
          <input type="submit" value="Submit" />
        </form>
      );
    }
    if(this.state.submitted && this.state.playlistURL !== null){
      // const temp = this.encodeURIComponent(this.state.playlistURL).replace(':', '%3A').replace('/', '%2F').bind(this)
    // //   alert(this.getURL())
    // //   // return(
    // //   //   //make api call
    // //   //     alert(temp)
    // //   // );
    }
  }
  // this.useEffect(encodeURIComponent(this.state.playlistURL).replace(':', '%3A').replace('/', '%2F'))

  render() {
    return (
      <div>
        {this.renderFunc()}
      </div>
    );
  }
  // render() {
  //    return (
  //       <div>
  //         <form>
  //         <label>
  //           Name:
  //           <input type="text" name="name" />
  //         </label>
  //         <input type="submit" value="Submit" />
  //         </form>


  //          <button onClick = {this.updateState}>CLICK</button>
  //          <h4>{this.state.data}</h4>
  //       </div>
  //    );
  // }
}
export default App;