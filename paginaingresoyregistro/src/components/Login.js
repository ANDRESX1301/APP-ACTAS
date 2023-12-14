import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Login.css'; // Importa tu archivo SaaS

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  // Usa 'useNavigate' para obtener el objeto 'history'
  const navigate = useNavigate();
/*
  const handleLogin = () => {
    // Lógica para manejar la autenticación
    console.log(`Iniciar sesión con email: ${email} y contraseña: ${password}`);
  };
*/

const handleLogin = async () => {
  try {
      const response = await fetch('http://localhost:5000/login', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, password }),
      });

        // Si es JSON, analizar la respuesta como JSON
        const data = await response.json();

        if (data.success) {
          // Redirigir al usuario a la página deseada después del inicio de sesión exitoso
          navigate('/home', { state: { userData: data.data } });
        } else {
          console.error('Credenciales incorrectas');
        }
  } catch (error) {
      console.error('Error al realizar la solicitud:', error);
  }
};


  return (
    <div className='container'>
      <h2>Iniciar Sesión</h2>
      <form>
        <label>
          Correo Electrónico:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="input-field" // Agrega una clase para los estilos
          />
        </label>
        <br />
        <label>
          Contraseña:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="input-field" // Agrega una clase para los estilos
          />
        </label>
        <br />
        <button type="button" onClick={handleLogin} className="login-button">
          Iniciar Sesión
        </button>
      </form>
      <p>
        ¿No tienes una cuenta? <Link to="/signup">Registrarse</Link>
      </p>
    </div>
  );
};

export default Login;
