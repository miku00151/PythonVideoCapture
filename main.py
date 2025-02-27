import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import numpy as np
from pygrabber.dshow_graph import FilterGraph

class CaptureCardViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Capture Viewer")

        # Get video capture device here.
        self.graph = FilterGraph()
        self.devices = self.graph.get_input_devices()

        # resolution opinions 
        self.resolutions = {
            "640x360 (16:9)": (640, 360),
            "1280x720 (16:9)": (1280, 720),
            "1920x1080 (16:9)": (1920, 1080)
        }

        # FPS
        self.fps_options = [15, 30, 60]

        # UI
        self.device_label = tk.Label(root, text="Video Capture:")
        self.device_label.pack()

        self.device_combobox = ttk.Combobox(root, values=self.devices)
        self.device_combobox.pack()

        # Resolution
        self.resolution_label = tk.Label(root, text="Resolution:")
        self.resolution_label.pack()
        self.resolution_combobox = ttk.Combobox(root, values=list(self.resolutions.keys()))
        self.resolution_combobox.current(1)  # Default resolution is 1280x720.
        self.resolution_combobox.pack()

        # 選擇 FPS
        self.fps_label = tk.Label(root, text="FPS:")
        self.fps_label.pack()
        self.fps_combobox = ttk.Combobox(root, values=self.fps_options)
        self.fps_combobox.current(1)  # Default FPS is 30.
        self.fps_combobox.pack()


        self.start_button = tk.Button(root, text="Start View", command=self.start_capture)
        self.start_button.pack()

    def start_capture(self):
        selected_index = self.device_combobox.current()
        if selected_index == -1:
            return
        
        # Get selected resolution and FPS.
        selected_fps = int(self.fps_combobox.get())
        selected_resolution = self.resolution_combobox.get()
        width, height = self.resolutions[selected_resolution]

        self.capture_window = tk.Toplevel(self.root)
        self.capture_window.title("View Window")
        self.capture_window.resizable(False,False)

        self.video_label = tk.Label(self.capture_window)
        self.video_label.pack()

        self.cap = cv2.VideoCapture(selected_index)  # Start video capture view
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, selected_fps)

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        # selected_resolution = self.resolution_combobox.get()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # frame = cv2.resize(frame, self.resolutions[selected_resolution])
            image = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=image)
            self.video_label.imgtk = imgtk
            self.video_label.config(image=imgtk)

        self.capture_window.after(10, self.update_frame)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("640x360")
    app = CaptureCardViewer(root)
    root.mainloop()
