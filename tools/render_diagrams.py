from __future__ import annotations

from dataclasses import dataclass, field
from html import escape
from math import atan2, cos, sin, pi
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
NAVY = "#17324D"
BLUE = "#245B83"
TEAL = "#0F766E"
INK = "#233548"
MUTED = "#5E7183"
PALE = "#EAF4FF"
PALE2 = "#F4F8FC"
GOLD = "#FFF2CC"
WHITE = "#FFFFFF"
LINE = "#65798C"


@dataclass
class Scene:
    width: int
    height: int
    title: str
    subtitle: str
    owner: str
    card: str
    shapes: list[tuple] = field(default_factory=list)

    def rect(self, x, y, w, h, fill=WHITE, stroke="none", sw=1, rx=0):
        self.shapes.append(("rect", x, y, w, h, fill, stroke, sw, rx))

    def line(self, x1, y1, x2, y2, stroke=LINE, sw=2, dash=None, arrow=None):
        self.shapes.append(("line", x1, y1, x2, y2, stroke, sw, dash))
        if arrow:
            angle = atan2(y2 - y1, x2 - x1)
            length = 14
            half = 6
            bx = x2 - length * cos(angle)
            by = y2 - length * sin(angle)
            px = half * sin(angle)
            py = -half * cos(angle)
            points = [(x2, y2), (bx + px, by + py), (bx - px, by - py)]
            fill = WHITE if arrow == "open" else stroke
            self.poly(points, fill, stroke, sw)

    def ellipse(self, x, y, w, h, fill=WHITE, stroke=BLUE, sw=2):
        self.shapes.append(("ellipse", x, y, w, h, fill, stroke, sw))

    def poly(self, points, fill=WHITE, stroke=BLUE, sw=2):
        self.shapes.append(("poly", tuple(points), fill, stroke, sw))

    def text(self, x, y, value, size=20, fill=INK, weight="normal", anchor="start", line_height=None):
        lines = value.split("\n") if isinstance(value, str) else list(value)
        self.shapes.append(("text", x, y, tuple(lines), size, fill, weight, anchor, line_height or size * 1.22))


def frame(scene: Scene):
    scene.rect(0, 0, scene.width, scene.height, WHITE, "none", 0)
    scene.rect(0, 0, scene.width, 112, NAVY, NAVY, 0)
    scene.text(46, 47, scene.title, 31, WHITE, "bold")
    scene.text(46, 81, scene.subtitle, 17, "#D8E7F2")
    chip_x = scene.width - 490
    scene.rect(chip_x, 22, 448, 68, "#244E68", "#4B7891", 1.5, 14)
    scene.text(chip_x + 18, 49, "Responsável: " + scene.owner, 18, WHITE, "bold")
    scene.text(chip_x + 18, 73, "Trello " + scene.card, 14, "#D8E7F2")
    scene.text(42, scene.height - 20, "PP1 | Modelagem UML | Proposta baseada nos cartões do projeto", 14, MUTED)


def box(scene: Scene, x, y, w, h, label, fill=PALE, stroke=BLUE, size=20, rx=14, weight="normal"):
    scene.rect(x, y, w, h, fill, stroke, 2, rx)
    lines = label.split("\n")
    line_height = size * 1.22
    first = y + h / 2 - (len(lines) - 1) * line_height / 2 + size * 0.34
    scene.text(x + w / 2, first, lines, size, INK, weight, "middle", line_height)


def oval(scene: Scene, cx, cy, w, h, label, size=20):
    scene.ellipse(cx - w / 2, cy - h / 2, w, h, PALE, BLUE, 2.2)
    lines = label.split("\n")
    lh = size * 1.2
    first = cy - (len(lines) - 1) * lh / 2 + size * 0.34
    scene.text(cx, first, lines, size, INK, "normal", "middle", lh)


