// Home.js
import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const Home = () => {
  // Obtén el estado de la ubicación que contiene la información del usuario
  const location = useLocation();
  const userData = location.state && location.state.userData;
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await fetch('http://localhost:5000/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      const data = await response.json();

      if (data.success) {
        // Redirigir al usuario a la página de inicio de sesión después de cerrar sesión
        navigate('/');
      } else {
        console.error('Error al cerrar sesión:', data.message);
      }
    } catch (error) {
      console.error('Error al realizar la solicitud:', error);
    }
  };

  return (
    <div>
      <h1>Bienvenido, has iniciado sesión correctamente</h1>
      {userData && (
        <div>
          <p>Email: {userData.email}</p>
          <p>Nombre: {userData.nombre}</p>
          <p>Apellido: {userData.apellido}</p>
        </div>
      )}
       <button onClick={handleLogout}>Cerrar Sesión</button>
    </div>
  );
};

export default Home;
