from filaArray import *

class ElementoNaoExiste(ValueError):
    pass

class SetWithQueue:
    def __init__(self):
        self._lista = FilaArray()
        self._set = dict()

    def size(self):
        # O(1), FUNCAO SIMPLES
        return len(self._lista)
    
    def __len__(self):
        return self.size()
    
    def __str__(self):
        return str(self._lista)
    
    def list(self):
        # O(1) --- REVISAR
        return [i for i in self._set.keys()]
    
    def add(self, value):
        # O(1) AMORTIZADO
        # POR ENQUANTO POIS CONTAINS É O(1) E O UNICO CASO DE O(N) SERIA NO AUMENTO DO TAMANHO DA FILA
        if self.contains(value):
            return
        
        self._set[value] = self.size()
        self._lista.enqueue(value)

    def remove(self, value):
        # O(N)
        # Necessário realizar loop em todos os valores
        if not self.contains(value):
            raise ElementoNaoExiste("Element not found")
        
        if self._lista.is_empty():
            raise FilaVazia("A fila está vazia.")
        
        aux = FilaArray()
        
        while not self._lista.is_empty():
            item = self._lista.first()
            
            if item != value:
                aux.enqueue(item)
                
            self._lista.dequeue()
            
        self._lista = aux
        
        del self._set[value] 
        
        return
    
    def contains(self, value):
        # O(1) --- REVISAR
        return value in self._set.keys()
     
    