import cx_Freeze

executables = [cx_Freeze.Executable(
    script="spongebob.py", icon="bobicon.ico")]

cx_Freeze.setup(
    name="BOB ESPONJA CALÇA QUADRADA",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables = executables
)