def actor(scene: Scene, cx, top, label):
    scene.ellipse(cx - 17, top, 34, 34, WHITE, NAVY, 3)
    scene.line(cx, top + 34, cx, top + 91, NAVY, 3)
    scene.line(cx - 29, top + 54, cx + 29, top + 54, NAVY, 3)
    scene.line(cx, top + 91, cx - 27, top + 127, NAVY, 3)
    scene.line(cx, top + 91, cx + 27, top + 127, NAVY, 3)
    scene.text(cx, top + 153, label, 18, NAVY, "bold", "middle")


def make_use_cases() -> Scene:
    s = Scene(1500, 1060, "Casos de uso do portal acadêmico", "Atores e funcionalidades centrais do site da faculdade", "Felipe Rafael", "#39")
    frame(s)
    s.rect(230, 145, 1040, 760, "#FBFDFF", BLUE, 2.5, 20)
    s.text(750, 184, "Portal Acadêmico da Faculdade", 25, NAVY, "bold", "middle")
    # Actor associations stay behind the use-case ellipses.
    s.line(133, 500, 350, 425, LINE, 1.8)
    s.line(133, 500, 350, 585, LINE, 1.8)
    s.line(133, 500, 335, 745, LINE, 1.8)
    s.line(1367, 423, 1150, 425, LINE, 1.8)
    s.line(1367, 423, 1150, 585, LINE, 1.8)
    s.line(1367, 753, 1165, 745, LINE, 1.8)
    oval(s, 750, 270, 270, 88, "Autenticar usuário", 21)
    oval(s, 500, 425, 300, 92, "Realizar matrícula", 21)
    oval(s, 500, 585, 300, 92, "Consultar notas", 21)
    oval(s, 500, 745, 330, 92, "Consultar calendário\ne avisos", 20)
    oval(s, 1000, 425, 300, 92, "Consultar turmas", 21)
    oval(s, 1000, 585, 300, 92, "Lançar ou atualizar notas", 20)
    oval(s, 1000, 745, 330, 92, "Gerenciar turmas, disciplinas,\ncalendário e avisos", 18)
    actor(s, 100, 425, "Aluno")
    actor(s, 1400, 350, "Professor")
    actor(s, 1400, 680, "Secretaria /\nCoordenação")
    s.rect(280, 835, 940, 44, GOLD, "#C39A3B", 1.2, 10)
    s.text(750, 862, "As operações restritas pressupõem autenticação; regras de matrícula ficam configuráveis.", 16, INK, "normal", "middle")
    return s


def class_box(scene, x, y, w, h, name, attrs, stereotype=None):
    scene.rect(x, y, w, h, PALE2, BLUE, 2, 8)
    scene.rect(x, y, w, 42, "#DCECF8", BLUE, 1.5, 8)
    scene.rect(x, y + 34, w, 8, "#DCECF8", "none", 0)
    title = (stereotype + "\n" if stereotype else "") + name
    if stereotype:
        scene.text(x + w / 2, y + 18, stereotype, 13, MUTED, "normal", "middle")
        scene.text(x + w / 2, y + 38, name, 20, NAVY, "bold", "middle")
    else:
        scene.text(x + w / 2, y + 27, name, 21, NAVY, "bold", "middle")
    start_y = y + 67 if stereotype else y + 70
    scene.text(x + 15, start_y, attrs, 16, INK, "normal", "start", 22)


