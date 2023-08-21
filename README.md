# Librería de Operaciones para Números Complejos

Esta es una librería de Python que proporciona funciones para realizar operaciones en números complejos, incluyendo operaciones básicas, conversión de representaciones y cálculos de propiedades.

## Operaciones Soportadas

La librería incluye las siguientes operaciones para números complejos:

- **Suma:** `sumacplx(complejo1, complejo2)`
- **Producto:** `mutcplx(complejo1, complejo2)`
- **Resta:** `restcplx(complejo1, complejo2)`
- **División:** `divcplx(complejo1, complejo2)`
- **Módulo:** `modulcplx(complejo1)`
- **Conjugado:** `conjucplx(complejo1)`
- **Conversión Polar a Cartesiano:** `ConverPolarCart(coordenadas_polares)`
- **Conversión Cartesiano a Polar:** `ConverCartPolar(coordenadas_cartesianas)`
- **Fase:** `retornarFase(complejo1)`

## Requisitos

- [PyCharm 3.11](https://www.jetbrains.com/pycharm/)

## Uso

1. Clona este repositorio en tu máquina local.
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones proporcionadas para realizar operaciones con números complejos.

## Ejemplo de Uso

```python
import libcplx as lc

# Operaciones básicas
c1 = (3, 4)
c2 = (1, 2)
sum_result = lc.sumacplx(c1, c2)
print("Suma:", sum_result)

# Conversión polar a cartesiano
cordenada_Polar = (5, 0.927295218)
cartesian_result = lc.ConverPolarCart(cordenada_Polar)
print("Coordenadas cartesianas:", cartesian_result)
```
## Autor
**Jose Ricardo Vasquez Vega**