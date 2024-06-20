# Signature App

Signature App is a Python-based application that allows users to create digital signatures on a canvas and save them as images with or without backgrounds. The application uses `tkinter` for the user interface and `Pillow` for image manipulation.

## Features
- Responsive canvas for drawing signatures.
- Option to choose ink color.
- Save signatures with or without backgrounds.
- Save signatures to a user-selected directory.
- Clear the canvas option.

## Prerequisites
Make sure you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

1. **Clone the repository or download the zip and extract:**

    ```bash
    git clone https://github.com/username/signature-app.git
    cd signature-app
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Interact with the application:**
    - Draw signatures by clicking and dragging the mouse on the canvas.
    - Click "Save with Background" to save the signature with a background.
    - Click "Save without Background" to save the signature without a background (transparent).
    - Click "Clear" to clear the canvas.
    - Click "Choose Ink Color" to select the ink color.

3. **Select Save Directory:**
    - When the application opens, you will be prompted to select a directory to save the images.

## Project Structure

signature-app/
│
├── main.py
├── README.md
└── requirements.txt


## Example Screenshot

<img width="976" alt="Screenshot 2024-06-20 at 18 51 50" src="https://github.com/akufikri/signatures-py/assets/108182945/511da38e-9006-4c4c-af82-21264d86afd6">

## Contribution

1. Fork the repository.
2. Create a new branch: `git checkout -b new-feature`.
3. Make changes and commit: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin new-feature`.
5. Submit a pull request.
