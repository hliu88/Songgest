import logo from './logo.svg';
import './App.css';
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import React, { useEffect, useState, Component } from 'react';
import axios from 'axios';

/*class App extends Component{
    constructor(props){
        super(props);
        this.state = {state: false, playlist: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event){
        this.setState({value: event.target.state});
    }
    
    handleSubmit(event){
        console.log('making requests')
        const apiURL = "http://songgest.herokuapp.com//"
        const [getMessage, setGetMessage] = {}
        axios.get(apiURL)
        .then(response=>{ setGetMessage(response.data);
        })
        .then(json=>{this.setState({state: response});})
        .catch((error)=>{
            console.log(error);
        });
    }
    
    render(){
        
      return (
        <div className="App">
              <h1>Songgest</h1>
              <h1>{this.state.state}</h1>
        </div>
      );
    }
}*/

function App() {
    
    const [getMessage, setGetMessage] = useState('')
    const [playlistID, setPlaylistID] = useState('')
    const apiURL = "http://songgest.herokuapp.com//"
    
    axios.get(apiURL).then((response)=>{ setGetMessage(response.data);
    }).catch((error)=>{
        console.log(error);
    });
    
    function validateForm(){
        return playlistID.length > 0;
    }
    
    setInterval((1000));
    
  return (

    <div className="Login">
          <Form.Group size="lg" controlId="playlistID"></Form.Group>
            <Form.Label>Playlist Link</Form.Label>
            <Form.Control
                autoFocus
                type = "email"
                value = {playlistID}
                onChange={(e)=>setPlaylistID(e.target.value)}>
            </Form.Control>
          <Button block size="lg" type="submit" disabled={!validateForm()}>
                    Login
                  </Button>
          <h1>{playlistID}</h1>
    </div>
          
          /*<div className="App">
                <h1>Songgest</h1>
                <h1>{getMessage.state}</h1>
          </div>*/
          
  );
    
}

export default App;

