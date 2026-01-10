# Quicksort 
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Binary Search - Base
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Lower bound (first element >= target)
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Upper bound (first element > target)
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

"""
| Categoria  | Algoritmo principale | Quando usarlo         | Variante / Note da sapere                                                            | Colloquio: cosa dire                                                                                                    |
| ---------- | -------------------- | --------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Search** | Binary Search        | Array **ordinato**    | Lower bound / upper bound, array rotati                                              | “Uso Binary Search; per array non ordinati valuterei sorting o hash map. Posso estendere a lower/upper bound se serve.” |
| **Sort**   | QuickSort            | Qualsiasi array/lista | MergeSort (stabile, garantito O(n log n)), HeapSort (in-place, garantito O(n log n)) | “Uso QuickSort per velocità media e familiarità; Merge/HeapSort hanno vantaggi in certe situazioni.”                    |


Extra / Regole pratiche:

- Per array/matrici/list/linked list → questa combo basta quasi sempre.
- Non serve sapere implementazioni dettagliate di Merge/Heap se sai spiegare quando sono utili.
- Se non ricordi esatta implementazione → meglio spiegare l’idea chiara che stare zitti.
- Grafi, alberi, DP → richiedono algoritmi specifici, ma non rientrano in questo “base search/sort”.
"""

"""
Esempio concreto di come usare lower_bound

lower_bound([1,2,3], 4)

mid è inizialmente 0 + 3 // 2 = 1
arr[1] è 2, minore del target, allora left diventa 2

allo step dopo mid diventa 2 + (3-2) // 2 = 2
arr[2] è 3, minore del target, allora left diventa 3

mi fermo perchè left == right, e torno 3

siccome 3 è piu grande della lunghezza posso affermare che non esiste nell'array! Uguale ma opposto per upper bound. Dunque è safe usarlo senza fare ulteriori check.
"""