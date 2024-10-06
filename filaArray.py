class FilaVazia(Exception):
    pass

class FilaArray:

    TAM_PADRAO = 10

    def __init__(self):
        self._dados = [None] * FilaArray.TAM_PADRAO
        self._tamanho = 0
        self._inicio = 0

    def enqueue(self, value):
        if self._tamanho == len(self._dados):
            # CHEIA
            self._altera_tamanho(self._tamanho * 2)

        posicao = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[posicao] = value
        self._tamanho += 1

    def dequeue(self):
        if self.is_empty():
            raise FilaVazia ("A fila está vazia.")
        
        saida = self._dados[self._inicio]
        self._dados[self._inicio] = None

        self._inicio += 1
        self._tamanho -= 1

        if 0 < self._tamanho <= len(self._dados) // 4:
            nova_capacidade = max(FilaArray.TAM_PADRAO, len(self._dados) // 2)
            self._altera_tamanho(nova_capacidade)

        return saida
    
    def __len__(self):
        return self._tamanho
    
    def __str__(self):
        posicao = self._inicio
        saida = "["
        
        for k in range(self._tamanho):
            if saida != "[":
                saida += ', '
            saida += str(self._dados[posicao])
            posicao = (1 + posicao) % len(self._dados)

        saida += f'] Tamanho: {len(self)}. Capacidade {len(self._dados)}.\n'
        return saida
    
    def is_empty(self):
        return (self._tamanho == 0)
    
    def first(self):
        if self.is_empty():
            raise FilaVazia ("A fila está vazia.")
        return (self._dados[self._inicio])

    def _altera_tamanho(self, novo_tamanho):
        dados_atuais = self._dados

        self._dados = [None] * novo_tamanho
        posicao = self._inicio
        
        for x in range(self._tamanho):
            self._dados[x] = dados_atuais[posicao]
            posicao = (1 + posicao) % len(dados_atuais)

        self._inicio = 0