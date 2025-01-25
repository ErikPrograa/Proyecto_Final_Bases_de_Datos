# Sistema de Gestión de Bases de Datos para MMORPG

Este proyecto implementa un sistema integral de gestión de bases de datos para un juego de rol multijugador masivo en línea (MMORPG). El sistema integra Python y MySQL para gestionar diversas entidades y funcionalidades.

## Características

- **Gestión de Base de Datos**: Estructura y relaciones definidas para entidades críticas del juego como usuarios, personajes, objetos, misiones y más.
- **Operaciones CRUD**: Implementación de funcionalidades de Crear, Leer, Actualizar, Eliminar para todas las tablas.
- **Autenticación de Usuarios**: Incluye un sistema de inicio de sesión para la verificación de usuarios.
- **Integración con Python**: Scripts en Python manejan las interacciones con la base de datos MySQL.

---

## Comenzando

### Requisitos Previos

- Python 3.x
- Servidor MySQL
- Conector MySQL para Python


---

## Esquema de la Base de Datos

La base de datos contiene las siguientes tablas:

1. **Usuarios**: Almacena información de los usuarios.
2. **Personajes**: Representa los personajes controlados por los jugadores.
3. **Objetos**: Detalles sobre los objetos del juego.
4. **Misiones**: Tareas asignadas a los jugadores.
5. **Logros**: Hitos y recompensas para los jugadores.
6. **Inventario**: Rastrea los objetos poseídos por los personajes.
7. **Gremios**: Grupos creados por los jugadores para colaborar.
8. **Clasificaciones**: Información de tablas de clasificación.
9. **Mascotas**: Compañeros poseídos por los personajes.
10. **Casas**: Viviendas en el juego para los personajes.
11. **Zonas y Mapas**: Divisiones geográficas en el juego.
12. **Enemigos**: NPC enemigos que encuentran los jugadores.
13. **Intercambios**: Intercambio de objetos entre jugadores.
14. **Relaciones**: Conexiones sociales entre usuarios.
15. **Eventos**: Eventos especiales con duración limitada en el juego.
16. **Habilidades y Encantamientos**: Habilidades y mejoras para personajes y objetos.

---

## Operaciones CRUD

Las operaciones CRUD están implementadas para todas las entidades principales. Ejemplos:

### Tabla de Usuarios
- **Crear**: Agrega un nuevo usuario.
- **Leer**: Muestra los datos de los usuarios.
- **Actualizar**: Modifica la información existente de un usuario.
- **Eliminar**: Elimina un usuario.

### Tabla de Personajes
Operaciones CRUD similares permiten gestionar los personajes de los jugadores.

La funcionalidad CRUD detallada para todas las tablas está incluida en los scripts de Python.

---

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python
- **Base de Datos**: MySQL
- **Bibliotecas**: `mysql-connector-python`

---

## Estructura del Proyecto

- `app.py`: Contiene los scripts en Python para las operaciones de la base de datos.
- `Mysql_Tablas_BDDMMORPG.sql`: Script SQL para crear el esquema de la base de datos.

---




## Créditos
Proyecto desarrollado por Erik en enero de 2025.




