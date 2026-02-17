# 📝 Gerenciador de Tarefas em Python

Este é o nosso primeiro projeto prático! Um aplicativo de terminal desenvolvido para organizar tarefas de forma simples, com foco em validação de dados e experiência visual via CLI.

---

### 📝 Descrição do Projeto
O objetivo foi criar uma ferramenta onde o usuário pudesse gerenciar uma lista de afazeres sem que o programa travasse com entradas erradas. Utilizamos loops de repetição, listas e códigos de cores para tornar o terminal mais amigável.

**⚙️ Funcionalidades:**
* **Adicionar tarefas:** Permite inserir novos itens na lista.
* **Lista numerada:** Exibe as tarefas com índices visíveis para o usuário.
* **Remover tarefas:** Exclusão inteligente (o usuário digita o número que vê, e o código trata o índice).
* **Limpar lista:** Apaga todos os itens de uma vez.
* **Validação:** O sistema não aceita opções inexistentes ou entradas inválidas.

---

### 🚀 Como inicializar o projeto
O projeto foi desenvolvido em **Python puro**, sem necessidade de bibliotecas externas (pip).

**Requisitos:**
- Python 3.x instalado.
- Terminal com suporte a cores (Linux, Mac ou CMD/PowerShell atualizados).

**Passos para executar:**

1. **Criação rápida via Terminal:**
   Se estiver no Linux ou Mac, você pode criar o arquivo e colar o código rapidamente:
   ```bash
   nano main.py
(Cole o código, salve com Ctrl + O, Enter e saia com Ctrl + X).

Execução:
Dentro da pasta onde o arquivo main.py está salvo, rode:

Bash
python main.py
🧠 Solução Criativa & Aprendizados
Ajuste de Índice: Como o Python começa a contar do 0, mas o usuário vê o 1, implementamos a lógica de remover - 1 para facilitar a usabilidade.

Feedback Visual: Usamos códigos ANSI (\033[...m) para diferenciar sucessos (verde), erros (vermelho) e títulos (azul).

Pausa Dramática: Utilizamos o time.sleep() para que as mensagens não sumissem rápido demais, melhorando a leitura.

👨‍💻 Desenvolvedores

[Enzo Peralva - GitHub](https://github.com/Enzoperalva)

[Koname - GitHub](https://github.com/AllBlueBR)