def make_classes() -> Scene:
    s = Scene(1680, 1190, "Modelo de domínio e classes", "Estrutura acadêmica, vínculos e dados consultados pelo portal", "Andrei Albuquerque", "#38")
    frame(s)
    # Inheritance bus and associations are drawn before class boxes.
    s.line(835, 290, 835, 322, LINE, 2)
    s.line(770, 322, 1410, 322, LINE, 2)
    for x in (770, 1090, 1410):
        s.line(x, 355, x, 322, LINE, 2)
    s.line(835, 322, 835, 290, LINE, 2, arrow="open")
    # Domain associations with multiplicities.
    row_y = 650
    for x1, x2 in ((230, 350), (550, 670), (870, 990), (1190, 1310)):
        s.line(x1, row_y, x2, row_y, LINE, 2)
    s.text(235, 635, "1", 15, MUTED)
    s.text(305, 635, "1..*", 15, MUTED)
    s.text(555, 635, "1", 15, MUTED)
    s.text(625, 635, "0..*", 15, MUTED)
    s.text(875, 635, "1", 15, MUTED)
    s.text(945, 635, "0..*", 15, MUTED)
    s.text(1195, 635, "1", 15, MUTED)
    s.text(1265, 635, "0..*", 15, MUTED)
    s.text(290, 674, "compõe", 14, MUTED, "normal", "middle")
    s.text(610, 674, "é ofertada em", 14, MUTED, "normal", "middle")
    s.text(930, 674, "recebe", 14, MUTED, "normal", "middle")
    s.text(1250, 674, "reúne", 14, MUTED, "normal", "middle")
    # Actors align with their main domain classes to keep associations clear.
    s.line(1090, 465, 1090, 615, LINE, 2)
    s.text(1105, 525, "realiza", 14, MUTED)
    s.line(770, 465, 770, 615, LINE, 2)
    s.text(782, 525, "ministra", 14, MUTED)
    # Academic office maintains calendar and notices. The outer route avoids the class row.
    s.line(1545, 412, 1625, 412, LINE, 2)
    s.line(1625, 412, 1625, 930, LINE, 2)
    s.line(1625, 930, 1520, 930, LINE, 2, arrow="open")
    s.text(1580, 885, "publica", 15, MUTED, "normal", "middle")
    s.line(1545, 412, 1650, 412, LINE, 2)
    s.line(1650, 412, 1650, 1040, LINE, 2)
    s.line(1650, 1040, 710, 1040, LINE, 2)
    s.line(600, 1040, 600, 1010, LINE, 2, arrow="open")
    s.text(1120, 1030, "mantém calendário", 15, MUTED, "normal", "middle")

    class_box(s, 660, 150, 350, 140, "Usuario", ["id: UUID", "nome: texto", "email: texto"], "<<abstrata>>")
    class_box(s, 970, 355, 240, 110, "Aluno", ["matricula: texto"])
    class_box(s, 650, 355, 240, 110, "Professor", ["registro: texto"])
    class_box(s, 1275, 355, 270, 110, "Secretaria", ["setor: texto"])
    class_box(s, 30, 615, 200, 165, "Curso", ["id: UUID", "codigo: texto", "nome: texto"])
    class_box(s, 350, 615, 200, 165, "Disciplina", ["id: UUID", "codigo: texto", "nome: texto", "cargaHoraria: inteiro"])
    class_box(s, 670, 615, 200, 165, "Turma", ["id: UUID", "periodo: texto", "status: StatusTurma"])
    class_box(s, 990, 615, 200, 165, "Matricula", ["id: UUID", "data: data", "status: StatusMatricula"])
    class_box(s, 1310, 615, 200, 165, "Nota", ["id: UUID", "etapa: texto", "valor: decimal"])
    class_box(s, 450, 870, 300, 140, "EventoAcademico", ["titulo: texto", "inicio/fim: dataHora"])
    class_box(s, 1300, 870, 220, 140, "Aviso", ["titulo: texto", "publicadoEm: dataHora"])
    return s


def diamond(scene, cx, cy, size, label):
    half = size / 2
    scene.poly([(cx, cy - half), (cx + half, cy), (cx, cy + half), (cx - half, cy)], GOLD, "#B7791F", 2)
    scene.text(cx, cy + 6, label, 16, INK, "bold", "middle")


def activity_start(scene, cx, cy):
    scene.ellipse(cx - 10, cy - 10, 20, 20, NAVY, NAVY, 1)


def activity_end(scene, cx, cy):
    scene.ellipse(cx - 15, cy - 15, 30, 30, WHITE, NAVY, 4)
    scene.ellipse(cx - 8, cy - 8, 16, 16, NAVY, NAVY, 1)


