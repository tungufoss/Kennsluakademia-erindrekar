# Erindrekinn vinnur, nemandinn ber ábyrgð

**Helga Ingimundardóttir** ([ORCID 0000-0002-2780-3546](https://orcid.org/0000-0002-2780-3546))  
Iðnaðarverkfræði-, vélaverkfræði- og tölvunarfræðideild, Háskóli Íslands

[Ráðstefna Kennsluakademíu opinberu háskólanna 2026](https://kennsluakademia.hi.is/radstefna-kennsluakademiunnar/), Saga, Háskóli Íslands, 20. nóvember 2026  
Málstofa 1: **Gervigreind og ábyrgð í námi**, S-261, kl. 9:00–10:30

> Erindið hefur einnig verið aðlagað sem 15 mínútna útgáfa fyrir [Hugbúnaðarráðstefnu Ský: Hugbúnaðargerð án handskrifaðs kóða](https://www.sky.is/vidburdur/3168-2026-vidburdur-1118), 18. nóvember 2026. Undirfyrirsögn: **Faglegt vinnulag með AI-erindrekum**.

## Tengt efni

- **Útgefið erindi (PDF):** [erindrekar-1.pdf](https://kennsluakademia.hi.is/wp-content/uploads/2026/11/erindrekar-1.pdf)
- **Afrit (PDF):** [erindrekar.pdf](erindrekar.pdf)
- **Vefútgáfa:** [Kennsluakademía – erindið](https://tungufoss.github.io/Kennsluakademia-erindrekar/)
- **Glærur Kennsluakademíu:** [slides/](https://tungufoss.github.io/Kennsluakademia-erindrekar/slides/)
- **Ráðstefna Ský:** [Hugbúnaðargerð án handskrifaðs kóða](https://www.sky.is/vidburdur/3168-2026-vidburdur-1118)
- **Glærur Ský:** [slides/sky.html](https://tungufoss.github.io/Kennsluakademia-erindrekar/slides/sky.html)

## Útdráttur

AI-erindrekar geta tekið við markmiði, lesið samhengi verkefnis, breytt skrám og keyrt verkfæri. Nemendur eru þegar farnir að nota þá, en kennsla og leiðbeiningar um gervigreind snúast enn oftast um spjallkerfi. Í IÐN302G Upplýsingaverkfræði við Háskóla Íslands er notkun erindreka fléttuð inn í raunveruleg gagnaverkefni og GitHub-vinnuferli. Erindið fjallar um hvernig má kenna afmörkun, Git, kóðarýni, prófanir og sameiginlega ábyrgð um leið og nemendur læra að vinna með AI-erindreka. Fyrstu reynslusporin sýna bæði áhuga og áskoranir; þau eru lýsandi vísbendingar úr nýju sviði, ekki mat á áhrifum.

**Lykilorð:** AI-erindrekar, hugbúnaðargerð, Git, kóðarýni, sameiginleg ábyrgð, háskólakennsla

## Vinsamlega vitnið í þetta verk sem

Ingimundardóttir, H. (2026). *Erindrekinn vinnur, nemandinn ber ábyrgð*. Ráðstefna Kennsluakademíu opinberu háskólanna, Háskóli Íslands, Reykjavík.

```bibtex
@inproceedings{Ingimundardottir2026Erindrekinn,
  author    = {Ingimundardóttir, Helga},
  title     = {Erindrekinn vinnur, nemandinn ber ábyrgð},
  booktitle = {Ráðstefna Kennsluakademíu opinberu háskólanna},
  address   = {Háskóli Íslands, Reykjavík},
  month     = nov,
  year      = {2026},
  url       = {https://kennsluakademia.hi.is/wp-content/uploads/2026/11/erindrekar-1.pdf}
}
```

## Merki

- [logo-short.svg](quarto/logo-short.svg) sýnir „KENNSLU AKADEMÍA“.
- [logo-long.svg](quarto/logo-long.svg) bætir við „OPINBERU HÁSKÓLANNA“.
- Bæði nota merkið í [favicon.svg](quarto/favicon.svg) og hafa texta sem SVG-texta í Arial Bold.

## Building

The paper is authored in [erindrekar.qmd](erindrekar.qmd). The two RevealJS presentations use the HÍ theme from [tungufoss/quarto-hi](https://github.com/tungufoss/quarto-hi):

```bash
quarto render erindrekar.qmd
quarto render slides/index.qmd
quarto render slides/sky.qmd
```

The GitHub Pages workflow renders the article and both slide decks on updates to `main` and deploys them to the project site.

## Leyfi

MIT. Sjá [LICENCE](LICENCE).
