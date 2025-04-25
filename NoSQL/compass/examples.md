
> En la opción de find:

Consultar las peliculas de fantasia
```js
{genres: "Fantasy"}
```

Consultar peliculas por título:
```js
{ title: "The Blue Bird" }
```

Consultar peliculas por año:
```js
{ year: 1980 }
```

Buscar peliculas por director:
```js
{ directors: "Maurice Tourneur" }
```

Películas con IMDb mayor o igual a 6:
```js
{ "imdb.rating": { $gte: 6 } }
```

Películas lanzadas en un país:
```js
{ countries: "USA" }
```

Películas con un # de comentarios:
```js
{ num_mflix_comments: 0 }
```

Películas que su título tenga una palabra clave:
```js
{ title: /Bird/ }
```

Películas cuyo plot contenga una palabra clave:
```js
{ plot: /children/ }
```

Obtener todas las películas con una calificación de Tomato Meter mayor o igual a 60%:
```js
{ "tomatoes.viewer.meter": { $gte: 60 } }
```

Consultar todas las películas que al menos un premio:
```js
{ "tomatoes.viewer.meter": { $gte: 60 } }
```

> ## En otra parte

Analizar como modificar y eliminar un documento,
pero con nuestra base de datos "my_store".

> ## Hacer unas consultar en mongo shell.

En mongo shell las consultas deben ser completas:

Obtener los teatro de una ciudad: 
```js
db.theaters.find({ "location.address.city": "Bloomington" })
```

Limpiar consola: 
```js
cls
```

Buscar teatros cercanos a una ubicación específica:

_Consulta geoespacial: La consulta find con $near se utiliza para buscar documentos basados en su cercanía a un punto geográfico específico. Asegúrate de tener un índice geoespacial en el campo geo.coordinates para que funcione correctamente._
```js
db.theaters.find({
  "location.geo": {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [-93.24565, 44.85466]
      },
      $maxDistance: 10000  // 10 km
    }
  }
})
```

Buscar todos los teatros de un estado especifico:
```js
db.theaters.find({ "location.address.state": "MN" })
```

> ## Consultas especiales en la mongo shell:

Mostrar todas las bases de datos:
```js
show databases
```

Ajustar una base de datos:
```js
use("mi_base_datos")
```

Mostrar todas las colecciones: 
```js
show colleccionts
```