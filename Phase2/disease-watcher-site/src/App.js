import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Navbar from './components/Navbar'
import Home from './pages/Home'
import Outbreaks from './pages/Outbreaks'
import Diseasepage from './pages/Diseasepage'
import Advice from './pages/advice'

function App() {
  return (
    <Router className="App" >
        <Navbar></Navbar>
        <Switch>
          <Route path='/' exact >
              <Diseasepage> </Diseasepage>
          </Route>
          <Route path='/outbreaks'>
              <Outbreaks></Outbreaks>
          </Route>
          <Route path='/diseasechart'>
            <Home></Home>
          </Route>
        </Switch>
    </Router>
  );
}

export default App;
