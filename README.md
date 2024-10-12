# Integrantes

João Henrique Barbosa Fernandes Alencar</br>
Eike Fabrício da Silva

# Conteúdo Consultado

Inicialmente foi consultado a forma qual o Java fazia de forma interna o tipo `LinkedHashSet<E>` e foi identificado o uso de tabelas hash. Considerando isso, na implementação inicial do método
`SetWithQueue#contains`, foi feito utilizando dicionário, que após revisão, não foi permitido utilizar outra estrutura de dado além da fila em si.

Partimos então para a implementação do Python sob o `set`, que também utiliza tabelas hash, garantindo O(1) no `set#contains`, `set#discard` e `set#add`.

Com isso em mente, consultamos os materiais disponibilizados no Classroom sobre filas e conhecimento próprio sobre a linguagem, aplicando as restrições que um tipo Set deveria possuir.

# Comentário da Equipe sobre realização

Tudo que foi requisitado na atividade foi feito.

# Possíveis problemas, dificuldades encontradas ou funcionalidades que deveriam ser implementadas

* Houve uma certa dificuldade na implementação da função `SetWithQueue#contains`, vez que para atingir O(1), não seria possível sem utilizar alguma outra estrutura, como dicionários ou tabelas hash.

* Como `SetWithQueue#contains` é O(n), automaticamente adicionar e remover do `SetWithQueue` também serão.

* Não sabíamos se poderíamos no método `SetWithQueue#list` passar os valores internos da `FilaArray`, portanto, fizemos um loop sob a fila, criando uma outra fila anterior e apontando o nosso valor interno para ela depois. Assim, todos os métodos, exceto pelo `SetWithQueue#size`, são O(n).
