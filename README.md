# PP1 - Diagramas UML do site da faculdade

Conjunto condensado de diagramas para modelar o Portal Acadêmico da Faculdade. Os arquivos estão separados por tipo de diagrama; cada fonte PlantUML acompanha seu SVG vetorial. O PDF reúne os cinco diagramas em páginas separadas.

## Diagramas e responsáveis

| Diagrama | Responsável indicado no desenho | Cartão do Trello |
|---|---|---|
| Casos de uso | Felipe Rafael | 39 - Regras de negócio e condições dos casos de uso |
| Classes e domínio | Andrei Albuquerque | 38 - Tipos e restrições dos atributos |
| Atividade de matrícula | Samuel | 36 - Fluxo de matrícula |
| Sequência de matrícula | Joab (joabfr4nca2018) | 40 - Rastreabilidade final entre requisitos e diagramas |
| Sequência de consulta de notas | Pedro Henrique Almeida Durães | 37 - Sequência de consulta acadêmica |

## Estrutura

- `diagramas/casos-de-uso/` - casos de uso do aluno, professor e secretaria/coordenação.
- `diagramas/classes/` - modelo de domínio e associações principais.
- `diagramas/atividades/` - fluxo de matrícula com validação e correção de pendências.
- `diagramas/sequencia/` - sequências de matrícula e consulta de notas.
- `output/pdf/pp1-diagramas-uml.pdf` - versão consolidada, um diagrama por página.

Cada pasta de tipo contém o `.puml` editável e o `.svg` pronto para visualização, impressão ou inclusão em relatório.

## Escopo e decisões a validar

Os nomes de funcionalidades vêm dos cartões do quadro PP1: matrícula, consulta de notas, turmas, disciplinas, calendário, avisos e modelagem de classes. Como não havia arquivos de especificação na pasta de referências, os diagramas tratam como proposta alguns detalhes de negócio: pré-requisitos, vagas, conflitos de horário e o perfil Secretaria/Coordenação. Confirme essas regras com o enunciado e com o grupo antes de apresentar a versão final.

As operações restritas pressupõem autenticação. O diagrama não define tecnologia, telas, banco de dados físico nem regras numéricas que não aparecem nos cartões.

## Gerar novamente os SVGs e o PDF

Com Python e a biblioteca ReportLab instalados, execute `python tools/render_diagrams.py` na raiz do repositório. As fontes PlantUML permanecem disponíveis para ajustes do modelo.
