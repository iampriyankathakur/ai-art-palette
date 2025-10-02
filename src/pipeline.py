import argparse
import matplotlib.pyplot as plt
from palette_extractor import extract_palette
from recommender import recommend_complements

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to image file")
    parser.add_argument("--output", default="assets/palette_output.png", help="Path to save palette image")
    args = parser.parse_args()

    colors = extract_palette(args.image, num_colors=5)
    complements = recommend_complements(colors)

    # Plot palette
    fig, ax = plt.subplots(2, 1, figsize=(8, 4))
    
    ax[0].imshow([colors/255.0])
    ax[0].set_title("Extracted Palette")
    ax[0].axis("off")
    
    ax[1].imshow([complements/255.0])
    ax[1].set_title("Complementary Palette")
    ax[1].axis("off")

    plt.savefig(args.output)
    plt.close()

    print(f"✅ Palette saved at {args.output}")
