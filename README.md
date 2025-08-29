#task1: File Reading and Error Handling in Python

## 📌 Overview
This Python program demonstrates:
1. Reading the first two lines from a file (`file.txt`).
2. Handling the case when a file does not exist (`sample.txt`) using exception handling.

---

## ⚙️ Features
- **Read Mode (`r+`)**: Opens the file for reading and writing.
- **Read Lines**: Reads the first two lines of a file using `readline()`.
- **Error Handling**: Uses `try-except` to catch `FileNotFoundError` if a file does not exist.


task2:# Write and Append data to file

## 📌 Overview
This project demonstrates basic **file handling operations** in Python:
1. Writing user input to a file (`output.txt` or `file.txt`).
2. Appending additional data to the same file.
3. Reading the file contents.
4. Handling missing files gracefully using exception handling.

The program showcases key Python concepts like file modes, string manipulation, and error handling.

---

## ⚙️ Features
- **Write Mode (`w`)**: Overwrites or creates a new file and writes user input.
- **Append Mode (`a`)**: Adds new text to an existing file without erasing previous content.
- **Read Mode (`r` or `r+`)**: Reads data from the file.
- **Clean Output**: `.strip()` removes extra whitespace and newline characters when printing lines.
