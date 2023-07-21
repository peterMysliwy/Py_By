from pathlib import Path
"""
try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
finally:
    # Some code .....(always executed)
    """

"""
LOGGING
    LEVELS Debug, Info, Warning, Error, Critical
"""
views = {'chart': 'base_uis.UI_chart', 'power supply': 'loaders.Ps_loader', 'click': 'loaders.loadClickMe'}

# current working directory is where the python file that executes the directory function
# STRIP PATH -> remove 1 level from the path structure
current_directory = Path().cwd().parent

# add level to the current path
current_directory = current_directory / 'base_uis'
print(f'current directory -> {current_directory}')

# read all python file names in the directory and assign to names
names = [i.name for i in current_directory.glob('*.py')]
print(f'list of files in: {current_directory.name} -> {names}')

stem_names = []
for i in current_directory.glob('*.py'):
    stem_names.append(i.stem)
print(f'stem -> {stem_names}')

print(views['chart'])

