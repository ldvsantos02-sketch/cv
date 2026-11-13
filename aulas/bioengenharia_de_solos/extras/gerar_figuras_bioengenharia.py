"""Figuras da auditoria de Bioengenharia. PNG 300 dpi e SVG em img/.
Curvas sintéticas: não representam calibração de solos nem de espécies.
Dependências: numpy e matplotlib. Caminhos relativos ao próprio script.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np

OUT = Path(__file__).resolve().parents[3] / "img"
OUT.mkdir(parents=True, exist_ok=True)
NAVY, GREEN, GOLD, GREY = "#193c60", "#347454", "#b59042", "#526477"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
    "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none",
    "axes.labelcolor": NAVY, "text.color": NAVY, "axes.titleweight": "bold"})

def canvas(title):
    f, ax = plt.subplots(1, 2, figsize=(13, 5.7))
    f.subplots_adjust(left=.07, right=.97, top=.83, bottom=.22, wspace=.25)
    f.suptitle(title, fontsize=18, weight="bold")
    return f, ax

def save(f, name, note):
    f.text(.5, .04, note, ha="center", fontsize=10, color=GREY)
    for ext in ("png", "svg"):
        f.savefig(OUT / f"{name}.{ext}", dpi=300, facecolor="white")
    plt.close(f)
    print(name)

def boxes(ax, rows):
    ax.axis("off")
    ax.set(xlim=(0, 10), ylim=(0, 10))
    for i, (title, desc) in enumerate(rows):
        y = 9-i*(9/len(rows))
        h = 8/len(rows)
        ax.add_patch(Rectangle((0, y-h), 10, h, facecolor="#f1f5f8", edgecolor=NAVY))
        ax.text(.3, y-.45, title, fontsize=12, weight="bold", va="top")
        ax.text(.3, y-h+.3, desc, fontsize=10, va="bottom")

def profile():
    f, (a, b) = canvas("Perfil de alteração e contraste hidráulico")
    a.axis("off")
    a.set(xlim=(0, 10), ylim=(0, 10))
    rows = [(7.5, 10, "#5c4434", "Solum superficial", "Raízes, estrutura e aporte de água"),
            (5.5, 7.5, "#aa642e", "Camada contrastante", "Condutividade a verificar por ensaio"),
            (2.5, 5.5, "#d39861", "Saprolito", "Fraturas e estruturas herdadas"),
            (0, 2.5, "#78818b", "Rocha", "Circulação nas descontinuidades")]
    for lo, hi, color, title, desc in rows:
        a.add_patch(Rectangle((0, lo), 4, hi-lo, facecolor=color, edgecolor="white", lw=2))
        a.text(2, (lo+hi)/2, title.replace(" ", "\n", 1), color="white", ha="center", va="center", weight="bold")
        a.text(4.3, (lo+hi)/2, desc.replace(" e ", "\ne ", 1), fontsize=10, va="center")
    for x in (1, 2, 3):
        a.annotate("", xy=(x, 7.6), xytext=(x, 9.8),
                   arrowprops=dict(arrowstyle="->", color="#b6d9ef", lw=2))
    boxes(b, [("1 · Investigar o aporte", "Chuva e água de montante"),
              ("2 · Comparar as camadas", "Estrutura, condutividade e fraturas"),
              ("3 · Medir a resposta", "Saturação e poropressão, se presentes"),
              ("4 · Avaliar o mecanismo", "Erosão interna ou instabilidade")])
    save(f, "bs_perfil_intemperismo_ruptura",
         "Esquema sem escala. Contatos entre camadas não implicam automaticamente impermeabilidade ou ruptura.")

def roots():
    f, (a, b) = canvas("Resistência do solo e contribuição radicular")
    x = np.linspace(0, 80, 100)
    t = 5+x*np.tan(np.deg2rad(30))
    a.plot(x, t, color=GREY, lw=2, label="Sem contribuição radicular")
    a.plot(x, t+10, color=GREEN, lw=2.5, label="Com Δcᵣ = 10 kPa (ilustrativo)")
    a.fill_between(x, t, t+10, alpha=.12, color=GREEN)
    a.set(xlabel="Tensão normal efetiva σ′ (kPa)", ylabel="Resistência τf (kPa)",
          title="A · Mesmo atrito, intercepto adicional")
    a.legend(fontsize=9, loc="lower right")
    a.grid(alpha=.2)
    d = np.linspace(.5, 6, 100)
    sigma = 20*d**(-.5)
    b.plot(d, sigma, lw=2.5, color=NAVY, label="Tensão de ruptura σᵣ")
    twin = b.twinx()
    twin.spines["right"].set_visible(True)
    twin.plot(d, sigma*np.pi*d*d/4, color=GOLD, ls="--", lw=2.5, label="Força de ruptura F")
    b.set(xlabel="Diâmetro d (mm)", ylabel="Tensão σᵣ (MPa)",
          title="B · Tensão não é força")
    twin.set_ylabel("Força F (N)", color=GOLD)
    b.text(2.7, 24, "σᵣ = 20 d⁻⁰·⁵\nF = σᵣ πd²/4", fontsize=12)
    b.legend(loc="lower left", fontsize=9)
    twin.legend(loc="upper right", fontsize=9)
    b.grid(alpha=.2)
    save(f, "bs_mohr_coulomb_coesao_radicular",
         "Parâmetros didáticos: c′ = 5 kPa; φ′ = 30°. Curva radicular fictícia, sem representar uma espécie.")

def compaction():
    f, (a, b) = canvas("Compactação: critérios diferentes conforme a função")
    w = np.linspace(9, 27, 100)
    a.plot(w, 1.70-.0025*(w-18)**2, color=NAVY, lw=3)
    a.plot(18, 1.70, "o", color=GOLD, ms=9)
    a.annotate("wót = 18%\nDs,máx = 1,70 g cm⁻³", xy=(18, 1.70), xytext=(10, 1.74),
               arrowprops=dict(arrowstyle="->", color=GOLD))
    a.set(xlabel="Teor de água gravimétrico (%)", ylabel="Densidade seca (g cm⁻³)",
          title="A · Exemplo de curva de Proctor", ylim=(1.45, 1.83))
    a.grid(alpha=.2)
    boxes(b, [("Zona estrutural", "Energia, curva de Proctor e GC especificados.\nControle de densidade e umidade."),
              ("Zona de enraizamento", "RP com umidade registrada; porosidade,\ninfiltração e distribuição das raízes."),
              ("Consistência: LL, LP e IP", "IP = LL − LP. Umidade ótima do Proctor\nnão é necessariamente umidade plástica.")])
    save(f, "bs_indicadores_fisicos_compactacao",
         "Curva sintética. Limiares de densidade e RP dependem do solo e das plantas; GC depende da função e da especificação.")

def terraces():
    f, (a, b) = canvas("Terraços: seção, espaçamento e destino da água")
    for ax in (a, b):
        ax.axis("off")
        ax.set(xlim=(0, 10), ylim=(0, 7))
    a.plot([0, 3, 4.4, 5.3, 6.3, 7.5, 10], [4, 4, 2.8, 2.8, 4.8, 4, 4], color="#906142", lw=4)
    a.add_patch(Polygon([[3.35, 3.7], [4.4, 2.8], [5.3, 2.8], [5.8, 3.7]],
                        facecolor="#b9d7e9"))
    a.text(3, 2, "Canal", fontsize=13)
    a.text(6.2, 5.4, "Camalhão", fontsize=13)
    a.text(.2, 6.5, "Seção conceitual, sem escala", weight="bold")
    a.text(.2, .4, "Em nível: armazenar e infiltrar, se adequado.\nEm gradiente: conduzir à saída protegida.", fontsize=11)
    b.plot([.5, 8.7], [6, 1.1], color="#906142", lw=4)
    b.plot([1, 7, 7], [5.7, 5.7, 2.1], color=GREY, ls="--")
    b.annotate("", xy=(7, 6.2), xytext=(1, 6.2), arrowprops=dict(arrowstyle="<->", color=NAVY))
    b.text(4, 6.4, "EH (m)", ha="center")
    b.annotate("", xy=(7.5, 2.1), xytext=(7.5, 5.7), arrowprops=dict(arrowstyle="<->", color=GOLD))
    b.text(7.8, 3.9, "EV (m)")
    b.text(.5, 1.3, "D (%) = 100 EV / EH", fontsize=16, weight="bold")
    b.text(.5, .4, "EV = 1 m e D = 8% → EH = 12,5 m", fontsize=11)
    save(f, "bs_terraceamento_secoes_espacamento",
         "O EV exige critério regional e verificação hidráulica. A relação geométrica não determina, sozinha, o espaçamento admissível.")

def channel():
    f, (a, b) = canvas("Canal trapezoidal: geometria e verificação")
    a.axis("off")
    a.set(xlim=(-.5, 9), ylim=(-.5, 5))
    a.plot([0, 2, 6, 8], [4, 1, 1, 4], lw=4, color="#906142")
    a.add_patch(Polygon([[.67, 3], [2, 1], [6, 1], [7.33, 3]], facecolor="#b9d7e9"))
    a.plot([.67, 7.33], [3, 3], color=NAVY)
    a.annotate("", xy=(6, .5), xytext=(2, .5), arrowprops=dict(arrowstyle="<->"))
    a.text(4, 0, "b · base", ha="center")
    a.annotate("", xy=(4, 1), xytext=(4, 3), arrowprops=dict(arrowstyle="<->"))
    a.text(4.2, 2, "y")
    a.annotate("", xy=(7.33, 3.3), xytext=(.67, 3.3), arrowprops=dict(arrowstyle="<->"))
    a.text(4, 3.6, "T = b + 2zy", ha="center")
    a.text(6.7, 1.4, "z H : 1 V", fontsize=10)
    a.text(6.3, 4.4, "Borda livre", color=GOLD)
    boxes(b, [("Geometria", "Ah = (b + zy)y\nPm = b + 2y√(1 + z²)     Rh = Ah/Pm"),
              ("Capacidade", "V = Rh²ᐟ³ Sf¹ᐟ² / n     Q = AhV\nResolver y para a vazão de projeto."),
              ("Estabilidade", "τ₀ = ρgRhSf     V ≤ Vadm     τ₀ ≤ τadm\nConferir fase inicial, curvas e saída.")])
    save(f, "bs_canal_escoadouro_trapezoidal_manning",
         "Geometria sem escala. Comprimentos em m; área em m²; Q em m³/s; V em m/s; Sf em m/m e tensão em Pa.")

if __name__ == "__main__":
    for draw in (profile, roots, compaction, terraces, channel):
        draw()
