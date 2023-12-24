import React from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import Home from './components/Home';
import AltaCliente from './components/AltaCliente';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/Signup" element={<Signup />} />
        <Route path="/" element={<Login />} />  
        <Route path="/Home" element={<Home />} /> 
        <Route path="/AltaCliente" element={<AltaCliente />} />      
      </Routes>
    </Router>
  );
}

export default App;
