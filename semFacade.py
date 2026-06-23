# --- Componentes Complexos do Computador ---
class FonteAlimentacao:
    def ligar_energia(self):
        print("Fonte: Fornecendo energia para os componentes.")

class PlacaMae:
    def iniciar_boot(self):
        print("Placa-Mãe: Executando o POST e iniciando o BIOS.")

class SistemaOperativo:
    def carregar_sistema(self):
        print("SO: Carregando o ambiente de trabalho.")


# --- Código do Cliente (Tu tentando ligar o PC) ---
fonte = FonteAlimentacao()
placa = PlacaMae()
so = SistemaOperativo()

print(">>> Tentando ligar o computador manualmente...")
fonte.ligar_energia()
placa.iniciar_boot()
so.carregar_sistema()
print(">>> Computador pronto para uso!")