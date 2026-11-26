# Diagramas UML - Site da Faculdade

Diagramas simples do portal acadêmico, separados por tipo. Os arquivos `.drawio` podem ser abertos e editados no draw.io; os PNGs servem para visualização rápida e o PDF reúne os cinco diagramas, um por página.

## Responsáveis

| Diagrama | Responsável |
|---|---|
| Casos de uso | Felipe Rafael |
| Casos de uso ampliados | Samuel |
| Classes e domínio | Andrei Albuquerque |
| Atividade de matrícula | Samuel |
| Sequência de matrícula | Joab |
| Sequência de consulta de notas | Pedro Henrique Almeida Durães |
| Componentes e telas | Felipe Rafael |

## Diagramas draw.io, PNG e PDF

Samuel é o responsável pelos casos de uso ampliados. Veja [perfis e generalização](diagramas/casos-de-uso/perfis-e-generalizacao.drawio) ou [relações na matrícula](diagramas/casos-de-uso/matricula-include-extend.drawio) no draw.io. Os dois desenhos também estão disponíveis em [PNG de perfis](diagramas/casos-de-uso/perfis-e-generalizacao.png) e [PNG de matrícula](diagramas/casos-de-uso/matricula-include-extend.png).

- `diagramas/casos-de-uso/casos-de-uso-portal.drawio` e `.png` - casos de uso do portal acadêmico.
- `diagramas/classes/classes.drawio` e `modelo-de-dominio.png` - modelo de classes e domínio.
- `diagramas/atividades/matricula.drawio` e `.png` - fluxo de matrícula.
- `diagramas/sequencia/matricula.drawio`, `consulta-notas.drawio` e os respectivos PNGs - diagramas de sequência.
- `prints/` - quatro capturas do quadro Trello em ordem das etapas.
- `output/pdf/pp1-diagramas-uml.pdf` - versão consolidada com os cinco diagramas, pronta para abrir ou imprimir.
- [Guia de apresentação do grupo](output/pdf/pp1-roteiro-apresentacao.pdf) - explicações por integrante, diagramas de apoio e evolução semanal no Trello.

Os PNGs abrem diretamente nos visualizadores de imagem comuns. O PDF abre nos leitores disponíveis em diferentes sistemas e dispositivos. Os arquivos `.drawio` abrem no site app.diagrams.net ou no aplicativo draw.io para computador.

As sequências mostram o fluxo principal. Pré-requisitos, vagas, conflitos de horário e o perfil da Secretaria/Coordenação devem ser conferidos com o enunciado e com o grupo.

O diagrama de classes é um modelo conceitual inicial. As associações ainda não exibem multiplicidades, e a posição de algumas linhas na versão draw.io difere do PNG. Antes da entrega final, o grupo deve confirmar as regras e alinhar as duas versões.

## Evolução do Kanban

Veja a [reconstrução das discussões por ciclo](discussoes-por-ciclo.md), baseada nos cartões dos prints.

Os arquivos `prints/etapa-01.png` a `etapa-04.png` registram a fase de modelagem. As datas e semanas desses quatro registros não aparecem nas imagens.

A pasta [`prints/simulacao/`](prints/simulacao/) reúne os registros da segunda fase, que **simula** a construção do portal; os cartões não comprovam implementação real:

1. [Semana 1](prints/simulacao/semana-01.png): base, dados e navegação do portal.
2. [Semana 2](prints/simulacao/semana-02.png): início do fluxo de matrícula.
3. [Semana 3](prints/simulacao/semana-03.png): consulta de notas e calendário.
4. [Semana 4](prints/simulacao/semana-04.png): integração e testes.
5. [Semana 5](prints/simulacao/semana-05.png): preparação da apresentação.
6. [Encerramento](prints/simulacao/encerramento.png): atividades em Done.

No Kanban, Backlog reúne atividades previstas, Doing mostra trabalho em andamento, Review indica revisão e Done reúne atividades concluídas. Na simulação, cada cartão recebeu um único responsável; as pessoas variaram conforme a atividade. João e Uyara são professores e não foram responsáveis pelas novas atividades.

O material é uma proposta de apresentação e modelagem; as regras acadêmicas devem ser validadas antes de implementar o sistema.

## Componentes e telas

O arquivo editável [telas-e-servicos.drawio](diagramas/componentes/telas-e-servicos.drawio) e sua versão em [PNG](diagramas/componentes/telas-e-servicos.png) mostram os componentes propostos e suas dependências UML. O PDF original mantém os cinco diagramas de modelagem.
