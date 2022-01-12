import cx_Freeze

executables = [cx_Freeze.Executable("MainGame.py")]

cx_Freeze.setup(
    name="Ping Pong Game",
    options={"build_exe": {"packages": ["pygame"],}},
    executables=executables,
)
