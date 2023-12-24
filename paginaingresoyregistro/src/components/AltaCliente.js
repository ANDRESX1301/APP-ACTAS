import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './Login.css';

const AltaCliente = () => {
  const [nombrersocial, setnombrersocial] = useState('');
  const [representante, setrepresentante] = useState('');
  const [recurso, setrecurso] = useState('');
  const [errorRecursoYaExiste, setErrorRecursoYaExiste] = useState('');
  const [exitoRegistro, setExitoRegistro] = useState('');
  // Obtén el estado de la ubicación que contiene la información del usuario
  const location = useLocation();
  const userData = location.state && location.state.userData;
  const navigate = useNavigate();
  useEffect(() => {
    // Lógica para verificar si userData está presente y si no, redirigir a la página de inicio
    if (!userData) {
      navigate('/');
    }
  }, [navigate, userData]);
  // Ejemplo en tu componente de AltaCliente.js
  const handleAltaCliente = async () => {


    try {
        const response = await fetch('http://localhost:5000/altacliente', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nombrersocial, representante, recurso}),
        });

        const data = await response.json();
        //console.log(data); //  Aqui con este console se imprime la respuest jsonfy de backend
        //Puedes manejar la respuesta del backend aquí
        if (data.success) {
          setErrorRecursoYaExiste(''); // Limpiar mensaje de error ya que fue exitoso
          setExitoRegistro('CLIENTE registrado con exito');
          
        } else {
          setExitoRegistro(''); // Limpiar mensaje de éxito ya que hubo un error
          setErrorRecursoYaExiste('Ya existe un Cliente con ese recurso');
        }
    } catch (error) {
        console.error('Error al realizar la solicitud:', error);
    }
  };

    const handleSubmit = (event) => {
      event.preventDefault();
      handleAltaCliente();
    };

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
    <div className='container'>
      <h2>Registrarse</h2>
      <form onSubmit={handleSubmit}> 
        <label>
          Nombre Razon Social:
          <input type="text" value={nombrersocial} onChange={(e) => setnombrersocial(e.target.value)} className='imput-field' />
        </label>
        <br />
        <label>
          Representante:
          <input type="text" value={representante} onChange={(e) => setrepresentante(e.target.value)} className='imput-field' />
        </label>
        <br />
        <label>
          Recurso:
          <input type="text" value={recurso} onChange={(e) => setrecurso(e.target.value)} className='imput-field' />
        </label>
        <br />
        <button type="submit"  className='login-button'>
          Registrarse
        </button>
        {errorRecursoYaExiste && <p style={{ color: 'red' }}>{errorRecursoYaExiste}</p>}
        {exitoRegistro && <p style={{ color: 'green' }}>{exitoRegistro}</p>}
      </form>
      <button onClick={handleLogout} className="logout-button">Cerrar Sesión</button>
    </div>
  );
};

export default AltaCliente;
