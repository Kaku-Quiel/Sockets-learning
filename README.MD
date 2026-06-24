# Aprendizaje de Sockets

Este proyecto recopila varios ejercicios y tareas de práctica con sockets en Python. Incluye ejemplos básicos de cliente/servidor, un sistema de transferencia de archivos por red, y una tarea de calculadora remota. Además, contiene materiales de un proyecto avanzado con WebSockets para un sistema de pedidos.

---

## Estructura del repositorio

- `tasks/syntax/`
  - `Socket.py`: clase de ayuda para crear sockets TCP, aceptar conexiones y enviar/recibir mensajes en texto plano.
  - `server.py`: servidor básico que escucha conexiones TCP en `0.0.0.0:5000`, acepta un cliente y procesa mensajes JSON.
  - `client.py`: cliente que se conecta al servidor, envía mensajes JSON con información básica y muestra la respuesta.

- `tasks/review/`
  - `instrucciones.html`: tarea avanzada de protocolo de transferencia de archivos con sockets puros en Python. Explica cómo implementar comandos como `listar`, `subir`, `descargar` y `salir`, usando metadatos y transferencia en bloques.

- `tasks/test/`
  - `instrucciones.html`: tarea de calculadora remota que describe un cliente/servidor simple donde el cliente envía operaciones matemáticas y el servidor devuelve el resultado.

---

## Contenido de cada carpeta

### `tasks/syntax/`
Este conjunto muestra un ejemplo práctico de sockets TCP en Python:

- `Socket.py` define métodos para:
  - crear un servidor TCP y asociarlo a una IP/puerto,
  - aceptar conexiones,
  - crear un cliente TCP,
  - enviar (`msgSend`) y recibir (`msgRcv`) cadenas UTF-8.

- `server.py` utiliza `Socket.socketServer` y `Socket.socketAccept` para recibir una conexión y procesar mensajes JSON.
- `client.py` crea un cliente TCP, se conecta al servidor y envía mensajes JSON con un objeto que contiene `nombre`, `id`, `estado` y `mensaje`.

Este ejemplo es útil para entender cómo funcionan:

- sockets TCP en modo cliente/servidor,
- codificación y decodificación de JSON sobre la red,
- ciclo de envío/recepción de mensajes.

### `tasks/review/`
La instrucción describe un ejercicio avanzado de transferencia de archivos que enseña:

- cómo enviar y recibir archivos usando sockets puros sin hilos,
- la importancia de un protocolo de aplicación claro: metadatos + bloques binarios,
- comandos específicos (`listar`, `subir`, `descargar`, `salir`),
- manejo de errores cuando el archivo no existe,
- lectura y escritura en modo binario (`rb`, `wb`),
- la diferencia entre `send()` y `sendall()`,
- la construcción de una carpeta local para archivos del cliente y otra para archivos del servidor.

### `tasks/test/`
Este ejercicio se enfoca en:

- crear un servidor de calculadora remota,
- parsear operaciones matemáticas simples recibidas como texto,
- dar soporte a los operadores `+`, `-`, `*` y `/`,
- enviar resultados o mensajes de error al cliente,
- cerrar la conexión correctamente cuando el usuario escribe `salir`.

Aquí se practica el uso de sockets con comunicación textual y el diseño de un protocolo sencillo para intercambio de comandos.

---

## Temas principales que se estudian

- Programación de sockets TCP en Python.
- Arquitectura cliente/servidor.
- Envío y recepción de datos textuales y binarios.
- Construcción de protocolos de comunicación propios.
- Uso básico de JSON para mensajes.
- Implementación de tareas específicas: calculadora remota y transferencia de archivos.
- Conceptos avanzados del proyecto `job/`: WebSockets, APIs REST, autenticación, base de datos y frontend.

---

## Cómo utilizar este repositorio

1. Abre el archivo `README.MD` para tener una visión rápida.
2. Lee `tasks/syntax/Socket.py`, `tasks/syntax/server.py` y `tasks/syntax/client.py` para entender el flujo básico.
3. Revisa `tasks/test/instrucciones.html` para el ejercicio de la calculadora remota.
4. Revisa `tasks/review/instrucciones.html` para la tarea de transferencia de archivos.
5. Consulta `job/instrucciones.html` si quieres un caso real más completo y conectado con un sistema de pedidos en tiempo real.

---

## Recomendación de estudio

- Comienza por `tasks/syntax/` para dominar la comunicación básica.
- Avanza a `tasks/test/` para practicar comandos y parseo de operaciones.
- Luego estudia `tasks/review/` para aprender transferencia de archivos y protocolos más robustos.
- Finalmente, analiza `job/instrucciones.html` para ver cómo aplicar sockets y WebSockets en un proyecto más grande.

---

## Notas finales

Este repositorio es una colección de ejercicios progresivos: desde ejemplos simples hasta tareas más complejas. El objetivo es aprender paso a paso cómo funcionan las conexiones de red en Python y cómo diseñar sistemas que intercambian datos entre cliente y servidor.
