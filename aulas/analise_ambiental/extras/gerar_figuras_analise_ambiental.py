#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera as 11 figuras didatico-cientificas (PNG 300 dpi + SVG) para a disciplina
Analise Ambiental (Bacharelado em Geografia - UEFS).
Paleta institucional: #2135A6, #27368C, #586BA6, #0F2E49, #2E7D32, #D97706, #B03A2E
"""

import os
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, FancyArrowPatch

OUT_DIR = str(Path(__file__).resolve().parents[3] / "img")
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

C_PRIMARY = "#2135A6"
C_DARK = "#0F2E49"
C_SECONDARY = "#27368C"
C_ACCENT = "#586BA6"
C_LIGHT = "#EEF2FA"
C_GREEN = "#2E7D32"
C_GREEN_BG = "#E8F5E9"
C_AMBER = "#D97706"
C_AMBER_BG = "#FEF3C7"
C_RED = "#B03A2E"
C_RED_BG = "#FDEDEC"
C_GRAY = "#4B5563"


def save_both(fig, name):
    png_path = os.path.join(OUT_DIR, f"{name}.png")
    svg_path = os.path.join(OUT_DIR, f"{name}.svg")
    fig.savefig(png_path, dpi=300, bbox_inches="tight", pad_inches=0.18)
    fig.savefig(svg_path, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    print(f"[OK] {name}.png / .svg")


def draw_box(ax, x, y, w, h, title, body="", fc=C_LIGHT, ec=C_PRIMARY, title_color=C_DARK,
             body_color="#1F2937", title_fs=10.0, body_fs=8.2, lw=1.6, round_pad=0.01):
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad={round_pad},rounding_size=0.018",
                         facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2)
    ax.add_patch(box)
    if body:
        n_title_lines = title.count("\n") + 1
        top_y = y + h - h * 0.08
        ax.text(x + w / 2, top_y, title, ha="center", va="top",
                fontsize=title_fs, fontweight="bold", color=title_color, zorder=3, linespacing=1.18)
        title_drop = 0.042 * n_title_lines + 0.018
        body_center_y = (y + (top_y - title_drop)) / 2
        ax.text(x + w / 2, body_center_y, body, ha="center", va="center",
                fontsize=body_fs, color=body_color, zorder=3, linespacing=1.22)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center",
                fontsize=title_fs, fontweight="bold", color=title_color, zorder=3)


def draw_arrow(ax, x1, y1, x2, y2, color=C_PRIMARY, lw=2.0, style="-|>"):
    arr = FancyArrowPatch((x1, y1), (x2, y2),
                          arrowstyle=style, mutation_scale=15,
                          linewidth=lw, color=color, zorder=4)
    ax.add_patch(arr)


# =============================================================================
# 1. aa_mendonca_socioambiental (Aula 3.1)
# =============================================================================
def fig_01_mendonca():
    fig, ax = plt.subplots(figsize=(12.5, 6.3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.95, "Evolução Epistemológica da Abordagem Ambiental na Geografia (Mendonça, 2001)",
            ha="center", va="center", fontsize=13.5, fontweight="bold", color=C_DARK)
    ax.text(0.5, 0.90, "Da dicotomia física/humana à síntese socioambiental (S ↔ N)",
            ha="center", va="center", fontsize=10, color=C_GRAY)

    draw_box(ax, 0.03, 0.54, 0.28, 0.30,
             "1º Momento (Séc. XIX – 1950)\nGeografia Clássica",
             "Meio Ambiente = Natureza (Quadro Físico)\n• Descrição corológica das paisagens\n• Separação Geografia Física vs. Humana\n• Sociedade vista como agente externo",
             fc="#F8FAFC", ec=C_ACCENT, title_color=C_SECONDARY, title_fs=9.6, body_fs=8.0)

    draw_box(ax, 0.36, 0.54, 0.28, 0.30,
             "2º Momento (1950 – 1980)\nRevolução Teorético-Sistêmica",
             "Geossistemas e Ecodinâmica\n• Sotchava (1963), Bertrand (1968), Tricart (1977)\n• Monteiro (1976): Sistema Clima Urbano\n• Ab'Sáber (1969): 3 níveis da Geomorfologia",
             fc=C_LIGHT, ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.6, body_fs=8.0)

    draw_box(ax, 0.69, 0.54, 0.28, 0.30,
             "3º Momento (Pós-1985)\nGeografia Socioambiental",
             "Síntese Sociedade ↔ Natureza (S ↔ N)\n• Mendonça (2001) e Suertegaray (2001)\n• Problemas ecológicos + conflitos sociais\n• Justiça ambiental, risco e vulnerabilidade",
             fc=C_GREEN_BG, ec=C_GREEN, title_color=C_GREEN, title_fs=9.6, body_fs=8.0)

    draw_arrow(ax, 0.315, 0.69, 0.355, 0.69, color=C_PRIMARY, lw=2.2)
    draw_arrow(ax, 0.645, 0.69, 0.685, 0.69, color=C_GREEN, lw=2.2)

    draw_box(ax, 0.03, 0.07, 0.57, 0.39,
             "Os Três Níveis de Abordagem de Aziz Ab'Sáber (1969)",
             "1. Compartimentação Topográfica Regional: macroformas do relevo e níveis de base\n"
             "2. Estrutura Superficial da Paisagem: depósitos correlativos, linhas de pedra e solos\n"
             "3. Fisiologia da Paisagem: dinâmica atual (hidrologia, erosão e ação antrópica)",
             fc="#FFFBEB", ec=C_AMBER, title_color="#92400E", title_fs=10.0, body_fs=8.3)

    draw_box(ax, 0.63, 0.07, 0.34, 0.39,
             "Núcleo da Geografia Socioambiental",
             "Natureza (Geologia + Relevo + Clima +\nHidrologia + Solos + Biota)\n"
             "          ⇅  Co-produção Histórica\n"
             "Sociedade (Estado + Capital + Técnica +\nTrabalho + Território + Classes)",
             fc="#EFF6FF", ec=C_PRIMARY, title_color=C_DARK, title_fs=10.0, body_fs=8.3)

    save_both(fig, "aa_mendonca_socioambiental")


# =============================================================================
# 2. aa_risco_vulnerabilidade_fragilidade (Aula 4.1)
# =============================================================================
def fig_02_risco():
    fig, ax = plt.subplots(figsize=(12.5, 6.3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.95, "Distinção Operacional: Suscetibilidade, Fragilidade, Vulnerabilidade e Risco",
            ha="center", va="center", fontsize=13.5, fontweight="bold", color=C_DARK)
    ax.text(0.5, 0.90, "Alinhado à PNPDEC (Lei 12.608/2012), IPT/Ministério das Cidades, Ross (1994) e Crepani et al. (2001)",
            ha="center", va="center", fontsize=9.8, color=C_GRAY)

    draw_box(ax, 0.03, 0.52, 0.29, 0.32,
             "PERIGO / AMEAÇA (P)\ne SUSCETIBILIDADE",
             "Dimensão Físico-Natural\n• Suscetibilidade: propensão intrínseca\n  do terreno (litologia, declive, solo)\n• Perigo (Hazard): probabilidade temporal\n  de evento (chuva extrema, cheia)",
             fc="#EFF6FF", ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.5, body_fs=8.0)

    draw_box(ax, 0.355, 0.52, 0.29, 0.32,
             "FRAGILIDADE AMBIENTAL\n(Ross, 1994; Crepani, 2001)",
             "Dimensão Ecodinâmica Integrada\n• Potencial: equilíbrio morfogenético\n  natural (relevo + solo + clima)\n• Emergente: fragilidade potencial\n  alterada pelo uso e cobertura da terra",
             fc="#FEF3C7", ec=C_AMBER, title_color="#92400E", title_fs=9.5, body_fs=8.0)

    draw_box(ax, 0.68, 0.52, 0.29, 0.32,
             "EXPOSIÇÃO (E) e\nVULNERABILIDADE (V)",
             "Dimensão Social e Territorial\n• Exposição: população, moradias e\n  infraestrutura na área atingível\n• Vulnerabilidade: fragilidade social\n  e baixa capacidade de resposta",
             fc=C_RED_BG, ec=C_RED, title_color=C_RED, title_fs=9.5, body_fs=8.0)

    draw_arrow(ax, 0.175, 0.51, 0.34, 0.40, color=C_PRIMARY, lw=2.2)
    draw_arrow(ax, 0.50, 0.51, 0.50, 0.40, color=C_AMBER, lw=2.2)
    draw_arrow(ax, 0.825, 0.51, 0.66, 0.40, color=C_RED, lw=2.2)

    draw_box(ax, 0.12, 0.18, 0.76, 0.21,
             "RISCO SOCIOAMBIENTAL / GEODINÂMICO:   R = P × E × V",
             "Sem exposição humana ou patrimônio (E = 0), há perigo natural ou fragilidade, mas NÃO há risco social.\n"
             "Graus de Risco Urbano (IPT): R1 (Baixo) | R2 (Médio) | R3 (Alto - monitoramento) | R4 (Muito Alto - remoção)",
             fc="#1E293B", ec=C_DARK, title_color="#F8FAFC", body_color="#E2E8F0", title_fs=10.5, body_fs=8.2)

    draw_box(ax, 0.03, 0.03, 0.94, 0.11,
             "Capacidade de Suporte (Carrying Capacity): Limite máximo de pressão que um geossistema absorve sem romper sua resiliência.",
             "", fc=C_GREEN_BG, ec=C_GREEN, title_color=C_GREEN, title_fs=9.0)

    save_both(fig, "aa_risco_vulnerabilidade_fragilidade")


# =============================================================================
# 3. aa_sistema_ambiental_escalas (Aula 6.1)
# =============================================================================
def fig_03_escalas():
    fig, ax = plt.subplots(figsize=(12.5, 6.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.95, "Análise Ambiental Integrada: Subsistemas e Compatibilidade Escalar",
            ha="center", va="center", fontsize=13.5, fontweight="bold", color=C_DARK)
    ax.text(0.5, 0.90, "Articulação entre Subsistemas (Rodriguez, Silva & Cavalcanti, 2017) e Escalas de Planejamento (Castro, 1995; IBGE)",
            ha="center", va="center", fontsize=9.5, color=C_GRAY)

    draw_box(ax, 0.03, 0.50, 0.44, 0.35,
             "SISTEMA AMBIENTAL (UNIDADE DE SÍNTESE)",
             "Entradas: Energia Solar, Precipitação, Capital, Trabalho\n"
             "────────────────────────────────────\n"
             "[Subsistema Físico-Natural] ⇄ [Subsistema Socioeconômico]\n"
             "            ↘                            ↙\n"
             "     [Subsistema Político-Institucional / Legal]\n"
             "────────────────────────────────────\n"
             "Saídas: Água, Biomassa, Produção, Sedimentos, Efluentes",
             fc=C_LIGHT, ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.6, body_fs=8.0)

    draw_box(ax, 0.50, 0.50, 0.47, 0.35,
             "Roteiro didático adaptado da análise integrada",
             "1. Organização: pergunta, escala e produtos\n"
             "2. Inventário: bases, fontes, datas e campo\n"
             "3. Análise: processos e relações\n"
             "4. Integração: unidades e conexões\n"
             "5. Diagnóstico: problemas e potencialidades\n"
             "6. Prognóstico: cenários com e sem ação\n"
             "7. Proposição: prioridades, indicadores e revisão",
             fc=C_GREEN_BG, ec=C_GREEN, title_color=C_GREEN, title_fs=9.6, body_fs=8.0)

    ax.text(0.5, 0.43, "Exemplos indicativos de escalas: justificar conforme objetivo, base e precisão",
            ha="center", va="center", fontsize=11, fontweight="bold", color=C_DARK)

    scales = [
        ("Regional / Estadual\n1:250.000 a 1:100.000", "ZEE Estadual (Dec. 4.297/02)\nPlanos de Bacia Hidrográfica\n──────────\nGeossistema / Região\nLandsat / Sentinel", "#DBEAFE", C_PRIMARY),
        ("Municipal / Sub-bacia\n1:50.000 a 1:25.000", "Plano Diretor Municipal\nZoneamento Ambiental\n──────────\nGeofácies / Sub-bacia\nSentinel-2 / CBERS-4A", "#E0E7FF", C_SECONDARY),
        ("Local / Empreendimento\n1:10.000 a 1:5.000", "EIA-RIMA (CONAMA 01/86)\nCarta Geotécnica (IPT)\n──────────\nGeótopo / Vertente\nOrtofotos / VANT", "#FEF3C7", C_AMBER),
        ("Detalhe / Executivo\n1:2.000 a 1:500", "PRAD (IN IBAMA 14/2024)\nBioengenharia e CAR/PRA\n──────────\nFeição Erosiva / Talude\nGNSS RTK + Campo", "#DCFCE7", C_GREEN),
    ]

    x0 = 0.03
    w = 0.222
    gap = 0.017
    for i, (esc, body_txt, fc, ec) in enumerate(scales):
        xi = x0 + i * (w + gap)
        draw_box(ax, xi, 0.05, w, 0.34, esc, body_txt,
                 fc=fc, ec=ec, title_color=ec, title_fs=9.0, body_fs=7.8)

    save_both(fig, "aa_sistema_ambiental_escalas")


# =============================================================================
# 4. aa_bacia_strahler_hidrograma (Aula 7.1)
# =============================================================================
def fig_04_bacia():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.8))
    fig.suptitle("Bacia Hidrográfica: Hierarquia Fluvial de Strahler (1952) e Resposta Hidrológica",
                 fontsize=13.5, fontweight="bold", color=C_DARK, y=0.98)

    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")
    ax1.set_title("A) Divisor Topográfico, APP e Ordem de Strahler", fontsize=11, color=C_PRIMARY, pad=8)

    watershed_xy = np.array([
        [5.0, 0.6], [2.2, 1.4], [0.9, 3.8], [1.1, 6.8], [2.6, 8.9],
        [5.0, 9.4], [7.5, 8.9], [9.0, 6.8], [9.1, 3.8], [7.8, 1.4], [5.0, 0.6]
    ])
    poly = Polygon(watershed_xy, closed=True, facecolor="#ECFDF5", edgecolor=C_DARK,
                   linewidth=2.2, linestyle="--", zorder=1)
    ax1.add_patch(poly)
    ax1.text(5.0, 9.62, "Divisor Topográfico (Linha de Cumeada)", ha="center", va="bottom",
             fontsize=8.8, fontweight="bold", color=C_DARK)

    ax1.plot([5.0, 5.0], [0.6, 4.2], color="#1D4ED8", lw=4.5, zorder=3)
    ax1.plot([5.0, 3.4], [4.2, 6.4], color="#2563EB", lw=3.0, zorder=3)
    ax1.plot([5.0, 6.6], [4.2, 6.4], color="#2563EB", lw=3.0, zorder=3)
    tribs = [
        ([3.4, 2.1], [6.4, 8.0]),
        ([3.4, 4.2], [6.4, 8.2]),
        ([6.6, 5.8], [6.4, 8.2]),
        ([6.6, 7.9], [6.4, 8.0]),
        ([5.0, 2.3], [2.6, 4.2]),
        ([5.0, 7.7], [2.4, 4.0]),
    ]
    for tx, ty in tribs:
        ax1.plot(tx, ty, color="#60A5FA", lw=1.8, zorder=3)

    for px, py in [(2.0, 8.2), (4.2, 8.4), (5.8, 8.4), (8.0, 8.2), (2.1, 4.4), (7.9, 4.2)]:
        ax1.text(px, py, "1ª", fontsize=9, fontweight="bold", color="#1E40AF",
                 bbox=dict(boxstyle="circle,pad=0.18", fc="white", ec="#60A5FA"))

    ax1.text(3.6, 5.4, "2ª", fontsize=9.5, fontweight="bold", color="white",
             bbox=dict(boxstyle="circle,pad=0.2", fc="#2563EB", ec="#1E3A8A"))
    ax1.text(6.4, 5.4, "2ª", fontsize=9.5, fontweight="bold", color="white",
             bbox=dict(boxstyle="circle,pad=0.2", fc="#2563EB", ec="#1E3A8A"))
    ax1.text(5.55, 2.0, "3ª Ordem", fontsize=9.5, fontweight="bold", color="white",
             bbox=dict(boxstyle="round,pad=0.25", fc="#1D4ED8", ec="#1E3A8A"))

    ax1.scatter([5.0], [0.6], s=90, color=C_RED, zorder=5)
    ax1.text(5.0, 0.1, "Exutório (Seção de Controle Q)", ha="center", va="center",
             fontsize=9, fontweight="bold", color=C_RED)

    ax1.text(5.0, -0.7,
             "Índices: Kc = 0,28·P/√A  |  Kf = A/L²  |  Dd = ΣL/A  |  tc = 0,0195·L^0,77·S^-0,385",
             ha="center", va="center", fontsize=8.4, color=C_DARK,
             bbox=dict(boxstyle="round,pad=0.3", fc=C_LIGHT, ec=C_PRIMARY))

    t = np.linspace(0, 12, 300)
    q_cons = 12 + 38 * np.exp(-0.5 * ((t - 6.2) / 1.8) ** 2) * (t > 1.0)
    q_deg = 8 + 88 * np.exp(-0.5 * ((t - 3.2) / 0.85) ** 2) * (t > 1.0)

    ax2.plot(t, q_cons, color=C_GREEN, lw=2.8, label="Bacia Conservada (Alta infiltração, maior tc)")
    ax2.fill_between(t, 0, q_cons, color=C_GREEN, alpha=0.14)

    ax2.plot(t, q_deg, color=C_RED, lw=2.8, linestyle="-",
             label="Bacia Desmatada / Impermeabilizada (Menor tc)")
    ax2.fill_between(t, q_deg, 0, color=C_RED, alpha=0.12)

    ax2.axhline(68, color=C_AMBER, linestyle="--", lw=1.6, label="Vazão de referência hipotética")
    ax2.annotate("Pico de Cheia (Qp)\nRisco de Inundação", xy=(3.2, 95), xytext=(0.4, 78),
                 arrowprops=dict(arrowstyle="->", color=C_RED, lw=1.6),
                 fontsize=8.8, fontweight="bold", color=C_RED)
    ax2.annotate("Escoamento Amortecido\ne Recarga de Base", xy=(6.2, 50), xytext=(7.1, 55),
                 arrowprops=dict(arrowstyle="->", color=C_GREEN, lw=1.6),
                 fontsize=8.8, fontweight="bold", color=C_GREEN)

    ax2.set_title("B) Hidrogramas sintéticos: cenários didáticos, sem calibração local",
                  fontsize=11, color=C_PRIMARY, pad=8)
    ax2.set_xlabel("Tempo (horas após início da chuva)", fontsize=9.5, fontweight="bold")
    ax2.set_ylabel("Vazão no Exutório Q (m³/s)", fontsize=9.5, fontweight="bold")
    ax2.set_xlim(0, 12)
    ax2.set_ylim(0, 118)
    ax2.grid(True, linestyle=":", alpha=0.5)
    ax2.legend(loc="upper right", fontsize=8.2, frameon=True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    save_both(fig, "aa_bacia_strahler_hidrograma")


# =============================================================================
# 5. aa_catena_morfopedologica (Aula 8.1)
# =============================================================================
def fig_05_catena():
    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    ax.text(6.0, 7.15, "Topossequência hipotética: testar a relação entre material, água e posição na vertente",
            ha="center", va="center", fontsize=12.5, fontweight="bold", color=C_DARK)

    x = np.linspace(0.5, 11.5, 300)
    y_surf = 5.4 - 3.3 / (1 + np.exp(-(x - 5.5) * 0.95)) + 0.15 * np.exp(-((x - 2.0) / 1.8) ** 2)
    solum_depth = 1.65 * np.exp(-((x - 2.2) / 3.2) ** 2) + 0.55
    y_b_top = y_surf - 0.38
    y_rock = y_surf - solum_depth

    ax.fill_between(x, 0.6, y_rock, color="#CBD5E1", zorder=1)
    ax.fill_between(x, y_rock, y_b_top, color="#D97706", alpha=0.55, zorder=2)
    ax.fill_between(x, y_b_top, y_surf, color="#92400E", alpha=0.75, zorder=3)
    ax.plot(x, y_surf, color="#14532D", lw=2.8, zorder=4)

    ax.fill_between([9.8, 11.5], [1.6, 1.6], [2.15, 2.15], color="#3B82F6", alpha=0.8, zorder=4)
    ax.text(10.65, 1.85, "Canal Fluvial\n+ APP", ha="center", va="center",
            fontsize=8.5, fontweight="bold", color="white", zorder=5)

    compartments = [
        (2.0, 6.25, "1. TOPO / INTERFLÚVIO\nLatossolo (Bw profundo, bem drenado)\nPredomínio de Infiltração Vertical\nPedogênese > Morfogênese", C_GREEN_BG, C_GREEN),
        (5.5, 5.15, "2. MEIA-ENCOSTA\nArgissolo / Luvissolo (Gradiente Textural A/Bt)\nDescontinuidade Hidráulica (contraste a verificar)\nFluxo Subsuperficial Lateral + Sulcos", C_AMBER_BG, C_AMBER),
        (8.3, 3.65, "3. SOPÉ / COLÚVIO\nCambissolo / Planossolo\nInvestigar surgências e fluxos\nVerificar atividade erosiva", C_RED_BG, C_RED),
        (10.6, 3.35, "4. PLANÍCIE ALUVIAL\nGleissolo / Neossolo Flúvico\nHidromorfismo e Deposição\nAmortecimento de Cheias", "#EFF6FF", C_PRIMARY),
    ]
    for cx, cy, txt, fc, ec in compartments:
        ax.text(cx, cy, txt, ha="center", va="center", fontsize=8.0, color="#111827",
                bbox=dict(boxstyle="round,pad=0.3", fc=fc, ec=ec, lw=1.5), zorder=6)

    draw_arrow(ax, 2.0, 5.4, 2.0, 4.3, color=C_PRIMARY, lw=2.2)
    ax.text(2.0, 4.1, "Infiltração\nProfunda", ha="center", va="top", fontsize=8, fontweight="bold", color=C_PRIMARY)

    draw_arrow(ax, 4.3, 4.2, 6.5, 2.9, color=C_RED, lw=2.4)
    ax.text(5.2, 3.2, "Escoamento Superficial\n(Hortoniano: I > f) + Fluxo no topo do Bt",
            ha="center", va="top", fontsize=8, fontweight="bold", color=C_RED, rotation=-24)

    draw_arrow(ax, 7.3, 2.0, 8.7, 2.25, color="#1D4ED8", lw=2.2)
    ax.text(8.0, 1.75, "Exfiltração / Piping", ha="center", va="top", fontsize=8, fontweight="bold", color="#1D4ED8")

    ax.text(3.2, 1.1, "Substrato Rochoso / Alterita (Horizonte C / R)", fontsize=9.5,
            fontweight="bold", color="#334155")

    save_both(fig, "aa_catena_morfopedologica")


# =============================================================================
# 6. aa_ross_crepani_algebra_mapas (Aula 9.1)
# =============================================================================
def fig_06_ross_crepani():
    fig, ax = plt.subplots(figsize=(12.5, 6.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.95, "Modelagem Cartográfica em SIG: Fragilidade (Ross, 1994) vs. Vulnerabilidade (Crepani et al., 2001)",
            ha="center", va="center", fontsize=13, fontweight="bold", color=C_DARK)
    ax.text(0.5, 0.90, "Operações distintas: registrar regras, tabelas de reclassificação e adaptações",
            ha="center", va="center", fontsize=9.5, color=C_GRAY)

    layers = [
        ("PI 1 · Geomorfologia / Declividade", "Ross: <6% (1) a >30% (5) ou Matriz 11–55\nCrepani: Dissecação, amplitude e declive (1,0 a 3,0)"),
        ("PI 2 · Pedologia", "Textura, estrutura, profundidade e drenagem\nConsultar as tabelas e a correspondência com o SiBCS atual"),
        ("PI 3 · Geologia / Litologia", "Tema da formulação de Crepani\nConsultar a classe litológica e sua nota no método"),
        ("PI 4 · Clima", "Crepani: precipitação e duração do período chuvoso\nEm aplicações de Ross, declarar a adaptação utilizada"),
        ("PI 5 · Uso e Cobertura da Terra", "Proteção, continuidade, sazonalidade e manejo\nCategoria de UC não equivale a classe de cobertura"),
    ]

    y_positions = [0.73, 0.57, 0.41, 0.25, 0.09]
    for (title, desc), y0 in zip(layers, y_positions):
        draw_box(ax, 0.03, y0, 0.44, 0.13, title, desc,
                 fc=C_LIGHT, ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.0, body_fs=7.7)
        draw_arrow(ax, 0.475, y0 + 0.065, 0.535, 0.46, color=C_ACCENT, lw=1.7)

    draw_box(ax, 0.54, 0.30, 0.175, 0.32,
             "ÁLGEBRA DE\nMAPAS (SIG)",
             "Crepani:\n(G+R+S+Vg+C)/5\n\nRoss:\ncombinação e legenda\nhierárquicas",
             fc="#1E293B", ec=C_DARK, title_color="#F8FAFC", body_color="#E2E8F0",
             title_fs=9.5, body_fs=8.0)

    draw_arrow(ax, 0.72, 0.50, 0.76, 0.64, color=C_PRIMARY, lw=2.2)
    draw_arrow(ax, 0.72, 0.42, 0.76, 0.26, color=C_GREEN, lw=2.2)

    draw_box(ax, 0.765, 0.49, 0.21, 0.36,
             "Carta de Fragilidade\nEmergente (Ross, 1994)",
             "1 · Muito Fraca\n"
             "2 · Fraca\n"
             "3 · Média\n"
             "4 · Forte\n"
             "5 · Muito Forte",
             fc=C_AMBER_BG, ec=C_AMBER, title_color="#92400E", title_fs=9.2, body_fs=8.0)

    draw_box(ax, 0.765, 0.08, 0.21, 0.36,
             "Vulnerabilidade Natural\n(Crepani et al., 2001)",
             "1,0 a 1,3 · Estável (Pedog.)\n"
             "1,4 a 1,7 · Mod. Estável\n"
             "1,8 a 2,2 · Med. Vulnerável\n"
             "2,3 a 2,6 · Mod. Vulnerável\n"
             "2,7 a 3,0 · Vulnerável (Morf.)",
             fc=C_GREEN_BG, ec=C_GREEN, title_color=C_GREEN, title_fs=9.2, body_fs=8.0)

    save_both(fig, "aa_ross_crepani_algebra_mapas")


# =============================================================================
# 7. aa_dpsir_iqa_conama357 (Aula 11.1)
# =============================================================================
def fig_07_dpsir():
    fig, ax = plt.subplots(figsize=(12.5, 6.3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.95, "Matriz Causal FPEIR (DPSIR), Índice de Qualidade da Água (IQA) e CONAMA 357/2005",
            ha="center", va="center", fontsize=13, fontweight="bold", color=C_DARK)
    ax.text(0.5, 0.90, "Articulação entre Indicadores de Pressão-Estado-Impacto-Resposta e Enquadramento de Corpos Hídricos",
            ha="center", va="center", fontsize=9.5, color=C_GRAY)

    dpsir = [
        ("F · Força Motriz\n(Driving Force)", "Expansão urbana\nsem saneamento;\nAgronegócio intensivo", "#EFF6FF", C_PRIMARY),
        ("P · Pressão\n(Pressure)", "Lançamento de esgoto\nin natura; Desmatamento\nde mata ciliar", "#FEF3C7", C_AMBER),
        ("E · Estado\n(State)", "Queda de OD (<4 mg/L);\nAlta DBO, Coliformes,\nFósforo e Turbidez", C_RED_BG, C_RED),
        ("I · Impacto\n(Impact)", "Eutrofização (IET);\nMorte de peixes;\nDoenças hídricas", "#FCE7F3", "#9D174D"),
        ("R · Resposta\n(Response)", "ETE, Outorga, Enqua-\ndramento CONAMA 357\ne Restauração de APP", C_GREEN_BG, C_GREEN),
    ]
    w = 0.172
    gap = 0.02
    x0 = 0.03
    for i, (t, b, fc, ec) in enumerate(dpsir):
        xi = x0 + i * (w + gap)
        draw_box(ax, xi, 0.54, w, 0.27, t, b, fc=fc, ec=ec, title_color=ec, title_fs=9.0, body_fs=7.8)
        if i < 4:
            draw_arrow(ax, xi + w + 0.002, 0.675, xi + w + gap - 0.002, 0.675, color=C_DARK, lw=1.8)

    ax.plot([0.89, 0.89, 0.30, 0.30], [0.815, 0.85, 0.85, 0.815], color=C_GREEN, lw=1.8, linestyle="--")
    ax.text(0.60, 0.855, "Retroalimentação de Gestão Ambiental (Controle na Fonte e Restauração)",
            ha="center", va="bottom", fontsize=8.3, fontweight="bold", color=C_GREEN)

    draw_box(ax, 0.03, 0.05, 0.45, 0.43,
             "IQA — 9 Parâmetros e Pesos (wi) no Produtório",
             "1. Oxigênio Dissolvido - OD (0,17)  | 6. Nitrogênio Total (0,10)\n"
             "2. Coliformes Termotoler. (0,15)    | 7. Fósforo Total (0,10)\n"
             "3. pH da Água (0,12)                | 8. Turbidez - NTU (0,08)\n"
             "4. DBO₅,₂₀ (0,10)                   | 9. Sólidos Totais (0,08)\n"
             "5. Variação de Temperatura (0,10)\n"
             "────────────────────────────────────\n"
             "Faixas da tabela ANA para BA/SP: Ótima (80–100) | Boa (52–79) | Aceitável (37–51)\n"
             "Ruim (20–36) | Péssima (0–19)",
             fc=C_LIGHT, ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.2, body_fs=7.6)

    draw_box(ax, 0.50, 0.05, 0.47, 0.43,
             "Classes de Águas Doces — CONAMA nº 357/2005",
             "• Classe Especial: abast. c/ desinfecção; preservação integral\n"
             "• Classe 1: abast. c/ trat. simplificado; recreação; OD ≥ 6 mg/L\n"
             "• Classe 2: abast. c/ trat. convencional; irrigação; OD ≥ 5 mg/L\n"
             "• Classe 3: abast. c/ trat. avançado; dessedentação; OD ≥ 4 mg/L\n"
             "• Classe 4: navegação e harmonia paisagística; OD ≥ 2 mg/L\n"
             "────────────────────────────────────\n"
             "CONAMA 430/2011 (Efluentes) e CONAMA 506/2024 (Ar)",
             fc="#FFFBEB", ec=C_AMBER, title_color="#92400E", title_fs=9.2, body_fs=7.6)

    save_both(fig, "aa_dpsir_iqa_conama357")


# =============================================================================
# 8. aa_perfil_solo_sibcs_capacidade_uso (Aula 12.1)
# =============================================================================
def fig_08_solo_sibcs():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 6.0), gridspec_kw={"width_ratios": [1.05, 1.35]})
    fig.suptitle("Horizontes Pedológicos (SiBCS) e Classes de Capacidade de Uso das Terras (Lepsch et al., 2015)",
                 fontsize=13, fontweight="bold", color=C_DARK, y=0.98)

    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")
    ax1.set_title("A) Perfil hipotético e truncamento (cm ilustrativos)", fontsize=10.8, color=C_PRIMARY)

    horiz_cons = [
        (8.3, 9.0, "#14532D", "O (0–5 cm)", "Serapilheira / Húmus"),
        (6.9, 8.3, "#3F2E21", "A (5–25 cm)", "Mineral + Mat. Orgânica"),
        (5.7, 6.9, "#A1887F", "E (25–40 cm)", "Eluvial (Perda de argila)"),
        (3.2, 5.7, "#B45309", "B (40–110 cm)", "Bt (textural, neste exemplo)"),
        (1.6, 3.2, "#D97706", "C (110–160 cm)", "Saprolito / Rocha alterada"),
        (0.5, 1.6, "#64748B", "R (> 160 cm)", "Rocha Matriz consolidada"),
    ]
    ax1.text(2.45, 9.45, "SOLO CONSERVADO", ha="center", va="center", fontsize=9.0, fontweight="bold", color=C_GREEN)
    for y0, y1, col, hname, hdesc in horiz_cons:
        rect = Rectangle((0.3, y0), 4.3, y1 - y0, facecolor=col, edgecolor="white", lw=1.2)
        ax1.add_patch(rect)
        ax1.text(2.45, (y0 + y1) / 2, f"{hname}\n{hdesc}", ha="center", va="center",
                 fontsize=7.3, fontweight="bold", color="white")

    ax1.text(7.55, 6.35, "SOLO DEGRADADO\n(Decapitado: sem O, A, E)", ha="center", va="center",
             fontsize=8.3, fontweight="bold", color=C_RED)
    horiz_deg = [
        (3.2, 5.5, "#B45309", "B Exposto (0–60 cm)", "Propriedades a verificar"),
        (1.6, 3.2, "#D97706", "C (60–110 cm)", "Material a caracterizar"),
        (0.5, 1.6, "#64748B", "R (> 110 cm)", "Rocha Matriz"),
    ]
    for y0, y1, col, hname, hdesc in horiz_deg:
        rect = Rectangle((5.4, y0), 4.3, y1 - y0, facecolor=col, edgecolor="white", lw=1.2)
        ax1.add_patch(rect)
        ax1.text(7.55, (y0 + y1) / 2, f"{hname}\n{hdesc}", ha="center", va="center",
                 fontsize=7.3, fontweight="bold", color="white")

    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")
    ax2.set_title("B) Sistema de Capacidade de Uso das Terras (Classes I a VIII)", fontsize=10.8, color=C_PRIMARY)

    classes = [
        ("Classe I", "Grupo A · Cultivos Anuais/Perenes s/ restrição (Plano, profundo)", "#15803D"),
        ("Classe II", "Grupo A · Cultivos c/ práticas simples (Plantio em nível / terraços)", "#16A34A"),
        ("Classe III", "Grupo A · Cultivos c/ práticas intensivas (Declive moderado)", "#65A30D"),
        ("Classe IV", "Grupo A · Cultivos anuais ocasionais; risco erosivo elevado", "#CA8A04"),
        ("Classe V", "Grupo B · Pastagem/Silvicultura s/ erosão (Várzea / pedregoso)", "#D97706"),
        ("Classe VI", "Grupo B · Pastagem/Reflorestamento c/ práticas conservacionistas", "#EA580C"),
        ("Classe VII", "Grupo B · Silvicultura/Pastagem muito restrita (Forte declive)", "#DC2626"),
        ("Classe VIII", "Grupo C · Preservação Integral de Flora/Fauna e Abrigo Hídrico", "#991B1B"),
    ]
    for i, (cname, cdesc, col) in enumerate(classes):
        y = 8.6 - i * 1.02
        rect = FancyBboxPatch((0.2, y), 9.6, 0.78, boxstyle="round,pad=0.02,rounding_size=0.08",
                              facecolor=col, edgecolor="white", lw=1.2)
        ax2.add_patch(rect)
        ax2.text(0.45, y + 0.39, f"{cname}  |  {cdesc}", ha="left", va="center",
                 fontsize=7.9, fontweight="bold", color="white")

    ax2.text(5.0, 0.25, "Subclasses de Limitação:  e (erosão/declive)  |  s (solo raso/pedregoso/químico)  |  a (excesso de água)  |  c (clima/seca)",
             ha="center", va="center", fontsize=8.0, fontweight="bold", color=C_DARK,
             bbox=dict(boxstyle="round,pad=0.25", fc=C_LIGHT, ec=C_PRIMARY))

    plt.tight_layout(rect=[0, 0.02, 1, 0.94])
    save_both(fig, "aa_perfil_solo_sibcs_capacidade_uso")


# =============================================================================
# 9. aa_evolucao_vocoroca_piping (Aula 13.1)
# =============================================================================
def fig_09_vocoroca():
    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.95, "Processos de Erosão Hídrica e Dinâmica de Voçorocamento",
            ha="center", va="center", fontsize=13.5, fontweight="bold", color=C_DARK)
    ax.text(0.5, 0.90, "Esquema didático: mecanismos podem coexistir; não representam uma sequência obrigatória",
            ha="center", va="center", fontsize=9.5, color=C_GRAY)

    stages = [
        ("1 · Efeito Splash\n(Impacto da Gota)",
         "• Energia cinética rompe\n  agregados superficiais\n• Selamento dos poros\n• Redução drástica da\n  infiltração (f)",
         "#EFF6FF", C_PRIMARY),
        ("2 · Erosão Laminar\n(Sheet Erosion)",
         "• Escoamento difuso (I > f)\n• Remoção seletiva de\n  argila, silte e MO\n• Exposição de raízes\n  e perda de fertilidade",
         "#FEF3C7", C_AMBER),
        ("3 · Sulcos e Ravinas\n(Rill & Gully Erosion)",
         "• Fluxo concentrado:\n  τ₀ = γ·Rₕ·S > τc\n• Incisão nos horizontes\n  A e B (sazonal)\n• Investigar fluxos subsuperficiais",
         "#FFEDD5", "#EA580C"),
        ("4 · Voçoroca\n(Múltiplos Mecanismos)",
         "• Caracterizar material e fluxos\n• Erosão interna (Piping /\n  Sapping) na base do talude\n• Solapamento e queda de\n  blocos (recuo remontante)",
         C_RED_BG, C_RED),
    ]
    w = 0.215
    gap = 0.025
    x0 = 0.03
    for i, (t, b, fc, ec) in enumerate(stages):
        xi = x0 + i * (w + gap)
        draw_box(ax, xi, 0.48, w, 0.36, t, b, fc=fc, ec=ec, title_color=ec, title_fs=9.3, body_fs=7.9)
        if i < 3:
            draw_arrow(ax, xi + w + 0.003, 0.66, xi + w + gap - 0.003, 0.66, color=C_DARK, lw=2.0)

    draw_box(ax, 0.03, 0.06, 0.46, 0.35,
             "Mecanismo Geotécnico de Recuo da Cabeceira (Headcut)",
             "1. Escoamento em cascata escava poço de dissipação (plunge pool)\n"
             "2. Investigar exfiltração, saturação e possível erosão interna\n"
             "3. Solapamento basal cria fendas de tração no topo do talude\n"
             "4. Ruptura do bloco → avanço remontante em direção ao divisor",
             fc=C_LIGHT, ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.3, body_fs=8.0)

    draw_box(ax, 0.52, 0.06, 0.45, 0.35,
             "Monitoramento Morfométrico Auditável em Campo",
             "• Pinos de Erosão (Erosion Pins): hastes graduadas nos taludes e\n"
             "  interflúvios para medir lâmina erodida (mm/ano) e recuo (m/evento)\n"
             "• Estacas de Sedimentação: medição da cunha de assoreamento\n"
             "• VANT (SfM) / LiDAR: Modelo Digital de Diferença (DoD = MDE_t2\n"
             "  − MDE_t1) para estimar volumes, com corregistro e limite de detecção",
             fc=C_GREEN_BG, ec=C_GREEN, title_color=C_GREEN, title_fs=9.3, body_fs=8.0)

    save_both(fig, "aa_evolucao_vocoroca_piping")


# =============================================================================
# 10. aa_palicadas_retencao_mecanismo (Aula 14.1)
# =============================================================================
def fig_10_palicadas():
    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.2)
    ax.axis("off")

    ax.text(6.0, 6.85, "Mecanismo Hidrossedimentológico de Paliçadas Permeáveis (Check-Dams) em Ravinas/Voçorocas",
            ha="center", va="center", fontsize=12.8, fontweight="bold", color=C_DARK)
    ax.text(6.0, 6.45, "Esquema de retenção: eficiência depende de vazão, material, geometria, implantação e manutenção",
            ha="center", va="center", fontsize=9.5, color=C_GRAY)

    # Perfil longitudinal original mais elevado para não tocar nas caixas inferiores
    x_bed = np.array([1.0, 11.0])
    y_bed = np.array([5.5, 2.3])
    ax.plot(x_bed, y_bed, color=C_RED, lw=2.5, linestyle="--", zorder=2)
    ax.fill_between([1.0, 11.0], [1.75, 1.75], [5.5, 2.3], color="#E2E8F0", zorder=1)

    dams_x = [4.0, 7.0, 10.0]
    for i, dx in enumerate(dams_x):
        yb = 5.5 - 0.32 * (dx - 1.0)
        yt = yb + 0.95
        x_up = dx - 2.3
        y_up = 5.5 - 0.32 * (x_up - 1.0)
        poly_sed = Polygon([[x_up, y_up], [dx, yb], [dx, yt - 0.12]], closed=True,
                           facecolor="#FDE68A", edgecolor="#D97706", lw=1.5, zorder=3)
        ax.add_patch(poly_sed)
        ax.text(dx - 0.95, yb + 0.28, f"Cunha #{i+1} (S_eq)",
                ha="center", va="center", fontsize=7.8, fontweight="bold", color="#92400E", zorder=5)

        rect_dam = Rectangle((dx - 0.12, yb - 0.20), 0.24, 1.15, facecolor="#78350F", edgecolor="#451A03", lw=1.5, zorder=6)
        ax.add_patch(rect_dam)
        ax.text(dx + 0.15, yt + 0.12, f"Paliçada {i+1}\n(Permeável)", ha="left", va="bottom",
                fontsize=8.0, fontweight="bold", color="#451A03", zorder=7)

        ax.plot([dx - 0.35, dx - 0.35], [yt - 0.15, yt + 0.30], color=C_GREEN, lw=2.5, zorder=6)
        ax.plot([dx - 0.50, dx - 0.20], [yt + 0.20, yt + 0.20], color=C_GREEN, lw=2.0, zorder=6)

    draw_arrow(ax, 1.2, 5.65, 2.9, 5.1, color="#1D4ED8", lw=2.2)
    ax.text(2.0, 5.75, "Escoamento Concentrado\n(Alta Energia Cinética)", ha="center", va="bottom",
            fontsize=8.2, fontweight="bold", color="#1D4ED8")

    draw_box(ax, 0.4, 0.15, 5.4, 1.45,
             "Efeito Hidráulico e Geomorfológico Imediato",
             "• A barreira permeável cria remanso, reduzindo a velocidade (v)\n"
             "• O remanso pode favorecer a deposição de parte da carga\n"
             "• Verificar erosão lateral, fundação e efeitos a jusante",
             fc=C_LIGHT, ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.0, body_fs=7.8)

    draw_box(ax, 6.1, 0.15, 5.5, 1.45,
             "Sucessão Bioengenheira (Longo Prazo)",
             "• O sedimento úmido retido é colonizado por gramíneas (Vetiver)\n"
             "• Com a degradação da madeira, reavaliar a função estrutural\n"
             "  e a manutenção; raízes não garantem estabilidade permanente",
             fc=C_GREEN_BG, ec=C_GREEN, title_color=C_GREEN, title_fs=9.0, body_fs=7.8)

    save_both(fig, "aa_palicadas_retencao_mecanismo")


# =============================================================================
# 11. aa_codigo_florestal_app_rl_snuc (Aula 15.1)
# =============================================================================
def fig_11_legislacao():
    fig, ax = plt.subplots(figsize=(12.5, 6.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.95, "Zoneamento Legal do Imóvel Rural (Lei 12.651/2012) e Categorias do SNUC (Lei 9.985/2000)",
            ha="center", va="center", fontsize=13, fontweight="bold", color=C_DARK)
    ax.text(0.5, 0.90, "Áreas de Preservação Permanente (APP), Reserva Legal (RL), CAR/PRA e Unidades de Conservação",
            ha="center", va="center", fontsize=9.5, color=C_GRAY)

    draw_box(ax, 0.03, 0.39, 0.30, 0.46,
             "1 · APPs (Art. 4º, Lei 12.651/12)\nProteção conforme o regime legal",
             "Faixas Marginais (Rios Perenes/Interm.):\n"
             "• Rio < 10 m largura  →  30 m de APP\n"
             "• Rio 10 a 50 m       →  50 m de APP\n"
             "• Rio 50 a 200 m      → 100 m de APP\n"
             "• Rio 200 a 600 m     → 200 m de APP\n"
             "• Rio > 600 m         → 500 m de APP\n"
             "──────────────────────────\n"
             "• Nascentes perenes: raio mín. 50 m\n"
             "• Encostas: declividade > 45° (100%)\n"
             "• Topo de morro: h ≥ 100 m, i média > 25°; terço superior",
             fc=C_GREEN_BG, ec=C_GREEN, title_color=C_GREEN, title_fs=9.0, body_fs=7.6)

    draw_box(ax, 0.35, 0.39, 0.30, 0.46,
             "2 · Reserva Legal (Art. 12)\ne Instrumentos (CAR / PRA)",
             "Percentual Mínimo do Imóvel Rural:\n"
             "• Amazônia Legal (Floresta): 80%\n"
             "• Amazônia Legal (Cerrado):  35%\n"
             "• Amazônia Legal (Campos):   20%\n"
             "• Demais Regiões e Biomas\n"
             "  (Caatinga, Mata Atlântica e\n"
             "   Cerrado fora da Am. Legal): 20%\n"
             "──────────────────────────\n"
             "• Admite manejo florestal sustentável\n"
             "• CAR obrigatório e PRA (Art. 61-A)",
             fc=C_LIGHT, ec=C_PRIMARY, title_color=C_PRIMARY, title_fs=9.0, body_fs=7.6)

    draw_box(ax, 0.67, 0.39, 0.30, 0.46,
             "3 · SNUC (Lei 9.985/2000)\n12 Categorias de UCs",
             "Grupo I · Proteção Integral (5):\n"
             "• Estação Ecológica (ESEC)\n"
             "• Reserva Biológica (REBIO)\n"
             "• Parque Nacional / Estadual / Mun.\n"
             "• Monumento Natural (MONA)\n"
             "• Refúgio de Vida Silvestre (REVIS)\n"
             "──────────────────────────\n"
             "Grupo II · Uso Sustentável (7):\n"
             "• APA, ARIE, FLONA, RESEX,\n"
             "  RDS, Reserva de Fauna e RPPN",
             fc="#FEF3C7", ec=C_AMBER, title_color="#92400E", title_fs=9.0, body_fs=7.6)

    draw_box(ax, 0.03, 0.05, 0.94, 0.29,
             "Instrumentos de Recuperação, Incentivo Econômico e Governança Estadual (Bahia)",
             "• PRAD (IN IBAMA nº 14/2024 no âmbito do Ibama): diagnóstico da área degradada, seleção de técnicas (regeneração,\n"
             "  nucleação, plantio total, bioengenharia), indicadores de monitoramento, cronograma e responsabilidade técnica compatível.\n"
             "• PNPSA (Lei Federal nº 14.119/2021): Pagamento por Serviços Ambientais (conservação hídrica, carbono, biodiversidade).\n"
             "• Política Estadual da Bahia (Lei nº 10.431/2006 e Decreto nº 14.024/2012): SEMA, CEPRAM e INEMA (licenciamento e outorga).",
             fc="#F8FAFC", ec=C_DARK, title_color=C_DARK, title_fs=9.5, body_fs=7.9)

    save_both(fig, "aa_codigo_florestal_app_rl_snuc")


if __name__ == "__main__":
    fig_01_mendonca()
    fig_02_risco()
    fig_03_escalas()
    fig_04_bacia()
    fig_05_catena()
    fig_06_ross_crepani()
    fig_07_dpsir()
    fig_08_solo_sibcs()
    fig_09_vocoroca()
    fig_10_palicadas()
    fig_11_legislacao()
    print("Todas as 11 figuras foram regeneradas com sucesso!")
