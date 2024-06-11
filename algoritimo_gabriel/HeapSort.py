def heap_sort(lista, n, i):
	maior_indice = i 
	l = 2 * i + 1 
	r = 2 * i + 2 

	if l < n and lista[i] < lista[l]:
		maior_indice = l

	if r < n and lista[maior_indice] < lista[r]:
		maior_indice = r

	if maior_indice != i:
		(lista[i], lista[maior_indice]) = (lista[maior_indice], lista[i]) 

		heap_sort(lista, n, maior_indice)

def heapSort(lista):
	n = len(lista)

	for i in range(n // 2, -1, -1):
		heap_sort(lista, n, i)

	for i in range(n - 1, 0, -1):
		(lista[i], lista[0]) = (lista[0], lista[i]) 
		heap_sort(lista, i, 0)

arr = [12, 11, 13, 5, 1, 4, 9, 6, 7, ]
heapSort(arr)
n = len(arr)
sorted_array = []

print('Resultado da ordenação: ')
for i in range(n):
	sorted_array.append(arr[i])
	
print(sorted_array)

