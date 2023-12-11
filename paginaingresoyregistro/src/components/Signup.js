import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css';

const Signup = () => {
  const [nombre, setnombre] = useState('');
  const [apellido, setapellido] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

/*  const handleSignup = () => {
    // Lógica para manejar el registro de usuario
    console.log(`Registrarse con Nombre: ${nombre}, Apellido: ${apellido}, Email: ${email} y Contraseña: ${password}`);
  };*/

  // Ejemplo en tu componente de Signup.js
    const handleSignup = async () => {
      try {
          const response = await fetch('http://localhost:5000/signup', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ nombre, apellido, email,password }),
          });

          const data = await response.json();
          console.log(data); // Puedes manejar la respuesta del backend aquí
      } catch (error) {
          console.error('Error al realizar la solicitud:', error);
      }
    };


  return (
    <div className='container'>
      <h2>Registrarse</h2>
      <form>
        <label>
          Nombre:
          <input type="text" value={nombre} onChange={(e) => setnombre(e.target.value)} className='imput-field' />
        </label>
        <br />
        <label>
          Apellido:
          <input type="text" value={apellido} onChange={(e) => setapellido(e.target.value)} className='imput-field' />
        </label>
        <br />
        <label>
          Correo Electrónico:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className='imput-field' />
        </label>
        <br />
        <label>
          Contraseña:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className='imput-field' />
        </label>
        <br />
        <button type="button" onClick={handleSignup} className='login-button'>
          Registrarse
        </button>
      </form>
      <p>
        ¿Ya tienes una cuenta? <Link to="/">Iniciar Sesión</Link>
      </p>
    </div>
  );
};

export default Signup;
