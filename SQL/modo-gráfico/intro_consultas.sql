SHOW DATABASES;

USE bd_python_abril;

SELECT *
FROM productos;

INSERT INTO productos(nombre,precio,existencias,categoria)
VALUES ('Boing',18.5,10,'Jugos');

SELECT nombre,precio
FROM productos;

SELECT nombre,precio
FROM productos
WHERE precio<=14.5;

SELECT nombre,precio
FROM productos
WHERE precio BETWEEN 15 AND 17;

SELECT nombre
FROM productos
WHERE existencias < 5;

SELECT *
FROM productos
WHERE categoria = "Chocolates";

SELECT *
FROM productos
ORDER BY precio DESC; /* ASC para ascendente */

SELECT *
FROM productos
ORDER BY categoria ASC;

/*cantidad no es una columna organica de productos*/
SELECT categoria, COUNT(*) AS cantidad
FROM productos
GROUP BY categoria
ORDER BY cantidad ASC;

-- Este otro tipo de comentario --
SELECT categoria, AVG(precio) AS promedio
FROM productos
GROUP BY categoria;

SELECT nombre, precio
FROM productos
WHERE categoria LIKE '%late%';

/* LAS SIGUIENTES CONSULTAS SON EQUIVALENTES */

SELECT nombre
FROM productos
WHERE categoria IN ('Jugos','Chocolates');

SELECT nombre
FROM productos
WHERE categoria = 'Jugos' OR categoria = 'Chocolates';

/* Aplicando una promoción del 10% de descuento a la categoría de jugos*/
SELECT nombre, precio, precio*0.9 AS precio_especial
FROM productos
WHERE categoria = 'Jugos' AND existencias > 5
ORDER BY nombre;

SELECT *
FROM productos
WHERE categoria NOT IN ('Jugos','Chocolates');

SELECT nombre
FROM productos
WHERE id IN (SELECT id FROM productos WHERE categoria = 'Jugos');