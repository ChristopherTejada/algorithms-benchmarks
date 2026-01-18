Bubble Sort (ordenamiento burbuja) es un algoritmo de ordenamiento muy sencillo y clásico.
Recorre repetidamente la lista comparando pares de elementos adyacentes. Si están en el orden incorrecto, los intercambia. Con cada pasada, el elemento más grande "burbujea" hacia el final de la lista.

Complejidad:

(+)Peor caso: 𝑂(𝑛^2)

(+)Mejor caso: 𝑂(𝑛)
si se optimiza con una bandera que detecta si hubo intercambios.

El problema: Es ineficiente para listas grandes porque hace muchas comparaciones innecesarias.

Se puede mejorar:

Optimización con bandera (swapped): Si en una pasada no se hace ningún intercambio, significa que la lista ya está ordenada y se puede terminar antes.

Reducir iteraciones: En cada pasada, el último elemento ya está en su lugar, por lo que no hace falta volver a compararlo.


## Sample Results

Benchmark executed with 2000 random integers:

- Bubble Sort: ~0.8s
- Quick Sort: ~0.02s

This demonstrates the practical impact of algorithmic complexity
(O(n²) vs O(n log n)).
