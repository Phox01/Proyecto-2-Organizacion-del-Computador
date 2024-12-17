# Proyecto-2-Organizacion-del-Computador

# Registro de Obras de Arte para la Galería de Arte Nacional

## 1. Descripción del Programa
Este programa implementa un sistema para registrar, gestionar y consultar las obras de arte de la Galería de Arte Nacional, ubicada en el centro de la ciudad. El objetivo principal es administrar la información de las pinturas y sus estados, cumpliendo con las siguientes especificaciones.

---

## 2. Estructura de la Base de Datos
### 2.1. Información Registrada por Pintura
1. **Cota**: Código único que identifica cada pintura, compuesto por 4 letras seguidas de 4 dígitos (por ejemplo: ABCD1234).
2. **Nombre**: Nombre de la pintura, limitado a una palabra de máximo 10 caracteres (ejemplo: "ATARDECER" o "NARANJAL"). No puede haber nombres duplicados.
3. **Precio**: Valor estimado de la obra, representado como un número real no negativo.
4. **Año**: Año de creación de la pintura.
5. **Estado**: Condición actual de la pintura, que puede ser:
   - "EN EXHIBICIÓN"
   - "EN MANTENIMIENTO"

---

## 3. Operaciones Disponibles

### 3.1. Inserción de una Nueva Pintura
Permite registrar una nueva pintura en la base de datos, verificando las condiciones para cada campo:
- La **Cota** debe ser única.
- El **Nombre** no debe repetirse.
- El **Precio** debe ser mayor o igual a cero.

### 3.2. Consulta de una Pintura
Permite buscar una pintura registrada por:
- **Cota**: Utilizando un índice basado en este campo.
- **Nombre**: Utilizando un índice basado en este campo.

### 3.3. Puesta en Mantenimiento
Cambia el estado de una pintura a "EN MANTENIMIENTO". La pintura puede ser buscada por su **Cota** o su **Nombre**.

### 3.4. Puesta en Exhibición
Cambia el estado de una pintura a "EN EXHIBICIÓN". La pintura puede ser buscada por su **Cota** o su **Nombre**.

### 3.5. Eliminación de una Pintura
Realiza una eliminación lógica de una pintura del sistema, marcándola como eliminada sin eliminarla físicamente.

### 3.6. Compactador
Elimina físicamente las pinturas que fueron eliminadas lógicamente y actualiza los índices correspondientes.

---

## 4. Plataforma
El programa está desarrollado en **Python** y utiliza vectores en memoria para gestionar la información. Además, cuenta con las siguientes funcionalidades adicionales:

- **Persistencia de datos**: Al finalizar la ejecución, los datos se guardan en un archivo de texto en el disco duro.
- **Carga de datos**: Al iniciar el programa, se leen los datos guardados previamente desde el archivo.

Para la defensa del proyecto, el sistema debe incluir al menos 10 pinturas cargadas.

---

## 5. Entregables y Plazos
1. **Entrega del Programa**: El código fuente debe entregarse el día **3 de julio**.
2. **Defensa del Proyecto**: Se realizará el **4 de julio**, con horario a acordar con el preparador.

---

## 6. Notas
- Es importante validar correctamente las condiciones para cada campo durante la inserción de nuevas pinturas.
- El sistema debe ser eficiente tanto en la consulta como en las operaciones de mantenimiento y compactación.
- Se debe garantizar que los índices se actualicen correctamente tras la compactación.

