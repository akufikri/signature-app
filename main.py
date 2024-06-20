import tkinter as tk
from tkinter import Canvas, colorchooser, filedialog
from PIL import Image, ImageDraw
import os

class SignatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signature App")

        self.canvas = Canvas(root, bg="#202020")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X)
        self.button_save_with_bg = tk.Button(self.button_frame, text="Save with Background", command=lambda: self.save_signature(with_background=True))
        self.button_save_without_bg = tk.Button(self.button_frame, text="Save without Background", command=lambda: self.save_signature(with_background=False))
        self.button_clear = tk.Button(self.button_frame, text="Clear", command=self.clear_canvas)
        self.button_choose_color = tk.Button(self.button_frame, text="Choose Ink Color", command=self.choose_color)
        
        self.button_save_with_bg.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_save_without_bg.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_clear.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_choose_color.pack(side=tk.LEFT, padx=5, pady=5)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<ButtonRelease-1>", self.end_paint)
        self.canvas.bind("<Configure>", self.resize_canvas)

        self.image = Image.new("RGBA", (500, 300), (32, 32, 32, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.last_x, self.last_y = None, None
        self.ink_color = "white"
        self.is_drawing = False
        self.save_path = None
        self.file_counter = 1

        # Prompt user to select save path at the start
        self.set_save_path()

    def resize_canvas(self, event):
        new_image = Image.new("RGBA", (event.width, event.height), (32, 32, 32, 255))
        new_image.paste(self.image, (0, 0))
        self.image = new_image
        self.draw = ImageDraw.Draw(self.image)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Ink Color")
        if color_code:
            self.ink_color = color_code[1]

    def start_paint(self, event):
        self.is_drawing = True
        self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        if self.is_drawing:
            x, y = event.x, event.y
            if self.last_x is not None and self.last_y is not None:
                self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.ink_color, width=2)
                self.draw.line([self.last_x, self.last_y, x, y], fill=self.ink_color, width=2)
            self.last_x, self.last_y = x, y

    def end_paint(self, event):
        if self.is_drawing:
            if self.last_x == event.x and self.last_y == event.y:
                self.dot(event)
            self.is_drawing = False
            self.last_x, self.last_y = None, None

    def dot(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x+2, y+2, fill=self.ink_color, outline=self.ink_color)
        self.draw.ellipse([x, y, x+2, y+2], fill=self.ink_color)

    def set_save_path(self):
        self.save_path = filedialog.askdirectory(title="Select Directory to Save Images")
        if not self.save_path:
            self.root.destroy()  # Close the app if no directory is selected

    def save_signature(self, with_background=True):
        if self.save_path:
            file_name = f"signature_{self.file_counter}.png"
            file_path = os.path.join(self.save_path, file_name)
            if not with_background:
                signature_only = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
                signature_only.paste(self.image, (0, 0), self.image)
                signature_only.save(file_path)
            else:
                self.image.save(file_path)
            print(f"Signature saved as {file_path}")
            self.file_counter += 1
        else:
            print("No save path selected")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGBA", (self.canvas.winfo_width(), self.canvas.winfo_height()), (32, 32, 32, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.last_x, self.last_y = None, None

if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()
