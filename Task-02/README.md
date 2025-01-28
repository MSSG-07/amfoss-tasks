# Pixelated Problem Solver

## Overview
To confirm you're not a robot, this task involves creating or using a `.png` file containing a simple arithmetic expression (e.g., “2 + 2”). Then, write a Python script to interpret the image, evaluate the expression, and return the result.

---

## Approach
The script uses the `Pillow` library to load and preprocess the image and `pytesseract` for OCR to extract the arithmetic expression. The extracted text is then parsed and evaluated using Python's `eval()` function. Test images with basic expressions like “3 * 5” were used to validate the script’s accuracy.

---
