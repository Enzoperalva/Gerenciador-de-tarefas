📋 GERENCIADOR DE TAREFAS
Gerenciador simples feito em Python para organizar tarefas pelo terminal.

⚙️ FUNCIONALIDADES
text
[1] Adicionar tarefa
[2] Listar tarefas
[3] Remover tarefa  
[4] Limpar lista
[5] Sair
🚀 COMO EXECUTAR
bash
# Clone o repositório
git clone https://github.com/seuusuario/gerenciador-tarefas.git

# Entre na pasta
cd gerenciador-tarefas

# Execute
python gerenciador.py
📸 EXEMPLO RÁPIDO
text
Opção: 1
Tarefa: Estudar Python
✅ Adicionada!

Opção: 2
1. Estudar Python

Opção: 3
Digite o número da tarefa: 1
❌ Removida!
🧠 DESTAQUE TÉCNICO
Validação de remoção: O programa só permite remover tarefas que existem.

python
while remover not in range(len(lista)):
    print('Tarefa inválida')
    remover = int(input('Digite novamente: '))
📁 ESTRUTURA
text
gerenciador-tarefas/
├── gerenciador.py    # Código principal
└── README.md         # Este arquivo
👨‍💻 FEITO COM
Python 3

Cores ANSI no terminal

Muito café ☕

