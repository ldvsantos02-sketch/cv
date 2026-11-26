// Keep the published HTML punctuation and the PDF download consistent.
const base = new URL("./", import.meta.url);
const output = new URL("./_book/", base);
const pdfName = "APOSTILA_ANALISE_AMBIENTAL_CHF662_UEFS.pdf";

async function normalize(directory: URL) {
  for await (const entry of Deno.readDir(directory)) {
    const file = new URL(entry.name + (entry.isDirectory ? "/" : ""), directory);
    if (entry.isDirectory && entry.name === "capitulos") {
      await normalize(file);
    } else if (entry.isFile && /\.(html|json|xml)$/.test(entry.name)) {
      const before = await Deno.readTextFile(file);
      let after = before.replace(/[\u2012-\u2015]/g, "-");
      if (entry.name === "index.html") {
        after = after.replace(
          /<h1([^>]*)>Apresentação e orientação de estudo<\/h1>/,
          "<h2$1>Apresentação e orientação de estudo</h2>",
        );
      }
      if (entry.name.endsWith(".html") && !after.includes('data-book-tables="true"')) {
        let number = 0;
        after = after.replace(/<table\b[\s\S]*?<\/table>/g, (table) =>
          `<div class="book-table-scroll" role="region" aria-label="Tabela ${++number}" tabindex="0">${table}</div>`);
        after = after.replace(/<main\b/, '<main data-book-tables="true"');
      }
      if (after !== before) await Deno.writeTextFile(file, after);
    }
  }
}

await normalize(output);

const canonical = new URL("../../aulas/analise_ambiental/apostila/" + pdfName, base);
const download = new URL(pdfName, output);
try {
  await Deno.stat(download);
} catch (error) {
  if (!(error instanceof Deno.errors.NotFound)) throw error;
  await Deno.copyFile(canonical, download);
}
