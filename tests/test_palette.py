from src.palette_extractor import extract_palette

def test_extract_palette():
    colors = extract_palette("data/sample_image.jpg", num_colors=3)
    assert len(colors) == 3
