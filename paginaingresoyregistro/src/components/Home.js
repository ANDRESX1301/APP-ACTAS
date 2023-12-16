// Home.js
import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './botones.css';
import './sessionp.css';

const Home = () => {
  // Obtén el estado de la ubicación que contiene la información del usuario
  const location = useLocation();
  const userData = location.state && location.state.userData;
  const navigate = useNavigate();
  const [opciones, setOpciones] = useState([]);

  useEffect(() => {
    // Lógica para verificar si userData está presente y si no, redirigir a la página de inicio
    if (!userData) {
      navigate('/');
    }
  
    const obtenerOpciones = async () => {
      try {
        const response = await fetch('http://localhost:5000/opciones', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
        const data = await response.json();
  
        if (data.success) {
          setOpciones(data.opciones);
        } else {
          console.error('Error al obtener opciones:', data.message);
        }
      } catch (error) {
        console.error('Error al realizar la solicitud:', error);
      }
    };
  
    obtenerOpciones(); // Llama a la función para obtener las opciones al cargar el componente
  }, [navigate, userData]);

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
      {/* Lado izquierdo con opcioes */}
      <div className="sidebar">
        <h2>Opciones</h2>
        <button className="flag-button">{userData?.email}</button>
        <button className="flag-button">{userData?.email}</button>
        {/* Agrega más botones según sea necesario */}
        <ul>
          {opciones?.map((opcion, index) => (
            <li key={index}>
              {Object.keys(opcion).map((clave, subIndex) => (
                <div key={subIndex}>
                  <strong>{clave}:</strong> {opcion[clave]}
                </div>
              ))}
            </li>
          ))}
        </ul>
      
        <button onClick={handleLogout} className="logout-button">Cerrar Sesión</button>
      </div>
    </div>
  );
    
};

export default Home;
