CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL, 
    precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

INSERT INTO clientes (nombre, email) VALUES 
('Dulce Ibarra', 'dulce.ibarra@gmail'),
('Lupita Medellin', 'lupita@gmail');

INSERT INTO productos (nombre, precio) VALUES 
('Coca Cola', 20.00),
('Pepsi', 18.00),
('Sabritas', 15.00),
('Doritos', 22.00);

INSERT INTO ventas (cliente_id, producto_id, cantidad) VALUES 
(1, 1, 2),
(1, 3, 1),
(2, 2, 1),
(2, 4, 3);