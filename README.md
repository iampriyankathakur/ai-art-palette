# 🎨 AI Art Palette Recommender

Upload an image and this project generates a **color palette** using AI clustering.  
It also recommends **complementary colors** for design.

---

## 🚀 Features
- Extract dominant colors from images
- Generate a palette visualization
- Recommend complementary colors
- Export palette as PNG or JSON

---

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/ai-art-palette.git
cd ai-art-palette
pip install -r requirements.txt
```
## ▶️ Usage
```
python src/pipeline.py --image data/sample_image.jpg
```

## Output:
```
Palette image saved to assets/palette_output.png
```

### 📊 Tech Stack
```
Python

Image Processing: OpenCV, PIL

Clustering: scikit-learn (k-means)

Visualization: matplotlib

```

## Requirements

```txt
opencv-python
matplotlib
scikit-learn
numpy
pillow
pytest
```

