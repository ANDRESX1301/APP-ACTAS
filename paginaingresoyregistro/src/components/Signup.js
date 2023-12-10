import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Signup = () => {
  const [nombre, setnombre] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSignup = () => {
    // Lógica para manejar el registro de usuario
    console.log(`Registrarse con Nombre: ${nombre}, Apellido: ${lastName}, Email: ${email} y Contraseña: ${password}`);
  };

  return (
    <div>
      <h2>Registrarse</h2>
      <form>
        <label>
          NombreA:
          <input type="text" value={nombre} onChange={(e) => setnombre(e.target.value)} />
        </label>
        <br />
        <label>
          Apellido:
          <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} />
        </label>
        <br />
        <label>
          Correo Electrónico:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <label>
          Contraseña:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <br />
        <button type="button" onClick={handleSignup}>
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
