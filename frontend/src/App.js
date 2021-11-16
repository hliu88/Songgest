import React from 'react';
import './App.css';

class App extends React.Component {

  constructor(props) {
     super(props);

     this.state = {
        playlistURL: null,
        playlistURL_coded: null,
        submitted: null,
        postId: null,
        initialGet: null,
     }
     this.handleChange = this.handleChange.bind(this);
     this.handleSubmit = this.handleSubmit.bind(this);
     this.updateState = this.updateState.bind(this);
  };

  async componentDidMount() {
      const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
          // body: JSON.stringify({ title: 'React POST Request Example' })
      };
      const response = await fetch('http://127.0.0.1:8000/suggest/' + this.state.playlistURL_coded, requestOptions);
      const data = await response.json();
      this.setState({ postId: data.return });
      alert(this.state.postId)
  }


  getURL(){
    return this.state.playlistURL
  }

  updateState() {
     this.setState({data: 'Data updated...'})
  }

  handleChange(event) {    
    this.setState({playlistURL: event.target.value,
                   playlistURL_coded: encodeURIComponent(this.state.playlistURL)
                  });  
  }

  handleSubmit(event) {
    this.setState({submitted: true})
  }

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
    if(this.state.submitted && this.state.playlistURL !== null && this.state.initialGet === null){
      // this.componentDidMount()
      // this.setState({initialGet: true})
      // alert(this.state.postId)
    }
  }

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