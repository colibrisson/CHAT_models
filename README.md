# CHAT models: Chinese Historical documents Automatic Transcription models

[![DOI](https://doi.org/10.5281/zenodo.8325545)

![Reading Cat](./assets/reading_cat.png)

This repository contains segmentation and transcription models trained using the [kraken OCR engine](https://github.com/mittagessen/kraken).

This work is part of an ongoing project by the Numerica Sinologica consortium to build open-source digital tools for pre-modern Chinese studies.

## Segmentation model

- `chat_rec.mlmodel` is trained to segment binary images with a 9:16 aspect ratio.

## Recognition model

- `chat_rec.mlmodel` was trained on an expansive dataset of 1.7 million lines sourced from prints and manuscripts spanning the 10th to the 20th century. The model achieved an accuracy exceeding 99% across various test datasets. For optimal performance, it's recommended to apply the model on binary images.

## Getting Started

To test the models, install kraken and run:

`python test/test_chat_models.py`

## Acknowledgement

We wish to thank kraken main developer, Benjamin Kiessling, and the eScriptorium project directors, Daniel Stökl Ben Ezra and Peter Stokes, for their support.

This work received funding from the Centre Chine, Corée, Japon (UMR 8173), the Centre de recherche sur les civilisations de l'Asie orientale (UMR 8155), the Institut d'Asie orientale (UMR 5062), the Institut Universitaire de France, and the Vietnamica project (ERC 833933).

We gratefully acknowledge support from the CNRS/IN2P3 Computing Center (Lyon - France) and manuscriptologIA (DIM - STN) for providing computing and data-processing resources needed for this work.

## License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. See [LICENSE](./LICENCE) for details.

## Citation

<!-- ```
@software{colin_brisson_2023_7539324,
  author       = {Colin Brisson and
                  Frédéric Constant and
                  Bui Marc},
  title        = {{colibrisson/numerica\_sinologica\_siku\_htr\_models: 
                   First release}},
  month        = jan,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0.0.1},
  doi          = {10.5281/zenodo.7539324},
  url          = {https://doi.org/10.5281/zenodo.7539324}
}
``` -->