def make_activity() -> Scene:
    s = Scene(1500, 1060, "Atividades do fluxo de matrícula e consulta", "Dois fluxos acadêmicos em um único diagrama de atividade", "Samuel", "#36")
    frame(s)
    panels = [(40, 145, 690, 850), (770, 145, 690, 850)]
    for x, y, w, h in panels:
        s.rect(x, y, w, h, WHITE, "#B8C7D4", 2, 18)
    s.rect(41, 225, 343, 769, "#F5FAFF", "none", 0, 0)
    s.rect(385, 225, 344, 769, "#FBFCFD", "none", 0, 0)
    s.rect(771, 225, 343, 769, "#F5FAFF", "none", 0, 0)
    s.rect(1115, 225, 344, 769, "#FBFCFD", "none", 0, 0)
    s.line(385, 225, 385, 994, "#B8C7D4", 1.5)
    s.line(1115, 225, 1115, 994, "#B8C7D4", 1.5)
    s.text(385, 184, "Matrícula acadêmica", 23, NAVY, "bold", "middle")
    s.text(1115, 184, "Consulta de notas", 23, NAVY, "bold", "middle")
    s.text(212, 214, "Aluno", 16, MUTED, "bold", "middle")
    s.text(557, 214, "Portal", 16, MUTED, "bold", "middle")
    s.text(942, 214, "Aluno", 16, MUTED, "bold", "middle")
    s.text(1287, 214, "Portal", 16, MUTED, "bold", "middle")

    # Enrollment flow.
    activity_start(s, 212, 260)
    s.line(212, 270, 212, 292, arrow="closed")
    box(s, 92, 292, 240, 70, "Selecionar período\ne disciplinas", size=18)
    s.line(332, 327, 425, 327, arrow="closed")
    s.line(425, 327, 425, 392)
    s.line(425, 392, 435, 392, arrow="closed")
    box(s, 435, 392, 245, 88, "Validar pré-requisitos,\nvagas e conflitos", fill="#E8F6F3", stroke=TEAL, size=18)
    s.line(557, 480, 557, 490, arrow="closed")
    diamond(s, 557, 540, 100, "Válidas?")
    s.line(507, 540, 448, 540)
    s.line(448, 540, 448, 622)
    s.line(448, 622, 332, 622, arrow="closed")
    s.text(462, 525, "Não", 15, MUTED, "bold")
    box(s, 92, 587, 240, 70, "Corrigir disciplinas", fill=GOLD, stroke="#B7791F", size=18)
    s.line(212, 587, 212, 362, arrow="closed")
    s.line(557, 590, 557, 690)
    s.line(557, 690, 390, 690)
    s.line(390, 690, 390, 742)
    s.line(390, 742, 332, 742, arrow="closed")
    s.text(572, 635, "Sim", 15, MUTED, "bold")
    box(s, 92, 707, 240, 70, "Confirmar matrícula", size=18)
    s.line(332, 742, 415, 742)
    s.line(415, 742, 415, 840)
    s.line(415, 840, 435, 840, arrow="closed")
    box(s, 435, 800, 245, 80, "Registrar vínculo e\ngerar protocolo", fill="#E8F6F3", stroke=TEAL, size=18)
    s.line(557, 880, 557, 932, arrow="closed")
    activity_end(s, 557, 950)

    # Grade consultation flow.
    activity_start(s, 942, 260)
    s.line(942, 270, 942, 292, arrow="closed")
    box(s, 822, 292, 240, 70, "Escolher período", size=18)
    s.line(1062, 327, 1150, 327)
    s.line(1150, 327, 1150, 392)
    s.line(1150, 392, 1162, 392, arrow="closed")
    box(s, 1162, 392, 245, 80, "Buscar notas\npublicadas", fill="#E8F6F3", stroke=TEAL, size=18)
    s.line(1284, 472, 1284, 490, arrow="closed")
    diamond(s, 1284, 540, 100, "Disponíveis?")
    s.line(1234, 540, 1085, 540)
    s.line(1085, 540, 1085, 654)
    s.line(1085, 654, 1062, 654, arrow="closed")
    s.text(1095, 525, "Sim", 15, MUTED, "bold")
    box(s, 822, 619, 240, 70, "Exibir notas por\ndisciplina", size=18)
    s.line(1284, 590, 1284, 815)
    s.line(1284, 815, 1062, 815, arrow="closed")
    s.text(1298, 705, "Não", 15, MUTED, "bold")
    box(s, 822, 780, 240, 70, "Informar lançamento\npendente", fill=GOLD, stroke="#B7791F", size=18)
    s.line(942, 689, 942, 695, arrow="closed")
    activity_end(s, 942, 710)
    s.line(942, 850, 942, 875, arrow="closed")
    activity_end(s, 942, 890)
    return s


