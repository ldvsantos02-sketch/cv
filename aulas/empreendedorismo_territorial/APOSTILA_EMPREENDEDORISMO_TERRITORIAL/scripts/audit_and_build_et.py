# -*- coding: utf-8 -*-
"""
Auditoria pedagógica, sintática e compilação dos PDFs (por unidade e apostila completa)
da Apostila de Empreendedorismo Tecnológico e Desenvolvimento Territorial (PPGPT/UEFS).
Salva diretamente na pasta do site indicada pelo usuário.
"""
import os
import re
import sys
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DISCIPLINA = os.path.dirname(ROOT)
SECTIONS = os.path.join(ROOT, "sections")
MOD_PDF_DIR = os.path.join(ROOT, "unidades_pdf")
BUILD_DIR = os.path.join(ROOT, ".build_tex")
os.makedirs(MOD_PDF_DIR, exist_ok=True)
os.makedirs(BUILD_DIR, exist_ok=True)

CHAPTER_FILES = [
    "unid1_cap01.tex", "unid1_cap02.tex", "unid1_cap03.tex", "unid1_cap04.tex", "unid1_cap05.tex", "unid1_cap06.tex",
    "unid2_cap07.tex", "unid2_cap08.tex", "unid2_cap09.tex", "unid2_cap10.tex", "unid2_cap11.tex",
    "unid3_cap12.tex", "unid3_cap13.tex", "unid3_cap14.tex",
    "unid4_cap15.tex",
]

SIMULADO_FILES = [
    "unid1_simulado.tex", "unid2_simulado.tex", "unid3_simulado.tex", "98_avaliacao_geral_final.tex",
]

OTHER_FILES = [
    "00_capa_e_abertura.tex", "01_cronograma_15_encontros.tex", "99_formulario_glossario_referencias.tex",
]

UNITS = [
    ("Unidade_I_Territorio_e_Ecossistemas", "Unidade I — Território e Ecossistemas",
     ["sections/unid1_cap01", "sections/unid1_cap02", "sections/unid1_cap03", "sections/unid1_cap04", "sections/unid1_cap05", "sections/unid1_cap06", "sections/unid1_simulado"]),
    ("Unidade_II_Processo_e_Estrategia", "Unidade II — Processo e Estratégia",
     ["sections/unid2_cap07", "sections/unid2_cap08", "sections/unid2_cap09", "sections/unid2_cap10", "sections/unid2_cap11", "sections/unid2_simulado"]),
    ("Unidade_III_Projetos_e_Viabilidade", "Unidade III — Projetos e Viabilidade",
     ["sections/unid3_cap12", "sections/unid3_cap13", "sections/unid3_cap14", "sections/unid3_simulado"]),
    ("Unidade_IV_Sintese_Territorial", "Unidade IV — Síntese Territorial e Seminário Final",
     ["sections/unid4_cap15"]),
]

FORBIDDEN = [r"\bbasta resolver\b", r"\bobviamente\b", r"\bfazendo as contas\b"]


def audit():
    print("=" * 74)
    print("AUDITORIA PEDAGÓGICA E SINTÁTICA — EMPREENDEDORISMO TERRITORIAL")
    print("=" * 74)
    errors, warnings = [], []
    for fname in OTHER_FILES + CHAPTER_FILES + SIMULADO_FILES:
        fpath = os.path.join(SECTIONS, fname)
        if not os.path.exists(fpath):
            errors.append(f"AUSENTE: {fname}")
            continue
        text = open(fpath, "r", encoding="utf-8").read()
        if r"\documentclass" in text or r"\begin{document}" in text:
            errors.append(f"{fname}: contém \\documentclass ou \\begin{{document}}")
        for pat in FORBIDDEN:
            if re.search(pat, text, flags=re.IGNORECASE):
                warnings.append(f"{fname}: expressão proibida ({pat})")
        for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text):
            fig_abs = os.path.join(ROOT, m.group(1).replace("/", os.sep))
            if not os.path.exists(fig_abs):
                errors.append(f"{fname}: figura ausente -> {m.group(1)}")
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
            print(f"  {fname:20s} | Exemplos: {n_ex:2d} | Erros: {n_err:2d} | MCQs: {n_alt:2d} | {'OK' if not missing else missing}")
            if missing:
                errors.append(f"{fname}: etapas ausentes {missing}")
    print("-" * 74)
    print(f"Erros críticos: {len(errors)} | Avisos: {len(warnings)}")
    for e in errors:
        print("  [ERRO]", e)
    return len(errors) == 0


def run_xelatex(tex_path, jobname, out_pdf_path):
    cmd = [
        "xelatex", "-interaction=nonstopmode", "-halt-on-error",
        f"-output-directory={BUILD_DIR}", f"-jobname={jobname}", tex_path,
    ]
    for pass_num in (1, 2):
        res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res.returncode != 0:
            print(f"[FALHA XeLaTeX] {jobname} (pass {pass_num})")
            log_file = os.path.join(BUILD_DIR, f"{jobname}.log")
            if os.path.exists(log_file):
                lines = open(log_file, "r", encoding="utf-8", errors="replace").readlines()
                for idx, line in enumerate(lines):
                    if line.startswith("!"):
                        print("".join(lines[max(0, idx - 3):min(len(lines), idx + 15)]))
                        break
            return False
    shutil.copy2(os.path.join(BUILD_DIR, f"{jobname}.pdf"), out_pdf_path)
    print(f"[PDF GERADO] {out_pdf_path}")
    return True


def build_all(build_units=True):
    pdf_name = "APOSTILA_EMPREENDEDORISMO_TERRITORIAL_PPGPT_UEFS.pdf"
    final_pdf = os.path.join(ROOT, pdf_name)
    if not run_xelatex(os.path.join(ROOT, "main.tex"), "APOSTILA_EMPREENDEDORISMO_TERRITORIAL_PPGPT_UEFS", final_pdf):
        return False
    site_copy = os.path.join(SITE_DISCIPLINA, pdf_name)
    shutil.copy2(final_pdf, site_copy)
    print(f"[CÓPIA NO SITE] {site_copy}")
    if build_units:
        for slug, title, includes in UNITS:
            wrapper_path = os.path.join(BUILD_DIR, f"{slug}.tex")
            inc_lines = "\n".join([f"\\input{{{inc}}}" for inc in includes])
            wrapper_tex = f"""\\documentclass[11pt, a4paper, oneside]{{book}}
\\usepackage{{styles/apostila_et}}
\\setcounter{{tocdepth}}{{1}}
\\setcounter{{secnumdepth}}{{2}}
\\begin{{document}}
\\tableofcontents
{inc_lines}
\\end{{document}}
"""
            open(wrapper_path, "w", encoding="utf-8").write(wrapper_tex)
            if not run_xelatex(wrapper_path, slug, os.path.join(MOD_PDF_DIR, f"{slug}.pdf")):
                return False
    return True


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode == "audit":
        sys.exit(0 if audit() else 1)
    elif mode == "main":
        sys.exit(0 if (audit() and build_all(False)) else 1)
    else:
        sys.exit(0 if (audit() and build_all(True)) else 1)
