import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Navbar from './components/Navbar'
import Home from './pages/Home'

function App() {
  return (
    <Router className="App">
        <Navbar></Navbar>
        <Switch>
          <Route path='/' exact >
              <Home></Home>
          </Route>
          
        </Switch>
    </Router>
  );
}

export default App;
