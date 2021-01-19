import React from 'react'
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'
import axios from 'axios'

const BASE_URI = 'http://localhost:5000'

function App() {
    const client = axios.create({
        baseURL: BASE_URI,
        json: true
    })

    
    
    return (
        <Router>        
            <Switch>
                <Route exact path="/" component
            </Switch>
        </Router>
    );
}

export default App;
