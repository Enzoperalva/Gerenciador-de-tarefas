README.md - COMPLETO PARA COPIAR

# 📋 GERENCIADOR DE TAREFAS

Gerenciador simples feito em Python para organizar tarefas pelo terminal.

---

## ⚙️ FUNCIONALIDADES

- [1] Adicionar tarefa
- [2] Listar tarefas  
- [3] Remover tarefa
- [4] Limpar lista
- [5] Sair

---

## 🚀 COMO EXECUTAR

bash
git clone https://github.com/seuusuario/gerenciador-tarefas.git
cd gerenciador-tarefas
python gerenciador.py

========================================
        GERENCIADOR DE TAREFAS         
========================================
[ 1 ] Adicionar tarefa
[ 2 ] Lista de tarefas
[ 3 ] Remover tarefa
[ 4 ] Limpar lista
[ 5 ] Sair

Opção: 1
Adicione alguma tarefa: Estudar Python
✅ TAREFA ADICIONADA
Deseja continuar? [S/N] N

Opção: 2
1. Estudar Python

Opção: 3
Tarefa [ 1 ]: Estudar Python
Qual tarefa remover? 1
❌ TAREFA REMOVIDA

🧠 DESTAQUE TÉCNICO
Validação de remoção: O programa só permite remover tarefas que existem.
while remover not in range(len(adicionar_tarefa)):
    print('TAREFA NÃO ENCONTRADA')
    # Mostra a lista novamente
    remover = int(input('Qual tarefa? '))
    remover = remover - 1
Ajuste de índice: Usuário vê [1], [2], [3] mas Python guarda como 0, 1, 2.
remover = remover - 1  # Converte para índice correto
adicionar_tarefa.pop(remover)

📁 ESTRUTURA DO PROJETO
gerenciador-tarefas/
├── gerenciador.py    # Código principal
└── README.md         # Documentação

🛠️ TECNOLOGIAS
Python 3

Códigos ANSI para cores

Time para pausas

📄 LICENÇA
Este projeto está sob a licença MIT.
