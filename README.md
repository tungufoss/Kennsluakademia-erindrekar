# Erindrekinn vinnur, nemandinn ber ábyrgð

**Helga Ingimundardóttir** ([ORCID 0000-0002-2780-3546](https://orcid.org/0000-0002-2780-3546))  
Iðnaðarverkfræði-, vélaverkfræði- og tölvunarfræðideild, Háskóli Íslands

[Ráðstefna Kennsluakademíu opinberu háskólanna 2026](https://kennsluakademia.hi.is/radstefna-kennsluakademiunnar/), Saga, Háskóli Íslands, 20. nóvember 2026  
Málstofa 1: **Gervigreind og ábyrgð í námi**, S-261, kl. 9:00–10:30

> Ágripið var jafnframt kynnt fyrir atvinnulíf á [Hugbúnaðarráðstefnu Ský: Hugbúnaðargerð án handskrifaðs kóða](https://www.sky.is/vidburdur/3168-2026-vidburdur-1118), 18. nóvember 2026 (15 mínútna útgáfa). Undirfyrirsögn: **Faglegt vinnulag með AI-erindrekum**.

## Tengt efni

- **Vefútgáfa:** [Kennsluakademía – erindið](https://tungufoss.github.io/Kennsluakademia-erindrekar/)
- **Glærur:** [slides/](https://tungufoss.github.io/Kennsluakademia-erindrekar/slides/)
- **Útgefið erindi (PDF):** [erindrekar-1.pdf](https://kennsluakademia.hi.is/wp-content/uploads/2026/11/erindrekar-1.pdf)
- **Ráðstefna Kennsluakademíu:** [radstefna-kennsluakademiunnar](https://kennsluakademia.hi.is/radstefna-kennsluakademiunnar/)
- **Ráðstefna Ský:** [Hugbúnaðargerð án handskrifaðs kóða](https://www.sky.is/vidburdur/3168-2026-vidburdur-1118)
- **Glærur Ský:** [slides/sky.html](https://tungufoss.github.io/Kennsluakademia-erindrekar/slides/sky.html)

## Útdráttur

AI-erindrekar geta tekið við markmiði, lesið samhengi verkefnis, breytt skrám og keyrt verkfæri. Nemendur eru þegar farnir að nota þá, en kennsla og leiðbeiningar um gervigreind snúast enn oftast um spjallkerfi. Í IÐN302G Upplýsingaverkfræði við Háskóla Íslands er notkun erindreka fléttuð inn í raunveruleg gagnaverkefni og GitHub-vinnuferli. Erindið fjallar um hvernig má kenna afmörkun, Git, kóðarýni, prófanir og sameiginlega ábyrgð um leið og nemendur læra að vinna með AI-erindreka. Fyrstu reynslusporin sýna bæði áhuga og áskoranir; þau eru lýsandi vísbendingar úr nýju sviði, ekki mat á áhrifum.

**Lykilorð:** AI-erindrekar, hugbúnaðargerð, Git, kóðarýni, sameiginleg ábyrgð, háskólakennsla

## Vinsamlega vitnið í þetta verk sem

Ingimundardóttir, Helga. 2026. „Erindrekinn vinnur, nemandinn ber ábyrgð.“ *Ráðstefna Kennsluakademíu opinberu háskólanna*, Saga, Háskóli Íslands, Reykjavík, 20. nóvember 2026. <https://kennsluakademia.hi.is/wp-content/uploads/2026/11/erindrekar-1.pdf>.

```bibtex
@inproceedings{ingimundardottir2026erindrekar,
  author = {Ingimundardóttir, Helga},
  title = {Erindrekinn vinnur, nemandinn ber ábyrgð},
  booktitle = {Ráðstefna Kennsluakademíu opinberu háskólanna},
  date = {2026-11-20},
  address = {Saga, Háskóli Íslands, Reykjavík},
  url = {https://kennsluakademia.hi.is/wp-content/uploads/2026/11/erindrekar-1.pdf}
}
```

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
