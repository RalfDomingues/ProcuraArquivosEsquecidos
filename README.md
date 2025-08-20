# 📁 Scanner de Arquivos Inativos

Este script em **Python** varre discos do Windows em busca de arquivos e pastas **inativos** (não acessados nos últimos 90 dias por padrão) e gera um relatório detalhado com o espaço ocupado.

---

## ⚙️ Funcionalidades

- Varre arquivos e pastas de um disco selecionado.  
- Ignora diretórios específicos configurados pelo usuário.  
- Verifica inatividade com base no último acesso.  
- Calcula o tamanho de arquivos e pastas inativos.  
- Gera um log em `.txt` com os resultados.  
- Suporta múltiplos discos no Windows.  

---

## 🛠 Configurações

- `LIMITE_DIAS`: Define o período de inatividade em dias (padrão: 90).  
- `DIRETORIOS_EXCLUIDOS`: Lista de pastas que serão ignoradas durante a varredura.

---

## 🚀 Como Usar

1. Certifique-se de ter Python instalado no Windows.  
2. Clone ou faça download do projeto.  
3. Instale a dependência necessária:  
   ```bash
   pip install psutil
