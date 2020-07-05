from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pathlib", "urllib3", "queue"],
                     'include_files': ["wppbot.py", "cliente.py", "menu.png", "quemSomos.png", "Carta de Serviços.pdf", "chromedriver.exe"],
                     "includes": [],
                     "excludes": [],
                    }

# GUI applications require a different base on Windows (the default is for a
# console application).
#base = None
#if sys.platform == "win32":
base = "Win32GUI"

setup(  name = "Chatbot Coltech",
        version = "1.0",
        description = "Chatbot para WhatsApp da Coltech",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])
