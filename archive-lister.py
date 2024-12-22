import zipfile
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import py7zr
import rarfile

class ArchiveContentLister:
    def __init__(self, root):
        self.root = root
        self.root.title("Archive Content Lister")
        self.root.geometry("600x400")
        
        # Create output directory if it doesn't exist
        self.output_dir = Path('output')
        self.output_dir.mkdir(exist_ok=True)

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # File selection frame
        select_frame = ttk.Frame(self.root, padding="10")
        select_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.file_path = tk.StringVar()
        ttk.Label(select_frame, text="Archive File:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(select_frame, textvariable=self.file_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(select_frame, text="Browse", command=self.browse_file).grid(row=0, column=2)

        # Output information
        output_frame = ttk.Frame(self.root, padding="10")
        output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        ttk.Label(output_frame, text="Output Directory:").grid(row=0, column=0, sticky=tk.W)
        self.output_label = ttk.Label(output_frame, text=str(self.output_dir.absolute()))
        self.output_label.grid(row=0, column=1, sticky=tk.W)

        # Process button
        ttk.Button(self.root, text="Process Archive File", command=self.process_zip).grid(row=2, column=0, pady=10)

        # Status display
        self.status_var = tk.StringVar()
        ttk.Label(self.root, textvariable=self.status_var).grid(row=3, column=0, pady=10)

    def browse_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[
                ("Archive files", "*.zip;*.7z;*.rar"),
                ("ZIP files", "*.zip"),
                ("7Z files", "*.7z"),
                ("RAR files", "*.rar"),
                ("All files", "*.*")
            ]
        )
        if filename:
            self.file_path.set(filename)

    def list_archive_contents(self, archive_path):
        extension = Path(archive_path).suffix.lower()
        files = []
        
        if extension == '.zip':
            with zipfile.ZipFile(archive_path, 'r') as archive:
                files = archive.namelist()
        elif extension == '.7z':
            with py7zr.SevenZipFile(archive_path, 'r') as archive:
                files = archive.getnames()
        elif extension == '.rar':
            with rarfile.RarFile(archive_path, 'r') as archive:
                files = archive.namelist()
        else:
            raise ValueError(f"Unsupported archive format: {extension}")
        
        return files

    def process_zip(self):
        archive_path = self.file_path.get()
        if not archive_path:
            messagebox.showerror("Error", "Please select an archive file first")
            return

        try:
            archive_name = Path(archive_path).name
            output_path = self.output_dir / f"{archive_name}.txt"
            
            file_list = self.list_archive_contents(archive_path)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                for filename in file_list:
                    f.write(filename + '\n')
            
            self.status_var.set(f"Success! Listed {len(file_list)} files to {output_path}")
            
        except (zipfile.BadZipFile, py7zr.Bad7zFile, rarfile.BadRarFile):
            self.status_var.set("Error: The file is not a valid archive file")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = ArchiveContentLister(root)
    root.mainloop()

if __name__ == "__main__":
    main()