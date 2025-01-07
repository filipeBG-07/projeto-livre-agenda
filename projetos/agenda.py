import datetime
from menu import menu

 

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.jornada_trabalho = datetime.timedelta(hours=10)
        self.intervalo = datetime.timedelta(hours=1, minutes=30)
        self.agenda = {}  # Dicionário: {data: {horario: Agendamento}}

    def __str__(self):
        return self.nome


class Procedimento:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return self.nome


class Agendamento:
    def __init__(self, funcionario, procedimento, horario, data):
        self.funcionario = funcionario
        self.procedimento = procedimento
        self.horario = horario
        self.data = data

    def __str__(self):
        return f"{self.funcionario} - {self.procedimento} - {self.horario.strftime('%H:%M')} - {self.data.strftime('%d/%m/%Y')}"


class Barbearia:
    def __init__(self):
        self.funcionarios = {}
        self.procedimentos = {}
        self.agendamentos = {}  # Dicionário: {data: {funcionario: {horario: Agendamento}}}

    def adicionar_funcionario(self, funcionario):
        self.funcionarios[funcionario.nome] = funcionario

    def adicionar_procedimento(self, procedimento):
        self.procedimentos[procedimento.nome] = procedimento

    def agendar(self, funcionario_nome, procedimento_nome, horario, data):
        funcionario = self.funcionarios.get(funcionario_nome)
        procedimento = self.procedimentos.get(procedimento_nome)

        if not funcionario or not procedimento:
            return "Funcionário ou procedimento não encontrado."

        if data not in self.agendamentos:
            self.agendamentos[data] = {}
        if funcionario not in self.agendamentos[data]:
            self.agendamentos[data][funcionario] = {}

        if horario in self.agendamentos[data][funcionario]:
            return "Horário indisponível."

        agendamento = Agendamento(funcionario, procedimento, horario, data)
        self.agendamentos[data][funcionario][horario] = agendamento

        return "Agendamento realizado com sucesso."

    def listar_horarios_disponiveis(self, funcionario, data):
        # Implementar lógica para calcular horários disponíveis com base na jornada, intervalo e agendamentos
        pass

    def listar_agendamentos(self):
        for data, funcionarios in self.agendamentos.items():
            for funcionario, horarios in funcionarios.items():
                for horario, agendamento in horarios.items():
                    print(agendamento)



barbearia = Barbearia()

#criando os funcinários
filipe = Funcionario("filipe")
luis = Funcionario("luis")
amaral = Funcionario("amaral")
mateus = Funcionario("mateus")

barbearia.adicionar_funcionario(filipe)
barbearia.adicionar_funcionario(luis)
barbearia.adicionar_funcionario(amaral)
barbearia.adicionar_funcionario(mateus)

# Criando os procedimentos
corte = Procedimento("corte de cabelo", 35.00)
barba = Procedimento("barba", 20.00)
corte_barba = Procedimento(  "corte e barba", 50.00)

barbearia.adicionar_procedimento(corte)
barbearia.adicionar_procedimento(barba)
barbearia.adicionar_procedimento(corte_barba)

data_agendamento = datetime.date(2024, 10, 27)
horario_agendamento = datetime.datetime(2024, 10, 27, 9, 0)

barbearia.agendar("filipe", "corte de cabelo", horario_agendamento, data_agendamento)

barbearia.listar_agendamentos()