-- Template acadêmico UEFS: um único QMD gera RevealJS (HTML) e Beamer (PDF).
-- Derivado do modelo da qualificação (PLANTERR), generalizado para aulas.
--
-- Metadados lidos do YAML (todos opcionais):
--   academico:
--     cabecalho: [linha em negrito, linha 2, linha 3]   # capa
--     rodape: "UEFS · Disciplina"                       # rodapé de cada slide
--     local: "Feira de Santana – Bahia"                 # linha final da capa
--     segunda-linha: "Orientador: ..."                  # linha abaixo do autor
--
-- Seções (#) aceitam o atributo rotulo="..." com o nome curto exibido na régua.

local is_beamer = FORMAT:match("beamer") ~= nil
local is_reveal = FORMAT:match("revealjs") ~= nil

local encoding_repairs = {
  {"â", "‐"},
  {"â€", "‐"},
  {"â", "‑"},
  {"â€‘", "‑"},
  {"â", "‒"},
  {"â€’", "‒"},
  {"â", "–"},
  {"â€“", "–"},
  {"â", "—"},
  {"â€”", "—"},
  {"â", "―"},
  {"â€•", "―"},
  {"â", "‖"},
  {"â€–", "‖"},
  {"â", "‗"},
  {"â€—", "‗"},
  {"â", "‘"},
  {"â€˜", "‘"},
  {"â", "’"},
  {"â€™", "’"},
  {"â", "‚"},
  {"â€š", "‚"},
  {"â", "‛"},
  {"â€›", "‛"},
  {"â", "“"},
  {"â€œ", "“"},
  {"â", "”"},
  {"â€", "”"},
  {"â", "„"},
  {"â€ž", "„"},
  {"â", "‟"},
  {"â€Ÿ", "‟"},
  {"â ", "†"},
  {"â€ ", "†"},
  {"â¡", "‡"},
  {"â€¡", "‡"},
  {"â¢", "•"},
  {"â€¢", "•"},
  {"â£", "‣"},
  {"â€£", "‣"},
  {"â¤", "․"},
  {"â€¤", "․"},
  {"â¥", "‥"},
  {"â€¥", "‥"},
  {"â¦", "…"},
  {"â€¦", "…"},
  {"â§", "‧"},
  {"â€§", "‧"},
  {"â¨", " "},
  {"â€¨", " "},
  {"â©", " "},
  {"â€©", " "},
  {"âª", "‪"},
  {"â€ª", "‪"},
  {"â«", "‫"},
  {"â€«", "‫"},
  {"â¬", "‬"},
  {"â€¬", "‬"},
  {"â­", "‭"},
  {"â€­", "‭"},
  {"â®", "‮"},
  {"â€®", "‮"},
  {"â¯", " "},
  {"â€¯", " "},
  {"â°", "‰"},
  {"â€°", "‰"},
  {"â±", "‱"},
  {"â€±", "‱"},
  {"â²", "′"},
  {"â€²", "′"},
  {"â³", "″"},
  {"â€³", "″"},
  {"â´", "‴"},
  {"â€´", "‴"},
  {"âµ", "‵"},
  {"â€µ", "‵"},
  {"â¶", "‶"},
  {"â€¶", "‶"},
  {"â·", "‷"},
  {"â€·", "‷"},
  {"â¸", "‸"},
  {"â€¸", "‸"},
  {"â¹", "‹"},
  {"â€¹", "‹"},
  {"âº", "›"},
  {"â€º", "›"},
  {"â", "←"},
  {"â†", "←"},
  {"â", "↑"},
  {"â†‘", "↑"},
  {"â", "→"},
  {"â†’", "→"},
  {"â", "↓"},
  {"â†“", "↓"},
  {"â", "↔"},
  {"â†”", "↔"},
  {"â ", "≠"},
  {"â‰ ", "≠"},
  {"â¡", "≡"},
  {"â‰¡", "≡"},
  {"â¢", "≢"},
  {"â‰¢", "≢"},
  {"â£", "≣"},
  {"â‰£", "≣"},
  {"â¤", "≤"},
  {"â‰¤", "≤"},
  {"â¥", "≥"},
  {"â‰¥", "≥"},
  {"â¬", "€"},
  {"â‚¬", "€"},
  {"â", "−"},
  {"âˆ’", "−"},
  {"â", "∞"},
  {"âˆž", "∞"},
  {"Â ", " "},
  {"Â¡", "¡"},
  {"Â¢", "¢"},
  {"Â£", "£"},
  {"Â¤", "¤"},
  {"Â¥", "¥"},
  {"Â¦", "¦"},
  {"Â§", "§"},
  {"Â¨", "¨"},
  {"Â©", "©"},
  {"Âª", "ª"},
  {"Â«", "«"},
  {"Â¬", "¬"},
  {"Â­", "­"},
  {"Â®", "®"},
  {"Â¯", "¯"},
  {"Â°", "°"},
  {"Â±", "±"},
  {"Â²", "²"},
  {"Â³", "³"},
  {"Â´", "´"},
  {"Âµ", "µ"},
  {"Â¶", "¶"},
  {"Â·", "·"},
  {"Â¸", "¸"},
  {"Â¹", "¹"},
  {"Âº", "º"},
  {"Â»", "»"},
  {"Â¼", "¼"},
  {"Â½", "½"},
  {"Â¾", "¾"},
  {"Â¿", "¿"},
  {"Ã", "À"},
  {"Ã€", "À"},
  {"Ã", "Á"},
  {"Ã", "Â"},
  {"Ã‚", "Â"},
  {"Ã", "Ã"},
  {"Ãƒ", "Ã"},
  {"Ã", "Ä"},
  {"Ã„", "Ä"},
  {"Ã", "Å"},
  {"Ã…", "Å"},
  {"Ã", "Æ"},
  {"Ã†", "Æ"},
  {"Ã", "Ç"},
  {"Ã‡", "Ç"},
  {"Ã", "È"},
  {"Ãˆ", "È"},
  {"Ã", "É"},
  {"Ã‰", "É"},
  {"Ã", "Ê"},
  {"ÃŠ", "Ê"},
  {"Ã", "Ë"},
  {"Ã‹", "Ë"},
  {"Ã", "Ì"},
  {"ÃŒ", "Ì"},
  {"Ã", "Í"},
  {"Ã", "Î"},
  {"ÃŽ", "Î"},
  {"Ã", "Ï"},
  {"Ã", "Ð"},
  {"Ã", "Ñ"},
  {"Ã‘", "Ñ"},
  {"Ã", "Ò"},
  {"Ã’", "Ò"},
  {"Ã", "Ó"},
  {"Ã“", "Ó"},
  {"Ã", "Ô"},
  {"Ã”", "Ô"},
  {"Ã", "Õ"},
  {"Ã•", "Õ"},
  {"Ã", "Ö"},
  {"Ã–", "Ö"},
  {"Ã", "×"},
  {"Ã—", "×"},
  {"Ã", "Ø"},
  {"Ã˜", "Ø"},
  {"Ã", "Ù"},
  {"Ã™", "Ù"},
  {"Ã", "Ú"},
  {"Ãš", "Ú"},
  {"Ã", "Û"},
  {"Ã›", "Û"},
  {"Ã", "Ü"},
  {"Ãœ", "Ü"},
  {"Ã", "Ý"},
  {"Ã", "Þ"},
  {"Ãž", "Þ"},
  {"Ã", "ß"},
  {"ÃŸ", "ß"},
  {"Ã ", "à"},
  {"Ã¡", "á"},
  {"Ã¢", "â"},
  {"Ã£", "ã"},
  {"Ã¤", "ä"},
  {"Ã¥", "å"},
  {"Ã¦", "æ"},
  {"Ã§", "ç"},
  {"Ã¨", "è"},
  {"Ã©", "é"},
  {"Ãª", "ê"},
  {"Ã«", "ë"},
  {"Ã¬", "ì"},
  {"Ã­", "í"},
  {"Ã®", "î"},
  {"Ã¯", "ï"},
  {"Ã°", "ð"},
  {"Ã±", "ñ"},
  {"Ã²", "ò"},
  {"Ã³", "ó"},
  {"Ã´", "ô"},
  {"Ãµ", "õ"},
  {"Ã¶", "ö"},
  {"Ã·", "÷"},
  {"Ã¸", "ø"},
  {"Ã¹", "ù"},
  {"Ãº", "ú"},
  {"Ã»", "û"},
  {"Ã¼", "ü"},
  {"Ã½", "ý"},
  {"Ã¾", "þ"},
  {"Ã¿", "ÿ"},
  {"Ä", "Ā"},
  {"Ä€", "Ā"},
  {"Ä", "ā"},
  {"Ä", "Ă"},
  {"Ä‚", "Ă"},
  {"Ä", "ă"},
  {"Äƒ", "ă"},
  {"Ä", "Ą"},
  {"Ä„", "Ą"},
  {"Ä", "ą"},
  {"Ä…", "ą"},
  {"Ä", "Ć"},
  {"Ä†", "Ć"},
  {"Ä", "ć"},
  {"Ä‡", "ć"},
  {"Ä", "Ĉ"},
  {"Äˆ", "Ĉ"},
  {"Ä", "ĉ"},
  {"Ä‰", "ĉ"},
  {"Ä", "Ċ"},
  {"ÄŠ", "Ċ"},
  {"Ä", "ċ"},
  {"Ä‹", "ċ"},
  {"Ä", "Č"},
  {"ÄŒ", "Č"},
  {"Ä", "č"},
  {"Ä", "Ď"},
  {"ÄŽ", "Ď"},
  {"Ä", "ď"},
  {"Ä", "Đ"},
  {"Ä", "đ"},
  {"Ä‘", "đ"},
  {"Ä", "Ē"},
  {"Ä’", "Ē"},
  {"Ä", "ē"},
  {"Ä“", "ē"},
  {"Ä", "Ĕ"},
  {"Ä”", "Ĕ"},
  {"Ä", "ĕ"},
  {"Ä•", "ĕ"},
  {"Ä", "Ė"},
  {"Ä–", "Ė"},
  {"Ä", "ė"},
  {"Ä—", "ė"},
  {"Ä", "Ę"},
  {"Ä˜", "Ę"},
  {"Ä", "ę"},
  {"Ä™", "ę"},
  {"Ä", "Ě"},
  {"Äš", "Ě"},
  {"Ä", "ě"},
  {"Ä›", "ě"},
  {"Ä", "Ĝ"},
  {"Äœ", "Ĝ"},
  {"Ä", "ĝ"},
  {"Ä", "Ğ"},
  {"Äž", "Ğ"},
  {"Ä", "ğ"},
  {"ÄŸ", "ğ"},
  {"Ä ", "Ġ"},
  {"Ä¡", "ġ"},
  {"Ä¢", "Ģ"},
  {"Ä£", "ģ"},
  {"Ä¤", "Ĥ"},
  {"Ä¥", "ĥ"},
  {"Ä¦", "Ħ"},
  {"Ä§", "ħ"},
  {"Ä¨", "Ĩ"},
  {"Ä©", "ĩ"},
  {"Äª", "Ī"},
  {"Ä«", "ī"},
  {"Ä¬", "Ĭ"},
  {"Ä­", "ĭ"},
  {"Ä®", "Į"},
  {"Ä¯", "į"},
  {"Ä°", "İ"},
  {"Ä±", "ı"},
  {"Ä²", "Ĳ"},
  {"Ä³", "ĳ"},
  {"Ä´", "Ĵ"},
  {"Äµ", "ĵ"},
  {"Ä¶", "Ķ"},
  {"Ä·", "ķ"},
  {"Ä¸", "ĸ"},
  {"Ä¹", "Ĺ"},
  {"Äº", "ĺ"},
  {"Ä»", "Ļ"},
  {"Ä¼", "ļ"},
  {"Ä½", "Ľ"},
  {"Ä¾", "ľ"},
  {"Ä¿", "Ŀ"},
  {"Å", "ŀ"},
  {"Å€", "ŀ"},
  {"Å", "Ł"},
  {"Å", "ł"},
  {"Å‚", "ł"},
  {"Å", "Ń"},
  {"Åƒ", "Ń"},
  {"Å", "ń"},
  {"Å„", "ń"},
  {"Å", "Ņ"},
  {"Å…", "Ņ"},
  {"Å", "ņ"},
  {"Å†", "ņ"},
  {"Å", "Ň"},
  {"Å‡", "Ň"},
  {"Å", "ň"},
  {"Åˆ", "ň"},
  {"Å", "ŉ"},
  {"Å‰", "ŉ"},
  {"Å", "Ŋ"},
  {"ÅŠ", "Ŋ"},
  {"Å", "ŋ"},
  {"Å‹", "ŋ"},
  {"Å", "Ō"},
  {"ÅŒ", "Ō"},
  {"Å", "ō"},
  {"Å", "Ŏ"},
  {"ÅŽ", "Ŏ"},
  {"Å", "ŏ"},
  {"Å", "Ő"},
  {"Å", "ő"},
  {"Å‘", "ő"},
  {"Å", "Œ"},
  {"Å’", "Œ"},
  {"Å", "œ"},
  {"Å“", "œ"},
  {"Å", "Ŕ"},
  {"Å”", "Ŕ"},
  {"Å", "ŕ"},
  {"Å•", "ŕ"},
  {"Å", "Ŗ"},
  {"Å–", "Ŗ"},
  {"Å", "ŗ"},
  {"Å—", "ŗ"},
  {"Å", "Ř"},
  {"Å˜", "Ř"},
  {"Å", "ř"},
  {"Å™", "ř"},
  {"Å", "Ś"},
  {"Åš", "Ś"},
  {"Å", "ś"},
  {"Å›", "ś"},
  {"Å", "Ŝ"},
  {"Åœ", "Ŝ"},
  {"Å", "ŝ"},
  {"Å", "Ş"},
  {"Åž", "Ş"},
  {"Å", "ş"},
  {"ÅŸ", "ş"},
  {"Å ", "Š"},
  {"Å¡", "š"},
  {"Å¢", "Ţ"},
  {"Å£", "ţ"},
  {"Å¤", "Ť"},
  {"Å¥", "ť"},
  {"Å¦", "Ŧ"},
  {"Å§", "ŧ"},
  {"Å¨", "Ũ"},
  {"Å©", "ũ"},
  {"Åª", "Ū"},
  {"Å«", "ū"},
  {"Å¬", "Ŭ"},
  {"Å­", "ŭ"},
  {"Å®", "Ů"},
  {"Å¯", "ů"},
  {"Å°", "Ű"},
  {"Å±", "ű"},
  {"Å²", "Ų"},
  {"Å³", "ų"},
  {"Å´", "Ŵ"},
  {"Åµ", "ŵ"},
  {"Å¶", "Ŷ"},
  {"Å·", "ŷ"},
  {"Å¸", "Ÿ"},
  {"Å¹", "Ź"},
  {"Åº", "ź"},
  {"Å»", "Ż"},
  {"Å¼", "ż"},
  {"Å½", "Ž"},
  {"Å¾", "ž"},
  {"Å¿", "ſ"},
  {"Æ", "ƀ"},
  {"Æ€", "ƀ"},
  {"Æ", "Ɓ"},
  {"Æ", "Ƃ"},
  {"Æ‚", "Ƃ"},
  {"Æ", "ƃ"},
  {"Æƒ", "ƃ"},
  {"Æ", "Ƅ"},
  {"Æ„", "Ƅ"},
  {"Æ", "ƅ"},
  {"Æ…", "ƅ"},
  {"Æ", "Ɔ"},
  {"Æ†", "Ɔ"},
  {"Æ", "Ƈ"},
  {"Æ‡", "Ƈ"},
  {"Æ", "ƈ"},
  {"Æˆ", "ƈ"},
  {"Æ", "Ɖ"},
  {"Æ‰", "Ɖ"},
  {"Æ", "Ɗ"},
  {"ÆŠ", "Ɗ"},
  {"Æ", "Ƌ"},
  {"Æ‹", "Ƌ"},
  {"Æ", "ƌ"},
  {"ÆŒ", "ƌ"},
  {"Æ", "ƍ"},
  {"Æ", "Ǝ"},
  {"ÆŽ", "Ǝ"},
  {"Æ", "Ə"},
  {"Æ", "Ɛ"},
  {"Æ", "Ƒ"},
  {"Æ‘", "Ƒ"},
  {"Æ", "ƒ"},
  {"Æ’", "ƒ"},
  {"Æ", "Ɠ"},
  {"Æ“", "Ɠ"},
  {"Æ", "Ɣ"},
  {"Æ”", "Ɣ"},
  {"Æ", "ƕ"},
  {"Æ•", "ƕ"},
  {"Æ", "Ɩ"},
  {"Æ–", "Ɩ"},
  {"Æ", "Ɨ"},
  {"Æ—", "Ɨ"},
  {"Æ", "Ƙ"},
  {"Æ˜", "Ƙ"},
  {"Æ", "ƙ"},
  {"Æ™", "ƙ"},
  {"Æ", "ƚ"},
  {"Æš", "ƚ"},
  {"Æ", "ƛ"},
  {"Æ›", "ƛ"},
  {"Æ", "Ɯ"},
  {"Æœ", "Ɯ"},
  {"Æ", "Ɲ"},
  {"Æ", "ƞ"},
  {"Æž", "ƞ"},
  {"Æ", "Ɵ"},
  {"ÆŸ", "Ɵ"},
  {"Æ ", "Ơ"},
  {"Æ¡", "ơ"},
  {"Æ¢", "Ƣ"},
  {"Æ£", "ƣ"},
  {"Æ¤", "Ƥ"},
  {"Æ¥", "ƥ"},
  {"Æ¦", "Ʀ"},
  {"Æ§", "Ƨ"},
  {"Æ¨", "ƨ"},
  {"Æ©", "Ʃ"},
  {"Æª", "ƪ"},
  {"Æ«", "ƫ"},
  {"Æ¬", "Ƭ"},
  {"Æ­", "ƭ"},
  {"Æ®", "Ʈ"},
  {"Æ¯", "Ư"},
  {"Æ°", "ư"},
  {"Æ±", "Ʊ"},
  {"Æ²", "Ʋ"},
  {"Æ³", "Ƴ"},
  {"Æ´", "ƴ"},
  {"Æµ", "Ƶ"},
  {"Æ¶", "ƶ"},
  {"Æ·", "Ʒ"},
  {"Æ¸", "Ƹ"},
  {"Æ¹", "ƹ"},
  {"Æº", "ƺ"},
  {"Æ»", "ƻ"},
  {"Æ¼", "Ƽ"},
  {"Æ½", "ƽ"},
  {"Æ¾", "ƾ"},
  {"Æ¿", "ƿ"},
  {"Ç", "ǀ"},
  {"Ç€", "ǀ"},
  {"Ç", "ǁ"},
  {"Ç", "ǂ"},
  {"Ç‚", "ǂ"},
  {"Ç", "ǃ"},
  {"Çƒ", "ǃ"},
  {"Ç", "Ǆ"},
  {"Ç„", "Ǆ"},
  {"Ç", "ǅ"},
  {"Ç…", "ǅ"},
  {"Ç", "ǆ"},
  {"Ç†", "ǆ"},
  {"Ç", "Ǉ"},
  {"Ç‡", "Ǉ"},
  {"Ç", "ǈ"},
  {"Çˆ", "ǈ"},
  {"Ç", "ǉ"},
  {"Ç‰", "ǉ"},
  {"Ç", "Ǌ"},
  {"ÇŠ", "Ǌ"},
  {"Ç", "ǋ"},
  {"Ç‹", "ǋ"},
  {"Ç", "ǌ"},
  {"ÇŒ", "ǌ"},
  {"Ç", "Ǎ"},
  {"Ç", "ǎ"},
  {"ÇŽ", "ǎ"},
  {"Ç", "Ǐ"},
  {"Ç", "ǐ"},
  {"Ç", "Ǒ"},
  {"Ç‘", "Ǒ"},
  {"Ç", "ǒ"},
  {"Ç’", "ǒ"},
  {"Ç", "Ǔ"},
  {"Ç“", "Ǔ"},
  {"Ç", "ǔ"},
  {"Ç”", "ǔ"},
  {"Ç", "Ǖ"},
  {"Ç•", "Ǖ"},
  {"Ç", "ǖ"},
  {"Ç–", "ǖ"},
  {"Ç", "Ǘ"},
  {"Ç—", "Ǘ"},
  {"Ç", "ǘ"},
  {"Ç˜", "ǘ"},
  {"Ç", "Ǚ"},
  {"Ç™", "Ǚ"},
  {"Ç", "ǚ"},
  {"Çš", "ǚ"},
  {"Ç", "Ǜ"},
  {"Ç›", "Ǜ"},
  {"Ç", "ǜ"},
  {"Çœ", "ǜ"},
  {"Ç", "ǝ"},
  {"Ç", "Ǟ"},
  {"Çž", "Ǟ"},
  {"Ç", "ǟ"},
  {"ÇŸ", "ǟ"},
  {"Ç ", "Ǡ"},
  {"Ç¡", "ǡ"},
  {"Ç¢", "Ǣ"},
  {"Ç£", "ǣ"},
  {"Ç¤", "Ǥ"},
  {"Ç¥", "ǥ"},
  {"Ç¦", "Ǧ"},
  {"Ç§", "ǧ"},
  {"Ç¨", "Ǩ"},
  {"Ç©", "ǩ"},
  {"Çª", "Ǫ"},
  {"Ç«", "ǫ"},
  {"Ç¬", "Ǭ"},
  {"Ç­", "ǭ"},
  {"Ç®", "Ǯ"},
  {"Ç¯", "ǯ"},
  {"Ç°", "ǰ"},
  {"Ç±", "Ǳ"},
  {"Ç²", "ǲ"},
  {"Ç³", "ǳ"},
  {"Ç´", "Ǵ"},
  {"Çµ", "ǵ"},
  {"Ç¶", "Ƕ"},
  {"Ç·", "Ƿ"},
  {"Ç¸", "Ǹ"},
  {"Ç¹", "ǹ"},
  {"Çº", "Ǻ"},
  {"Ç»", "ǻ"},
  {"Ç¼", "Ǽ"},
  {"Ç½", "ǽ"},
  {"Ç¾", "Ǿ"},
  {"Ç¿", "ǿ"},
  {"È", "Ȁ"},
  {"È€", "Ȁ"},
  {"È", "ȁ"},
  {"È", "Ȃ"},
  {"È‚", "Ȃ"},
  {"È", "ȃ"},
  {"Èƒ", "ȃ"},
  {"È", "Ȅ"},
  {"È„", "Ȅ"},
  {"È", "ȅ"},
  {"È…", "ȅ"},
  {"È", "Ȇ"},
  {"È†", "Ȇ"},
  {"È", "ȇ"},
  {"È‡", "ȇ"},
  {"È", "Ȉ"},
  {"Èˆ", "Ȉ"},
  {"È", "ȉ"},
  {"È‰", "ȉ"},
  {"È", "Ȋ"},
  {"ÈŠ", "Ȋ"},
  {"È", "ȋ"},
  {"È‹", "ȋ"},
  {"È", "Ȍ"},
  {"ÈŒ", "Ȍ"},
  {"È", "ȍ"},
  {"È", "Ȏ"},
  {"ÈŽ", "Ȏ"},
  {"È", "ȏ"},
  {"È", "Ȑ"},
  {"È", "ȑ"},
  {"È‘", "ȑ"},
  {"È", "Ȓ"},
  {"È’", "Ȓ"},
  {"È", "ȓ"},
  {"È“", "ȓ"},
  {"È", "Ȕ"},
  {"È”", "Ȕ"},
  {"È", "ȕ"},
  {"È•", "ȕ"},
  {"È", "Ȗ"},
  {"È–", "Ȗ"},
  {"È", "ȗ"},
  {"È—", "ȗ"},
  {"È", "Ș"},
  {"È˜", "Ș"},
  {"È", "ș"},
  {"È™", "ș"},
  {"È", "Ț"},
  {"Èš", "Ț"},
  {"È", "ț"},
  {"È›", "ț"},
  {"È", "Ȝ"},
  {"Èœ", "Ȝ"},
  {"È", "ȝ"},
  {"È", "Ȟ"},
  {"Èž", "Ȟ"},
  {"È", "ȟ"},
  {"ÈŸ", "ȟ"},
  {"È ", "Ƞ"},
  {"È¡", "ȡ"},
  {"È¢", "Ȣ"},
  {"È£", "ȣ"},
  {"È¤", "Ȥ"},
  {"È¥", "ȥ"},
  {"È¦", "Ȧ"},
  {"È§", "ȧ"},
  {"È¨", "Ȩ"},
  {"È©", "ȩ"},
  {"Èª", "Ȫ"},
  {"È«", "ȫ"},
  {"È¬", "Ȭ"},
  {"È­", "ȭ"},
  {"È®", "Ȯ"},
  {"È¯", "ȯ"},
  {"È°", "Ȱ"},
  {"È±", "ȱ"},
  {"È²", "Ȳ"},
  {"È³", "ȳ"},
  {"È´", "ȴ"},
  {"Èµ", "ȵ"},
  {"È¶", "ȶ"},
  {"È·", "ȷ"},
  {"È¸", "ȸ"},
  {"È¹", "ȹ"},
  {"Èº", "Ⱥ"},
  {"È»", "Ȼ"},
  {"È¼", "ȼ"},
  {"È½", "Ƚ"},
  {"È¾", "Ⱦ"},
  {"È¿", "ȿ"},
  {"É", "ɀ"},
  {"É€", "ɀ"},
  {"É", "Ɂ"},
  {"É", "ɂ"},
  {"É‚", "ɂ"},
  {"É", "Ƀ"},
  {"Éƒ", "Ƀ"},
  {"É", "Ʉ"},
  {"É„", "Ʉ"},
  {"É", "Ʌ"},
  {"É…", "Ʌ"},
  {"É", "Ɇ"},
  {"É†", "Ɇ"},
  {"É", "ɇ"},
  {"É‡", "ɇ"},
  {"É", "Ɉ"},
  {"Éˆ", "Ɉ"},
  {"É", "ɉ"},
  {"É‰", "ɉ"},
  {"É", "Ɋ"},
  {"ÉŠ", "Ɋ"},
  {"É", "ɋ"},
  {"É‹", "ɋ"},
  {"É", "Ɍ"},
  {"ÉŒ", "Ɍ"},
  {"É", "ɍ"},
  {"É", "Ɏ"},
  {"ÉŽ", "Ɏ"},
  {"É", "ɏ"},
  {"Î", "Α"},
  {"Î‘", "Α"},
  {"Î", "Β"},
  {"Î’", "Β"},
  {"Î", "Γ"},
  {"Î“", "Γ"},
  {"Î", "Δ"},
  {"Î”", "Δ"},
  {"Î", "Ε"},
  {"Î•", "Ε"},
  {"Î", "Ζ"},
  {"Î–", "Ζ"},
  {"Î", "Η"},
  {"Î—", "Η"},
  {"Î", "Θ"},
  {"Î˜", "Θ"},
  {"Î", "Ι"},
  {"Î™", "Ι"},
  {"Î", "Κ"},
  {"Îš", "Κ"},
  {"Î", "Λ"},
  {"Î›", "Λ"},
  {"Î", "Μ"},
  {"Îœ", "Μ"},
  {"Î", "Ν"},
  {"Î", "Ξ"},
  {"Îž", "Ξ"},
  {"Î", "Ο"},
  {"ÎŸ", "Ο"},
  {"Î ", "Π"},
  {"Î¡", "Ρ"},
  {"Î¢", "΢"},
  {"Î£", "Σ"},
  {"Î¤", "Τ"},
  {"Î¥", "Υ"},
  {"Î¦", "Φ"},
  {"Î§", "Χ"},
  {"Î¨", "Ψ"},
  {"Î©", "Ω"},
  {"Îª", "Ϊ"},
  {"Î«", "Ϋ"},
  {"Î¬", "ά"},
  {"Î­", "έ"},
  {"Î®", "ή"},
  {"Î¯", "ί"},
  {"Î°", "ΰ"},
  {"Î±", "α"},
  {"Î²", "β"},
  {"Î³", "γ"},
  {"Î´", "δ"},
  {"Îµ", "ε"},
  {"Î¶", "ζ"},
  {"Î·", "η"},
  {"Î¸", "θ"},
  {"Î¹", "ι"},
  {"Îº", "κ"},
  {"Î»", "λ"},
  {"Î¼", "μ"},
  {"Î½", "ν"},
  {"Î¾", "ξ"},
  {"Î¿", "ο"},
  {"Ï", "π"},
  {"Ï€", "π"},
  {"Ï", "ρ"},
  {"Ï", "ς"},
  {"Ï‚", "ς"},
  {"Ï", "σ"},
  {"Ïƒ", "σ"},
  {"Ï", "τ"},
  {"Ï„", "τ"},
  {"Ï", "υ"},
  {"Ï…", "υ"},
  {"Ï", "φ"},
  {"Ï†", "φ"},
  {"Ï", "χ"},
  {"Ï‡", "χ"},
  {"Ï", "ψ"},
  {"Ïˆ", "ψ"},
  {"Ï", "ω"},
  {"Ï‰", "ω"},
}

local function repair_encoding(text)
  if not (text:find("Ã",1,true) or text:find("Â",1,true) or text:find("â",1,true) or text:find("Ä",1,true) or text:find("Å",1,true) or text:find("Î",1,true) or text:find("Ï",1,true)) then return text end
  for pass = 1, 2 do
    for _, pair in ipairs(encoding_repairs) do
      text = text:gsub(pair[1], function() return pair[2] end)
    end
  end
  return text
end

local function str(value)
  if value == nil then return "" end
  return repair_encoding(pandoc.utils.stringify(value))
end

local function latex(text)
  return pandoc.write(pandoc.Pandoc({pandoc.Plain({pandoc.Str(text)})}), "latex"):gsub("%s+$", "")
end

local function html_escape(text)
  return (text:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

local function strip_number(text)
  -- Lua patterns operate on bytes: a character class containing ·/–/— can
  -- remove only the first byte of the separator and leave invalid UTF-8.
  for _, separator in ipairs({"·", "%.", "%-", "–", "—", ":"}) do
    local stripped, count = text:gsub("^%d+%s*" .. separator .. "%s*", "", 1)
    if count > 0 then return stripped end
  end
  return text
end

local function list(value)
  local items = {}
  if value == nil then return items end
  if type(value) == "table" and value.t == nil and #value > 0 then
    for _, item in ipairs(value) do items[#items + 1] = str(item) end
  elseif type(value) == "table" and (value.t == "MetaList") then
    for _, item in ipairs(value) do items[#items + 1] = str(item) end
  else
    items[1] = str(value)
  end
  return items
end

local function file_exists(path)
  local handle = io.open(path, "rb")
  if handle then handle:close() return true end
  return false
end

-- Caminho relativo (a partir da pasta do QMD) para um arquivo ao lado do filtro.
local function asset_path(name)
  local here = pandoc.path.directory(PANDOC_SCRIPT_FILE)
  local full = pandoc.path.join({here, name})
  local ok, relative = pcall(pandoc.path.make_relative, full, pandoc.system.get_working_directory())
  local path = ok and relative or full
  return (path:gsub("\\", "/"))
end

---------------------------------------------------------------------------
-- 1. Estrutura: slides, seções e régua de progresso
---------------------------------------------------------------------------
local function layout(doc)
  if not is_beamer and not is_reveal then return doc end
  local meta = doc.meta.academico or {}
  local header_lines = list(meta.cabecalho)
  local footer = str(meta.rodape)
  local place = str(meta["local"])
  local second = str(meta["segunda-linha"])
  local date = str(doc.meta.date)
  local place_line = table.concat((function()
    local parts = {}
    if place ~= "" then parts[#parts + 1] = place end
    if date ~= "" then parts[#parts + 1] = date end
    return parts
  end)(), " · ")

  local blocks = pandoc.List()
  local sections = {}
  local frame = 1 -- capa
  local first_section_frame = nil
  for index, block in ipairs(doc.blocks) do
    if block.t == "HorizontalRule" then
      -- A heading already starts a slide. Keep explicit breaks elsewhere:
      -- older decks also use untitled slides separated only by ---.
      local next_block = doc.blocks[index + 1]
      if not (next_block and next_block.t == "Header" and next_block.level <= 2) then
        blocks:insert(block)
        frame = frame + 1
      end
    else
      if block.t == "Header" and block.level <= 2 then
        frame = frame + 1
        if block.level == 1 then
          local name = strip_number(str(block.content))
          block.content = pandoc.Inlines(name)
          local label = block.attributes["rotulo"] or name
          block.attributes["rotulo"] = nil
          if is_reveal then block.attributes["data-academic-label"] = label end
          if #sections > 0 then sections[#sections].last = frame - 1 end
          sections[#sections + 1] = {first = frame, label = label}
          first_section_frame = first_section_frame or frame
        end
      end
      blocks:insert(block)
    end
  end
  if #sections > 0 then sections[#sections].last = frame end
  doc.blocks = blocks

  if is_reveal then
    local lines = {}
    for index, line in ipairs(header_lines) do
      local text = html_escape(line)
      lines[#lines + 1] = index == 1 and ("<p><strong>" .. text .. "</strong></p>") or ("<p>" .. text .. "</p>")
    end
    local config = string.format(
      '<div id="academic-config" hidden aria-hidden="true" data-footer="%s" data-place="%s" data-second="%s">'
      .. '<img class="academic-cover-ribbon" src="%s" alt="" aria-hidden="true" width="298" height="2048">'
      .. '<header class="academic-institution-header"><div>%s</div></header></div>',
      html_escape(footer), html_escape(place_line), html_escape(second),
      html_escape(asset_path("fundo.png")), table.concat(lines))
    quarto.doc.include_text("after-body", config)
    return doc
  end

  -- Beamer: textos da capa/rodapé e faixas da régua calculadas a partir dos slides reais.
  local ranges = {}
  for index, section in ipairs(sections) do
    ranges[#ranges + 1] = string.format("\\AcademicSegment{%d}{%d}{%d}{%s}",
      index, section.first, section.last, latex(section.label))
  end
  local function line(index) return latex(header_lines[index] or "") end
  local defs = {
    "\\makeatletter",
    string.format("\\def\\AcademicSectionCount{%d}", #sections),
    string.format("\\def\\AcademicExpectedTotal{%d}", frame),
    string.format("\\def\\AcademicIntroFrames{%d}", (first_section_frame or frame + 1) - 1),
    "\\def\\AcademicSectionRanges{%\n" .. table.concat(ranges, "\n") .. "\n}",
    string.format("\\def\\AcademicHeaderOne{%s}", line(1)),
    string.format("\\def\\AcademicHeaderTwo{%s}", line(2)),
    string.format("\\def\\AcademicHeaderThree{%s}", line(3)),
    string.format("\\def\\AcademicFooterLabel{%s}", latex(footer)),
    string.format("\\def\\AcademicSecondLine{%s}", latex(second)),
    string.format("\\def\\AcademicPlaceLine{%s}", latex(place_line)),
    string.format("\\def\\AcademicRibbon{%s}", asset_path("fundo.png")),
    "\\makeatother"
  }
  quarto.doc.include_text("in-header", table.concat(defs, "\n"))
  return doc
end

---------------------------------------------------------------------------
-- 2. Elementos de conteúdo
---------------------------------------------------------------------------
local function boxes(el)
  if not is_beamer then return nil end
  local environment
  if el.classes:includes("highlight-box") then
    environment = "alertblock"
  elseif el.classes:includes("info-box") or el.classes:includes("box") then
    environment = "exampleblock"
  end
  if not environment then return nil end
  el.content:insert(1, pandoc.RawBlock("latex", "\\begin{" .. environment .. "}{}"))
  el.content:insert(pandoc.RawBlock("latex", "\\end{" .. environment .. "}"))
  return el.content
end

-- [1]{.circle}: marcador numérico redondo.
local function circles(el)
  if not el.classes:includes("circle") then return nil end
  if is_beamer then
    return pandoc.RawInline("latex", "\\AcademicCircle{" .. latex(str(el.content)) .. "}")
  end
  return nil
end

-- <br> em células de tabela e textos curtos.
local function line_breaks(el)
  if is_beamer and el.format:match("html") and el.text:match("^<br%s*/?>$") then
    return pandoc.LineBreak()
  end
end

-- Bloco ```text com etapas separadas por ↓: fluxo numerado nos dois formatos.
local function flow(el)
  if not el.classes:includes("text") then return nil end
  if not is_beamer and not is_reveal then return nil end
  -- Console output and plain-text examples are also labelled ```text.
  -- Only transform the explicit arrow-separated workflows used in lectures.
  if not el.text:match("\n%s*↓%s*\n") then return nil end
  local steps = {}
  for line in el.text:gmatch("[^\r\n]+") do
    line = line:match("^%s*(.-)%s*$")
    if line ~= "↓" and line ~= "" then steps[#steps + 1] = line end
  end
  if is_reveal then
    local nodes = pandoc.List()
    for index, step in ipairs(steps) do
      local number = pandoc.Span({pandoc.Str(string.format("%02d", index))}, pandoc.Attr("", {"flow-step-number"}))
      nodes:insert(pandoc.Div({pandoc.Plain({number}), pandoc.Para({pandoc.Str(step)})}, pandoc.Attr("", {"academic-flow-step"})))
    end
    return pandoc.Div(nodes, pandoc.Attr("", {"academic-flow"}))
  end
  local commands = {"\\begin{center}\\begin{tikzpicture}[>=Latex, every node/.style={align=left, text=academicotexto}]"}
  for index, step in ipairs(steps) do
    local column = index <= 4 and index - 1 or 8 - index
    local row = index <= 4 and 0 or -1.90
    commands[#commands + 1] = string.format(
      "\\node[draw=academicoazul!15,fill=academicofundo,rounded corners=2pt,text width=2.95cm,minimum height=1.25cm,inner sep=5pt,font=\\fontsize{8.2}{10}\\selectfont] (step%d) at (%.2f,%.2f) {{\\color{academicoouro}\\bfseries %02d}\\\\[3pt]%s};",
      index, column * 3.62, row, index, latex(step))
  end
  for index = 1, #steps - 1 do
    local from = index < 4 and "east" or (index == 4 and "south" or "west")
    local to = index < 4 and "west" or (index == 4 and "north" or "east")
    commands[#commands + 1] = string.format("\\draw[->,academicocinza!70,line width=0.65pt] (step%d.%s) -- (step%d.%s);", index, from, index + 1, to)
  end
  commands[#commands + 1] = "\\end{tikzpicture}\\end{center}"
  return pandoc.RawBlock("latex", table.concat(commands, "\n"))
end

-- No PDF: formatos que o XeLaTeX não lê (webp, avif, gif, svg) são trocados pela
-- versão raster de mesmo nome (.png/.jpg), e toda figura ganha altura máxima.
local function images(el)
  if not is_beamer then return nil end
  local base, extension = el.src:match("^(.*)%.([%w]+)$")
  if base and ({webp = true, avif = true, gif = true, svg = true})[extension:lower()] then
    for _, candidate in ipairs({"png", "jpg", "jpeg", "PNG", "JPG"}) do
      if file_exists(base .. "." .. candidate) then el.src = base .. "." .. candidate break end
    end
  end
  if not el.attributes["height"] then
    if el.classes:includes("fig-full") then
      el.attributes["height"] = "40%"
    else
      el.attributes["height"] = "58%"
    end
  end
  return el
end

-- Corpo dos slides em tamanho \small no Beamer; o quadro reduz-se se exceder a área útil.
local function frames(el)
  if not is_beamer then return nil end
  if el.level == 2 then
    if not el.classes:includes("no-shrink") and not el.attributes["shrink"] then
      el.attributes["shrink"] = "0"
    end
    return {el, pandoc.RawBlock("latex", "\\small")}
  end
end

return {
  {Pandoc = layout},
  {Div = boxes, Span = circles, RawInline = line_breaks, CodeBlock = flow, Image = images, Header = frames, Str = function(el) el.text = repair_encoding(el.text); return el end}
}
