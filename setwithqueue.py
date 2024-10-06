from filaArray import FilaArray

class ElementoJaExiste(Exception):
    pass

class SetWithQueue:
    def __init__(self):
        self._lista = FilaArray()

    def size(self):
        return len(self._lista)
    
    def list(self):
        # IMPLEMENTADO USANDO O __STR__, TALVEZ MUDAR
        return(print(self._lista))
    
    def add(self, value):
        if self.contains(value):
            raise ElementoJaExiste("O elemento a ser adicionado já está na Fila.")
        self._lista.enqueue(value)

    def remove(self, value):
        # IMPLEMENTAR
        return
    
    ### PENSAR SE HA MANEIRA MELHOR DE IMPLEMENTAR
    def contains(self, value):
        # LISTA TEMPORARIA
        temp = []
        found = False
        
        # USA OS METODOS DE ENQUEUE E DEQUEUE PARA RODAR A LISTA BUSCANDO
        for i in range(len(self._lista)):
            current = self._lista.dequeue()
            temp.append(current)
            if current == value:
                found = True
        
        # DEVOLVENDO ITENS
        for item in temp:
            self._lista.enqueue(item)

        return found
     
    