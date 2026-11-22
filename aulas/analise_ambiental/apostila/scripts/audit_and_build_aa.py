# -*- coding: utf-8 -*-
"""
Auditoria pedagógica, sintática e compilação dos PDFs (por módulo e apostila completa)
da Apostila de Análise Ambiental (CHF662 — DCHF/UEFS).
"""
import os
import re
import sys
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_DISCIPLINA = os.path.dirname(ROOT)
SECTIONS = os.path.join(ROOT, "sections")
MOD_PDF_DIR = os.path.join(ROOT, "modulos_pdf")
BUILD_DIR = os.path.join(ROOT, ".build_tex")
os.makedirs(MOD_PDF_DIR, exist_ok=True)
os.makedirs(BUILD_DIR, exist_ok=True)

CHAPTER_FILES = [
    "mod1_cap01.tex", "mod1_cap02.tex", "mod1_cap03.tex", "mod1_cap04.tex",
    "mod2_cap05.tex", "mod2_cap06.tex",
    "mod3_cap07.tex", "mod3_cap08.tex", "mod3_cap09.tex",
    "mod4_cap10.tex", "mod4_cap11.tex", "mod4_cap12.tex",
    "mod5_cap13.tex", "mod5_cap14.tex", "mod5_cap15.tex",
]

SIMULADO_FILES = [
    "mod1_simulado.tex", "mod2_simulado.tex", "mod3_simulado.tex",
    "mod4_simulado.tex", "mod5_simulado.tex", "98_avaliacao_geral_final.tex",
]

OTHER_FILES = [
    "00_capa_e_abertura.tex", "01_cronograma_16_semanas.tex",
    "99_formulario_glossario_referencias.tex",
]

MODULES = [
    ("Modulo_1_Fundamentos_Epistemologicos_e_Conceituais", "Módulo 1 — Fundamentos Epistemológicos e Conceituais",
     ["sections/mod1_cap01", "sections/mod1_cap02", "sections/mod1_cap03", "sections/mod1_cap04", "sections/mod1_simulado"]),
    ("Modulo_2_AIA_e_Analise_Ambiental_Integrada", "Módulo 2 — AIA e Análise Ambiental Integrada",
     ["sections/mod2_cap05", "sections/mod2_cap06", "sections/mod2_simulado"]),
    ("Modulo_3_Bacias_Morfopedologia_Geossistemas_Fragilidade", "Módulo 3 — Bacias, Morfopedologia, Geossistemas e Fragilidade",
     ["sections/mod3_cap07", "sections/mod3_cap08", "sections/mod3_cap09", "sections/mod3_simulado"]),
    ("Modulo_4_Indicadores_Qualidade_Solo_e_Degradacao", "Módulo 4 — Indicadores, Qualidade do Solo e Degradação",
     ["sections/mod4_cap10", "sections/mod4_cap11", "sections/mod4_cap12", "sections/mod4_simulado"]),
    ("Modulo_5_Bioengenharia_Legislacao_PRAD_e_Diagnostico", "Módulo 5 — Bioengenharia, Legislação, PRAD e Diagnóstico Final",
     ["sections/mod5_cap13", "sections/mod5_cap14", "sections/mod5_cap15", "sections/mod5_simulado"]),
]

FORBIDDEN = [
    r"\bbasta resolver\b",
    r"\bobviamente\b",
    r"\bfazendo as contas\b",
]


