# --- Os componentes continuam exatamente os mesmos ---
class FonteAlimentacao:
    def ligar_energia(self):
        print("Fonte: Fornecendo energia para os componentes.")

class PlacaMae:
    def iniciar_boot(self):
        print("Placa-Mãe: Executando o POST e iniciando o BIOS.")

class SistemaOperativo:
    def carregar_sistema(self):
        print("SO: Carregando o ambiente de trabalho.")


# --- FACADE ---
class ComputadorFacade:
    def __init__(self):
        self.fonte = FonteAlimentacao()
        self.placa = PlacaMae()
        self.so = SistemaOperativo()

    def ligar(self):
        print("\n>>> [Facade] Apertando o botão Power...")
        self.fonte.ligar_energia()
        self.placa.iniciar_boot()
        self.so.carregar_sistema()
        print(">>> [Facade] Computador iniciado com sucesso! <<<")


# --- Código do Cliente ---
# Cliente só interage com a Facade:
meu_pc = ComputadorFacade()

# Apenas uma chamada resolve tudo:
meu_pc.ligar()