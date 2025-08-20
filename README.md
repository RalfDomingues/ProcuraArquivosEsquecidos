<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

    <h1>Scanner de Arquivos Inativos</h1>

    <p>Este projeto é um script em <strong>Python</strong> que varre discos do Windows em busca de arquivos e pastas inativos, ou seja, aqueles que não foram acessados nos últimos <strong>90 dias</strong> (configurável). O script gera um relatório detalhado em arquivo <code>.txt</code> com o tamanho de cada arquivo/pasta e o espaço total ocupado pelos inativos.</p>

    <h2>Funcionalidades</h2>
    <ul>
        <li>Varre todos os arquivos e pastas de um disco selecionado.</li>
        <li>Ignora diretórios específicos configurados pelo usuário.</li>
        <li>Verifica inatividade com base no último acesso.</li>
        <li>Calcula o tamanho de arquivos e pastas inativos.</li>
        <li>Gera um log em <code>.txt</code> com os resultados, incluindo espaço total ocupado.</li>
        <li>Suporta múltiplos discos e sistemas Windows.</li>
    </ul>

    <h2>Configurações</h2>
    <ul>
        <li><code>LIMITE_DIAS</code>: Define o período de inatividade em dias (padrão: 90).</li>
        <li><code>DIRETORIOS_EXCLUIDOS</code>: Lista de pastas que não serão varridas.</li>
    </ul>

    <h2>Como Usar</h2>
    <ol>
        <li>Certifique-se de ter Python instalado no Windows.</li>
        <li>Clone ou faça download do projeto.</li>
        <li>Execute o script: <code>python nome_do_arquivo.py</code></li>
        <li>O script exibirá os discos disponíveis. Digite a letra do disco que deseja escanear (ex: <code>C</code>).</li>
        <li>Aguarde enquanto o script realiza a varredura e gera o log.</li>
        <li>O relatório será salvo na mesma pasta do script com nome: <code>log_inativos_<letra>_<data>.txt</code></li>
    </ol>

    <h2>Exclusões</h2>
    <p>Diretórios como jogos, bibliotecas de aplicativos ou pastas críticas do sistema podem ser ignorados para evitar varreduras desnecessárias ou problemas de permissão. Exemplo padrão:</p>
    <ul>
        <li>D:\SteamLibrary</li>
        <li>C:\SteamLibrary</li>
        <li>D:\Genshin Impact game</li>
        <li>D:\WindowsApps</li>
        <li>D:\Stardew Valley</li>
        <li>D:\xbox games</li>
    </ul>

    <h2>Saída do Script</h2>
    <ul>
        <li>Lista de arquivos e pastas inativos com tamanho em MB/GB.</li>
        <li>Espaço total ocupado pelos arquivos inativos.</li>
        <li>Log em arquivo TXT gerado automaticamente.</li>
    </ul>

    <h2>Dependências</h2>
    <ul>
        <li><code>psutil</code> - Para listar discos e informações do sistema: <code>pip install psutil</code></li>
        <li>Módulos padrão do Python: <code>os</code>, <code>time</code>, <code>datetime</code>, <code>collections</code></li>
    </ul>

    <h2>Contato</h2>
    <p>Para dúvidas ou sugestões: <a href="mailto:seuemail@dominio.com">seuemail@dominio.com</a></p>

    <p>© 2025 Scanner de Arquivos Inativos. Todos os direitos reservados.</p>

</body>
</html>
