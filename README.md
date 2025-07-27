 📂 File Organizer Script

This is a simple Python script I made to automatically sort files in a folder based on their extensions. If your Downloads folder is a total mess—this script will help clean it up in seconds.

 💡 What it Does

- Checks all the files in a folder
- Finds out their extensions (like `.pdf`, `.jpg`, `.mp3`, etc.)
- Makes a separate folder for each type
- Moves the files into their matching folders

 🧰 What You Need

- Python 3 (with can use any version )
- Just the built-in `os` and `shutil` modules (no extra installations needed)

 ▶️ How to Use It

1. Save the script as `file_organizer.py`
2. Open your terminal or command prompt
3. Run this command:

```bash
python file_organizer.py


Examples
Before:
resume.pdf  photo.png  movie.mp4  code.py  notes.txt

After running the script:
📁 pdf
   └── resume.pdf
📁 png
   └── photo.png
📁 mp4
   └── movie.mp4
📁 py
   └── code.py
📁 txt
   └── notes.txt
