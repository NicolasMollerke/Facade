# Facade

### O que é?
O Facade é um padrão de desnvolvimento estrutural que permite a criação de uma interface simplicada para um subsistema complexo. Uma Facde fornece funcionalidade limitadas quando comparada com os subsistemas, visando incluir apenas as ações que o cliente se importa.

---

### Estutura:
1. A Facade fornece acceso a uma funcionalidade específica do subsistema. 
2. A criação de uma classe Facade Adicional pode ser feita com objetivo de prevendi a poluição de uma única facade com funcionalidade irrelevantes.
3. O Subsistema Complexo consiste em múltiplos objetos variados. Para torna-los funcionais você precisa ter conhecimento profundo nos detalhes de implementação. As classes do subsistema não sabem da existência da Facade.
4. O cliente tem acesso a Facade ao invés dos objetos do subsistema diretamente.
<img width="840" height="570" alt="Image" src="https://github.com/user-attachments/assets/09ac7cfb-6d1a-40f7-96d2-e48a6caca935" />


---

### Aplicação no mundo real
Em um contexto contidiano uma Facade funciona como um operador de uma loja que você liga para fazer um pedido. Esse operador seria como uma interface para o sistema de pedido, pagamentos, e vários sistemas de entrega.

---

### Quando usar?
* Você precisa de uma interfcae limitada mas simples para um subsistema complexo.
* Quer uma estrutura em camadas

---

### Prós e Contras

| Prós | Contras |
| :--- | :--- |
| Isolamentos de Complexidade | Barreira para Recursos Avançados |
| Baixo Acomplamento | Mais uma Camada de Código |
| Fácil Aprendizagem | |
