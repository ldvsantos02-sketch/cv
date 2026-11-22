# -*- coding: utf-8 -*-
"""
Gera todas as 15 figuras vetoriais (PDF) de alta resolução para a
Apostila Completa de Análise Ambiental (CHF662 — DCHF/UEFS).
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

NAVY = "#1B2A4A"
TEAL = "#0E7C7B"
FOREST = "#2D6A4F"
GOLD = "#C4983B"
ALERT = "#B02A37"
INK = "#22252A"
MUTED = "#5A6370"
SAND = "#D9B382"
WATER = "#2E86AB"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial"],
    "axes.edgecolor": "#CBD5E1",
    "axes.linewidth": 0.9,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "text.color": INK,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.12,
})


def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, format="pdf")
    plt.close(fig)
    print(f"OK: {name}")


# ---------------------------------------------------------------------------
# FIG 01 — Tríade Socioambiental e Sistema GTP (Cap. 3)
# ---------------------------------------------------------------------------
def fig01_triade_socioambiental():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.9))

    # Painel A: Geografia Socioambiental
    ax1.set_xlim(-2.3, 2.3)
    ax1.set_ylim(-1.9, 2.0)
    ax1.set_aspect("equal")
    ax1.axis("off")
    c1 = Circle((-0.6, 0.35), 1.05, fc=NAVY, alpha=0.20, ec=NAVY, lw=2)
    c2 = Circle((0.6, 0.35), 1.05, fc=FOREST, alpha=0.20, ec=FOREST, lw=2)
    c3 = Circle((0.0, -0.55), 1.05, fc=GOLD, alpha=0.22, ec=GOLD, lw=2)
    for c in (c1, c2, c3):
        ax1.add_patch(c)
    ax1.text(-1.15, 0.72, "Meio Físico\n(relevo, solo,\nclima, água)", ha="center", va="center", fontsize=8.3, fontweight="bold", color=NAVY)
    ax1.text(1.15, 0.72, "Meio Biótico\n(vegetação,\nfauna, biota)", ha="center", va="center", fontsize=8.3, fontweight="bold", color=FOREST)
    ax1.text(0.0, -1.08, "Sociedade & Território\n(uso da terra, técnica,\npolítica, economia)", ha="center", va="center", fontsize=8.3, fontweight="bold", color="#8A6418")
    ax1.text(0.0, 0.08, "ANÁLISE\nAMBIENTAL\nINTEGRADA", ha="center", va="center", fontsize=8.4, fontweight="bold", color=ALERT,
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=ALERT, lw=1.1))
    ax1.set_title("Integração Físico-Biótica e Socioespacial", fontsize=9.5, fontweight="bold", color=NAVY)

    # Painel B: Sistema GTP (Bertrand)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 5.2)
    ax2.axis("off")
    boxes = [
        (0.5, 3.3, 3.8, 1.2, "GEOSSISTEMA (G)\nFonte natural, dinâmica\nfísico-ecológica e tempo\nda natureza", "#EDF6F5", TEAL),
        (5.7, 3.3, 3.8, 1.2, "TERRITÓRIO (T)\nApropriação, gestão,\nrecurso econômico e\npoder institucional", "#FCF8EE", GOLD),
        (2.8, 0.6, 4.4, 1.25, "PAISAGEM (P)\nIdentidade cultural, percepção\nsocial, patrimônio e leitura\nintegrada do espaço", "#F4F7FA", NAVY),
    ]
    for x, y, w, h, txt, fc, ec in boxes:
        ax2.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=fc, ec=ec, lw=1.7))
        ax2.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=8.0, fontweight="bold", color=INK)
    ax2.annotate("", xy=(5.6, 3.9), xytext=(4.4, 3.9), arrowprops=dict(arrowstyle="<->", lw=1.8, color=NAVY))
    ax2.annotate("", xy=(3.7, 1.92), xytext=(2.4, 3.25), arrowprops=dict(arrowstyle="<->", lw=1.8, color=TEAL))
    ax2.annotate("", xy=(6.3, 1.92), xytext=(7.6, 3.25), arrowprops=dict(arrowstyle="<->", lw=1.8, color=GOLD))
    ax2.set_title("Sistema Tripolar GTP (Bertrand, 2004)", fontsize=9.5, fontweight="bold", color=NAVY)

    plt.tight_layout()
    save(fig, "fig01_triade_socioambiental.pdf")


# ---------------------------------------------------------------------------
# FIG 02 — Cadeia Aspecto → Impacto + Matriz de Risco (Cap. 4)
# ---------------------------------------------------------------------------
def fig02_aspecto_impacto_risco():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.7), gridspec_kw={"width_ratios": [1.3, 1.0]})

    # Painel A: Cadeia Causal
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 4.6)
    ax1.axis("off")
    ax1.text(5, 4.25, "Cadeia Causal na Análise de Impactos (Sánchez, 2013)", ha="center", fontsize=9.5, fontweight="bold", color=NAVY)
    steps = [
        (0.3, 2.3, 2.7, 1.4, "ATIVIDADE\nHUMANA\n(Causa)\nEx.: abertura de\nestrada em encosta", "#F4F7FA", NAVY),
        (3.65, 2.3, 2.7, 1.4, "ASPECTO\nAMBIENTAL\n(Mecanismo)\nEx.: exposição do\nsolo à chuva", "#FCF8EE", GOLD),
        (7.0, 2.3, 2.7, 1.4, "IMPACTO\nAMBIENTAL\n(Efeito)\nEx.: erosão linear e\nassoreamento", "#FDF3F4", ALERT),
    ]
    for x, y, w, h, txt, fc, ec in steps:
        ax1.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", fc=fc, ec=ec, lw=1.6))
        ax1.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.9, fontweight="bold", color=INK)
    ax1.annotate("", xy=(3.55, 3.0), xytext=(3.08, 3.0), arrowprops=dict(arrowstyle="->", lw=2.2, color=NAVY))
    ax1.annotate("", xy=(6.9, 3.0), xytext=(6.43, 3.0), arrowprops=dict(arrowstyle="->", lw=2.2, color=ALERT))

    ax1.add_patch(FancyBboxPatch((0.6, 0.4), 8.8, 1.25, boxstyle="round,pad=0.08", fc="#EDF6F5", ec=TEAL, lw=1.2))
    ax1.text(5.0, 1.02, "Distinção essencial: o ASPECTO é o elemento da atividade que interage com o ambiente;\no IMPACTO é a alteração resultante na qualidade ambiental (pode ser adverso ou benéfico).",
             ha="center", va="center", fontsize=8.0, color=NAVY, fontweight="bold")

    # Painel B: Matriz de Risco R = P x V
    grid = np.array([
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12],
        [4, 8, 12, 16],
    ])
    cmap_colors = {1: "#D8F3DC", 2: "#B7E4C7", 3: "#FFF3BF", 4: "#FFE066",
                   6: "#FFC078", 8: "#FFA94D", 9: "#FF8787", 12: "#FA5252", 16: "#C92A2A"}
    for r in range(4):
        for c in range(4):
            val = grid[r, c]
            fc = cmap_colors[val]
            tc = "white" if val >= 12 else INK
            ax2.add_patch(patches.Rectangle((c, r), 1, 1, fc=fc, ec="white", lw=1.5))
            lbl = "Baixo" if val <= 3 else ("Médio" if val <= 6 else ("Alto" if val <= 9 else "Crítico"))
            ax2.text(c + 0.5, r + 0.5, f"{val}\n({lbl})", ha="center", va="center", fontsize=7.6, fontweight="bold", color=tc)
    ax2.set_xlim(0, 4)
    ax2.set_ylim(0, 4)
    ax2.set_xticks([0.5, 1.5, 2.5, 3.5])
    ax2.set_xticklabels(["1\nBaixa", "2\nMédia", "3\nAlta", "4\nMuito alta"], fontsize=7.8)
    ax2.set_yticks([0.5, 1.5, 2.5, 3.5])
    ax2.set_yticklabels(["1 Baixo", "2 Médio", "3 Alto", "4 Crítico"], fontsize=7.8)
    ax2.set_xlabel("Vulnerabilidade (V)", fontsize=8.8, fontweight="bold")
    ax2.set_ylabel("Perigo / Ameaça (P)", fontsize=8.8, fontweight="bold")
    ax2.set_title("Matriz Conceitual de Risco (R = P × V)", fontsize=9.3, fontweight="bold", color=NAVY)

    plt.tight_layout()
    save(fig, "fig02_aspecto_impacto_risco.pdf")


# ---------------------------------------------------------------------------
# FIG 03 — Etapas da AIA + Hierarquia de Mitigação (Cap. 5)
# ---------------------------------------------------------------------------
def fig03_etapas_aia_mitigacao():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.1), gridspec_kw={"width_ratios": [1.35, 1.0]})

    # Painel A: Etapas da AIA
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 6.2)
    ax1.axis("off")
    ax1.text(5, 5.9, "Fluxo Metodológico da Avaliação de Impacto Ambiental", ha="center", fontsize=9.3, fontweight="bold", color=NAVY)
    etapas = [
        (5.05, "1. Triagem e Definição de Escopo (Termo de Referência)", NAVY, "#F4F7FA"),
        (4.15, "2. Diagnóstico Ambiental (Linha de Base: Físico, Biótico, Socioeconômico)", TEAL, "#EDF6F5"),
        (3.25, "3. Identificação, Previsão e Valoração dos Impactos (Matrizes / Redes)", GOLD, "#FCF8EE"),
        (2.35, "4. Prognóstico (Cenário com Projeto vs. Sem Projeto)", NAVY, "#F4F7FA"),
        (1.45, "5. Medidas Mitigadoras, Compensatórias e Planos de Gestão (PBA)", FOREST, "#EFF7F2"),
        (0.55, "6. Decisão Pública, Monitoramento e Auditoria Pós-Implantação", ALERT, "#FDF3F4"),
    ]
    for y, txt, ec, fc in etapas:
        ax1.add_patch(FancyBboxPatch((0.4, y), 9.2, 0.62, boxstyle="round,pad=0.06", fc=fc, ec=ec, lw=1.3))
        ax1.text(5.0, y + 0.31, txt, ha="center", va="center", fontsize=7.9, fontweight="bold", color=INK)
    for y in [5.05, 4.15, 3.25, 2.35, 1.45]:
        ax1.annotate("", xy=(5.0, y - 0.25), xytext=(5.0, y - 0.02), arrowprops=dict(arrowstyle="->", lw=1.4, color=MUTED))

    # Painel B: Hierarquia de Mitigação
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 6.2)
    ax2.axis("off")
    ax2.text(5, 5.9, "Hierarquia de Mitigação (Ordem de Prioridade)", ha="center", fontsize=9.3, fontweight="bold", color=NAVY)
    levels = [
        (4.5, 8.6, "1º EVITAR (Prevenção na origem)\nAlternativa locacional ou tecnológica", FOREST, "white"),
        (3.2, 7.2, "2º MINIMIZAR (Redução de magnitude)\nControle de erosão, filtros, cronograma", TEAL, "white"),
        (1.9, 5.8, "3º RECUPERAR / REABILITAR\nPRAD, revegetação, bioengenharia", GOLD, "white"),
        (0.6, 4.4, "4º COMPENSAR (Impacto residual)\nUnidades de conservação, reposição", ALERT, "white"),
    ]
    for y, w, txt, fc, tc in levels:
        x = (10 - w) / 2
        ax2.add_patch(FancyBboxPatch((x, y), w, 1.0, boxstyle="round,pad=0.08", fc=fc, ec="white", lw=1.2))
        ax2.text(5.0, y + 0.5, txt, ha="center", va="center", fontsize=7.8, fontweight="bold", color=tc)
    ax2.annotate("Preferível\n(menor custo\necológico)", xy=(0.5, 5.1), xytext=(0.5, 1.1),
                 arrowprops=dict(arrowstyle="->", lw=1.8, color=FOREST), fontsize=7.3, fontweight="bold", color=FOREST, ha="center")

    plt.tight_layout()
    save(fig, "fig03_etapas_aia_mitigacao.pdf")


# ---------------------------------------------------------------------------
# FIG 04 — Sistema Ambiental Aberto + Escalas Espaço-Temporais (Cap. 6)
# ---------------------------------------------------------------------------
def fig04_sistema_aberto_escalas():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.8), gridspec_kw={"width_ratios": [1.15, 1.05]})

    # Painel A: Sistema aberto
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 5.2)
    ax1.axis("off")
    ax1.text(5, 4.9, "Sistema Ambiental Aberto e Retroalimentação", ha="center", fontsize=9.3, fontweight="bold", color=NAVY)
    ax1.add_patch(FancyBboxPatch((0.2, 2.3), 2.1, 1.3, boxstyle="round,pad=0.08", fc="#EDF6F5", ec=TEAL, lw=1.5))
    ax1.text(1.25, 2.95, "ENTRADAS\n(Inputs)\nChuva, radiação\nsolar, insumos", ha="center", va="center", fontsize=7.8, fontweight="bold", color=NAVY)

    ax1.add_patch(FancyBboxPatch((3.0, 1.85), 4.0, 2.2, boxstyle="round,pad=0.1", fc="#F4F7FA", ec=NAVY, lw=1.8))
    ax1.text(5.0, 3.65, "SISTEMA GEOAMBIENTAL", ha="center", fontsize=8.3, fontweight="bold", color=NAVY)
    ax1.add_patch(FancyBboxPatch((3.3, 2.2), 1.5, 1.0, boxstyle="round,pad=0.06", fc="white", ec=FOREST, lw=1.1))
    ax1.text(4.05, 2.7, "Estoques\n(solo, água,\nbiomassa)", ha="center", va="center", fontsize=7.4)
    ax1.add_patch(FancyBboxPatch((5.2, 2.2), 1.5, 1.0, boxstyle="round,pad=0.06", fc="white", ec=GOLD, lw=1.1))
    ax1.text(5.95, 2.7, "Processos\n(infiltração,\nerosão, uso)", ha="center", va="center", fontsize=7.4)
    ax1.annotate("", xy=(5.15, 2.7), xytext=(4.85, 2.7), arrowprops=dict(arrowstyle="<->", lw=1.2, color=NAVY))

    ax1.add_patch(FancyBboxPatch((7.7, 2.3), 2.1, 1.3, boxstyle="round,pad=0.08", fc="#FDF3F4", ec=ALERT, lw=1.5))
    ax1.text(8.75, 2.95, "SAÍDAS\n(Outputs)\nVazão, sedimento,\ncalor, produção", ha="center", va="center", fontsize=7.8, fontweight="bold", color=ALERT)

    ax1.annotate("", xy=(2.95, 2.95), xytext=(2.35, 2.95), arrowprops=dict(arrowstyle="->", lw=2.0, color=TEAL))
    ax1.annotate("", xy=(7.65, 2.95), xytext=(7.05, 2.95), arrowprops=dict(arrowstyle="->", lw=2.0, color=ALERT))

    # Feedback
    ax1.annotate("", xy=(1.25, 2.2), xytext=(8.75, 2.2),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.25", lw=1.7, color=GOLD, ls="--"))
    ax1.text(5.0, 0.52, "Retroalimentação (Feedback): negativa = estabiliza; positiva = amplifica degradação",
             ha="center", fontsize=7.6, fontweight="bold", color="#8A6418",
             bbox=dict(boxstyle="round,pad=0.25", fc="#FCF8EE", ec=GOLD, lw=0.9))

    # Painel B: Escalas espaço-temporais
    pts = [
        (0.5, 0.5, "Splash / Selamento\n(cm² | minutos)", ALERT),
        (1.6, 1.5, "Sulcos e Ravinas\n(vertente | chuvas)", GOLD),
        (2.7, 2.4, "Microbacia / Voçoroca\n(km² | anos)", TEAL),
        (3.8, 3.3, "Bacia Regional\n(10³ km² | décadas)", NAVY),
        (4.7, 4.2, "Bioma / Clima\n(10⁶ km² | séculos)", FOREST),
    ]
    for x, y, lbl, col in pts:
        ax2.scatter([x], [y], s=180, color=col, alpha=0.85, edgecolors="white", lw=1.5, zorder=5)
        ax2.text(x, y + 0.34, lbl, ha="center", va="bottom", fontsize=7.2, fontweight="bold", color=col)
    ax2.plot([0.5, 4.7], [0.5, 4.2], "--", color="#CBD5E1", lw=1.2, zorder=1)
    ax2.set_xlim(-0.2, 5.5)
    ax2.set_ylim(0, 5.1)
    ax2.set_xticks([0.5, 2.7, 4.7])
    ax2.set_xticklabels(["Local\n(parcela)", "Meso\n(bacia)", "Macro\n(regional)"], fontsize=8)
    ax2.set_yticks([0.5, 2.4, 4.2])
    ax2.set_yticklabels(["Evento", "Anos", "Séculos"], fontsize=8)
    ax2.set_xlabel("Escala Espacial", fontsize=8.8, fontweight="bold")
    ax2.set_ylabel("Escala Temporal", fontsize=8.8, fontweight="bold")
    ax2.set_title("Acoplamento Escala Espacial × Temporal", fontsize=9.3, fontweight="bold", color=NAVY)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    save(fig, "fig04_sistema_aberto_escalas.pdf")


# ---------------------------------------------------------------------------
# FIG 05 — Bacia Hidrográfica e Hierarquia de Strahler (Cap. 7)
# ---------------------------------------------------------------------------
def fig05_bacia_hidrografica_strahler():
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.4)
    ax.axis("off")

    # Contorno da bacia (divisor topográfico)
    theta = np.linspace(0, 2 * np.pi, 200)
    bx = 4.6 + 3.6 * np.cos(theta) + 0.35 * np.sin(2 * theta)
    by = 2.7 + 2.1 * np.sin(theta) - 0.18 * np.cos(3 * theta)
    ax.fill(bx, by, color="#EDF6F5", alpha=0.65)
    ax.plot(bx, by, "--", color=GOLD, lw=2.3, label="Divisor topográfico (interflúvio)")

    # Canais de 1ª ordem
    o1 = [
        ([2.0, 3.0], [3.9, 3.3]),
        ([2.3, 3.0], [2.7, 3.3]),
        ([3.2, 4.2], [4.3, 3.5]),
        ([4.8, 4.2], [4.3, 3.5]),
        ([2.2, 3.3], [1.7, 2.0]),
        ([2.8, 3.3], [1.1, 2.0]),
        ([5.5, 6.2], [3.8, 3.0]),
        ([6.6, 6.2], [3.7, 3.0]),
        ([5.2, 6.0], [1.5, 2.1]),
    ]
    for xs, ys in o1:
        ax.plot(xs, ys, color="#64B5F6", lw=1.5)
        ax.text(xs[0] - 0.08, ys[0] + 0.05, "1", fontsize=7.5, fontweight="bold", color=WATER)

    # Canais de 2ª ordem
    o2 = [
        ([3.0, 4.6], [3.3, 2.8]),
        ([4.2, 4.6], [3.5, 2.8]),
        ([3.3, 5.3], [2.0, 2.5]),
        ([6.2, 6.5], [3.0, 2.4]),
    ]
    for xs, ys in o2:
        ax.plot(xs, ys, color=WATER, lw=2.5)
        ax.text((xs[0] + xs[1]) / 2, (ys[0] + ys[1]) / 2 + 0.12, "2", fontsize=8.2, fontweight="bold", color=NAVY)

    # Canal de 3ª ordem (rio principal)
    ax.plot([4.6, 5.3, 6.5, 8.2], [2.8, 2.5, 2.4, 2.3], color=NAVY, lw=4.0)
    ax.text(5.85, 2.62, "3ª ordem (Canal principal)", fontsize=8.4, fontweight="bold", color=NAVY)

    # Mata ciliar / área ripária ao longo do canal principal
    ax.plot([4.6, 5.3, 6.5, 7.9], [2.8, 2.5, 2.4, 2.32], color=FOREST, lw=10, alpha=0.22, solid_capstyle="round")

    # Exutório
    ax.scatter([8.2], [2.3], s=110, color=ALERT, zorder=6)
    ax.annotate("EXUTÓRIO\n(seção de saída de\nágua e sedimentos)", xy=(8.2, 2.3), xytext=(8.35, 3.45),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=ALERT), fontsize=8.0, fontweight="bold", color=ALERT)

    # Anotações pedagógicas
    ax.annotate("Divisor Topográfico\n(separa bacias vizinhas)", xy=(4.6, 4.65), xytext=(6.7, 4.75),
                arrowprops=dict(arrowstyle="->", lw=1.4, color=GOLD), fontsize=8.0, fontweight="bold", color="#8A6418")
    ax.annotate("Área Ripária / APP\n(filtro de sedimentos)", xy=(6.0, 2.42), xytext=(6.4, 0.85),
                arrowprops=dict(arrowstyle="->", lw=1.4, color=FOREST), fontsize=8.0, fontweight="bold", color=FOREST)
    ax.text(0.25, 0.35, "Regra de Strahler:  1 + 1 → 2  |  2 + 2 → 3  |  2 + 1 → 2 (mantém a maior ordem!)",
            fontsize=8.4, fontweight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=NAVY, lw=1.0))
    ax.set_title("Bacia Hidrográfica como Unidade Funcional e Hierarquia Fluvial de Strahler", fontsize=10, fontweight="bold", color=NAVY)
    save(fig, "fig05_bacia_hidrografica_strahler.pdf")


# ---------------------------------------------------------------------------
# FIG 06 — Perfil Morfopedológico de Vertente (Cap. 8)
# ---------------------------------------------------------------------------
def fig06_morfopedologia_vertente():
    fig, ax = plt.subplots(figsize=(9.2, 3.9))
    x = np.linspace(0, 10, 300)
    # Perfil da superfície: topo plano -> ombro convexo -> meia encosta retilínea -> sopé côncavo -> fundo de vale
    y = 3.6 - 0.25 * x - 1.2 * (1 / (1 + np.exp(-(x - 4.3) * 1.1)))
    y = y - y.min() + 0.65
    y_bed = y - (0.65 - 0.32 * np.exp(-((x - 4.5) ** 2) / 2.2) + 0.35 * np.exp(-((x - 9.0) ** 2) / 1.5))

    ax.fill_between(x, 0, y_bed, color="#CBD5E1", alpha=0.55, label="Rocha / Saprólito (substrato)")
    ax.fill_between(x, y_bed, y, color=SAND, alpha=0.72, label="Manto de solo (varia em espessura na vertente)")
    ax.plot(x, y, color=FOREST, lw=2.8)
    ax.plot(x, y_bed, "--", color=NAVY, lw=1.2)

    # Canal fluvial no fundo de vale
    ax.fill_between(x[x >= 9.0], y[x >= 9.0] - 0.2, y[x >= 9.0] + 0.08, color=WATER, alpha=0.8)
    ax.text(9.45, 0.95, "Rio", fontsize=8.2, fontweight="bold", color=WATER, ha="center")

    zones = [
        (1.0, 3.7, "TOPO\n(Interflúvio)\nDecliv. baixa\nInfiltração alta\nSolos profundos\n(Latossolos)", FOREST),
        (3.8, 3.25, "ALTA / MÉDIA VERTENTE\nDeclividade acentuada\nEscoamento veloz\nSolos rasos / pedregosos\n(Neossolos / Cambissolos)", ALERT),
        (6.8, 2.35, "BAIXA VERTENTE\n(Sopé côncavo)\nAcúmulo de água\ne colúvios\n(Argissolos / Planossolos)", GOLD),
        (8.9, 1.85, "FUNDO DE VALE\nPlanície fluvial\nSolos hidromórficos\n(Gleissolos)\nRisco de assoreamento", NAVY),
    ]
    for zx, zy, txt, col in zones:
        ax.text(zx, zy, txt, ha="center", va="bottom", fontsize=7.3, fontweight="bold", color=col,
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=col, alpha=0.92, lw=0.9))

    # Setas de infiltração e escoamento
    ax.annotate("", xy=(1.2, 2.8), xytext=(1.2, 3.45), arrowprops=dict(arrowstyle="->", lw=1.8, color=WATER))
    ax.annotate("", xy=(5.2, 1.9), xytext=(3.6, 2.75), arrowprops=dict(arrowstyle="->", lw=2.2, color=ALERT))
    ax.text(4.55, 2.15, "Escoamento\nsuperficial", fontsize=7.4, fontweight="bold", color=ALERT, rotation=-24)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.15)
    ax.set_xlabel("Distância ao longo da vertente (topossequência)", fontsize=9)
    ax.set_ylabel("Altitude relativa (m)", fontsize=9)
    ax.set_title("Morfopedologia: Relação Relevo–Solo–Água ao Longo de uma Vertente", fontsize=9.8, fontweight="bold", color=NAVY)
    ax.legend(loc="lower left", fontsize=8.0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig06_morfopedologia_vertente.pdf")


# ---------------------------------------------------------------------------
# FIG 07 — Ecodinâmica (Tricart) + Fragilidade Ambiental (Ross, 1994) (Cap. 9)
# ---------------------------------------------------------------------------
def fig07_ecodinamica_ross_matriz():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.8), gridspec_kw={"width_ratios": [1.05, 1.25]})

    # Painel A: Balanço Morfogênese vs Pedogênese (Tricart)
    cats = ["Meios\nEstáveis", "Meios\nIntergrades", "Meios Fort.\nInstáveis"]
    pedo = [80, 50, 18]
    morfo = [20, 50, 82]
    x = np.arange(len(cats))
    w = 0.34
    ax1.bar(x - w / 2, pedo, w, color=FOREST, label="Pedogênese (formação de solo)")
    ax1.bar(x + w / 2, morfo, w, color=ALERT, label="Morfogênese (erosão / remoção)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(cats, fontsize=8.3, fontweight="bold")
    ax1.set_ylim(0, 102)
    ax1.set_ylabel("Predomínio relativo (%)", fontsize=8.6)
    ax1.set_title("Ecodinâmica de Tricart (1977)\nMorfogênese vs. Pedogênese", fontsize=9.2, fontweight="bold", color=NAVY)
    ax1.legend(fontsize=7.6, loc="upper center")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Painel B: Matriz Ross (Fragilidade Potencial × Grau de Proteção do Uso da Terra = Fragilidade Emergente)
    mat = np.array([
        [1, 1, 2, 2, 3],
        [1, 2, 2, 3, 4],
        [2, 2, 3, 4, 4],
        [2, 3, 4, 4, 5],
        [3, 4, 4, 5, 5],
    ])
    colors_r = {1: "#D8F3DC", 2: "#95D5B2", 3: "#FFE066", 4: "#FFA94D", 5: "#E03131"}
    labels_r = {1: "1\nM. Fraca", 2: "2\nFraca", 3: "3\nMédia", 4: "4\nForte", 5: "5\nM. Forte"}
    for r in range(5):
        for c in range(5):
            v = mat[r, c]
            ax2.add_patch(patches.Rectangle((c, r), 1, 1, fc=colors_r[v], ec="white", lw=1.4))
            ax2.text(c + 0.5, r + 0.5, labels_r[v], ha="center", va="center",
                     fontsize=7.0, fontweight="bold", color="white" if v == 5 else INK)
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 5)
    ax2.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5])
    ax2.set_xticklabels(["1\nMata densa", "2\nCapoeira", "3\nPastagem", "4\nCultivo", "5\nSolo exp."], fontsize=7.2)
    ax2.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5])
    ax2.set_yticklabels(["1 M. Fraca", "2 Fraca", "3 Média", "4 Forte", "5 M. Forte"], fontsize=7.4)
    ax2.set_xlabel("Classe de Proteção do Uso e Cobertura da Terra", fontsize=8.4, fontweight="bold")
    ax2.set_ylabel("Fragilidade Potencial (Relevo+Solo+Clima)", fontsize=8.0, fontweight="bold")
    ax2.set_title("Matriz de Fragilidade Emergente (Ross, 1994)", fontsize=9.2, fontweight="bold", color=NAVY)

    plt.tight_layout()
    save(fig, "fig07_ecodinamica_ross_matriz.pdf")


# ---------------------------------------------------------------------------
# FIG 08 — Ciclo PEIR aplicado ao Semiárido Baiano (Cap. 10)
# ---------------------------------------------------------------------------
def fig08_modelo_peir_semiarido():
    fig, ax = plt.subplots(figsize=(9.2, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.2)
    ax.axis("off")

    ax.text(5, 4.92, "Modelo PEIR (OCDE / PNUMA) Aplicado à Inserção Eólica e Energética no Semiárido Baiano",
            ha="center", fontsize=9.4, fontweight="bold", color=NAVY)

    cards = [
        (0.4, 2.8, 4.0, 1.65, "PRESSÃO (P)\n• Abertura de acessos e platôs de torres\n• Supressão de Caatinga e trânsito pesado\n• Alteração de vazões no São Francisco", "#FCF8EE", GOLD),
        (5.6, 2.8, 4.0, 1.65, "ESTADO (E)\n• Taxa de solo exposto e compactação\n• Fragmentação de habitats na Caatinga\n• Densidade de drenagem e cobertura vegetal", "#F4F7FA", NAVY),
        (5.6, 0.45, 4.0, 1.65, "IMPACTO (I)\n• Erosão linear na base de torres e acessos\n• Interferência com avifauna local (colisão)\n• Assoreamento e conflitos socioambientais", "#FDF3F4", ALERT),
        (0.4, 0.45, 4.0, 1.65, "RESPOSTA (R)\n• PRAD, drenagem e bioengenharia de solos\n• Monitoramento de fauna e ruído\n• Ordenamento territorial e compensação", "#EFF7F2", FOREST),
    ]
    for x, y, w, h, txt, fc, ec in cards:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=fc, ec=ec, lw=1.8))
        ax.text(x + 0.18, y + h / 2, txt, ha="left", va="center", fontsize=7.9, color=INK, fontweight="bold")

    ax.annotate("", xy=(5.5, 3.62), xytext=(4.5, 3.62), arrowprops=dict(arrowstyle="->", lw=2.2, color=NAVY))
    ax.annotate("", xy=(7.6, 2.2), xytext=(7.6, 2.72), arrowprops=dict(arrowstyle="->", lw=2.2, color=ALERT))
    ax.annotate("", xy=(4.5, 1.28), xytext=(5.5, 1.28), arrowprops=dict(arrowstyle="->", lw=2.2, color=FOREST))
    ax.annotate("", xy=(2.4, 2.72), xytext=(2.4, 2.2), arrowprops=dict(arrowstyle="->", lw=2.2, color=GOLD))

    save(fig, "fig08_modelo_peir_semiarido.pdf")


# ---------------------------------------------------------------------------
# FIG 09 — Gráfico Radar de Indicadores de Qualidade do Solo (Cap. 11)
# ---------------------------------------------------------------------------
def fig09_qualidade_solo_radar():
    labels = ["Matéria\nOrgânica", "Porosidade\nTotal", "Taxa de\nInfiltração",
              "Estabilidade\nde Agregados", "Baixa Densidade\n(1/Ds norm.)", "Cobertura\nVegetal"]
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    # Valores normalizados ilustrativos (0 a 1)
    ref = [0.90, 0.88, 0.92, 0.86, 0.85, 0.95] + [0.90]
    rec = [0.68, 0.72, 0.75, 0.70, 0.68, 0.78] + [0.68]
    deg = [0.28, 0.35, 0.22, 0.30, 0.32, 0.18] + [0.28]

    fig, ax = plt.subplots(figsize=(6.8, 4.4), subplot_kw=dict(polar=True))
    ax.plot(angles, ref, "o-", lw=2.2, color=FOREST, label="Referência (Caatinga conservada)")
    ax.fill(angles, ref, color=FOREST, alpha=0.14)
    ax.plot(angles, rec, "s--", lw=2.0, color=TEAL, label="Área em recuperação (bioengenharia)")
    ax.fill(angles, rec, color=TEAL, alpha=0.12)
    ax.plot(angles, deg, "^-", lw=2.2, color=ALERT, label="Área degradada (solo exposto/compactado)")
    ax.fill(angles, deg, color=ALERT, alpha=0.14)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=8.4, fontweight="bold", color=NAVY)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(["0,2", "0,4", "0,6", "0,8", "1,0"], fontsize=7.5, color=MUTED)
    ax.set_ylim(0, 1.05)
    ax.set_title("Exemplo Didático de Índice Integrado de Qualidade do Solo\n(Indicadores normalizados de 0 a 1 — Doran & Parkin, 1994)",
                 fontsize=9.2, fontweight="bold", color=NAVY, pad=16)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=1, fontsize=8.0, frameon=True)
    save(fig, "fig09_qualidade_solo_radar.pdf")


# ---------------------------------------------------------------------------
# FIG 10 — Evolução dos Processos Erosivos Lineares (Cap. 12)
# ---------------------------------------------------------------------------
def fig10_evolucao_erosao_linear():
    fig, ax = plt.subplots(figsize=(9.4, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.4)
    ax.axis("off")

    ax.text(5, 4.1, "Sequência Evolutiva da Erosão Hídrica — Do Impacto da Gota à Voçoroca",
            ha="center", fontsize=9.8, fontweight="bold", color=NAVY)

    stages = [
        (0.2, "1. SPLASH\n(Salpicamento)", "Impacto da gota\ndesagrega torrões\ne gera selamento", "#EDF6F5", TEAL),
        (2.15, "2. EROSÃO\nLAMINAR", "Escoamento em\nlâmina remove\ncamada fértil", "#FCF8EE", GOLD),
        (4.1, "3. SULCOS\n(< 0,5 m)", "Fluxo concentra-se\nem pequenos canais\n(ainda reversíveis)", "#FFF0DC", "#D97706"),
        (6.05, "4. RAVINAS\n(> 0,5 m)", "Incisão profunda\npor escoamento\nsuperficial", "#FDE8E8", ALERT),
        (8.0, "5. VOÇOROCA\n(Colapso)", "Atinge o lençol\nfreático (piping)\ne solapa taludes", "#8B1E3F", "#5E1229"),
    ]
    for i, (x, title, desc, fc, ec) in enumerate(stages):
        tc_t = "white" if i == 4 else ec
        tc_d = "white" if i == 4 else INK
        ax.add_patch(FancyBboxPatch((x, 1.35), 1.78, 2.3, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.6))
        ax.text(x + 0.89, 3.15, title, ha="center", va="center", fontsize=8.0, fontweight="bold", color=tc_t)
        ax.plot([x + 0.12, x + 1.66], [2.65, 2.65], color=tc_t, lw=0.7, alpha=0.55)
        ax.text(x + 0.89, 2.0, desc, ha="center", va="center", fontsize=7.5, color=tc_d)
        if i < 4:
            ax.annotate("", xy=(x + 2.08, 2.5), xytext=(x + 1.84, 2.5),
                        arrowprops=dict(arrowstyle="->", lw=1.9, color=NAVY))

    # Barra inferior de custo de recuperação
    ax.annotate("", xy=(9.6, 0.72), xytext=(0.4, 0.72), arrowprops=dict(arrowstyle="->", lw=2.8, color=ALERT))
    ax.text(5.0, 0.30, "Aumento exponencial da severidade, perda de solo e custo de recuperação (prevenir custa muito menos!)",
            ha="center", fontsize=8.2, fontweight="bold", color=ALERT)
    save(fig, "fig10_evolucao_erosao_linear.pdf")


# ---------------------------------------------------------------------------
# FIG 11 — Sensibilidade da USLE à Cobertura Vegetal (Fator C) (Cap. 12)
# ---------------------------------------------------------------------------
def fig11_usle_sensibilidade():
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    cenarios = ["Solo exposto\n(C = 1,00)", "Cultivo morro\nabaixo (C = 0,40)", "Pastagem degrad.\n(C = 0,15)",
                "Manejo conserv.\n(C = 0,05 | P = 0,5)", "Caatinga / Mata\ndensa (C = 0,005)"]
    # A = R * K * LS * C * P com R=6000, K=0.03, LS=1.5 -> R*K*LS = 270 t/ha/ano
    base = 6000 * 0.03 * 1.5
    perdas = [base * 1.0, base * 0.40, base * 0.15, base * 0.05 * 0.5, base * 0.005]
    cores = [ALERT, "#D97706", GOLD, TEAL, FOREST]
    bars = ax.bar(cenarios, perdas, color=cores, width=0.55, edgecolor="white", lw=1.2)
    for b, v in zip(bars, perdas):
        ax.text(b.get_x() + b.get_width() / 2, v + 5, f"{v:.1f}".replace(".", ","), ha="center", fontsize=8.5, fontweight="bold")
    ax.axhline(12, ls="--", color=NAVY, lw=1.4, label="Limite ilustrativo de tolerância de perda de solo (12 t/ha·ano)")
    ax.set_ylim(0, 310)
    ax.set_ylabel("Perda de solo estimada A (t/ha·ano)", fontsize=8.8)
    ax.set_title("Exemplo Didático da USLE (A = R·K·L·S·C·P): Efeito Protetor da Cobertura Vegetal",
                 fontsize=9.4, fontweight="bold", color=NAVY)
    ax.legend(loc="upper right", fontsize=8.0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig11_usle_sensibilidade.pdf")


# ---------------------------------------------------------------------------
# FIG 12 — Corte Técnico de Paliçadas Permeáveis + Biomanta (Cap. 13)
# ---------------------------------------------------------------------------
def fig12_bioengenharia_palicada_talude():
    fig, ax = plt.subplots(figsize=(9.2, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.6)

    # Fundo original da ravina (declividade íngreme)
    x_orig = np.array([0.5, 9.5])
    y_orig = np.array([3.6, 0.6])
    ax.fill_between(x_orig, 0, y_orig, color=SAND, alpha=0.55)
    ax.plot(x_orig, y_orig, "--", color=ALERT, lw=1.8, label="Perfil original íngreme do leito da ravina")

    # Paliçadas em 3 degraus e cunhas de sedimento retido
    pals = [(3.0, 2.77, 0.72), (5.5, 1.93, 0.72), (8.0, 1.10, 0.72)]
    for idx, (px, py, ph) in enumerate(pals):
        # Sedimento depositado a montante (patamar com menor declividade)
        x_up = px - 2.1
        y_up = np.interp(x_up, x_orig, y_orig)
        poly = Polygon([(x_up, y_up), (px, py + ph - 0.08), (px, py)], fc="#C29B61", alpha=0.85, ec=NAVY, lw=0.8)
        ax.add_patch(poly)
        # Estrutura da paliçada (bambu/madeira permeável)
        ax.add_patch(patches.Rectangle((px - 0.09, py - 0.35), 0.18, ph + 0.35, fc="#5C4033", ec=NAVY, lw=1.2, zorder=5))
        # Estacas vivas brotando no patamar
        for dx in [-1.2, -0.6]:
            ax.plot([px + dx, px + dx], [py + ph * 0.45, py + ph + 0.45], color=FOREST, lw=2.2, zorder=6)
            ax.scatter([px + dx], [py + ph + 0.48], s=65, color=FOREST, zorder=6)

    ax.annotate("Paliçada permeável\n(reduz velocidade do fluxo,\nretém sedimentos, drena água)",
                xy=(5.5, 2.65), xytext=(6.2, 3.65),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=NAVY), fontsize=8.0, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=NAVY))
    ax.annotate("Cunha de sedimento\n+ revegetação (novo perfil\nescalonado mais suave)",
                xy=(4.3, 2.45), xytext=(1.2, 3.9),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=FOREST), fontsize=8.0, fontweight="bold", color=FOREST,
                bbox=dict(boxstyle="round,pad=0.25", fc="#EFF7F2", ec=FOREST))
    ax.annotate("Escoamento dissipado\n(menor energia cinética)", xy=(9.1, 1.15), xytext=(7.2, 0.25),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=WATER), fontsize=7.9, fontweight="bold", color=WATER)

    ax.set_xlabel("Perfil longitudinal do canal erosivo (montante → jusante)", fontsize=8.8)
    ax.set_ylabel("Cota relativa (m)", fontsize=8.8)
    ax.set_title("Bioengenharia de Água e Solo: Estabilização de Ravina por Paliçadas Permeáveis em Série",
                 fontsize=9.5, fontweight="bold", color=NAVY)
    ax.legend(loc="lower left", fontsize=8.0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig12_bioengenharia_palicada_talude.pdf")


# ---------------------------------------------------------------------------
# FIG 13 — Efeitos Mecânicos e Hidrológicos das Raízes em Taludes (Cap. 13)
# ---------------------------------------------------------------------------
def fig13_efeitos_raizes_solo():
    fig, ax = plt.subplots(figsize=(8.8, 3.7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.6)
    ax.axis("off")

    ax.text(5, 4.3, "Como a Vegetação Estabiliza Encostas e Margens (Gray & Sotir, 1996; Durlo & Sutili, 2005)",
            ha="center", fontsize=9.3, fontweight="bold", color=NAVY)

    # Coluna esquerda: Hidrológicos
    ax.add_patch(FancyBboxPatch((0.3, 0.45), 4.3, 3.45, boxstyle="round,pad=0.1", fc="#EDF6F5", ec=TEAL, lw=1.6))
    ax.text(2.45, 3.55, "EFEITOS HIDROLÓGICOS", ha="center", fontsize=9.0, fontweight="bold", color=TEAL)
    h_txt = (
        "1. Interceptação pela copa:\n"
        "   dissipa energia cinética da chuva (evita splash).\n\n"
        "2. Rugosidade e serapilheira:\n"
        "   retarda o escoamento superficial e aumenta\n"
        "   a taxa de infiltração.\n\n"
        "3. Evapotranspiração:\n"
        "   remove água do solo, reduz poropressão\n"
        "   positiva e eleva a sucção matricial."
    )
    ax.text(0.55, 1.95, h_txt, ha="left", va="center", fontsize=7.9, color=INK)

    # Coluna direita: Mecânicos
    ax.add_patch(FancyBboxPatch((5.4, 0.45), 4.3, 3.45, boxstyle="round,pad=0.1", fc="#EFF7F2", ec=FOREST, lw=1.6))
    ax.text(7.55, 3.55, "EFEITOS MECÂNICOS (RAÍZES)", ha="center", fontsize=9.0, fontweight="bold", color=FOREST)
    m_txt = (
        "1. Reforço por tração (coesão radicular cᵣ):\n"
        "   raízes finas funcionam como fibras armando\n"
        "   a matriz do solo contra cisalhamento.\n\n"
        "2. Ancoragem em camadas profundas:\n"
        "   raízes pivotantes atravessam o plano potencial\n"
        "   de ruptura e fixam o manto superficial.\n\n"
        "3. Retenção e contenção (arqueamento):\n"
        "   troncos e raízes estruturais retêm sedimentos."
    )
    ax.text(5.65, 1.95, m_txt, ha="left", va="center", fontsize=7.9, color=INK)

    ax.annotate("", xy=(5.32, 2.2), xytext=(4.68, 2.2), arrowprops=dict(arrowstyle="<->", lw=2.0, color=GOLD))
    ax.text(5.0, 2.55, "Sinergia", ha="center", fontsize=7.8, fontweight="bold", color="#8A6418")
    save(fig, "fig13_efeitos_raizes_solo.pdf")


# ---------------------------------------------------------------------------
# FIG 14 — Licenciamento Trifásico + Faixas de APP (Lei 12.651/2012) (Cap. 14)
# ---------------------------------------------------------------------------
def fig14_licenciamento_apps():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.8), gridspec_kw={"width_ratios": [1.05, 1.25]})

    # Painel A: Licenciamento Trifásico
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 5.2)
    ax1.axis("off")
    ax1.text(5, 4.9, "Licenciamento Ambiental Trifásico\n(Res. CONAMA 237/1997)", ha="center", fontsize=9.0, fontweight="bold", color=NAVY)
    lics = [
        (3.35, "LP — Licença Prévia\nAprova localização e viabilidade ambiental\n(etapa do EIA/RIMA e audiências)", "#F4F7FA", NAVY),
        (1.9, "LI — Licença de Instalação\nAutoriza o início das obras conforme\nplanos de controle e PBA", "#FCF8EE", GOLD),
        (0.45, "LO — Licença de Operação\nAutoriza funcionamento após verificar\ncumprimento das condicionantes", "#EFF7F2", FOREST),
    ]
    for y, txt, fc, ec in lics:
        ax1.add_patch(FancyBboxPatch((0.5, y), 9.0, 1.05, boxstyle="round,pad=0.08", fc=fc, ec=ec, lw=1.6))
        ax1.text(5.0, y + 0.52, txt, ha="center", va="center", fontsize=7.7, fontweight="bold", color=INK)
    ax1.annotate("", xy=(5.0, 3.03), xytext=(5.0, 3.30), arrowprops=dict(arrowstyle="->", lw=1.8, color=NAVY))
    ax1.annotate("", xy=(5.0, 1.58), xytext=(5.0, 1.85), arrowprops=dict(arrowstyle="->", lw=1.8, color=GOLD))

    # Painel B: Faixas de APP de cursos d'água (Lei 12.651/2012, Art. 4º)
    larguras = ["< 10 m", "10 a 50 m", "50 a 200 m", "200 a 600 m", "> 600 m"]
    apps = [30, 50, 100, 200, 500]
    bars = ax2.barh(larguras, apps, color=[TEAL, TEAL, FOREST, FOREST, NAVY], height=0.55)
    for b, v in zip(bars, apps):
        ax2.text(v + 12, b.get_y() + b.get_height() / 2, f"{v} m (cada margem)", va="center", fontsize=8.1, fontweight="bold", color=INK)
    ax2.set_xlim(0, 680)
    ax2.set_xlabel("Largura mínima da APP a partir da calha regular (m)", fontsize=8.4)
    ax2.set_ylabel("Largura do curso d'água", fontsize=8.4)
    ax2.set_title("APPs Marginais — Código Florestal (Lei nº 12.651/2012)", fontsize=9.0, fontweight="bold", color=NAVY)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    save(fig, "fig14_licenciamento_apps.pdf")


# ---------------------------------------------------------------------------
# FIG 15 — Fluxograma do Trabalho Prático Final (Cap. 15)
# ---------------------------------------------------------------------------
def fig15_fluxo_diagnostico_final():
    fig, ax = plt.subplots(figsize=(9.4, 3.7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.4)
    ax.axis("off")

    ax.text(5, 4.12, "Roteiro de Construção do Trabalho Prático Final — Diagnóstico Ambiental Aplicado (50% da Nota)",
            ha="center", fontsize=9.3, fontweight="bold", color=NAVY)

    steps = [
        (0.25, 2.25, "1. RECORTE ESPACIAL\nMicrobacia, encosta,\nmargem ou APP-alvo", "#F4F7FA", NAVY),
        (3.55, 2.25, "2. CARACTERIZAÇÃO\nRelevo, solo, drenagem,\nvegetação e uso da terra", "#EDF6F5", TEAL),
        (6.85, 2.25, "3. DEGRADAÇÃO\nErosão, assoreamento,\nconflitos e passivos", "#FDF3F4", ALERT),
        (6.85, 0.35, "4. INDICADORES\nMatriz PEIR / solo e\nfragilidade (Ross)", "#FCF8EE", GOLD),
        (3.55, 0.35, "5. PROPOSTA TÉCNICA\nConservação, PRAD e\nbioengenharia de solo", "#EFF7F2", FOREST),
        (0.25, 0.35, "6. PRODUTO FINAL\nMapas, relatório técnico\ne socialização (Sem. 16)", "#F4F7FA", NAVY),
    ]
    for x, y, txt, fc, ec in steps:
        ax.add_patch(FancyBboxPatch((x, y), 2.9, 1.35, boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=1.6))
        ax.text(x + 1.45, y + 0.675, txt, ha="center", va="center", fontsize=7.9, fontweight="bold", color=INK)

    ax.annotate("", xy=(3.48, 2.92), xytext=(3.22, 2.92), arrowprops=dict(arrowstyle="->", lw=2.0, color=NAVY))
    ax.annotate("", xy=(6.78, 2.92), xytext=(6.52, 2.92), arrowprops=dict(arrowstyle="->", lw=2.0, color=TEAL))
    ax.annotate("", xy=(8.3, 1.78), xytext=(8.3, 2.18), arrowprops=dict(arrowstyle="->", lw=2.0, color=ALERT))
    ax.annotate("", xy=(6.52, 1.02), xytext=(6.78, 1.02), arrowprops=dict(arrowstyle="->", lw=2.0, color=GOLD))
    ax.annotate("", xy=(3.22, 1.02), xytext=(3.48, 1.02), arrowprops=dict(arrowstyle="->", lw=2.0, color=FOREST))

    save(fig, "fig15_fluxo_diagnostico_final.pdf")


if __name__ == "__main__":
    fig01_triade_socioambiental()
    fig02_aspecto_impacto_risco()
    fig03_etapas_aia_mitigacao()
    fig04_sistema_aberto_escalas()
    fig05_bacia_hidrografica_strahler()
    fig06_morfopedologia_vertente()
    fig07_ecodinamica_ross_matriz()
    fig08_modelo_peir_semiarido()
    fig09_qualidade_solo_radar()
    fig10_evolucao_erosao_linear()
    fig11_usle_sensibilidade()
    fig12_bioengenharia_palicada_talude()
    fig13_efeitos_raizes_solo()
    fig14_licenciamento_apps()
    fig15_fluxo_diagnostico_final()
    print("Todas as 15 figuras vetoriais de Análise Ambiental foram geradas com sucesso!")
