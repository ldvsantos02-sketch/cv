# -*- coding: utf-8 -*-
"""
Gera todas as 15 figuras vetoriais (PDF) de alta resolução para a
Apostila Completa de Empreendedorismo Tecnológico e Desenvolvimento Territorial (PPGPT/UEFS).
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

INDIGO = "#1D2D50"
TEAL = "#136F63"
AMBER = "#C27D1A"
BURGUNDY = "#7A1C3A"
ALERT = "#B02A37"
INK = "#22252A"
MUTED = "#5A6370"

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


# FIG 01 — Destruição Criadora e Assimetrias Territoriais (Cap. 1)
def fig01_schumpeter_territorio():
    fig, ax = plt.subplots(figsize=(9.2, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.6)
    ax.axis("off")
    ax.text(5, 4.3, "Inovação Tecnológica (Schumpeter / Dosi) e Bifurcação Territorial", ha="center", fontsize=9.8, fontweight="bold", color=INDIGO)

    ax.add_patch(FancyBboxPatch((0.25, 1.5), 2.2, 1.7, boxstyle="round,pad=0.09", fc="#F3F6FA", ec=INDIGO, lw=1.6))
    ax.text(1.35, 2.35, "BASE DE P&D\nConhecimento,\nICT, capital humano,\ncultura técnica", ha="center", va="center", fontsize=7.9, fontweight="bold", color=INDIGO)

    ax.add_patch(FancyBboxPatch((3.15, 1.5), 2.5, 1.7, boxstyle="round,pad=0.09", fc="#FCF7EC", ec=AMBER, lw=1.6))
    ax.text(4.4, 2.35, "DESTRUIÇÃO CRIADORA\nNovas combinações\n(produto, processo,\nmercado, insumo)", ha="center", va="center", fontsize=7.9, fontweight="bold", color=INK)

    ax.add_patch(FancyBboxPatch((6.45, 2.55), 3.3, 1.35, boxstyle="round,pad=0.08", fc="#FDF3F4", ec=ALERT, lw=1.5))
    ax.text(8.1, 3.22, "CONCENTRAÇÃO (Path Dependence)\nAglomeração nos grandes centros;\nlock-in e drenagem de talentos", ha="center", va="center", fontsize=7.6, fontweight="bold", color=ALERT)

    ax.add_patch(FancyBboxPatch((6.45, 0.55), 3.3, 1.35, boxstyle="round,pad=0.08", fc="#EEF7F5", ec=TEAL, lw=1.5))
    ax.text(8.1, 1.22, "ESPECIALIZAÇÃO INTELIGENTE\nEnraizamento em ativos locais;\nretenção de valor no território", ha="center", va="center", fontsize=7.6, fontweight="bold", color=TEAL)

    ax.annotate("", xy=(3.08, 2.35), xytext=(2.52, 2.35), arrowprops=dict(arrowstyle="->", lw=2.0, color=INDIGO))
    ax.annotate("", xy=(6.38, 3.22), xytext=(5.72, 2.65), arrowprops=dict(arrowstyle="->", lw=1.9, color=ALERT))
    ax.annotate("", xy=(6.38, 1.22), xytext=(5.72, 2.05), arrowprops=dict(arrowstyle="->", lw=1.9, color=TEAL))
    save(fig, "fig01_schumpeter_territorio.pdf")


# FIG 02 — Cinco Forças de Porter vs. Eficiência Coletiva (Cap. 2)
def fig02_porter_eficiencia_coletiva():
    fig, ax = plt.subplots(figsize=(9.2, 4.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.8)
    ax.axis("off")
    ax.text(5, 4.5, "Cinco Forças de Porter (Firma Isolada) vs. Eficiência Coletiva (APL)", ha="center", fontsize=9.6, fontweight="bold", color=INDIGO)

    # Centro: Rivalidade
    ax.add_patch(FancyBboxPatch((3.35, 1.75), 3.3, 1.15, boxstyle="round,pad=0.08", fc="#F3F6FA", ec=INDIGO, lw=1.8))
    ax.text(5.0, 2.32, "RIVALIDADE ENTRE\nCONCORRENTES\n(Cooperação + Competição no APL)", ha="center", va="center", fontsize=7.8, fontweight="bold", color=INDIGO)

    # 4 forças ao redor
    cards = [
        (3.55, 3.45, 2.9, 0.85, "Ameaça de Novos Entrantes\n(Barreiras: escala, PI, capital)", "#FCF7EC", AMBER),
        (3.55, 0.35, 2.9, 0.85, "Produtos ou Serviços Substitutos\n(Pressão tecnológica)", "#FCF7EC", AMBER),
        (0.25, 1.85, 2.5, 0.95, "Poder de Barganha\ndos Fornecedores", "#EEF7F5", TEAL),
        (7.25, 1.85, 2.5, 0.95, "Poder de Barganha\ndos Compradores", "#EEF7F5", TEAL),
    ]
    for x, y, w, h, txt, fc, ec in cards:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.4))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.5, fontweight="bold", color=INK)

    ax.annotate("", xy=(5.0, 2.98), xytext=(5.0, 3.40), arrowprops=dict(arrowstyle="->", lw=1.6, color=AMBER))
    ax.annotate("", xy=(5.0, 1.68), xytext=(5.0, 1.25), arrowprops=dict(arrowstyle="->", lw=1.6, color=AMBER))
    ax.annotate("", xy=(3.28, 2.32), xytext=(2.82, 2.32), arrowprops=dict(arrowstyle="->", lw=1.6, color=TEAL))
    ax.annotate("", xy=(6.72, 2.32), xytext=(7.18, 2.32), arrowprops=dict(arrowstyle="->", lw=1.6, color=TEAL))
    save(fig, "fig02_porter_eficiencia_coletiva.pdf")


# FIG 03 — Modelo Causal de Ecossistema Empreendedor (Stam, 2015) (Cap. 3)
def fig03_ecossistema_stam():
    fig, ax = plt.subplots(figsize=(9.4, 3.7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.4)
    ax.axis("off")
    ax.text(5, 4.12, "Modelo Integrativo de Ecossistema Empreendedor (Stam, 2015; Isenberg, 2011)", ha="center", fontsize=9.4, fontweight="bold", color=INDIGO)

    cols = [
        (0.25, 2.2, "1. CONDIÇÕES DE BASE\n(Framework)\n• Instituições formais/informais\n• Cultura empreendedora\n• Infraestrutura física\n• Demanda regional", "#F3F6FA", INDIGO),
        (2.75, 2.2, "2. CONDIÇÕES SISTÊMICAS\n(Coração do Ecossistema)\n• Redes e capital social\n• Liderança e finanças\n• Talento e conhecimento\n• Serviços intermediários", "#EEF7F5", TEAL),
        (5.25, 2.2, "3. RESULTADOS\n(Outputs)\n• Startups inovadoras\n• Spin-offs acadêmicas\n• Negócios de impacto\n• Empreend. social", "#FCF7EC", AMBER),
        (7.75, 2.0, "4. IMPACTO\n(Outcomes)\n• Criação de valor\n  territorial\n• Empregos qualif.\n• Bem-estar social", "#FDF3F4", BURGUNDY),
    ]
    for i, (x, w, txt, fc, ec) in enumerate(cols):
        ax.add_patch(FancyBboxPatch((x, 0.85), w, 2.8, boxstyle="round,pad=0.08", fc=fc, ec=ec, lw=1.6))
        ax.text(x + 0.12, 2.25, txt, ha="left", va="center", fontsize=7.3, fontweight="bold", color=INK)
        if i < 3:
            ax.annotate("", xy=(x + w + 0.27, 2.25), xytext=(x + w + 0.03, 2.25),
                        arrowprops=dict(arrowstyle="->", lw=1.8, color=INDIGO))
    ax.annotate("", xy=(1.35, 0.78), xytext=(8.75, 0.78),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.14", lw=1.5, ls="--", color=TEAL))
    ax.text(5.0, 0.25, "Retroalimentação de longo prazo: sucessos reinvestem talento, mentoria e capital no território", ha="center", fontsize=7.6, fontweight="bold", color=TEAL)
    save(fig, "fig03_ecossistema_stam.pdf")


# FIG 04 — Hélice Quádrupla / Quíntupla (Cap. 4)
def fig04_helice_quintupla():
    fig, ax = plt.subplots(figsize=(8.4, 3.8))
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-2.1, 2.1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(0, 1.92, "Da Hélice Trípode à Hélice Quíntupla na Governança Territorial", ha="center", fontsize=9.8, fontweight="bold", color=INDIGO)

    # Anel externo: Socioecologia (5ª hélice)
    c_out = Circle((0, -0.05), 1.82, fc="#EEF7F5", alpha=0.55, ec=TEAL, lw=2.0, ls="--")
    ax.add_patch(c_out)
    ax.text(0, -1.72, "5ª Hélice: Meio Ambiente e Transição Socioecológica (Sustentabilidade)", ha="center", fontsize=7.8, fontweight="bold", color=TEAL)

    # 4 hélices internas
    nodes = [
        (-1.15, 0.75, "1. UNIVERSIDADE / ICT\nP&D, ciência, formação\ne spin-offs", INDIGO, "#F3F6FA"),
        (1.15, 0.75, "2. EMPRESAS / MERCADO\nProdução, risco, escala\ne cadeias produtivas", AMBER, "#FCF7EC"),
        (-1.15, -0.75, "3. ESTADO / GOVERNO\nMarco legal, subvenção,\ncompras públicas (missões)", BURGUNDY, "#FDF3F4"),
        (1.15, -0.75, "4. SOCIEDADE CIVIL\nDemandas sociais, cultura,\ncontrole social e ONGs", TEAL, "#EEF7F5"),
    ]
    for x, y, txt, ec, fc in nodes:
        ax.add_patch(FancyBboxPatch((x - 1.05, y - 0.42), 2.1, 0.84, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.5))
        ax.text(x, y, txt, ha="center", va="center", fontsize=7.3, fontweight="bold", color=INK)

    ax.add_patch(Circle((0, 0), 0.46, fc=INDIGO, ec="white", lw=1.8, zorder=5))
    ax.text(0, 0, "INOVAÇÃO\nTERRITORIAL", ha="center", va="center", fontsize=6.8, fontweight="bold", color="white", zorder=6)
    save(fig, "fig04_helice_quintupla.pdf")


# FIG 05 — Teoria da Mudança e Espectro de Impacto (Cap. 5)
def fig05_teoria_mudanca_espectro():
    fig, ax = plt.subplots(figsize=(9.4, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.3)
    ax.axis("off")
    ax.text(5, 4.02, "Cadeia Lógica da Teoria da Mudança (Negócios de Impacto Territorial)", ha="center", fontsize=9.5, fontweight="bold", color=INDIGO)

    boxes = [
        (0.2, 1.7, "1. INSUMOS\n(Inputs)\nCapital, equipe,\nsaberes locais", "#F3F6FA", INDIGO),
        (2.15, 1.7, "2. ATIVIDADES\nCapacitação, P&D,\nprodução local", "#EEF7F5", TEAL),
        (4.1, 1.7, "3. PRODUTOS\n(Outputs)\nBens/serviços\nentregues", "#FCF7EC", AMBER),
        (6.05, 1.7, "4. RESULTADOS\n(Outcomes)\nMudança direta\nno público-alvo", "#FDF3F4", BURGUNDY),
        (8.0, 1.78, "5. IMPACTO\nTransformação\nsocial/ambiental\nde longo prazo", "#136F63", "#0E4F46"),
    ]
    for i, (x, w, txt, fc, ec) in enumerate(boxes):
        tc = "white" if i == 4 else INK
        ax.add_patch(FancyBboxPatch((x, 1.45), w, 2.0, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.6))
        ax.text(x + w / 2, 2.45, txt, ha="center", va="center", fontsize=7.6, fontweight="bold", color=tc)
        if i < 4:
            ax.annotate("", xy=(x + w + 0.22, 2.45), xytext=(x + w + 0.03, 2.45),
                        arrowprops=dict(arrowstyle="->", lw=1.8, color=INDIGO))

    ax.add_patch(FancyBboxPatch((0.4, 0.35), 9.2, 0.72, boxstyle="round,pad=0.06", fc="#FCF7EC", ec=AMBER, lw=1.1))
    ax.text(5.0, 0.71, "Espectro: Filantropia tradicional  ←  Negócio de Impacto (retorno + impacto mensurável)  →  Empresa comercial pura",
            ha="center", va="center", fontsize=7.9, fontweight="bold", color=INDIGO)
    save(fig, "fig05_teoria_mudanca_espectro.pdf")


# FIG 06 — Tecnologia Social + Indicações Geográficas (Cap. 6)
def fig06_tecnologia_social_igs():
    fig, ax = plt.subplots(figsize=(9.2, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.3)
    ax.axis("off")
    ax.text(5, 4.02, "Valorização de Ativos Territoriais: Tecnologia Social (Dagnino) e Indicações Geográficas", ha="center", fontsize=9.3, fontweight="bold", color=INDIGO)

    ax.add_patch(FancyBboxPatch((0.3, 0.55), 4.4, 3.05, boxstyle="round,pad=0.1", fc="#EEF7F5", ec=TEAL, lw=1.6))
    ax.text(2.5, 3.25, "TECNOLOGIA SOCIAL (Dagnino, 2014)", ha="center", fontsize=8.8, fontweight="bold", color=TEAL)
    ax.text(0.55, 1.85, "• Adaptada ao pequeno produtor e à comunidade\n• Não discriminatória e horizontal\n• Orientada a mercado interno/solidário\n• Libera criatividade local e autonomia\n• Ex.: cisternas de placas, bioágua, cooperativas",
            ha="left", va="center", fontsize=7.8, color=INK)

    ax.add_patch(FancyBboxPatch((5.3, 0.55), 4.4, 3.05, boxstyle="round,pad=0.1", fc="#FCF7EC", ec=AMBER, lw=1.6))
    ax.text(7.5, 3.25, "INDICAÇÕES GEOGRÁFICAS (INPI)", ha="center", fontsize=8.8, fontweight="bold", color=AMBER)
    ax.text(5.55, 1.85, "• Indicação de Procedência (IP): reputação/\n  tradição consolidada de um território\n• Denominação de Origem (DO): qualidade deve-se\n  essencialmente ao meio geográfico (terroir)\n• Protege saber-fazer e retém prêmio de preço",
            ha="left", va="center", fontsize=7.8, color=INK)

    ax.annotate("", xy=(5.22, 2.05), xytext=(4.78, 2.05), arrowprops=dict(arrowstyle="<->", lw=2.0, color=INDIGO))
    save(fig, "fig06_tecnologia_social_igs.pdf")


# FIG 07 — Curva J / Vale da Morte e Effectuation vs Causation (Cap. 7)
def fig07_vale_da_morte():
    fig, ax = plt.subplots(figsize=(8.6, 3.7))
    t = np.linspace(0, 8, 200)
    # Fluxo de caixa acumulado típico (Curva J)
    cf = -2.2 * np.exp(-((t - 2.3) ** 2) / 1.8) + 0.55 * np.maximum(t - 3.6, 0) ** 1.35 - 0.35
    ax.plot(t, cf, color=INDIGO, lw=2.6, label="Fluxo de caixa acumulado do empreendimento tecnológico")
    ax.axhline(0, color=MUTED, lw=1.1, ls="--")
    ax.fill_between(t, cf, 0, where=(cf < 0), color=ALERT, alpha=0.15, label="Vale da Morte (queima de caixa em P&D e validação)")
    ax.fill_between(t, cf, 0, where=(cf >= 0), color=TEAL, alpha=0.15, label="Fase de retorno e escala sustentável")

    ax.annotate("Ponto de Mínimo\n(Maior risco financeiro)", xy=(2.3, -2.55), xytext=(0.4, -2.65),
                arrowprops=dict(arrowstyle="->", color=ALERT, lw=1.4), fontsize=8.0, fontweight="bold", color=ALERT)
    ax.annotate("Break-even\n(Payback)", xy=(4.7, 0), xytext=(4.1, 1.25),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.4), fontsize=8.2, fontweight="bold", color=TEAL)

    ax.set_xticks([0.8, 2.3, 4.7, 7.0])
    ax.set_xticklabels(["Pesquisa /\nIdeação", "Protótipo /\nValidação", "Tração /\nBreak-even", "Escala"], fontsize=8.2, fontweight="bold")
    ax.set_ylabel("Caixa acumulado (escala ilustrativa)", fontsize=8.8)
    ax.set_title("O 'Vale da Morte' Tecnológico e a Transição Bancada → Mercado", fontsize=9.6, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=7.9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig07_vale_da_morte.pdf")


# FIG 08 — Funil TAM / SAM / SOM (Cap. 8)
def fig08_tam_sam_som():
    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    ax.set_xlim(-3.2, 5.8)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")

    c_tam = Circle((0, 0), 1.9, fc="#F3F6FA", ec=INDIGO, lw=2.0)
    c_sam = Circle((0, -0.45), 1.35, fc="#FCF7EC", ec=AMBER, lw=2.0)
    c_som = Circle((0, -0.9), 0.78, fc="#EEF7F5", ec=TEAL, lw=2.2)
    for c in (c_tam, c_sam, c_som):
        ax.add_patch(c)

    ax.text(0, 1.35, "TAM", ha="center", fontsize=11, fontweight="bold", color=INDIGO)
    ax.text(0, 0.35, "SAM", ha="center", fontsize=11, fontweight="bold", color=AMBER)
    ax.text(0, -0.9, "SOM", ha="center", fontsize=11, fontweight="bold", color=TEAL)

    ax.annotate("TAM (Total Addressable Market)\nDemanda global ou nacional total do setor\n(ex.: mercado brasileiro de bioinsumos)",
                xy=(1.2, 1.2), xytext=(2.3, 1.15), arrowprops=dict(arrowstyle="->", color=INDIGO),
                fontsize=8.0, fontweight="bold", color=INDIGO)
    ax.annotate("SAM (Serviceable Available Market)\nParcela alcançável pelo seu modelo/tecnologia\n(ex.: propriedades do Semiárido Baiano)",
                xy=(1.05, -0.1), xytext=(2.3, -0.1), arrowprops=dict(arrowstyle="->", color=AMBER),
                fontsize=8.0, fontweight="bold", color="#8A5A10")
    ax.annotate("SOM (Serviceable Obtainable Market)\nFatia realista nos primeiros 2–3 anos\n(capacidade operacional + orçamento)",
                xy=(0.6, -1.1), xytext=(2.3, -1.3), arrowprops=dict(arrowstyle="->", color=TEAL),
                fontsize=8.0, fontweight="bold", color=TEAL)
    ax.text(1.3, 2.02, "Dimensionamento Realista de Mercado (TAM / SAM / SOM)", ha="center", fontsize=9.8, fontweight="bold", color=INDIGO)
    save(fig, "fig08_tam_sam_som.pdf")


# FIG 09 — Business Model Canvas + Ciclo Lean (Cap. 9)
def fig09_canvas_lean():
    fig, ax = plt.subplots(figsize=(9.5, 4.1))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.2)
    ax.axis("off")
    ax.text(5, 4.92, "Business Model Canvas (Osterwalder & Pigneur) — Os 9 Blocos Integrados", ha="center", fontsize=9.5, fontweight="bold", color=INDIGO)

    # Desenho do grid clássico 5 colunas x 2 linhas + rodapé
    blocks = [
        (0.2, 1.75, 1.85, 2.8, "Parcerias\nPrincipais\n(ICTs, APLs,\ncooperativas)", "#F3F6FA", INDIGO),
        (2.1, 3.18, 1.85, 1.37, "Atividades-\nChave\n(P&D, validação)", "#F3F6FA", INDIGO),
        (2.1, 1.75, 1.85, 1.37, "Recursos\nPrincipais\n(PI, equipe, lab.)", "#F3F6FA", INDIGO),
        (4.0, 1.75, 2.0, 2.8, "PROPOSTA DE\nVALOR\n(Dor resolvida +\nimpacto gerado)", "#FCF7EC", AMBER),
        (6.05, 3.18, 1.85, 1.37, "Relacionamento\ncom Clientes\n(suporte, cocriação)", "#EEF7F5", TEAL),
        (6.05, 1.75, 1.85, 1.37, "Canais\n(entrega, B2B,\nB2G, digital)", "#EEF7F5", TEAL),
        (7.95, 1.75, 1.85, 2.8, "Segmentos de\nClientes\n(quem paga e\nquem usa)", "#EEF7F5", TEAL),
        (0.2, 0.35, 4.75, 1.28, "Estrutura de Custos (CAPEX, OPEX, P&D, regularização)", "#FDF3F4", ALERT),
        (5.05, 0.35, 4.75, 1.28, "Fontes de Receita (venda, assinatura/SaaS, licenciamento de PI, fomento)", "#EFF7F2", TEAL),
    ]
    for x, y, w, h, txt, fc, ec in blocks:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04", fc=fc, ec=ec, lw=1.3))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.3, fontweight="bold", color=INK)
    save(fig, "fig09_canvas_lean.pdf")


# FIG 10 — Escada do Capital para Empreendimentos Tecnológicos (Cap. 10)
def fig10_escada_capital():
    fig, ax = plt.subplots(figsize=(9.2, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.6)
    ax.axis("off")
    ax.text(5, 4.32, "Escada do Capital: Instrumentos de Fomento e Investimento por Estágio de Maturidade", ha="center", fontsize=9.3, fontweight="bold", color=INDIGO)

    steps = [
        (0.3, 0.5, 1.75, 1.0, "1. Bootstrapping\n& Recursos Próprios\n(Ideação / MVP)", "#F3F6FA", INDIGO),
        (2.2, 1.1, 1.75, 1.1, "2. Subvenção\nEconômica (Não\nReembolsável)\nCNPq/FAPESB/\nFINEP/Centelha", "#EEF7F5", TEAL),
        (4.1, 1.7, 1.75, 1.1, "3. Investidor-Anjo\ne Aceleradoras\n(Validação inicial)", "#FCF7EC", AMBER),
        (6.0, 2.3, 1.75, 1.1, "4. Venture Capital\nSeed / Série A\n(Tração e escala)", "#FDF3F4", BURGUNDY),
        (7.9, 2.9, 1.85, 1.1, "5. Crédito Regional\n& BNDES / BNB\n(FNE Inovação,\nExpansão fabril)", "#1D2D50", "#121C36"),
    ]
    for i, (x, y, w, h, txt, fc, ec) in enumerate(steps):
        tc = "white" if i == 4 else INK
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.5))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.1, fontweight="bold", color=tc)
    ax.annotate("", xy=(9.4, 2.7), xytext=(0.6, 0.35), arrowprops=dict(arrowstyle="->", lw=2.0, color=TEAL, ls="--"))
    ax.text(5.8, 0.55, "Aumento da maturidade tecnológica (TRL), receita e redução do risco técnico", ha="center", fontsize=8.0, fontweight="bold", color=TEAL)
    save(fig, "fig10_escada_capital.pdf")


# FIG 11 — Open Innovation e Spin-off Acadêmica (Cap. 11)
def fig11_open_innovation_spinoff():
    fig, ax = plt.subplots(figsize=(9.2, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.3)
    ax.axis("off")
    ax.text(5, 4.02, "Inovação Aberta (Chesbrough) e Transição de Spin-off Acadêmica (ICT → Mercado)", ha="center", fontsize=9.3, fontweight="bold", color=INDIGO)

    ax.add_patch(FancyBboxPatch((0.3, 1.2), 2.8, 2.2, boxstyle="round,pad=0.09", fc="#F3F6FA", ec=INDIGO, lw=1.6))
    ax.text(1.7, 2.3, "ICT / UNIVERSIDADE\n(ex.: UEFS / NIT)\nPesquisa básica/aplicada,\npatentes, cultivares,\nsoftwares e laboratórios", ha="center", va="center", fontsize=7.6, fontweight="bold", color=INDIGO)

    ax.add_patch(FancyBboxPatch((3.6, 1.2), 2.8, 2.2, boxstyle="round,pad=0.09", fc="#FCF7EC", ec=AMBER, lw=1.6))
    ax.text(5.0, 2.3, "TRANSFERÊNCIA &\nINCUBAÇÃO\nLicenciamento de PI,\nroyalties, Marco Legal\nde CT&I (Lei 13.243/16)", ha="center", va="center", fontsize=7.6, fontweight="bold", color=INK)

    ax.add_patch(FancyBboxPatch((6.9, 1.2), 2.8, 2.2, boxstyle="round,pad=0.09", fc="#EEF7F5", ec=TEAL, lw=1.6))
    ax.text(8.3, 2.3, "SPIN-OFF ACADÊMICA\nOU PARCERIA CORPOR.\nProduto validado,\nmercado, geração de\nempregos e impostos", ha="center", va="center", fontsize=7.6, fontweight="bold", color=TEAL)

    ax.annotate("", xy=(3.52, 2.3), xytext=(3.18, 2.3), arrowprops=dict(arrowstyle="->", lw=2.0, color=INDIGO))
    ax.annotate("", xy=(6.82, 2.3), xytext=(6.48, 2.3), arrowprops=dict(arrowstyle="->", lw=2.0, color=TEAL))
    ax.text(5.0, 0.55, "Fluxo bidirecional: demandas reais do território retroalimentam novas agendas de pesquisa na universidade",
            ha="center", fontsize=7.9, fontweight="bold", color=BURGUNDY)
    save(fig, "fig11_open_innovation_spinoff.pdf")


# FIG 12 — Ciclo de Projetos e Matriz Locacional (Cap. 12)
def fig12_ciclo_projetos_localizacao():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.7), gridspec_kw={"width_ratios": [1.05, 1.15]})

    # Painel A: Ciclo de Projeto
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 5.2)
    ax1.axis("off")
    ax1.text(5, 4.9, "Ciclo de Elaboração de Projetos (Woiler & Mathias)", ha="center", fontsize=8.8, fontweight="bold", color=INDIGO)
    stages = [
        (3.8, "1. Estudo de Mercado e Demanda Territorial", INDIGO, "#F3F6FA"),
        (2.85, "2. Engenharia do Projeto e Decisão Locacional", TEAL, "#EEF7F5"),
        (1.9, "3. Orçamento: CAPEX + Capital de Giro + OPEX", AMBER, "#FCF7EC"),
        (0.95, "4. Projeção do Fluxo de Caixa e Viabilidade", BURGUNDY, "#FDF3F4"),
    ]
    for y, txt, ec, fc in stages:
        ax1.add_patch(FancyBboxPatch((0.4, y), 9.2, 0.68, boxstyle="round,pad=0.06", fc=fc, ec=ec, lw=1.4))
        ax1.text(5.0, y + 0.34, txt, ha="center", va="center", fontsize=7.8, fontweight="bold", color=INK)
    for y in [3.8, 2.85, 1.9]:
        ax1.annotate("", xy=(5.0, y - 0.25), xytext=(5.0, y - 0.02), arrowprops=dict(arrowstyle="->", lw=1.5, color=INDIGO))

    # Painel B: Exemplo visual de Matriz Locacional Ponderada
    cidades = ["Município A\n(Metrópole)", "Município B\n(Polo Regional)", "Município C\n(Periférico)"]
    scores = [7.45, 8.35, 6.20]
    cores = [INDIGO, TEAL, MUTED]
    bars = ax2.bar(cidades, scores, color=cores, width=0.52)
    for b, v in zip(bars, scores):
        ax2.text(b.get_x() + b.get_width() / 2, v + 0.2, f"{v:.2f}".replace(".", ","), ha="center", fontsize=9, fontweight="bold")
    ax2.set_ylim(0, 10)
    ax2.set_ylabel("Nota Ponderada (0 a 10)", fontsize=8.5)
    ax2.set_title("Decisão Locacional por Matriz Ponderada\n(Logística, P&D, Incentivos e Mão de Obra)", fontsize=8.8, fontweight="bold", color=INDIGO)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    save(fig, "fig12_ciclo_projetos_localizacao.pdf")


# FIG 13 — Perfil do VPL × Taxa de Desconto (TIR) (Cap. 13)
def fig13_perfil_vpl_tir():
    fig, ax = plt.subplots(figsize=(8.2, 3.8))
    # Projeto exemplo: CF0 = -100.000; CF1..3 = 45.000 -> TIR ≈ 16,65%
    cfs = [-100000, 45000, 45000, 45000]
    rates = np.linspace(0.0, 0.30, 150)
    vpls = [sum(cf / ((1 + r) ** t) for t, cf in enumerate(cfs)) / 1000.0 for r in rates]
    # Calcular TIR aproximada
    tir = np.interp(0.0, vpls[::-1], rates[::-1]) * 100

    ax.plot(rates * 100, vpls, color=INDIGO, lw=2.6, label="Curva do VPL (projeto exemplo: −R$ 100 mil + 3× R$ 45 mil)")
    ax.axhline(0, color=MUTED, lw=1.2)
    ax.axvline(12, ls="--", color=TEAL, lw=1.5, label="TMA = 12% a.a. → VPL = +R$ 8,08 mil (Viável!)")
    ax.scatter([12], [sum(cf / (1.12 ** t) for t, cf in enumerate(cfs)) / 1000.0], color=TEAL, s=65, zorder=5)
    ax.scatter([tir], [0], color=ALERT, s=75, zorder=6)
    ax.annotate(f"TIR ≈ {tir:.2f}%".replace(".", ",") + "\n(onde VPL = 0)",
                xy=(tir, 0), xytext=(tir + 2.5, 11.5),
                arrowprops=dict(arrowstyle="->", color=ALERT, lw=1.5),
                fontsize=8.3, fontweight="bold", color=ALERT,
                bbox=dict(boxstyle="round,pad=0.25", fc="#FDF3F4", ec=ALERT))
    ax.fill_between(rates * 100, 0, vpls, where=(np.array(vpls) >= 0), color=TEAL, alpha=0.12)
    ax.fill_between(rates * 100, 0, vpls, where=(np.array(vpls) < 0), color=ALERT, alpha=0.12)

    ax.set_xlim(0, 30)
    ax.set_xlabel("Taxa de Desconto / TMA (% ao ano)", fontsize=9)
    ax.set_ylabel("VPL (em R$ mil)", fontsize=9)
    ax.set_title("Gráfico Clássico de Viabilidade: Perfil do VPL em Função da Taxa de Desconto", fontsize=9.6, fontweight="bold", color=INDIGO)
    ax.grid(True, ls=":", alpha=0.6)
    ax.legend(loc="upper right", fontsize=8.0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig13_perfil_vpl_tir.pdf")


# FIG 14 — Fluxo de Caixa Descontado (EV vs Equity) e Venture Capital (Cap. 14)
def fig14_valuation_fcd_vc():
    fig, ax = plt.subplots(figsize=(9.2, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.3)
    ax.axis("off")
    ax.text(5, 4.02, "Arquitetura do Valuation por Fluxo de Caixa Descontado (Damodaran, 2010)", ha="center", fontsize=9.5, fontweight="bold", color=INDIGO)

    ax.add_patch(FancyBboxPatch((0.3, 1.4), 2.7, 2.0, boxstyle="round,pad=0.08", fc="#F3F6FA", ec=INDIGO, lw=1.6))
    ax.text(1.65, 2.4, "1. PROJEÇÃO DE FCL\nFluxos de Caixa Livres\n(anos 1 a N) +\nValor Terminal (VT)", ha="center", va="center", fontsize=7.8, fontweight="bold", color=INDIGO)

    ax.add_patch(FancyBboxPatch((3.65, 1.4), 2.7, 2.0, boxstyle="round,pad=0.08", fc="#FCF7EC", ec=AMBER, lw=1.6))
    ax.text(5.0, 2.4, "2. DESCONTO AO WACC\nEnterprise Value (EV)\n= Σ FCLₜ/(1+WACC)ᵗ\n+ VT/(1+WACC)ᴺ", ha="center", va="center", fontsize=7.6, fontweight="bold", color=INK)

    ax.add_patch(FancyBboxPatch((7.0, 1.4), 2.7, 2.0, boxstyle="round,pad=0.08", fc="#EEF7F5", ec=TEAL, lw=1.6))
    ax.text(8.35, 2.4, "3. EQUITY VALUE\nValor dos Sócios\n= EV − Dívida Bruta\n+ Caixa Disponível", ha="center", va="center", fontsize=7.8, fontweight="bold", color=TEAL)

    ax.annotate("", xy=(3.58, 2.4), xytext=(3.08, 2.4), arrowprops=dict(arrowstyle="->", lw=2.0, color=INDIGO))
    ax.annotate("", xy=(6.92, 2.4), xytext=(6.42, 2.4), arrowprops=dict(arrowstyle="->", lw=2.0, color=TEAL))
    ax.text(5.0, 0.55, "Em startups sem histórico (Dark Side of Valuation): complementa-se com Método de Venture Capital e Opções Reais",
            ha="center", fontsize=7.8, fontweight="bold", color=BURGUNDY)
    save(fig, "fig14_valuation_fcd_vc.pdf")


# FIG 15 — Rubrica e Articulação do Projeto Final (AV3 — 50%) (Cap. 15)
def fig15_projeto_final_av3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.6), gridspec_kw={"width_ratios": [1.1, 1.1]})

    # Painel A: Pizza dos pesos da Rubrica AV3
    labels = ["Leitura Territorial\n(30%)", "Estratégia & Modelo\n(30%)", "Viabilidade & Valuation\n(25%)", "Comunicação & Defesa\n(15%)"]
    sizes = [30, 30, 25, 15]
    cores = [INDIGO, TEAL, AMBER, BURGUNDY]
    ax1.pie(sizes, labels=labels, colors=cores, startangle=90,
            wedgeprops=dict(edgecolor="white", lw=1.6),
            textprops=dict(fontsize=7.8, fontweight="bold"))
    ax1.set_title("Pesos da Rubrica Oficial — AV3 (50% da Nota)", fontsize=9.2, fontweight="bold", color=INDIGO)

    # Painel B: Tripé de integração
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 5.2)
    ax2.axis("off")
    ax2.text(5, 4.85, "Tripé do Projeto Final Integrador (Aula 15)", ha="center", fontsize=9.2, fontweight="bold", color=INDIGO)
    tri = [
        (0.5, 3.25, "UNIDADE I → Diagnóstico Territorial\nSuperar isomorfismo; ler APL, SRI e Hélice", "#F3F6FA", INDIGO),
        (0.5, 1.85, "UNIDADE II → Estratégia & Modelo\nOportunidade, Canvas, PI, fomento regional", "#FCF7EC", AMBER),
        (0.5, 0.45, "UNIDADE III → Viabilidade & Retenção\nLocalização, VPL/TIR, Valuation e valor local", "#EEF7F5", TEAL),
    ]
    for x, y, txt, fc, ec in tri:
        ax2.add_patch(FancyBboxPatch((x, y), 9.0, 1.0, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.4))
        ax2.text(5.0, y + 0.5, txt, ha="center", va="center", fontsize=7.6, fontweight="bold", color=INK)

    plt.tight_layout()
    save(fig, "fig15_projeto_final_av3.pdf")


if __name__ == "__main__":
    fig01_schumpeter_territorio()
    fig02_porter_eficiencia_coletiva()
    fig03_ecossistema_stam()
    fig04_helice_quintupla()
    fig05_teoria_mudanca_espectro()
    fig06_tecnologia_social_igs()
    fig07_vale_da_morte()
    fig08_tam_sam_som()
    fig09_canvas_lean()
    fig10_escada_capital()
    fig11_open_innovation_spinoff()
    fig12_ciclo_projetos_localizacao()
    fig13_perfil_vpl_tir()
    fig14_valuation_fcd_vc()
    fig15_projeto_final_av3()
    print("Todas as 15 figuras vetoriais de Empreendedorismo Territorial foram geradas!")
