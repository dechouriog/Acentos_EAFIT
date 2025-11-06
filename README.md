# Proyecto Librería Acentos

Este proyecto está desarrollado en **FastAPI** y sigue una arquitectura organizada en carpetas para controladores, rutas, modelos y utilidades.  
Incluye autenticación de usuarios, manejo de libros y páginas básicas (login, registro, home).

---

##  Estructura del proyecto

- **controllers/** → Lógica de negocio  
  - `books_controller.py`  
  - `home_controller.py`  
  - `login_controller.py`  
  - `register_controller.py`  

- **db/** → Configuración de la base de datos  
  - `config.py`  

- **models/** → Modelos de datos  
  - `books.py`  
  - `users.py`  

- **routes/** → Definición de rutas  
  - `books_routes.py`  
  - `home_routes.py`  
  - `login_routes.py`  
  - `register_routes.py`  

- **static/** → Archivos estáticos (CSS)  
  - `styles.css`  

- **utils/** → Utilidades (ej: autenticación)  
  - `auth.py`  

- **views/** → Plantillas HTML (Jinja2)  
  - `base.html`  
  - `home.html`  
  - `login.html`  
  - `register.html`  

- **main.py** → Punto de entrada de la aplicación  
- **requirements.txt** → Dependencias del proyecto  


---

## Instalacion y ejecucion

1) Clonar repositorio  git clone <https://github.com/dechouriog/Acentos_EAFIT>

2) instalar dependencias / pip install -r requirements.txt

3) ejecutar servidor / uvicorn main:app --reload



