---


---

<h1 id="requisitos-de-la-aplicación-a-desarrollar">Requisitos de la aplicación a desarrollar</h1>
<p>A continuación se definen los requisitos de la aplicación web a desarrollar.<br>
Se quiere implementar un sistema de gestión de lugares para realizar conferencias, mediante el cual se pueda llevar a cabo la alta de un lugar para conferencias así como buscar una locación disponible, por ciudad, día y hora por parte de personas que necesiten un espacio.<br>
La aplicación consta de dos partes claramente diferenciadas. Una para personas que quieren publicar sus salas de conferencia y otra para personas que buscan un lugar.</p>
<h2 id="sistema-de-gestión-de-usuarios">Sistema de gestión de usuarios</h2>
<p>Es el mismo tanto para propietarios de lugares como conferenciantes.<br>
En este apartado se pueden realizar distintas acciones características de cualquier sistema de gestión de usuarios. Se pasa a comentar cada una de ellas:</p>
<h3 id="registro-de-usuarios">Registro de usuarios</h3>
<p>Se requerirán los siguientes campos para el registro de un nuevo usuario en la aplicación:</p>
<ul>
<li>Nombre</li>
<li>Apellidos.</li>
<li>Correo electrónico.</li>
<li>Fecha de nacimiento.</li>
<li>Foto de perfil.</li>
<li>Nombre de usuario</li>
<li>contraseña.</li>
</ul>
<h3 id="iniciar-sesión">Iniciar sesión</h3>
<p>Para el inicio de sesión se requerirá el nombre de usuario junto con su contraseña.</p>
<h3 id="cerrar-sesión">Cerrar sesión</h3>
<p>Es posible cerrarla cuando el usuario lo desee.</p>
<h3 id="cambio-de-contraseña">Cambio de contraseña</h3>
<p>Es posible que un usuario, previamente logueado en la aplicación, quiera cambiar la contraseña, lo cual es posible a través de un formulario en el que deberá de introducir la antigua contraseña y a continuación la nueva a almacenar.</p>
<h3 id="página-de-perfil-de-cliente">Página de perfil de cliente</h3>
<p>En la página de perfil del cliente se presentará diferente información relevante para el cliente como puede ser:</p>
<ul>
<li>Datos personales del usuario.</li>
<li>Foto de perfil del usuario si la subiera.</li>
<li>Listado de lugares de conferencia, separados por fecha de eventos que ya pasaron y futuros.</li>
</ul>
<h2 id="visión-de-salas-disponibles.">Visión de salas disponibles.</h2>
<p>Sin diferenciar si un ponente se ha registrado o no en la aplicación, es posible<br>
visualizar las distintas salas disponibles.<br>
En esta página, estarán disponibles filtros para las salas, pudiendo elegirlas por ciudad, nombre, tamaño, precio, y disponibilidad en cierta fecha.</p>
<h2 id="selección-de-una-sala-y-creación-de-evento.">Selección de una sala y creación de evento.</h2>
<p>De las distintas salas disponibles, es posible seleccionar una de ellas para ver datos como: el nombre, la dirección, tamaño, si dispone de personal de ayuda, espacios anexos libres, datos de interés. De forma opcional y si el locador ha subido fotos o vídeos, se podrán visualizar dentro de la propia página. A<br>
continuación, se mostrará un listado de los días o horas que estará libre la sala y una lista con los últimos comentarios de otros usuarios. Pudiendo en esta última zona realizar su propio comentario si se encuentra logueado en la aplicación en cuanto el evento haya terminado.</p>
<h1 id="en-cuanto-a-la-parte-de-administración-de-espacios">En cuanto a la parte de administración de espacios</h1>
<p>En esta parte cabe mencionar que no todos los usuarios registrados en la aplicación tendrán acceso. Solo tendrán permisos los se den de alta como propietarios de una sala. Estos usuarios propietarios podrán:</p>
<h2 id="añadir-modificar-y-eliminar-salas">Añadir, modificar y eliminar salas</h2>
<p>Tienen la posibilidad de gestionar las salas pudiendo crearlas, modificarlas o incluso eliminarlas. Para dar de alta una sala, se pedirán los siguientes campos en el formulario:</p>
<ul>
<li>Nombre.</li>
<li>Ubicación.</li>
<li>Dirección.</li>
<li>Tamaño (filas y asientos o cantidad).</li>
<li>Precio por hora.</li>
<li>Para modificarlas y eliminarlas, las salas serán elegidas de una lista.</li>
</ul>
<h2 id="visualizar-y-responder-los-comentarios-sobre-las-salas.">Visualizar y responder los comentarios sobre las salas.</h2>
<p>Otra opción disponible será la de visualizar todos los comentarios sobre una sala junto con su autor. No pudiendo en ningún caso modificarlos. Solo reportarlos para ser revisado por un administrador.</p>
<h2 id="administradores">Administradores</h2>
<p>Existirá un super administrador que podrá designar a otros administradores. Estos tendrán la capacidades habituales de un administrador. Podrán eliminar u ocultar usuarios salas así como comentarios. Así como restringir el acceso a usuarios.</p>
<h1 id="implementación-de-la-aplicación">Implementación de la aplicación</h1>
<p>El proceso de implementación de la aplicación se desarrolla siguiendo los requisitos recogidos en el apartado anterior anterior.</p>
<ul>
<li>Diseño de la interacción de los usuarios con la aplicación.</li>
<li>Diseño de la BBDD.</li>
<li>Levantar el sitio de administración de Django.</li>
<li>Desarrollo del modelado de la aplicación.</li>
<li>Desarrollo de los formularios que se usarán las vistas para recoger los datos.</li>
<li>Implementación de las funciones de vista que se van a utilizar</li>
<li>Configuración del URLconf.</li>
<li>Implementación de las plantillas que se mostrarán a los usuario de la aplicación.</li>
<li>Aplicación de diseño y estilo mediante bootstrap, así como diseño de logo y otros detalles.</li>
</ul>
<blockquote>
<p>Nota: Se utilizará Django 1.11 (LTS), Python 3.5.4 y como base de datos SQlite3.<br>
Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>

