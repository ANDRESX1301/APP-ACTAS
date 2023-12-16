import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css';

const Signup = () => {
  const [nombre, setnombre] = useState('');
  const [apellido, setapellido] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorEmail, setErrorEmail] = useState('');
  const [errorPassword, setErrorPassword] = useState('');

/*  const handleSignup = () => {
    // Lógica para manejar el registro de usuario
    console.log(`Registrarse con Nombre: ${nombre}, Apellido: ${apellido}, Email: ${email} y Contraseña: ${password}`);
  };*/

  // Ejemplo en tu componente de Signup.js
    const handleSignup = async () => {
      // Validar el formato del correo electrónico
      const formatoValido = /^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$/.test(email);

      if (!formatoValido) {
        setErrorEmail('El formato del correo electrónico no es válido el formato debe ser abc@def.com');
        return;
      } else {
        setErrorEmail('');
      }

      // Validar la contraseña
      const formatoContraseñaValido = /^(?=.*[A-Z])(?=.*\d).{8,}$/.test(password);

      if (!formatoContraseñaValido) {
        setErrorPassword('La contraseña debe contener al menos una mayúscula, un número y ser de al menos 8 caracteres');
        return;
      } else {
        setErrorPassword('');
      }
      // Si llegamos aquí, el formato del correo electrónico y la contraseña son válidos
      try {
          const response = await fetch('http://localhost:5000/signup', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ nombre, apellido, email, password }),
          });

          const data = await response.json();
          console.log(data); // Puedes manejar la respuesta del backend aquí
      } catch (error) {
          console.error('Error al realizar la solicitud:', error);
      }
    };

    const handleSubmit = (event) => {
      event.preventDefault();
      handleSignup();
    };
  

  return (
    <div className='container'>
      <h2>Registrarse</h2>
      <form onSubmit={handleSubmit}> 
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
          {errorEmail && <p style={{ color: 'red' }}>{errorEmail}</p>}
        </label>
        <br />
        <label>
          Contraseña:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className='imput-field' />
          {errorPassword && <p style={{ color: 'red' }}>{errorPassword}</p>}        
        </label>
        <br />
        <button type="submit"  className='login-button'>
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
