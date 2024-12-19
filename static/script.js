async function buscarusuarios() {
  const cedula = document.getElementById("cedula").value;
  const userInfo = document.getElementById("userInfo");
  const continuarButton = document.getElementById("continuarButton");

  // Resetear mensaje y botón antes de realizar la búsqueda
  userInfo.innerHTML = "";
  continuarButton.style.display = "none";

  try {
    const response = await fetch(`/BuscarUsuarios?cedula=${cedula}`);
    const data = await response.json();

    if (response.ok && data.success) {
      // Mostrar nombre del usuario
      userInfo.innerHTML = `BIENVENIDO/A ${data.nombre}`;

      // Mostrar botón si no ha votado
      if (!data.estado) {
        continuarButton.style.display = "block";
      } 
    } else {
      // Manejo de mensajes de error del servidor
      userInfo.innerHTML = data.message || "Error inesperado.";
    }
  } catch (error) {
    console.error("Error al buscar usuario:", error);
    userInfo.innerHTML = "Error al conectar con el servidor.";
  }
}

function redirigir() {
  window.location.href = "/votacion";
}


