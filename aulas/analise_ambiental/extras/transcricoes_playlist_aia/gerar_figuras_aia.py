# -*- coding: utf-8 -*-
"""Figuras originais da aula 5.1 (AIA e Planejamento Ambiental).

Gera, em PNG (300 dpi) e SVG, com a paleta do tema UEFS:
  (a) resistencia_resiliencia      - funcao do ecossistema ao longo do tempo
  (b) escala_qualidade_ambiental   - gradiente de qualidade ambiental
  (c) aia_aspecto_impacto          - cadeia atividade > aspecto > impacto > degradacao
  (d) aia_licencas_lp_li_lo        - fases do projeto e licencas ambientais
  (e) aia_areas_influencia         - ADA, AID e AII
  (f) aia_hierarquia_mitigacao     - evitar > minimizar > recuperar > compensar
  (g) aia_matriz_leopold           - esquema da matriz de interacao

Convencoes do projeto: DejaVu Sans, 300 dpi, PNG + SVG, bbox tight, fundo branco.
Regra desta revisao: nenhum traco, seta ou linha-guia pode cruzar texto.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Ellipse, FancyBboxPatch, Rectangle
from pathlib import Path

SAIDA = Path(__file__).resolve().parents[4] / "img"

# paleta alinhada ao tema uefs.scss
AZUL = "#2135A6"
AZUL_PROF = "#27368C"
AZUL_APOIO = "#586BA6"
AZUL_CLARO = "#C7D0EA"
AZUL_PALIDO = "#E8ECF7"
CINZA = "#6B7280"
CINZA_CLARO = "#D7DBE3"
GRAFITE = "#0D0D0D"
VERMELHO = "#B03A2E"
VERDE = "#2E7D32"
ROXO = "#7D3C98"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.labelsize": 12,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.8,
    "figure.facecolor": "white",
    "svg.fonttype": "none",
})


def salvar(fig, nome):
    for ext in ("png", "svg"):
        fig.savefig(SAIDA / f"{nome}.{ext}", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("OK:", SAIDA / f"{nome}.png")


def caixa(ax, x, y, w, h, face, edge, radius=0.12, lw=1.2, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z,
    ))


def seta(ax, p0, p1, color=AZUL_APOIO, lw=1.6, estilo="-|>", z=3):
    ax.annotate("", xy=p1, xytext=p0, zorder=z,
                arrowprops=dict(arrowstyle=estilo, color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=14))


# ============================================================ (a) resiliencia
fig, ax = plt.subplots(figsize=(7.6, 4.3))

NIVEL, FUNDO = 5.0, 1.5
t1 = np.linspace(0.00, 4.00, 400)
y1 = NIVEL + 0.25 * np.sin(2 * np.pi * t1)
t2 = np.linspace(4.00, 4.55, 60)                       # queda abrupta
y2 = NIVEL + (FUNDO - NIVEL) * (t2 - 4.00) / 0.55
t3 = np.linspace(4.55, 10.00, 400)                     # recuperacao
y3 = FUNDO + (NIVEL - FUNDO) * (1 - np.exp(-(t3 - 4.55) / 1.55))
t4 = np.linspace(10.00, 13.60, 400)
y4 = NIVEL + 0.25 * np.sin(2 * np.pi * (t4 - 10.0) + 0.3)

ax.axhspan(4.75, 5.25, color=AZUL_PALIDO, zorder=0)
for yy in (4.75, 5.25):
    ax.axhline(yy, color=CINZA, ls=":", lw=0.9, zorder=1)

for tt, yy in ((t1, y1), (t2, y2), (t3, y3), (t4, y4)):
    ax.plot(tt, yy, color=AZUL, lw=2.4, solid_capstyle="round", zorder=4)

# guia do nivel de fundo, curta, sem cruzar texto
ax.plot([3.60, 4.55], [FUNDO, FUNDO], color=CINZA, ls=":", lw=0.9, zorder=1)

# resistencia = magnitude da queda (seta vertical; texto a esquerda dela)
ax.annotate("", xy=(3.85, 4.75), xytext=(3.85, FUNDO), zorder=5,
            arrowprops=dict(arrowstyle="<->", color=ROXO, lw=1.6, mutation_scale=13))
ax.text(3.65, (4.75 + FUNDO) / 2, "Resistência\n(magnitude\nda queda)",
        color=ROXO, fontsize=9.5, ha="right", va="center", linespacing=1.35)

# resiliencia = tempo de retorno (seta horizontal; texto abaixo dela)
ax.annotate("", xy=(10.00, 0.95), xytext=(4.55, 0.95), zorder=5,
            arrowprops=dict(arrowstyle="<->", color=VERDE, lw=1.6, mutation_scale=13))
ax.text(7.28, 0.50, "Resiliência (tempo de retorno ao estado de referência)",
        color=VERDE, fontsize=9.5, ha="center", va="center")

# rotulos superiores, todos acima da curva
ax.text(0.10, 6.05, "Amplitude normal de variação\n(sistema estável)",
        color=CINZA, fontsize=9.5, ha="left", va="bottom", linespacing=1.35)
ax.annotate("Perturbação", xy=(4.28, 5.50), xytext=(4.95, 6.05),
            color=VERMELHO, fontsize=9.5, ha="left", va="bottom",
            arrowprops=dict(arrowstyle="->", color=VERMELHO, lw=1.4))
ax.text(10.05, 6.05, "Estado de referência\nrestabelecido",
        color=CINZA, fontsize=9.5, ha="left", va="bottom", linespacing=1.35)

ax.set_xlabel("Tempo", labelpad=8)
ax.set_ylabel("Função do ecossistema", labelpad=8)
ax.set_xlim(-0.2, 14.4)
ax.set_ylim(0, 7.1)
ax.set_xticks([])
ax.set_yticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
salvar(fig, "resistencia_resiliencia")

# ================================================= (b) escala de qualidade
fig, ax = plt.subplots(figsize=(7.6, 2.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 2.05)
ax.axis("off")

cmap = LinearSegmentedColormap.from_list(
    "qualidade", ["#8E1B16", "#C0392B", "#E08B2E", "#E8C33D", "#8FAE3F", "#2E7D32"]
)
ax.imshow(np.linspace(0, 1, 512).reshape(1, -1), cmap=cmap,
          extent=[0, 10, 0.80, 1.32], aspect="auto", zorder=1)

for x, label in [(1.0, "Altamente degradado"),
                 (5.0, "Agrícola / urbano\n(qualidade intermediária)"),
                 (9.0, "Próximo do natural")]:
    ax.plot([x, x], [1.32, 1.52], color="#333333", lw=0.9, zorder=3)
    ax.text(x, 1.58, label, ha="center", va="bottom", fontsize=9.5, linespacing=1.3)

# eixo de leitura abaixo da barra; rotulos abaixo da seta
ax.annotate("", xy=(9.85, 0.55), xytext=(0.15, 0.55), zorder=3,
            arrowprops=dict(arrowstyle="->", color="#333333", lw=1.5, mutation_scale=16))
ax.text(0.15, 0.36, "Menor qualidade ambiental", ha="left", va="top",
        fontsize=9.5, color="#333333")
ax.text(9.85, 0.36, "Maior qualidade ambiental", ha="right", va="top",
        fontsize=9.5, color="#333333")
salvar(fig, "escala_qualidade_ambiental")

# ============================================== (c) cadeia aspecto x impacto
fig, ax = plt.subplots(figsize=(9.8, 3.6))
ax.set_xlim(0, 10.6)
ax.set_ylim(0, 3.95)
ax.axis("off")

conceito = [
    "Atividade,\nproduto\nou serviço",
    "Aspecto ambiental\n(o que interage\ncom o meio)",
    "Impacto ambiental\n(alteração de um\ncomponente do meio)",
    "Degradação\nambiental\n(perda de serviços\necossistêmicos)",
]
exemplo = [
    "Operação de lavra",
    "Lançamento de\nefluente no rio",
    "Queda do oxigênio\ndissolvido a jusante",
    "Perda da pesca e do\nabastecimento local",
]
W, GAP = 2.2, 0.4
centros = [0.25 + W / 2 + i * (W + GAP) for i in range(4)]

for i, (cx, txt_c, txt_e) in enumerate(zip(centros, conceito, exemplo)):
    tom = [AZUL_APOIO, AZUL, AZUL_PROF, VERMELHO][i]
    fundo = "#F7E3E0" if i == 3 else AZUL_PALIDO
    caixa(ax, cx - W / 2, 2.05, W, 1.25, fundo, tom, lw=1.4)
    ax.text(cx, 2.675, txt_c, ha="center", va="center", fontsize=9,
            color=tom, fontweight="bold", linespacing=1.35, zorder=4)
    caixa(ax, cx - W / 2, 0.55, W, 0.95, "#FFFFFF", CINZA_CLARO, lw=1.0)
    ax.text(cx, 1.025, txt_e, ha="center", va="center", fontsize=8.8,
            color=CINZA, style="italic", linespacing=1.35, zorder=4)
    ax.plot([cx, cx], [1.50, 2.05], color=CINZA_CLARO, ls=":", lw=1.1, zorder=1)
    if i < 3:
        seta(ax, (cx + W / 2 + 0.04, 2.675), (cx + W / 2 + GAP - 0.04, 2.675), color=AZUL_APOIO)
        seta(ax, (cx + W / 2 + 0.04, 1.025), (cx + W / 2 + GAP - 0.04, 1.025),
             color=CINZA, lw=1.2)

ax.text(0.25, 3.60, "Cadeia causal", fontsize=10, color=GRAFITE,
        fontweight="bold", ha="left", va="bottom")
ax.text(0.25, 0.22, "Uma atividade gera vários aspectos; cada aspecto desencadeia vários impactos.",
        fontsize=9, color=CINZA, ha="left", va="center")
salvar(fig, "aia_aspecto_impacto")

# ============================================ (d) licencas LP / LI / LO
fig, ax = plt.subplots(figsize=(10.0, 3.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 3.95)
ax.axis("off")

fases = ["Planejamento e concepção", "Implantação (obra)", "Operação"]
licencas = [
    ("LP · Licença Prévia",
     "Aprova a concepção e a\nlocalização. Exige EIA/RIMA e\naudiência pública nos casos de\nimpacto significativo."),
    ("LI · Licença de Instalação",
     "Autoriza a construção.\nConsolida os Programas Básicos\nAmbientais (PBA) e as\ncondicionantes da LP."),
    ("LO · Licença de Operação",
     "Autoriza o funcionamento.\nExige monitoramento contínuo\ne renovação periódica\nda licença."),
]
W = 3.4
centros = [2.0, 6.0, 10.0]
tons = [AZUL_APOIO, AZUL_PROF, AZUL]

for cx, fase, (titulo, desc), tom in zip(centros, fases, licencas, tons):
    caixa(ax, cx - W / 2, 3.02, W, 0.52, AZUL_PALIDO, AZUL_CLARO, radius=0.08, lw=1.0)
    ax.text(cx, 3.28, fase, ha="center", va="center", fontsize=9.5,
            color=AZUL_PROF, fontweight="bold", zorder=4)
    caixa(ax, cx - W / 2, 0.90, W, 1.80, "#FFFFFF", tom, lw=1.6)
    caixa(ax, cx - W / 2, 2.22, W, 0.48, tom, tom, lw=1.6)
    ax.text(cx, 2.46, titulo, ha="center", va="center", fontsize=10.5,
            color="white", fontweight="bold", zorder=4)
    ax.text(cx, 1.53, desc, ha="center", va="center", fontsize=8.4,
            color=GRAFITE, linespacing=1.5, zorder=4)

# setas na faixa dos titulos: o vao entre as caixas esta livre de texto
for cx in centros[:-1]:
    seta(ax, (cx + W / 2 + 0.06, 2.46), (cx + W / 2 + 0.54, 2.46), color=AZUL_APOIO, lw=1.8)

ax.text(6.0, 0.42, "A abrangência dos impactos define o órgão licenciador: municipal, estadual ou federal.",
        ha="center", va="center", fontsize=9, color=CINZA)
salvar(fig, "aia_licencas_lp_li_lo")

# ================================================== (e) areas de influencia
fig, ax = plt.subplots(figsize=(9.4, 4.8))
ax.set_xlim(0, 13)
ax.set_ylim(-0.6, 6.4)
ax.axis("off")

ax.add_patch(Ellipse((3.5, 3.1), 6.6, 5.4, facecolor=AZUL_PALIDO,
                     edgecolor=AZUL_APOIO, lw=1.4, ls="--", zorder=1))
ax.add_patch(Ellipse((3.3, 2.9), 4.3, 3.6, facecolor=AZUL_CLARO,
                     edgecolor=AZUL_PROF, lw=1.6, zorder=2))
ax.add_patch(Ellipse((2.9, 2.7), 1.9, 1.5, facecolor=AZUL,
                     edgecolor=AZUL_PROF, lw=1.6, zorder=3))

ax.text(3.5, 5.30, "AII", ha="center", va="center", fontsize=12,
        color=AZUL_APOIO, fontweight="bold", zorder=4)
ax.text(3.3, 4.15, "AID", ha="center", va="center", fontsize=12,
        color=AZUL_PROF, fontweight="bold", zorder=4)
ax.text(2.9, 2.70, "ADA", ha="center", va="center", fontsize=11,
        color="white", fontweight="bold", zorder=4)

legenda = [
    (AZUL, AZUL_PROF, "ADA - Área Diretamente Afetada",
     "Área física ocupada pelo empreendimento:\ncanteiro, acessos, cava, barramento."),
    (AZUL_CLARO, AZUL_PROF, "AID - Área de Influência Direta",
     "Onde o impacto pode ser atribuído\ncausalmente à obra: ruído, poeira,\nsupressão, alteração de vazão."),
    (AZUL_PALIDO, AZUL_APOIO, "AII - Área de Influência Indireta",
     "Efeitos secundários e sistêmicos: pressão\nsobre serviços urbanos, dinâmica\neconômica, bacia a jusante."),
]
y = 5.55
for face, edge, titulo, desc in legenda:
    ax.add_patch(Rectangle((7.4, y - 0.26), 0.42, 0.30, facecolor=face,
                           edgecolor=edge, lw=1.2, zorder=3))
    ax.text(8.05, y - 0.11, titulo, ha="left", va="center", fontsize=10,
            color=AZUL_PROF, fontweight="bold")
    ax.text(8.05, y - 0.62, desc, ha="left", va="top", fontsize=8.8,
            color=GRAFITE, linespacing=1.45)
    y -= 1.95

ax.text(0.10, -0.30, "A delimitação muda conforme o meio analisado: a AII do meio biótico "
                     "raramente coincide com a do meio socioeconômico.",
        ha="left", va="center", fontsize=9, color=CINZA)
salvar(fig, "aia_areas_influencia")

# ============================================= (f) hierarquia da mitigacao
fig, ax = plt.subplots(figsize=(9.4, 4.2))
ax.set_xlim(0, 12.4)
ax.set_ylim(-1.35, 6.6)
ax.axis("off")

alturas = [5.00, 3.60, 2.40, 1.40, 0.70]
base = ["Impacto\npotencial", "após\nevitar", "após\nminimizar", "após\nrecuperar",
        "Impacto residual\ncompensado"]
tons = ["#B03A2E", "#C96A45", "#D79A4E", "#9FAE52", VERDE]
acoes = ["1. EVITAR", "2. MINIMIZAR", "3. RECUPERAR", "4. COMPENSAR"]
W, GAP = 1.50, 1.00
centros = [0.45 + W / 2 + i * (W + GAP) for i in range(5)]

ax.plot([0.15, 12.25], [0, 0], color="#333333", lw=1.0, zorder=1)
for cx, h, lbl, tom in zip(centros, alturas, base, tons):
    ax.add_patch(Rectangle((cx - W / 2, 0), W, h, facecolor=tom,
                           edgecolor="white", lw=1.0, zorder=2))
    ax.text(cx, -0.20, lbl, ha="center", va="top", fontsize=9,
            color=GRAFITE, linespacing=1.35)

for i, titulo in enumerate(acoes):
    gx = (centros[i] + centros[i + 1]) / 2
    topo = alturas[i]
    seta(ax, (centros[i] + W / 2 + 0.06, topo + 0.24),
         (centros[i + 1] - W / 2 - 0.06, topo + 0.24), color=AZUL_PROF, lw=1.6)
    ax.text(gx, topo + 0.44, titulo, ha="center", va="bottom", fontsize=9.5,
            color=AZUL_PROF, fontweight="bold")

ax.text(0.45, 6.40, "Impacto ambiental remanescente a cada etapa da hierarquia",
        ha="left", va="top", fontsize=10, color=GRAFITE, fontweight="bold")
salvar(fig, "aia_hierarquia_mitigacao")

# ================================================== (g) matriz de Leopold
fig, ax = plt.subplots(figsize=(8.4, 4.8))
acoes_col = ["Supressão\nde vegetação", "Terraplenagem", "Tráfego de\nveículos",
             "Lançamento\nde efluente", "Contratação\nde mão de obra"]
fatores = ["Qualidade do ar", "Qualidade da água", "Solos", "Fauna terrestre", "Emprego e renda"]
# (magnitude com sinal, importancia); None = sem interacao
celulas = [
    [(-4, 5), (-6, 6), (-5, 4), None, None],
    [(-3, 4), (-5, 7), None, (-8, 9), None],
    [(-7, 7), (-8, 8), None, (-3, 4), None],
    [(-8, 9), (-5, 6), (-4, 5), (-6, 7), None],
    [None, None, None, None, (7, 6)],
]

NC, NR = len(acoes_col), len(fatores)
ax.set_xlim(-0.05, NC + 0.05)
ax.set_ylim(-1.15, NR + 1.05)
ax.axis("off")

for j, acao in enumerate(acoes_col):
    ax.text(j + 0.5, NR + 0.12, acao, ha="center", va="bottom", fontsize=8.8,
            color=AZUL_PROF, fontweight="bold", linespacing=1.3)
for i, fator in enumerate(fatores):
    ax.text(-0.12, NR - i - 0.5, fator, ha="right", va="center", fontsize=8.8,
            color=AZUL_PROF, fontweight="bold")

for i in range(NR):
    for j in range(NC):
        v = celulas[i][j]
        y = NR - i - 1
        face = "#FFFFFF"
        if v is not None:
            face = "#F7E3E0" if v[0] < 0 else "#E3F0E4"
        ax.add_patch(Rectangle((j, y), 1, 1, facecolor=face,
                               edgecolor="#9CA3AF", lw=0.8, zorder=2))
        if v is not None:
            ax.plot([j + 0.06, j + 0.94], [y + 0.94, y + 0.06],
                    color="#9CA3AF", lw=0.7, zorder=3)
            cor = VERMELHO if v[0] < 0 else VERDE
            ax.text(j + 0.24, y + 0.70, f"{v[0]:+d}", ha="center", va="center",
                    fontsize=9, color=cor, fontweight="bold", zorder=4)
            ax.text(j + 0.76, y + 0.28, f"{v[1]}", ha="center", va="center",
                    fontsize=9, color=GRAFITE, zorder=4)

ax.text(0, -0.22,
        "Cada célula cruza uma ação do projeto com um fator ambiental: magnitude no canto\n"
        "superior esquerdo (−10 a +10, com sinal) e importância no canto inferior direito (1 a 10).",
        ha="left", va="top", fontsize=8.8, color=CINZA, linespacing=1.45)
salvar(fig, "aia_matriz_leopold")

# ============================================ (h) nove etapas do processo
fig, ax = plt.subplots(figsize=(10.4, 3.9))
ax.set_xlim(0, 12.6)
ax.set_ylim(0.78, 5.35)
ax.axis("off")

linhas = [
    ("PREPARAÇÃO\nDO ESTUDO", AZUL_APOIO,
     [(1, "Apresentação\nda proposta"), (2, "Triagem"), (3, "Determinação\ndo escopo")]),
    ("ESTUDO\nE ANÁLISE", AZUL_PROF,
     [(4, "Elaboração\ndo EIA/RIMA"), (5, "Análise técnica\ndo estudo"),
      (6, "Consulta e\naudiência pública")]),
    ("DECISÃO E\nSEGUIMENTO", AZUL,
     [(7, "Decisão do\nórgão ambiental"), (8, "Monitoramento\ne gestão"), (9, "Acompanhamento")]),
]
XL, WC, GC = 2.05, 3.05, 0.45
H, GV = 1.20, 0.42
y = 5.30 - H

for titulo, tom, cartoes in linhas:
    caixa(ax, 0.10, y, XL - 0.30, H, AZUL_PALIDO, tom, radius=0.08, lw=1.2)
    ax.text(0.10 + (XL - 0.30) / 2, y + H / 2, titulo, ha="center", va="center",
            fontsize=8.4, color=tom, fontweight="bold", linespacing=1.4, zorder=4)
    for j, (n, rot) in enumerate(cartoes):
        x = XL + j * (WC + GC)
        caixa(ax, x, y, WC, H, "#FFFFFF", tom, lw=1.5)
        ax.add_patch(plt.Circle((x + 0.42, y + H - 0.36), 0.22, color=tom, zorder=4))
        ax.text(x + 0.42, y + H - 0.36, str(n), ha="center", va="center",
                fontsize=9.5, color="white", fontweight="bold", zorder=5)
        ax.text(x + WC / 2 + 0.22, y + H / 2 - 0.14, rot, ha="center", va="center",
                fontsize=9, color=GRAFITE, linespacing=1.35, zorder=4)
        if j < 2:
            seta(ax, (x + WC + 0.06, y + H / 2), (x + WC + GC - 0.06, y + H / 2),
                 color=tom, lw=1.6)
    y -= (H + GV)
salvar(fig, "aia_etapas_processo")

# ================================== (i) planejamento e execucao do estudo
fig, ax = plt.subplots(figsize=(10.4, 4.9))
ax.set_xlim(0, 12.6)
ax.set_ylim(0, 6.3)
ax.axis("off")

W, G, H = 2.85, 0.35, 1.00
centros4 = [0.15 + W / 2 + i * (W + G) for i in range(4)]

ax.text(0.15, 6.18, "PLANEJAMENTO DO ESTUDO", fontsize=9.5, color=AZUL_APOIO,
        fontweight="bold", ha="left", va="top")
plan = ["Alternativas locacionais e\nreconhecimento\nambiental inicial",
        "Identificação preliminar\ndos impactos",
        "Determinação\ndo escopo",
        "Plano de trabalho e\ntermo de referência"]
for i, (cx, txt) in enumerate(zip(centros4, plan)):
    caixa(ax, cx - W / 2, 4.65, W, H, AZUL_PALIDO, AZUL_APOIO, lw=1.4)
    ax.text(cx, 5.15, txt, ha="center", va="center", fontsize=8.6,
            color=AZUL_PROF, linespacing=1.4, zorder=4)
    if i < 3:
        seta(ax, (cx + W / 2 + 0.04, 5.15), (cx + W / 2 + G - 0.04, 5.15), color=AZUL_APOIO)

ax.text(0.15, 4.26, "EXECUÇÃO DO ESTUDO", fontsize=9.5, color=AZUL,
        fontweight="bold", ha="left", va="top")
exe = ["Estudos de base\n(diagnóstico ambiental)",
       "Análise dos impactos",
       "Prognóstico e comparação\nde cenários",
       "EIA e RIMA"]
for i, (cx, txt) in enumerate(zip(centros4, exe)):
    destaque = (i == 1)
    caixa(ax, cx - W / 2, 2.70, W, H, "#EDF1FA" if destaque else "#FFFFFF",
          AZUL, lw=1.8 if destaque else 1.4)
    ax.text(cx, 3.20, txt, ha="center", va="center", fontsize=8.8,
            color=AZUL_PROF, fontweight="bold" if destaque else "normal",
            linespacing=1.4, zorder=4)
    if i < 3:
        seta(ax, (cx + W / 2 + 0.04, 3.20), (cx + W / 2 + G - 0.04, 3.20), color=AZUL)

ax.plot([centros4[1], centros4[1]], [2.70, 2.08], color=AZUL, ls=":", lw=1.2, zorder=1)
ax.plot([2.00, 10.60], [2.08, 2.08], color=AZUL, ls=":", lw=1.2, zorder=1)
det = ["Identificação\ndos impactos", "Previsão de magnitude\ne importância",
       "Plano de gestão\nambiental"]
WD = 2.53
cd = [2.00 + WD / 2 + i * (WD + 0.50) for i in range(3)]
for i, (cx, txt) in enumerate(zip(cd, det)):
    ax.plot([cx, cx], [2.08, 1.74], color=AZUL, ls=":", lw=1.2, zorder=1)
    caixa(ax, cx - WD / 2, 0.82, WD, 0.92, "#EDF1FA", AZUL_CLARO, lw=1.2)
    ax.text(cx, 1.28, txt, ha="center", va="center", fontsize=8.6,
            color=AZUL_PROF, linespacing=1.4, zorder=4)
    if i < 2:
        seta(ax, (cx + WD / 2 + 0.06, 1.28), (cd[i + 1] - WD / 2 - 0.06, 1.28),
             color=AZUL_APOIO, lw=1.4)
ax.text(0.15, 0.32, "A análise dos impactos é o núcleo técnico do EIA: identificar, prever e responder.",
        fontsize=9, color=CINZA, ha="left", va="center")
salvar(fig, "aia_planejamento_execucao")

# ================================================== (j) rede de interacao
fig, ax = plt.subplots(figsize=(10.6, 3.4))
ax.set_xlim(0, 12.95)
ax.set_ylim(0.25, 3.55)
ax.axis("off")

W, G, H = 2.90, 0.33, 0.95
etapas = ["Urbanização", "Impermeabilização\ndo solo", "Redução da taxa\nde infiltração",
          "Aumento do escoamento\nsuperficial", "Maior aporte hídrico\naos cursos de água",
          "Aumento rápido\nda vazão", "Danos e perdas\neconômicas"]
c1 = [0.15 + W / 2 + i * (W + G) for i in range(4)]
c2 = [0.15 + W / 2 + i * (W + G) for i in range(3)]


def cartao_rede(cx, cy, texto, n):
    caixa(ax, cx - W / 2, cy - H / 2, W, H, "#EDE7F3", ROXO, lw=1.4)
    ax.add_patch(plt.Circle((cx - W / 2 + 0.34, cy + H / 2 - 0.04), 0.20, color=ROXO, zorder=4))
    ax.text(cx - W / 2 + 0.34, cy + H / 2 - 0.04, str(n), ha="center", va="center",
            fontsize=8.6, color="white", fontweight="bold", zorder=5)
    ax.text(cx, cy - 0.10, texto, ha="center", va="center", fontsize=8.6,
            color=GRAFITE, linespacing=1.35, zorder=4)


for i, cx in enumerate(c1):
    cartao_rede(cx, 2.85, etapas[i], i + 1)
    if i < 3:
        seta(ax, (cx + W / 2 + 0.04, 2.85), (cx + W / 2 + G - 0.04, 2.85), color=ROXO)
for i, cx in enumerate(c2):
    cartao_rede(cx, 1.05, etapas[i + 4], i + 5)
    if i < 2:
        seta(ax, (cx + W / 2 + 0.04, 1.05), (cx + W / 2 + G - 0.04, 1.05), color=ROXO)

yq = 1.95
ax.plot([c1[3], c1[3]], [2.85 - H / 2, yq], color=ROXO, lw=1.5, zorder=2)
ax.plot([c1[3], c2[0]], [yq, yq], color=ROXO, lw=1.5, zorder=2)
seta(ax, (c2[0], yq), (c2[0], 1.05 + H / 2 + 0.03), color=ROXO, lw=1.5)
salvar(fig, "aia_rede_interacao")

# ========================================= (k) impactos diretos e indiretos
fig, ax = plt.subplots(figsize=(10.2, 4.4))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5.6)
ax.axis("off")

ax.add_patch(Rectangle((0.4, 3.35), 11.2, 1.15, facecolor="#C9DCB5", edgecolor="none", zorder=1))
ax.add_patch(Rectangle((0.4, 2.95), 11.2, 0.40, facecolor="#E6EFD9", edgecolor="none", zorder=1))
ax.add_patch(Rectangle((0.4, 2.35), 11.2, 0.60, facecolor="#5A5F66", edgecolor="none", zorder=2))
ax.add_patch(Rectangle((0.4, 1.95), 11.2, 0.40, facecolor="#E6EFD9", edgecolor="none", zorder=1))
ax.add_patch(Rectangle((0.4, 0.80), 11.2, 1.15, facecolor="#C9DCB5", edgecolor="none", zorder=1))
ax.plot([1.95, 11.45], [2.65, 2.65], color="#F2D16B", ls=(0, (6, 5)), lw=1.4, zorder=3)
ax.text(11.42, 3.92, "hábitat", ha="right", va="center", fontsize=8.4, color="#44632F", zorder=4)
ax.text(11.42, 1.37, "hábitat", ha="right", va="center", fontsize=8.4, color="#44632F", zorder=4)
ax.text(11.42, 3.15, "faixa de borda", ha="right", va="center", fontsize=8.0,
        color="#6E8A55", zorder=4)
ax.text(0.62, 2.65, "rodovia", ha="left", va="center", fontsize=8.4, color="white", zorder=4)

for x, rot in [(2.4, "Perda de hábitat\n(faixa de domínio)"),
               (6.0, "Mortalidade\npor atropelamento"),
               (9.6, "Poluição sonora,\ndo ar e da água")]:
    seta(ax, (x, 5.02), (x, 4.58), color=VERMELHO, lw=1.4)
    ax.text(x, 5.12, rot, ha="center", va="bottom", fontsize=8.8, color=VERMELHO,
            linespacing=1.35)
for x, rot in [(2.4, "Efeito barreira\ne efeito filtro"),
               (6.0, "Efeito de borda e\nmodificação do hábitat"),
               (9.6, "Afugentamento, predação\ne corredor ao longo da via")]:
    seta(ax, (x, 0.72), (x, 0.28), color=AZUL_PROF, lw=1.4)
    ax.text(x, 0.18, rot, ha="center", va="top", fontsize=8.8, color=AZUL_PROF,
            linespacing=1.35)
salvar(fig, "aia_impactos_rodovia")

# ====================================================== (l) curva do coletor
fig, ax = plt.subplots(figsize=(7.4, 4.0))
d = np.linspace(0, 16, 400)
S = 100 * (1 - np.exp(-d / 2.6))
ax.plot(d, S, color=AZUL, lw=2.4, zorder=4)
ax.plot([0, 8], [97, 97], color=CINZA, ls=":", lw=1.1, zorder=2)
ax.plot([8, 8], [0, 97], color=CINZA, ls=":", lw=1.1, zorder=2)
ax.plot([8], [97], "o", color=VERMELHO, ms=7, zorder=5)
ax.text(8.6, 54, "A partir daqui, cada dia\nadicional de campo acrescenta\npoucas espécies novas",
        fontsize=9, color=VERMELHO, ha="left", va="center", linespacing=1.4)
ax.text(0.7, 104, "Fase de descoberta rápida", fontsize=9, color=CINZA,
        ha="left", va="bottom")
ax.set_xlabel("Número de dias em campo", labelpad=8)
ax.set_ylabel("Número de espécies identificadas", labelpad=8)
ax.set_xlim(0, 16.5)
ax.set_ylim(0, 118)
ax.set_xticks([8])
ax.set_yticks([97])
ax.set_xticklabels(["8"])
ax.set_yticklabels(["100"])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
salvar(fig, "aia_curva_coletor")

# ========================================= (m) dados primarios e secundarios
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.0),
                               gridspec_kw={"width_ratios": [1.0, 1.05]})

k = np.linspace(0, 10, 300)
ax1.plot(k, 10 * np.exp(-k / 2.4) + 1.1, color=AZUL, lw=2.4, zorder=4)
ax1.annotate("Pouco conhecimento:\nimpacto previsto com\ngrande incerteza",
             xy=(0.95, 7.9), xytext=(2.3, 10.9), fontsize=8.8, color=VERMELHO,
             ha="left", va="top", linespacing=1.4,
             arrowprops=dict(arrowstyle="->", color=VERMELHO, lw=1.3))
ax1.annotate("Mais conhecimento:\nprevisão mais segura",
             xy=(7.8, 1.5), xytext=(4.9, 4.9), fontsize=8.8, color=VERDE,
             ha="left", va="top", linespacing=1.4,
             arrowprops=dict(arrowstyle="->", color=VERDE, lw=1.3))
ax1.set_xlabel("Nível de conhecimento do meio ambiente", labelpad=8, fontsize=10)
ax1.set_ylabel("Incerteza sobre os impactos", labelpad=8, fontsize=10)
ax1.set_xlim(0, 10.5)
ax1.set_ylim(0, 11.8)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

ax2.set_xlim(0, 9)
ax2.set_ylim(0, 6.6)
ax2.axis("off")
ax2.add_patch(Ellipse((3.3, 3.0), 4.4, 3.4, facecolor=AZUL_CLARO, edgecolor=AZUL_PROF,
                      lw=1.5, alpha=0.75, zorder=2))
ax2.add_patch(Ellipse((5.5, 3.0), 4.4, 3.4, facecolor="#D7E8CF", edgecolor=VERDE,
                      lw=1.5, alpha=0.75, zorder=2))
ax2.text(2.0, 5.30, "Dados que já existem", ha="center", va="bottom", fontsize=9.5,
         color=AZUL_PROF, fontweight="bold")
ax2.text(6.8, 5.30, "Dados necessários\nao estudo", ha="center", va="bottom", fontsize=9.5,
         color=VERDE, fontweight="bold", linespacing=1.35)
ax2.text(1.85, 3.0, "Existem, mas\nestão fora\ndo escopo", ha="center", va="center",
         fontsize=8.6, color=GRAFITE, linespacing=1.4, zorder=5)
ax2.text(4.4, 3.0, "Dados\nsecundários", ha="center", va="center", fontsize=9.2,
         color=AZUL_PROF, fontweight="bold", linespacing=1.4, zorder=5)
ax2.text(6.75, 3.0, "Dados\nprimários\n(coletar)", ha="center", va="center", fontsize=8.8,
         color=VERDE, fontweight="bold", linespacing=1.4, zorder=5)
ax2.text(0.10, 0.50, "O que já existe só serve se tiver qualidade, estiver atualizado\n"
                     "e estiver na escala do estudo.",
         ha="left", va="center", fontsize=8.8, color=CINZA, linespacing=1.45)
salvar(fig, "aia_dados_primarios_secundarios")

# ==================================================== (n) matriz ponderada
fig, (axA, axB) = plt.subplots(2, 1, figsize=(11.5, 6.2),
                               gridspec_kw={"height_ratios": [1.0, 1.0]})

fatores = ["Solos", "Água\nsuperficial", "Recarga", "Erosão", "Aves", "Emprego"]
acoes = [
    ("Modificação de hábitat", [-9, -7, -4, -10, -8, 0]),
    ("Alteração da cobertura do solo", [-5, -8, -8, -10, -4, 0]),
    ("Alteração da drenagem", [-9, -9, -9, -8, 0, 0]),
    ("Pavimentação de superfícies", [-10, -10, -10, -8, 0, 5]),
    ("Aterro", [0, -5, -10, 6, 0, 5]),
    ("Escavações de superfície", [-5, -7, -5, -9, 0, 5]),
]
NF, NA = len(fatores), len(acoes)
XR = 3.6


def cor_total(v):
    if v > 0:
        return "#A9D6A2"
    if v == 0:
        return "#F6E79B"
    return "#E49C92" if v > -8 else "#D4675A"


axA.set_xlim(0, XR + NF)
axA.set_ylim(0, NA + 2.0)
axA.axis("off")
axA.text(0, NA + 1.80, "Matriz ponderada: nota final de cada cruzamento",
         ha="left", va="top", fontsize=10, color=GRAFITE, fontweight="bold")
for j, f in enumerate(fatores):
    axA.text(XR + j + 0.5, NA + 0.12, f, ha="center", va="bottom", fontsize=8.4,
             color=AZUL_PROF, fontweight="bold", linespacing=1.3)
for i, (nome, vals) in enumerate(acoes):
    y = NA - i - 1
    destaque = (i == 0)
    axA.text(XR - 0.15, y + 0.5, nome, ha="right", va="center", fontsize=8.4,
             color=AZUL_PROF, fontweight="bold" if destaque else "normal")
    for j, v in enumerate(vals):
        axA.add_patch(Rectangle((XR + j, y), 1, 1, facecolor=cor_total(v),
                                edgecolor="white", lw=1.2, zorder=2))
        axA.text(XR + j + 0.5, y + 0.5, f"{v:+d}" if v else "0", ha="center", va="center",
                 fontsize=9, color=GRAFITE, fontweight="bold", zorder=4)
    if destaque:
        axA.add_patch(Rectangle((XR, y), NF, 1, facecolor="none", edgecolor=AZUL,
                                lw=2.2, zorder=5))

criterios = [
    ("Caráter (Ca)", [-1, -1, -1, -1, -1, 0]),
    ("Importância (I)", [2, 1, 1, 3, 1, 0]),
    ("Cobertura (Co)", [2, 2, 1, 2, 1, 0]),
    ("Duração (D)", [3, 2, 1, 3, 3, 0]),
    ("Reversibilidade (R)", [2, 2, 1, 2, 3, 0]),
]
totais = [-9, -7, -4, -10, -8, 0]
NL = len(criterios) + 1
axB.set_xlim(0, XR + NF)
axB.set_ylim(-1.05, NL + 1.5)
axB.axis("off")
axB.text(0, NL + 1.35, "Como a nota é formada - ação destacada: modificação de hábitat",
         ha="left", va="top", fontsize=10, color=AZUL, fontweight="bold")
for i, (nome, vals) in enumerate(criterios):
    y = NL - i - 1
    axB.text(XR - 0.15, y + 0.5, nome, ha="right", va="center", fontsize=8.4, color=GRAFITE)
    for j, v in enumerate(vals):
        axB.add_patch(Rectangle((XR + j, y), 1, 1, facecolor="#FFFFFF",
                                edgecolor="#B9BFC9", lw=0.8, zorder=2))
        axB.text(XR + j + 0.5, y + 0.5, str(v), ha="center", va="center",
                 fontsize=8.8, color=GRAFITE, zorder=4)
y = 0.0
axB.text(XR - 0.15, y + 0.5, "Total", ha="right", va="center", fontsize=9,
         color=AZUL, fontweight="bold")
for j, v in enumerate(totais):
    axB.add_patch(Rectangle((XR + j, y), 1, 1, facecolor=cor_total(v),
                            edgecolor=AZUL, lw=1.4, zorder=2))
    axB.text(XR + j + 0.5, y + 0.5, f"{v:+d}" if v else "0", ha="center", va="center",
             fontsize=9.2, color=GRAFITE, fontweight="bold", zorder=4)
axB.text(0, -0.18, "Total = Ca × (I + Co + D + R).  Em solos: −1 × (2 + 2 + 3 + 2) = −9.",
         ha="left", va="top", fontsize=8.8, color=CINZA)
salvar(fig, "aia_matriz_ponderada")
