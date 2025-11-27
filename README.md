# Sistema de Gerenciamento Acadêmico

Sistema em Python desenvolvido para gerenciamento básico de uma instituição de ensino via terminal, focado em cadastros, controle de notas e emissão de relatórios.

## 📋 Funcionalidades

Baseado nos requisitos do projeto, o sistema permite:

* **Cadastros:**
    * Cursos (Código e Nome).
    * Disciplinas (Código e Nome).
    * Professores (Matrícula, Nome, Disciplina e Curso).
    * Alunos (Matrícula, Nome e Curso).
* **Gestão Acadêmica:**
    * Lançamento de notas por aluno e disciplina.
    * Cálculo automático de médias.
    * Alteração de notas para alunos em recuperação.
* **Relatórios:**
    * Listagem geral de cadastros.
    * Alunos matriculados por curso/disciplina.
    * Boletim detalhado com todas as notas.
    * **Certificado de Conclusão** (com data de emissão).

## ⚖️ Regras de Negócio

O sistema aplica automaticamente as seguintes regras para definir a situação do aluno:

1.  **Aprovado:** Média geral das notas $\geq$ 7.0.
2.  **Recuperação:** Média geral $\geq$ 4.0 e $<$ 7.0.
    * *O sistema exibe as disciplinas com nota insuficiente e permite a alteração da nota.*
3.  **Reprovado:** Média geral $<$ 4.0.
4.  **Conclusão de Curso:** O certificado só é gerado se o aluno for aprovado e tiver cursado pelo menos **10 disciplinas**.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Conceitos:** Estruturas de controle (`if`, `for`, `while`), Funções, Listas e Dicionários.
* **Bibliotecas:** Nenhuma biblioteca externa necessária (apenas `datetime` nativa).

## 🚀 Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Execute o arquivo principal:
    ```bash
    python academico.py
    ```
3.  Siga as instruções do menu numérico no terminal.
