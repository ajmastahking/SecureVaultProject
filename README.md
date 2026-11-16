# README.MD is also included in the folder #

# SecureVault Beginner

A beginner-friendly, command-line password manager school project built with Python.

> **For learning only:** Passwords are saved as readable text in `passwords.json`. Do not store real passwords or personal credentials.

## Features

- Add an account with a username and password
- View saved accounts
- Search for an account by name
- Delete an account after confirmation
- Save and load data with JSON

## Requirements

- Python 3.9 or newer
- Visual Studio Code (recommended)
- No extra Python packages

## Run in VS Code (Windows)

1. Extract the ZIP file.
2. Open VS Code and choose **File > Open Folder**. Select `SecureVault_Beginner`.
3. Open **Terminal > New Terminal**.
4. Run:

   ```powershell
   py main.py
   ```

   If `py` isn't available, try `python main.py`.

The program creates `passwords.json` when you save your first account.

## Menu

```text
=== SecureVault Beginner ===
1. Add account
2. View accounts
3. Search account
4. Delete account
5. Exit
Choose 1-5:
```

## Files

- `main.py` — all program code
- `requirements.txt` — no third-party dependencies
- `.gitignore` — keeps saved credentials and local environments out of Git
- `passwords.json` — generated locally after adding an account

## Python concepts

- `input()` and `print()` for a CLI
- `while` loops for the menu
- `if` / `elif` / `else` for choices
- Functions for organizing tasks
- Dictionaries for storing accounts
- JSON for saving data between runs
- Basic error handling when loading files

## Example

Choose `1`, enter an account name such as `DemoWebsite`, username `student123`, and a fake password such as `example123`. Choose `2` to view it, `3` to search, or `4` to delete.

## Limitations and future improvements

This project does not encrypt passwords or use a master password. A future version could add secure encryption and password generation. It is not intended for storing actual credentials.
