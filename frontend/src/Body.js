import React from 'react';
import {useState,useEffect} from 'react';
import './Body.css';
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';



function Body(){
  const [playlistURL, setPlaylistURL] = useState({
    value: '',
    submitted: false,
    loaded: false})
  const[URL, setURL] = useState([]);
  const [impReturn, setImpReturn] = useState({
    value: '',
    loaded: false})
  const [analyReturn, setAnalyReturn] = useState({
    value: '',
    loaded: false})
  const [suggestReturn, setSuggestReturn] = useState({
    value: '',
    loaded: false,
    print: false,
  })

  const Form = () => {
    const handleSubmit = (e) => {
      e.preventDefault();
      setPlaylistURL({submitted:true})
      setURL(playlistURL.value)
      console.log(`Form submitted, ${playlistURL.value}`);    
      console.log(encodeURIComponent(playlistURL.value))
    }

    return(
      <div>
        <h2>Enter playlist URL</h2>
        <form onSubmit = {handleSubmit}>
            <input onChange = {(e) => setPlaylistURL({value:e.target.value})} value = {playlistURL.value}></input>
            <button type = 'submit'>Click to submit</button>
        </form>
        {/* {encodeURIComponent(playlistURL.value)} */}
      </div>
    );
  }

  const logOut = () =>{
    setPlaylistURL({
      loaded: null,
      data: null,
    })
    setURL(null)
  }

  const postImport = async() => {
    const data = await axios.post('/importPlaylist/' + encodeURIComponent(URL))
    setImpReturn({
      loaded: true,
      data: data.data.return,
    })
    if(impReturn.data === "playlist url invalid"){
      alert('invalid url, press logout and try again')
    }
    else{
      const data = await axios.put('/get_genre/' + encodeURIComponent(URL))
      setAnalyReturn({
        loaded: true,
        data: data.data.return,
      })
    }
  }

  const suggest = async() =>{
    setSuggestReturn({
      loaded:true,
    })
    if(analyReturn.data === 'genres added'){
      const data = await axios.get('/suggest/' + encodeURIComponent(URL))
      setSuggestReturn({
        loaded: true,
        print: true,
        data: data.data.return,
      })
    }
  }

  return (
    <div className="Body">
      <div style={{ display: "flex" }}>
        <button onClick = {logOut} style={{ marginLeft: "auto" }}>Logout</button >
      </div>

        {playlistURL.submitted?'':Form()}
        
        {playlistURL.submitted && !impReturn.loaded?
          <div>
            <h2>Import Playlist</h2>
            <button onClick = {postImport}>Import</button>
          </div>
        :''}

        {suggestReturn.data?'':
          <h5>{analyReturn.data}</h5>
        }
        {analyReturn.loaded && !suggestReturn.loaded?<button onClick = {suggest}>Suggest</button>:''}
        {suggestReturn.print?
        <a href={suggestReturn.data.slice(2,-2)} target="_blank" rel="noopener noreferrer">Suggested Playlist URL: {suggestReturn.data.slice(2,-2)}</a>:''}
    </div>
    
  );
}

export default Body;