def participant(scene, x, y, label, width=200):
    scene.rect(x - width / 2, y, width, 64, PALE, BLUE, 2, 12)
    lines = label.split("\n")
    lh = 18
    first = y + 29 - (len(lines) - 1) * lh / 2
    scene.text(x, first, lines, 16, NAVY, "bold", "middle", lh)
    scene.line(x, y + 64, x, scene.height - 65, "#91A4B4", 1.5, dash=[6, 6])


def message(scene, x1, x2, y, label, reply=False):
    scene.line(x1, y, x2, y, BLUE if not reply else TEAL, 2, dash=[7, 5] if reply else None, arrow="closed")
    scene.text((x1 + x2) / 2, y - 9, label, 15, INK, "normal", "middle")


def make_sequence_enrollment() -> Scene:
    s = Scene(1500, 1100, "Sequência de matrícula", "Interações e validações para registrar uma matrícula acadêmica", "Joab (joabfr4nca2018)", "#40")
    frame(s)
    xs = [135, 430, 725, 1020, 1315]
    labels = ["Aluno", "Portal web", "Serviço de\nmatrícula", "Validador\nacadêmico", "Repositório\nacadêmico"]
    for x, label in zip(xs, labels):
        participant(s, x, 145, label, 210)
    message(s, xs[0], xs[1], 245, "Solicitar matrícula no período")
    message(s, xs[1], xs[2], 292, "Listar ofertas disponíveis")
    message(s, xs[2], xs[4], 339, "Consultar turmas, vagas e vínculos")
    message(s, xs[4], xs[2], 386, "Retornar ofertas", reply=True)
    message(s, xs[2], xs[1], 433, "Apresentar opções", reply=True)
    message(s, xs[1], xs[0], 480, "Exibir disciplinas disponíveis", reply=True)
    message(s, xs[0], xs[1], 527, "Confirmar seleção")
    message(s, xs[1], xs[2], 574, "Registrar solicitação")
    message(s, xs[2], xs[3], 621, "Validar pré-requisitos, vagas e horários")
    # Combined fragment with the two business outcomes.
    s.rect(90, 655, 1370, 395, "none", "#52697D", 2, 0)
    s.rect(90, 655, 55, 30, "#EAF4FF", "#52697D", 1.5, 0)
    s.text(117, 676, "alt", 15, NAVY, "bold", "middle")
    s.text(165, 678, "[seleção válida]", 15, MUTED, "bold")
    message(s, xs[3], xs[2], 715, "Seleção válida", reply=True)
    message(s, xs[2], xs[4], 760, "Gravar matrícula")
    message(s, xs[4], xs[2], 805, "Retornar protocolo", reply=True)
    message(s, xs[2], xs[1], 850, "Confirmar matrícula", reply=True)
    message(s, xs[1], xs[0], 895, "Exibir protocolo", reply=True)
    s.line(90, 920, 1460, 920, "#52697D", 1.5, dash=[6, 5])
    s.text(165, 945, "[há pendências]", 15, MUTED, "bold")
    message(s, xs[3], xs[2], 965, "Retornar regras não atendidas", reply=True)
    message(s, xs[2], xs[1], 1000, "Informar motivos", reply=True)
    message(s, xs[1], xs[0], 1035, "Exibir pendências", reply=True)
    return s


