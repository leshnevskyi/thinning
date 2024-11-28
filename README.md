# Thinning

The project was created as a part of the Image Processing course. The goal is to demonstrate image thinning which is a morphological operation in image processing that reduces the width of lines or objects in a binary image to a single pixel in thickness, while retaining their overall structure and topology. Such a transformation is useful for OCR, pattern recognition, shape analysis, etc.

## Usage
The project depends on `uv` and Python v3.13. To start `thinning` run the following commands:
```console
cd ui
npm ci
npm run dev
```
These commands should start a dev server for the UI part. Now run the following commands to run the API server:
```console
cd api
uv venv
source .venv/bin/activate
uv run api
```
As a result, you should be able to go to `http://localhost:5173/` and upload images for thinning.

<img width="1352" alt="image" src="https://github.com/user-attachments/assets/4a0c8b44-9aed-4e65-8973-817844ed9151">
