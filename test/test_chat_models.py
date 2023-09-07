import os
import pathlib


def check_line_direction(baseline_seg: dict) -> dict:
    """Check if the lines are oriented top to bottom, if not inverse their direction.
    
    Parameters:
        baseline_seg (dict): A dictionary containing segmentation output
    
    Return: 
        baseline_seg (dict): A dictionary containing segmentation output with corrected line direction
    """
    
    lines = []
    for line in baseline_seg["lines"]:
        if line["baseline"][0][1] > line["baseline"][-1][1]:
            line["baseline"].reverse()
        lines.append(line)
    
    baseline_seg["lines"] = lines

    return baseline_seg

if __name__ == '__main__':

    # Check if kraken is installed
    try:
        from kraken import blla, rpred
        from kraken.lib import vgsl, models
    except ImportError:
        print("Install kraken OCR engine to run this script: https://github.com/mittagessen/kraken#installation.")
        exit(1)
    
    # This packages are kraken dependencies
    import torch
    from PIL import Image

    # Set number of threads to 1 to avoid multithreading issues
    torch.set_num_threads(1)

    # Set paths
    cwd = pathlib.Path.cwd()
    models_dir = cwd / "models"
    test_dir = cwd / "test" 
    seg_model_path = models_dir / "chat_seg.mlmodel"
    rec_model_path = models_dir / "chat_rec.mlmodel"

    # Check if all files exist
    assert seg_model_path.exists()
    assert rec_model_path.exists()

    # Load models
    seg_model = vgsl.TorchVGSLModel.load_model(seg_model_path)
    rec_model = models.load_any(rec_model_path)

    for img_path in test_dir.glob("*.png"):
        # Load image
        img = Image.open(img_path)

        # Segment the image
        baseline_seg = blla.segment(img, text_direction="vertical-rl", model=seg_model)
        
        # Check if the lines are oriented top to bottom, if not inverse their direction
        baseline_seg = check_line_direction(baseline_seg)

        # Iterate over the lines
        pred_it = rpred.rpred(rec_model, img, baseline_seg)
        for record in pred_it:
            print(record)

    print("Done!")