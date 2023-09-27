# Chinese Historical documents Automatic Transcription (CHAT) models

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8325545.svg)](https://doi.org/10.5281/zenodo.8325545)

![Reading Cat](./assets/reading_cat.png)

This repository contains segmentation and transcription models trained using the [kraken OCR engine](https://github.com/mittagessen/kraken).

This work is part of an ongoing project by the Numerica Sinologica consortium to build open-source digital tools for pre-modern Chinese studies.

## Segmentation model

**chat_seg.mlmodel** is trained to segment binary images that have a 9:16 aspect ratio. It identifies various regions:

- **Main**
- **Margin**
- **Illustration**
- **Other**

It also recognizes different line types:

- **default** (Standard line type)
- **DoubleLine**

## Recognition model

**chat_rec.mlmodel** was trained on an expansive dataset of 1.7 million lines sourced from prints and manuscripts spanning from the 10th to the 20th century. The model is able to recognize more than 16 000 characters with an accuracy exceeding 99%. 

For the best results, apply the model to binary images where the column width exceeds 90 pixels.

## Reading order model

We will publish a model to compute the reading order as soon as this feature get added to kraken main branch.
## Getting Started

Install kraken:
```bash
pip install kraken
```

Clone this repository:
```bash
git clone https://github.com/colibrisson/CHAT_models.git
cd ./CHAT_models
```

Run the demo:
```bash
python demo/chat_models_demo.py
```
For further details, please refer to the [kraken documentation](https://kraken.re/).

## Acknowledgement

We wish to thank kraken main developer, Benjamin Kiessling, and the eScriptorium project directors, Daniel Stökl Ben Ezra and Peter Stokes, for their support.

This work received funding from the Centre Chine, Corée, Japon (UMR 8173), the Centre de recherche sur les civilisations de l'Asie orientale (UMR 8155), the Institut d'Asie orientale (UMR 5062), the Institut Universitaire de France, and the Vietnamica project (ERC 833933).

We gratefully acknowledge support from the CNRS/IN2P3 Computing Center (Lyon - France), manuscriptologIA (DIM - STN) and Azzurra HPC center (Université Côte d'Azur) for providing computing and data-processing resources needed for this work.

## License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. See [LICENSE](./LICENCE) for details.

## Citation

```
@software{colin_brisson_2023_8383732,
  author       = {Colin Brisson and
                  Frédéric Constant and
                  Marc Bui},
  title        = {{Chinese Historical documents Automatic 
                   Transcription (CHAT) models}},
  month        = sep,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0},
  doi          = {10.5281/zenodo.8383732},
  url          = {https://doi.org/10.5281/zenodo.8383732}
}
```
