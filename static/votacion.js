//VOTACION HTML - REGISTRA EL VOTO AL BACKEND

async function registrarVoto(event) {
    event.preventDefault();  // Evitar el envío del formulario tradicional

    const voto = document.querySelector('input[name="voto"]:checked');  // Obtener el valor del voto seleccionado

    if (!voto) {
        alert("Por favor, selecciona una opción de votación.");
        return;
    }

    const response = await fetch('/RegistrarVoto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ voto: parseInt(voto.value) }),  // Enviar los datos como JSON
    });

    const result = await response.json();

    // Mostrar el mensaje en el modal
    const modal = document.getElementById("modal");
    const modalMessage = document.getElementById("modalMessage");
    const closeBtn = document.getElementById("closeBtn");
    const acceptBtn = document.getElementById("acceptBtn");

    if (response.ok) {
        modalMessage.textContent = result.mensaje;  // Mensaje de éxito
        modal.style.display = "block";  // Mostrar el modal
    } else {
        modalMessage.textContent = "Error: " + result.detail;  // Mensaje de error
        modal.style.display = "block";  // Mostrar el modal
    }

   

    // Cuando el usuario hace clic en "Aceptar", lo redirigimos a "/"
    acceptBtn.onclick = function () {
        window.location.href = "/";  // Redirige al usuario a home, el html de validacion
    }
}

document.querySelector('#votacionForm').addEventListener('submit', registrarVoto);  // Añadir el evento de submit



