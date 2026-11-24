# Diagramas UML - Site da Faculdade

Diagramas simples do portal acadêmico, separados por tipo. Cada desenho identifica seu responsável. O PDF contém os cinco diagramas, um por página.

## Responsáveis

| Diagrama | Responsável |
|---|---|
| Casos de uso | Felipe Rafael |
| Classes e domínio | Andrei Albuquerque |
| Atividade de matrícula | Samuel |
| Sequência de matrícula | Joab |
| Sequência de consulta de notas | Pedro Henrique Almeida Durães |

## Diagramas em PNG e PDF

- `diagramas/casos-de-uso/casos-de-uso-portal.png` - casos de uso do portal acadêmico.
- `diagramas/classes/modelo-de-dominio.png` - modelo de classes e domínio.
- `diagramas/atividades/matricula.png` - fluxo de matrícula.
- `diagramas/sequencia/matricula.png` e `diagramas/sequencia/consulta-notas.png` - diagramas de sequência.
- `prints/` - quatro capturas do quadro Trello em ordem das etapas.
- `output/pdf/pp1-diagramas-uml.pdf` - versão consolidada com os cinco diagramas, pronta para abrir ou imprimir.

Os PNGs abrem diretamente nos visualizadores de imagem comuns. O PDF abre nos leitores de PDF disponíveis em diferentes sistemas e dispositivos.

As sequências mostram o fluxo principal. Pré-requisitos, vagas, conflitos de horário e o perfil da Secretaria/Coordenação devem ser conferidos com o enunciado e com o grupo.

## Evolução do Kanban

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

O [diagrama de componentes e telas](diagramas/componentes/telas-e-servicos.png) apresenta uma proposta para a segunda fase simulada. As telas de acesso, aluno, professor e secretaria utilizariam serviços de autenticação e serviços acadêmicos, que dependem de um repositório. A imagem descreve uma arquitetura proposta, não uma implementação comprovada. O PDF original mantém os cinco diagramas de modelagem.
