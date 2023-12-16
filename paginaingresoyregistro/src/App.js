import React from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import Home from './components/Home';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/Signup" element={<Signup />} />
        <Route path="/" element={<Login />} />  
        <Route path="/Home" element={<Home />} />      
      </Routes>
    </Router>
  );
}

export default App;
