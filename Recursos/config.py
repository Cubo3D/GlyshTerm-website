#
# Arquivo de configuração do Glysh-Term
#
# Puxado automaticamente em "https://glysh-term.vercel.app/Recursos/config.py"
#
# Autor: Cubo3D
# Data da ultima modificação: 
# Versão: 1.0
#
# Versão descontinuado: false
#

# theme: ""

###########
## CORES ##
###########

background_color = "\033[38;2;255;150;0m"
border_color = "\033[38;2;255;250;0m"
text_color = "\033[38;2;255;255;255m"


############
## FONTES ##
############

font = "Ubuntu"
font_size = 14


######################
## ATALHOS DE TECLA ##
######################
#
#
#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Não suportado no momento, mas tentarei trazer na versão 1.5
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#
#
#


# Códigos ANSI para cores
RESET = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[38;2;255;255;255m"
CYAN = "\033[38;2;255;250;0m"
WHITE = "\033[38;2;255;150;0m"

# Exemplo de uso
print(f"{RED}Este texto é vermelho.{RESET}")
print(f"{GREEN}Este texto é verde.{RESET}")
print(f"{YELLOW}Este texto é amarelo.{RESET}")
print(f"{BLUE}Este texto é azul.{RESET}")
print(f"{MAGENTA}Este texto é magenta.{RESET}")
print(f"{CYAN}Este texto é ciano.{RESET}")
print(f"{WHITE}Este texto é branco.{RESET}")

print(f"Este texto é {RED}vermelho{RESET} e este é {BLUE}azul{RESET}.")
