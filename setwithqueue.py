from filaArray import *

class ElementoNaoExiste(ValueError):
    pass

class SetWithQueue:
    
    def __init__(self):
        self._lista = FilaArray()
        
    def size(self):
        return len(self._lista)
    
    def __len__(self):
        return self.size()
    
    def __str__(self):
        return str(self._lista)
    
    def list(self):
        '''
            Retorna todos os elementos presentes na estrutura em formato de lista.
            
            Ex.
                set = SetWithQueue()
                set.add(1)
                set.add(2)
                set.add(3)
                set.list() # [1, 2, 3]
        '''
        
        if self._lista.is_empty():
            return []

        aux = FilaArray()
        data = []
        
        while not self._lista.is_empty():
            item = self._lista.dequeue()
            
            aux.enqueue(item)
            data.append(item)
        
        self._lista = aux
        
        return data
    
    def add(self, value):
        '''
            Adiciona o item na estrutura, sendo O(n) pois precisa verificar se o item já não existe na estrutura.
        '''
        
        if self.contains(value):
            return
        
        self._lista.enqueue(value)
        
    def remove(self, value):
        '''
            Remove o item da estrutura, disparando exceções caso o item não exista ou caso esteja vazia.
            É O(n), pois percorre a estrutura por inteiro e verifica se o item passado via parâmetro está presente na 
            estrutura.
        '''
        
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
    
    def contains(self, value):
        '''
            Verifica se o item está presente na estrutura.
            O(n) pois percorre todos os elementos.
        '''
        
        if self._lista.is_empty():
            return False
        
        aux = FilaArray()
        item = None
        
        while not self._lista.is_empty():
            cursor = self._lista.dequeue()
            
            # Não posso dar break aqui, pois a fila ficaria incompleta
            if cursor == value:
                item = cursor
            
            aux.enqueue(cursor)
        
        self._lista = aux
            
        return item is not None
    