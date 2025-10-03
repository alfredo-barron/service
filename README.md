# API REST de Clientes, Productos y Ventas

Este proyecto implementa un **servicio REST** con Flask que maneja clientes, productos y ventas.  
Los datos se almacenan en **MySQL** dentro de un contenedor Docker.  

## 🚀 Requisitos previos

- Python 3.9+  
- Docker y Docker Compose  

---

## 🔧 Configuración del entorno virtual

Clona el repositorio y entra al proyecto:

```bash
git clone https://github.com/alfredo-barron/service.git
cd service
```

Crear y activar entorno virtual:

```bash
python3 -m venv entorno-ia
source entorno-ia/bin/activate   # Linux/Mac
entorno-ia\Scripts\activate      # Windows
```

## Despliegue con Docker Compose

Levantar los servicios:

```bash
docker-compose up -d --build
```

Esto iniciará:

- **API Flask** en http://localhost:8080/api 
- **MySQL**

Ver logs en tiempo real:

```bash
docker-compose logs -f
```

Detener los contenedoras_

```bash
docker-compose down
```

## Endpoints principales
- **Clientes**
    - GET /clientes &rarr; lista todos
    - GET /clientes/<id> &rarr; obtiene por ID
    - POST /clientes &rarr; crea un cliente
    - PUT /clientes/<id> &rarr; actualiza un cliente
    - DELETE /clientes/<id> &rarr; elimina un cliente
- **Productos** (Realizar los siguientes)
    - GET /productos
    - GET /productos/<id>
    - POST /productos
    - PUT /productos
    - DELETE /productos
- **Ventas** (Realizar los siguientes)
    - GET /ventas
    - GET /ventas/<id>
    - POST /ventas
    - PUT /ventas
    - DELETE /ventas

## Probar la API

Ejemplo con **curl**:

```bash
curl -X POST http://localhost:8080/clientes \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Alfredo Barrón", "correo": "alfredo.barron@ejemplo.com"}'
```