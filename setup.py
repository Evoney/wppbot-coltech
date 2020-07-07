from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pathlib", "urllib3", "queue"],
                     'include_files': ["src/wppbot.py", "src/classes", "src/assets", "src/chromedriver.exe"],
                     "includes": [],
                     "excludes": [],
                    }

# GUI applications require a different base on Windows (the default is for a
# console application).
#base = None
#if sys.platform == "win32":
base = "Win32GUI"

setup(  name = "Chatbot Coltech",
        version = "2.0",
        description = "Chatbot para WhatsApp da Coltech",
        options = {"build_exe": build_exe_options},
        executables = [Executable("src/main.py", base=base)])
