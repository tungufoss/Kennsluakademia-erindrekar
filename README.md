# Kennsluakademía – erindi

Þetta repo heldur utan um erindið **Erindrekinn vinnur, nemandinn ber ábyrgð: Mannleg stjórn í upplýsingaverkfræði**, fyrir Ráðstefnu Kennsluakademíu opinberu háskólanna. Verkefnið byggir á [sniðmáti ráðstefnunnar](https://github.com/HI-IDN/Conf-Kennsluakademia).

## Vinnuferli

Textinn er skrifaður í [erindrekar.qmd](erindrekar.qmd). Quarto býr til PDF og vefútgáfu úr sömu heimild:

```bash
quarto render erindrekar.qmd
```

Þetta endurmyndar `erindrekar.tex`, `erindrekar.pdf` og `erindrekar.html`. Breyttu `erindrekar.qmd`, ekki `erindrekar.tex`, því `erindrekar.tex` er mynduð skrá og skrifast yfir við birtingu. Vefútgáfan verður birt á [tungufoss.github.io/Kennsluakademia-erindrekar](https://tungufoss.github.io/Kennsluakademia-erindrekar/) þegar GitHub Pages hefur lokið fyrstu birtingu.

Til að forskoða vefútgáfuna með endurhleðslu:

```bash
quarto preview erindrekar.qmd --to haskoli-islands-html
```

## Uppsetning

- `erindrekar.qmd` – heimildarskjal með lýsigögnum og meginmáli.
- `references.bib` – heimildir.
- `kennsluakademia_conf.cls` og `quarto/` – útlit og stillingar fyrir PDF og vefútgáfu.
- `.github/workflows/publish.yml` – byggir PDF og vefútgáfu við uppfærslu á `main` og birtir vefútgáfuna á GitHub Pages.

GitHub Actions endurbyggir vefútgáfuna við birtingu en skilar ekki mynduðum skrám aftur í repo-ið. Keyrðu því `quarto render erindrekar.qmd` staðbundið ef `erindrekar.pdf` og `erindrekar.tex` eiga að fylgja uppfærslunni.

## Tengd verkefni

- [Kennsluakademía-IDN302G](https://github.com/tungufoss/Kennsluakademia-IDN302G) sýnir sambærilegt Quarto-vinnuferli fyrir annað erindi.
- [Sniðmát Kennsluakademíunnar](https://github.com/HI-IDN/Conf-Kennsluakademia) inniheldur nánari leiðbeiningar um uppsetningu og snið.

## Leyfi

MIT. Sjá [LICENCE](LICENCE).
