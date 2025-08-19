import os
import time
import psutil
from datetime import datetime
from collections import defaultdict

# Configurações
LIMITE_DIAS = 90 # Define o limite de inatividade em dias
limite_timestamp = time.time() - (LIMITE_DIAS * 86400) # Converte dias em timestamp (segundos)

# Diretórios que serão ignorados na varredura
DIRETORIOS_EXCLUIDOS = [
    r"D:\SteamLibrary",
    r"C:\SteamLibrary",
    r"D:\Genshin Impact game",
    r"D:\WindowsApps",
    r"D:\Stardew Valley",
    r"D:\xbox games"
]

# Função que verifica se um caminho está na lista de exclusão
def esta_excluido(caminho):
    caminho = os.path.abspath(caminho).lower()
    for excluido in DIRETORIOS_EXCLUIDOS:
        if caminho.startswith(os.path.abspath(excluido).lower()):
            return True
    return False

# Verifica se um arquivo está inativo (último acesso anterior ao limite)
def verificar_inatividade(caminho):
    try:
        ultimo_acesso = os.path.getatime(caminho)
        return ultimo_acesso < limite_timestamp
    except Exception:
        return False

# Retorna o tamanho de um arquivo em bytes
def tamanho_arquivo(caminho):
    try:
        return os.path.getsize(caminho)
    except Exception:
        return 0

# Converte bytes em MB e GB e formata como string
def formatar_tamanho(bytes_):
    mb = bytes_ / (1024 * 1024)
    gb = bytes_ / (1024 * 1024 * 1024)
    return f"{mb:.2f} MB / {gb:.2f} GB"

# Função principal que varre arquivos e pastas inativos com agregação
def buscar_inativos_com_agregacao(raiz_disco):
    resultados = []
    total_bytes = 0
    estrutura = defaultdict(list)

    for raiz, dirs, arquivos in os.walk(raiz_disco, topdown=False):
        if esta_excluido(raiz):
            continue

        todos_inativos = True
        total_tamanho_dir = 0
        inativos_no_diretorio = []

        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if esta_excluido(caminho):
                continue
            inativo = verificar_inatividade(caminho)
            estrutura[raiz].append((caminho, inativo))

            if inativo:
                inativos_no_diretorio.append(caminho)
                total_tamanho_dir += tamanho_arquivo(caminho)
            else:
                todos_inativos = False

        for subpasta in dirs:
            subpasta_path = os.path.join(raiz, subpasta)
            if subpasta_path in estrutura:
                arquivos_sub = estrutura[subpasta_path]
                if any(not ativo for _, ativo in arquivos_sub):
                    if any(ativo for _, ativo in arquivos_sub):
                        todos_inativos = False
                    else:
                        total_tamanho_dir += sum(tamanho_arquivo(f) for f, _ in arquivos_sub)

        if todos_inativos and inativos_no_diretorio:
            resultados.append((raiz, total_tamanho_dir))
            estrutura[raiz] = [(raiz, False)]
        else:
            for caminho in inativos_no_diretorio:
                resultados.append((caminho, tamanho_arquivo(caminho)))

        total_bytes += total_tamanho_dir

    return resultados, total_bytes

# Lista os discos disponíveis no Windows (ignorando CD-ROMs)
def listar_discos_windows():
    return [p.device.rstrip("\\") for p in psutil.disk_partitions(all=False) if 'cdrom' not in p.opts and p.fstype != '']

# Gera um log em arquivo TXT com os resultados
def gerar_log_txt(letra_disco, resultados, total_bytes):
    nome_arquivo = f"log_inativos_{letra_disco}_{datetime.now().strftime('%Y-%m-%d')}.txt"
    caminho_log = os.path.join(os.getcwd(), nome_arquivo)

    with open(caminho_log, "w", encoding="utf-8") as log:
        log.write(f"📁 Relatório de Arquivos/Pastas Inativos no Disco {letra_disco}:\n")
        log.write(f"(Inatividade superior a {LIMITE_DIAS} dias)\n\n")

        for caminho, tamanho in sorted(resultados):
            log.write(f"{caminho} ({formatar_tamanho(tamanho)})\n")

        log.write("\n📦 Espaço total ocupado por inativos:\n")
        log.write(f"{formatar_tamanho(total_bytes)}\n")

    print(f"\n📝 Log salvo em: {caminho_log}")

# Função principal que controla a execução do programa
def main():
    discos_disponiveis = listar_discos_windows()
    print("💽 Discos disponíveis:")
    for d in discos_disponiveis:
        print(f" - {d}")

    letra = input("\nDigite a letra do disco que deseja escanear (ex: C): ").strip().upper()
    if not letra.endswith(":"):
        letra += ":"
    caminho_disco = f"{letra}\\"

    if letra not in discos_disponiveis:
        print(f"\n❌ Disco '{letra}' não encontrado ou não montado.")
        return

    print(f"\n🔍 Iniciando varredura no disco {letra}...\n")
    try:
        resultados, total = buscar_inativos_com_agregacao(caminho_disco)
        print("\n✅ Arquivos e diretórios inativos (último acesso há mais de 3 meses):")
        for caminho, tamanho in sorted(resultados):
            print(f"{caminho} ({formatar_tamanho(tamanho)})")

        print("\n📦 Espaço total ocupado por inativos:")
        print(formatar_tamanho(total))

        gerar_log_txt(letra.strip(":"), resultados, total)

    except Exception as e:
        print(f"Erro ao acessar {caminho_disco}: {e}")

# Executa o script
if __name__ == "__main__":
    main()
