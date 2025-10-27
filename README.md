# 🔬 Microparticle Counting
Microscopic image & video stream processing for **automatic counting and tracking of micro‑particles** using computer vision.  
Developed by **[Martin Badrous](https://github.com/martinbadrous)**.

---

## 🌍 Overview
This project provides a pipeline to detect, track, and count micro‑particles in fluid samples (e.g., environmental monitoring, lab assays). Using classic computer vision (Hough, contour tracking) and Python, the code processes microscope frames or videos and outputs counts plus optional visualisation.

Key uses:
- Real‑time or offline particle counting from microscope video.
- Component in industrial or research workflows (microplastics, contamination, fluid analysis).
- Basis for more advanced systems (deep learning, multi‑camera, automation).

---

## 🧰 Features
- ✅ Detect particles via Hough circle detection or contour‑based tracking.
- ✅ Count particles across frames / video segments.
- ✅ Export results (counts, timestamps, optionally visuals).
- ✅ Lightweight Python implementation, easy to adapt or extend.
- ✅ Example demos included (still frames, video snippets).

---

## 🗂 Repository Structure
```bash
Microparticle‑counting/
├── Hough.py                   # Hough‑circle detection script
├── Hough‑tracker.py           # Hough + tracking across frames
├── Contour_tracker.py         # Contour‑based detection + tracking
├── plot.py                    # Visualise counts/results
├── DEMO‑PARTICLES … .jpg      # Example image frames
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

---

## 🚀 Installation & Usage
```bash
# 1. Clone this repository
git clone https://github.com/martinbadrous/Microparticle‑counting.git
cd Microparticle‑counting

# 2. Install Python dependencies
pip install ‑r requirements.txt

# 3. Run detection / tracking
# Example: for video or sequence of images
python Hough_tracker.py --input path/to/video_or_folder --output results.csv
```
> See the script header comments in `Hough.py` or `Contour_tracker.py` for detailed usage options (e.g., threshold settings, ROI, video vs frames).

---

## 🧩 Usage Scenarios
- **Laboratory assays**: count particles/objects in fluid under microscope, automating manual counting.
- **Microplastics monitoring**: detect particles in water samples via video microscopy.
- **Quality control**: track particulate matter in industrial production or filtration systems.
- **Prototype for AI systems**: Use as baseline before migrating to CNN‑based detectors.

---

## 📝 Notes & Tips
- Lighting and contrast matter: ensure good contrast between particles & background.
- Tune detection parameters (circle radius, threshold) for your particle size range.
- For video sequences: ensure stable camera and minimal motion blur.
- Consider upgrading to deep‑learning detectors (YOLO, U‑Net) if particles are irregular or obscured.

---

## 📚 Related Work
Check out other projects of mine for related computer vision pipelines:
- [Bone‑Loss Detection (medical image DL)](https://github.com/martinbadrous/Marginal‑Bone‑Loss‑Detection‑Using‑Deep‑Learning‑PyTorch)
- [TurtleBot3 Vision Applications](https://github.com/martinbadrous/Turtlebot3_applications)
- [Alto Parsing](https://github.com/martinbadrous/Alto_parsing)

---

## 👨‍💻 Author
**Martin Badrous**  
Computer Vision & Machine Learning Engineer  
📍 Based in France | 🇪🇬 Egyptian origin  
📧 martin.badrous@gmail.com • [GitHub](https://github.com/martinbadrous)

---

⭐ If you find this project useful, please give it a star on GitHub!
