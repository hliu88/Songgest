import React from 'react';
import {useState,useEffect} from 'react';
import './App.css';
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';



function App(){
  const [playlistURL, setPlaylistURL] = useState({
    value: '',
    loaded: false})    //value
  const [playlistURL_coded, setPlaylistURL_coded] = useState('')
  const [test,setTest] = useState('')
  const [impReturn, setImpReturn] = useState('')
  const [analyReturn, setAnalyReturn] = useState('')
  const [suggestReturn, setSuggestReturn] = useState('')
  // const [test,setTest] = useState({
  //   data: '',
  //   loading: true
  // })
  const [name,setName] = useState('')

  const handleClick = async() => {
    const data = await axios.get('/test')
    setTest({
        data: data.data.return,
        loading: false
    })
  }

  const Form = () => {
    const handleSubmit = (e) => {
      e.preventDefault();
      console.log(`Form submitted, ${playlistURL.value}`);    
      // setPlaylistURL({
      //   loaded: true
      // })
      console.log(encodeURIComponent(playlistURL.value))
    }

    return(
      <div>
        <h2>playlist URL</h2>
        <form onSubmit = {handleSubmit}>
            <input onChange = {(e) => setPlaylistURL({value:e.target.value})} value = {playlistURL.value}></input>
            <button type = 'submit'>Click to submit</button>
        </form>
        {encodeURIComponent(playlistURL.value)}
      </div>
    );
  }

  const postImport = async() => {
    // alert(encodeURIComponent(playlistURL.value))
    const data = await axios.post('/importPlaylist/' + encodeURIComponent(playlistURL.value))
    setImpReturn({
      loaded: true,
      data: data.data.return,
    })
  }

  const analyze = async() =>{
    if(impReturn.data == "playlist url invalid"){
      alert('invalid')
    }else{
      const data = await axios.put('/get_genre/' + encodeURIComponent(playlistURL.value))
      setAnalyReturn({
        loaded: true,
        data: data.data.return,
      })
    }
  }

  const suggest = async() =>{
    if(analyReturn.data == 'genres added'){
      const data = await axios.get('/suggest/' + encodeURIComponent(playlistURL.value))
      setSuggestReturn({
        loaded: true,
        data: data.data.return,
      })
    }
  }
  return (
    <div className="container">
        <h2>Get Test</h2>
        <button onClick = {handleClick}>Get Test</button>
        <div>
          {test.loading?'':
          test.data}
        </div>

        <div>
          {playlistURL.loaded?false:
          Form()}
        </div>
          
        <div>
          {playlistURL.loaded?true:
          <button onClick = {postImport}>Import playlist</button>}
          <h5>{impReturn.data}</h5>
        </div>

        <div>
          <button onClick = {analyze}>Analyze</button>
          <h5>{analyReturn.data}</h5>
        </div>

        <div>
          <button onClick = {suggest}>Suggest</button>
          <h5>{suggestReturn.data}</h5>
          
        </div>

    </div>
    
  );
}

export default App;