def make_sequence_grades() -> Scene:
    s = Scene(1500, 1000, "Sequência de consulta de notas", "Resposta do portal quando as notas estão disponíveis ou pendentes", "Pedro Henrique Almeida Durães", "#37")
    frame(s)
    xs = [180, 560, 940, 1320]
    labels = ["Aluno", "Portal web", "Serviço de notas", "Repositório\nacadêmico"]
    for x, label in zip(xs, labels):
        participant(s, x, 145, label, 220)
    message(s, xs[0], xs[1], 255, "Consultar notas do período")
    message(s, xs[1], xs[2], 315, "Buscar notas do aluno")
    message(s, xs[2], xs[3], 375, "Consultar matrículas e notas publicadas")
    message(s, xs[3], xs[2], 435, "Retornar notas e situação", reply=True)
    s.rect(110, 495, 1330, 350, "none", "#52697D", 2, 0)
    s.rect(110, 495, 55, 30, "#EAF4FF", "#52697D", 1.5, 0)
    s.text(137, 516, "alt", 15, NAVY, "bold", "middle")
    s.text(185, 518, "[notas publicadas]", 15, MUTED, "bold")
    message(s, xs[2], xs[1], 570, "Retornar notas por disciplina e etapa", reply=True)
    message(s, xs[1], xs[0], 625, "Exibir notas", reply=True)
    s.line(110, 670, 1440, 670, "#52697D", 1.5, dash=[6, 5])
    s.text(185, 695, "[notas pendentes]", 15, MUTED, "bold")
    message(s, xs[2], xs[1], 735, "Informar lançamento pendente", reply=True)
    message(s, xs[1], xs[0], 790, "Exibir aviso de pendência", reply=True)
    return s


def render_svg(scene: Scene, path: Path):
    items = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{scene.width}" height="{scene.height}" viewBox="0 0 {scene.width} {scene.height}">']
    items.append(f'<title>{escape(scene.title)}</title>')
    items.append(f'<desc>{escape("Responsável: " + scene.owner + ". " + scene.subtitle)}</desc>')
    for item in scene.shapes:
        kind = item[0]
        if kind == "rect":
            _, x, y, w, h, fill, stroke, sw, rx = item
            items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        elif kind == "ellipse":
            _, x, y, w, h, fill, stroke, sw = item
            items.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        elif kind == "line":
            _, x1, y1, x2, y2, stroke, sw, dash = item
            dash_attr = f' stroke-dasharray="{",".join(map(str, dash))}"' if dash else ""
            items.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{dash_attr}/>')
        elif kind == "poly":
            _, points, fill, stroke, sw = item
            pts = " ".join(f"{x},{y}" for x, y in points)
            items.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')
        elif kind == "text":
            _, x, y, lines, size, fill, weight, anchor, line_height = item
            anchor_map = {"start": "start", "middle": "middle", "end": "end"}
            for i, line in enumerate(lines):
                items.append(f'<text x="{x}" y="{y + i*line_height}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if weight == "bold" else 400}" fill="{fill}" text-anchor="{anchor_map[anchor]}">{escape(line)}</text>')
    items.append("</svg>")
    path.write_text("\n".join(items), encoding="utf-8")


def register_fonts():
    windows_fonts = Path("C:/Windows/Fonts")
    regular = windows_fonts / "arial.ttf"
    bold = windows_fonts / "arialbd.ttf"
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("DiagramArial", str(regular)))
        pdfmetrics.registerFont(TTFont("DiagramArialBold", str(bold)))
        return "DiagramArial", "DiagramArialBold"
    return "Helvetica", "Helvetica-Bold"


