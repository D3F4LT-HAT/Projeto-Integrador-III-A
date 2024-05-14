class Paciente:
    """
    Representa um paciente no sistema.

    Atributos:
        nome (str): Nome do paciente.
        idade (int): Idade do paciente.
        doenca (str): Doença do paciente.
        proximo (Paciente): Ponteiro para o próximo paciente na lista.
    """
    def __init__(self, nome, idade, doenca):
        self.nome = nome
        self.idade = idade
        self.doenca = doenca
        self.proximo = None

class ListaEncadeada:
    """
    Implementa a lista encadeada de pacientes.

    Atributos:
        inicio (Paciente): Ponteiro para o primeiro paciente da lista.
    """
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, nome, idade, doenca):
        """
        Insere um novo paciente no início da lista.

        Args:
            nome (str): Nome do paciente.
            idade (int): Idade do paciente.
            doenca (str): Doença do paciente.
        """
        novo_paciente = Paciente(nome, idade, doenca) # Cria um novo nó (paciente)
        novo_paciente.proximo = self.inicio # O próximo do novo paciente aponta para o inicio atual
        self.inicio = novo_paciente # O novo paciente se torna o inicio da lista

    def inserir_fim(self, nome, idade, doenca):
        """
        Insere um novo paciente no fim da lista.

        Args:
            nome (str): Nome do paciente.
            idade (int): Idade do paciente.
            doenca (str): Doença do paciente.
        """
        novo_paciente = Paciente(nome, idade, doenca) # Cria um novo nó (paciente)
        if self.inicio is None: # Se a lista estiver vazia
            self.inicio = novo_paciente # O novo paciente se torna o inicio da lista
            return
        atual = self.inicio # Começa do inicio da lista
        while atual.proximo is not None: # Percorre a lista até o último nó
            atual = atual.proximo
        atual.proximo = novo_paciente # O próximo do último nó aponta para o novo paciente

    def remover(self, nome):
        """
        Remove um paciente da lista pelo nome.

        Args:
            nome (str): Nome do paciente a ser removido.

        Returns:
            bool: True se o paciente foi removido, False caso contrário.
        """
        atual = self.inicio # Começa do inicio da lista
        anterior = None
        while atual is not None: # Percorre a lista
            if atual.nome == nome: # Se encontrar o paciente com o nome informado
                if anterior is None: # Se o paciente for o primeiro da lista
                    self.inicio = atual.proximo # O inicio da lista passa a ser o próximo do paciente removido
                else: # Se o paciente não for o primeiro da lista
                    anterior.proximo = atual.proximo # O próximo do nó anterior passa a ser o próximo do paciente removido
                return True # Retorna True indicando que o paciente foi removido
            anterior = atual # Atualiza o nó anterior
            atual = atual.proximo # Avança para o próximo nó
        return False # Retorna False se o paciente não foi encontrado

    def buscar(self, nome):
        """
        Busca um paciente na lista pelo nome.

        Args:
            nome (str): Nome do paciente a ser buscado.

        Returns:
            Paciente: O objeto Paciente se encontrado, None caso contrário.
        """
        atual = self.inicio # Começa do inicio da lista
        while atual is not None: # Percorre a lista
            if atual.nome == nome: # Se encontrar o paciente com o nome informado
                return atual # Retorna o objeto Paciente
            atual = atual.proximo # Avança para o próximo nó
        return None # Retorna None se o paciente não foi encontrado

    def imprimir(self):
        """
        Imprime a lista de pacientes.
        """
        atual = self.inicio # Começa do inicio da lista
        while atual is not None: # Percorre a lista
            print(f"Nome: {atual.nome}, Idade: {atual.idade}, Doença: {atual.doenca}")
            atual = atual.proximo # Avança para o próximo nó

    def ordenar_por_nome(self):
        """
        Ordena a lista de pacientes por nome em ordem alfabética.
        """
        if self.inicio is None: # Se a lista estiver vazia
            return
        atual = self.inicio # Começa do inicio da lista
        while atual.proximo is not None: # Percorre a lista
            proximo = atual.proximo
            while proximo is not None: # Percorre a lista a partir do próximo nó
                if atual.nome > proximo.nome: # Se o nome do nó atual for maior que o nome do próximo nó
                    # Troca as informações dos nós
                    atual.nome, proximo.nome = proximo.nome, atual.nome
                    atual.idade, proximo.idade = proximo.idade, atual.idade
                    atual.doenca, proximo.doenca = proximo.doenca, atual.doenca
                proximo = proximo.proximo # Avança para o próximo nó
            atual = atual.proximo # Avança para o próximo nó

# Cria uma instância da lista encadeada
lista_pacientes = ListaEncadeada()

# Loop principal do programa
while True:
    # Exibe o menu de opções
    print("\nSistema de Gerenciamento de Pacientes:")
    print("1. Inserir paciente no início")
    print("2. Inserir paciente no fim")
    print("3. Remover paciente")
    print("4. Buscar paciente")
    print("5. Imprimir lista de pacientes")
    print("6. Ordenar lista por nome")
    print("7. Sair")

# Lê a opção do usuário
    opcao = input("Digite a opção desejada: ")

    # Processa a opção escolhida
    if opcao == "1":
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        doenca = input("Digite a doença do paciente: ")
        lista_pacientes.inserir_inicio(nome, idade, doenca)
        print("Paciente inserido com sucesso!")
    elif opcao == "2":
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        doenca = input("Digite a doença do paciente: ")
        lista_pacientes.inserir_fim(nome, idade, doenca)
        print("Paciente inserido com sucesso!")
    elif opcao == "3":
        nome = input("Digite o nome do paciente a ser removido: ")
        if lista_pacientes.remover(nome):
            print("Paciente removido com sucesso!")
        else:
            print("Paciente não encontrado!")
    elif opcao == "4":
        nome = input("Digite o nome do paciente a ser buscado: ")
        paciente = lista_pacientes.buscar(nome)
        if paciente is not None:
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Doença: {paciente.doenca}")
        else:
            print("Paciente não encontrado!")
    elif opcao == "5":
        lista_pacientes.imprimir()
    elif opcao == "6":
        lista_pacientes.ordenar_por_nome()
        print("Lista ordenada por nome!")
    elif opcao == "7":
        break # Sai do loop
    else:
        print("Opção inválida!")