def audit():
    print("=" * 74)
    print("AUDITORIA PEDAGÓGICA E SINTÁTICA — CHF662 ANÁLISE AMBIENTAL")
    print("=" * 74)
    errors = []
    warnings = []
    all_files = OTHER_FILES + CHAPTER_FILES + SIMULADO_FILES

    for fname in all_files:
        fpath = os.path.join(SECTIONS, fname)
        if not os.path.exists(fpath):
            errors.append(f"AUSENTE: {fname}")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        if r"\documentclass" in text or r"\begin{document}" in text:
            errors.append(f"{fname}: contém \\documentclass ou \\begin{{document}}")

        for pat in FORBIDDEN:
            if re.search(pat, text, flags=re.IGNORECASE):
                warnings.append(f"{fname}: expressão proibida ({pat})")

        for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text):
            fig_rel = m.group(1)
            fig_abs = os.path.join(ROOT, fig_rel.replace("/", os.sep))
            if not os.path.exists(fig_abs):
                errors.append(f"{fname}: figura ausente -> {fig_rel}")

        begins = re.findall(r"\\begin\{([^}]+)\}", text)
        ends = re.findall(r"\\end\{([^}]+)\}", text)
        if len(begins) != len(ends):
            errors.append(f"{fname}: desbalanceamento begin({len(begins)}) vs end({len(ends)})")

        if fname in CHAPTER_FILES:
            checks = [
                ("capObjetivos", r"\\begin\{capObjetivos\}"),
                ("capRevisao", r"\\begin\{capRevisao\}"),
                ("Etapa 3", r"\\etapa\{3\}"),
                ("Etapa 4", r"\\etapa\{4\}"),
                ("Etapa 5", r"\\etapa\{5\}"),
                ("Etapa 6", r"\\etapa\{6\}"),
                ("Etapa 7", r"\\etapa\{7\}"),
                ("Etapa 8", r"\\etapa\{8\}"),
                ("boxResumo", r"\\begin\{boxResumo\}"),
                ("boxTeste", r"\\begin\{boxTeste\}"),
            ]
            missing = [lbl for lbl, rx in checks if not re.search(rx, text)]
            n_ex = len(re.findall(r"\\begin\{boxExemplo\}", text))
            n_err = len(re.findall(r"\\begin\{boxErro\}", text))
            n_alt = len(re.findall(r"\\begin\{alternativas\}", text))
            status = "OK" if not missing else f"FALTANDO: {missing}"
            print(f"  {fname:20s} | Exemplos: {n_ex:2d} | Erros: {n_err:2d} | MCQs: {n_alt:2d} | {status}")
            if missing:
                errors.append(f"{fname}: etapas ausentes {missing}")
            if n_ex < 5:
                warnings.append(f"{fname}: apenas {n_ex} exemplos (mínimo 5)")
            if n_err < 3:
                warnings.append(f"{fname}: apenas {n_err} quadros de erros (mínimo 3)")

    print("-" * 74)
    print(f"Erros críticos: {len(errors)} | Avisos: {len(warnings)}")
    for e in errors:
        print("  [ERRO]", e)
    for w in warnings:
        print("  [AVISO]", w)
    return len(errors) == 0


def run_xelatex(tex_path, jobname, out_pdf_path):
    cmd = [
        "xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={BUILD_DIR}",
        f"-jobname={jobname}",
        tex_path,
    ]
    for pass_num in (1, 2):
        res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res.returncode != 0:
            print(f"[FALHA XeLaTeX] {jobname} (pass {pass_num})")
            log_file = os.path.join(BUILD_DIR, f"{jobname}.log")
            if os.path.exists(log_file):
                with open(log_file, "r", encoding="utf-8", errors="replace") as f:
                    lines = f.readlines()
                for idx, line in enumerate(lines):
                    if line.startswith("!"):
                        print("".join(lines[max(0, idx - 3):min(len(lines), idx + 15)]))
                        break
            else:
                print(res.stdout[-2000:])
            return False
    built_pdf = os.path.join(BUILD_DIR, f"{jobname}.pdf")
    shutil.copy2(built_pdf, out_pdf_path)
    print(f"[PDF GERADO] {out_pdf_path}")
    return True


def build_all(build_modules=True):
    ok = True
    pdf_name = "APOSTILA_ANALISE_AMBIENTAL_CHF662_UEFS.pdf"
    final_pdf = os.path.join(ROOT, pdf_name)
    print("\nCompilando APOSTILA COMPLETA CHF662 (2 passadas XeLaTeX)...")
    if not run_xelatex(os.path.join(ROOT, "main.tex"), "APOSTILA_ANALISE_AMBIENTAL_CHF662_UEFS", final_pdf):
        return False
    # Copiar também na raiz da pasta oficial da disciplina (10 - ANALISE AMBIENTAL)
    parent_copy = os.path.join(PARENT_DISCIPLINA, pdf_name)
    shutil.copy2(final_pdf, parent_copy)
    print(f"[CÓPIA NA PASTA DA DISCIPLINA] {parent_copy}")

    if build_modules:
        print("\nCompilando PDFs individuais por módulo...")
        for slug, title, includes in MODULES:
            wrapper_path = os.path.join(BUILD_DIR, f"{slug}.tex")
            inc_lines = "\n".join([f"\\input{{{inc}}}" for inc in includes])
            wrapper_tex = f"""\\documentclass[11pt, a4paper, oneside]{{book}}
\\usepackage{{styles/apostila_aa}}
\\setcounter{{tocdepth}}{{1}}
\\setcounter{{secnumdepth}}{{2}}
\\begin{{document}}
\\tableofcontents
{inc_lines}
\\end{{document}}
"""
            with open(wrapper_path, "w", encoding="utf-8") as f:
                f.write(wrapper_tex)
            out_mod = os.path.join(MOD_PDF_DIR, f"{slug}.pdf")
            if not run_xelatex(wrapper_path, slug, out_mod):
                ok = False
    return ok


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode == "audit":
        sys.exit(0 if audit() else 1)
    elif mode == "main":
        if not audit():
            sys.exit(1)
        sys.exit(0 if build_all(build_modules=False) else 1)
    else:
        if not audit():
            sys.exit(1)
        sys.exit(0 if build_all(build_modules=True) else 1)
