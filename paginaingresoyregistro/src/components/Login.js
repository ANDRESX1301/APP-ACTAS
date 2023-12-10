import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css'; // Importa tu archivo SaaS

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // Lógica para manejar la autenticación
    console.log(`Iniciar sesión con email: ${email} y contraseña: ${password}`);
  };

  return (
    <div>
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