def pdf_polygon(c, points, fill, stroke, sw, height):
    p = c.beginPath()
    p.moveTo(points[0][0], height - points[0][1])
    for x, y in points[1:]:
        p.lineTo(x, height - y)
    p.close()
    c.setLineWidth(sw)
    if fill == "none":
        c.setFillColor(HexColor(WHITE))
        c.drawPath(p, stroke=1, fill=0)
    else:
        c.setFillColor(HexColor(fill))
        c.setStrokeColor(HexColor(stroke))
        c.drawPath(p, stroke=1, fill=1)


def render_pdf(scenes: list[Scene], path: Path):
    regular, bold = register_fonts()
    page_w, page_h = landscape(A4)
    c = canvas.Canvas(str(path), pagesize=(page_w, page_h), pageCompression=1)
    c.setTitle("PP1 - Diagramas UML do Portal Acadêmico")
    c.setAuthor("Grupo PP1 - Projeto do site da faculdade")
    for scene in scenes:
        scale = min((page_w - 34) / scene.width, (page_h - 30) / scene.height)
        xoff = (page_w - scene.width * scale) / 2
        yoff = (page_h - scene.height * scale) / 2
        c.saveState()
        c.translate(xoff, yoff)
        c.scale(scale, scale)
        for item in scene.shapes:
            kind = item[0]
            if kind == "rect":
                _, x, y, w, h, fill, stroke, sw, rx = item
                if fill != "none":
                    c.setFillColor(HexColor(fill))
                if stroke != "none":
                    c.setStrokeColor(HexColor(stroke))
                c.setLineWidth(sw)
                c.roundRect(x, scene.height - y - h, w, h, rx, stroke=stroke != "none", fill=fill != "none")
            elif kind == "ellipse":
                _, x, y, w, h, fill, stroke, sw = item
                c.setFillColor(HexColor(fill))
                c.setStrokeColor(HexColor(stroke))
                c.setLineWidth(sw)
                c.ellipse(x, scene.height - y - h, x + w, scene.height - y, stroke=1, fill=1)
            elif kind == "line":
                _, x1, y1, x2, y2, stroke, sw, dash = item
                c.setStrokeColor(HexColor(stroke))
                c.setLineWidth(sw)
                c.setDash(dash or [])
                c.line(x1, scene.height - y1, x2, scene.height - y2)
                c.setDash([])
            elif kind == "poly":
                _, points, fill, stroke, sw = item
                pdf_polygon(c, points, fill, stroke, sw, scene.height)
            elif kind == "text":
                _, x, y, lines, size, fill, weight, anchor, line_height = item
                c.setFillColor(HexColor(fill))
                face = bold if weight == "bold" else regular
                c.setFont(face, size)
                for i, line in enumerate(lines):
                    width = pdfmetrics.stringWidth(line, face, size)
                    xx = x - width / 2 if anchor == "middle" else x - width if anchor == "end" else x
                    c.drawString(xx, scene.height - (y + i * line_height), line)
        c.restoreState()
        c.showPage()
    c.save()


def main():
    cases = make_use_cases()
    classes = make_classes()
    activities = make_activity()
    seq_enrollment = make_sequence_enrollment()
    seq_grades = make_sequence_grades()
    outputs = [
        (cases, ROOT / "diagramas" / "casos-de-uso" / "casos-de-uso-portal.svg"),
        (classes, ROOT / "diagramas" / "classes" / "modelo-de-dominio.svg"),
        (activities, ROOT / "diagramas" / "atividades" / "matricula.svg"),
        (seq_enrollment, ROOT / "diagramas" / "sequencia" / "matricula.svg"),
        (seq_grades, ROOT / "diagramas" / "sequencia" / "consulta-notas.svg"),
    ]
    for scene, path in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        render_svg(scene, path)
    pdf = ROOT / "output" / "pdf" / "pp1-diagramas-uml.pdf"
    pdf.parent.mkdir(parents=True, exist_ok=True)
    render_pdf([cases, classes, activities, seq_enrollment, seq_grades], pdf)
    print(f"Gerados {len(outputs)} SVGs e PDF: {pdf}")


if __name__ == "__main__":
    main()
