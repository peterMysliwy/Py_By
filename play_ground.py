import os

# Set environment variables
"""
os.environ['PYSIDE_DESIGNER_PLUGINS'] = '/Users/petermysliwy/Desktop/pythonProject1/PyQt5-Video-Book-main/lib/python3.11/site-packages/PySide6/examples/designer/taskmenuextension/'
os.environ['API_PASSWORD'] = 'secret'
os.environ.setdefault('USER_2', 'True')
"""
# os.environ.setdefault('PYSIDE_DESIGNER_PLUGINS', '/Users/petermysliwy/Desktop/pythonProject1/PyQt5-Video-Book-main/lib/python3.11/site-packages/PySide6/examples/designer/taskmenuextension:')
# open -a "textedit" .bash_profile  -> location /Users/petermysliwy
# TERMINAL
# set a temporary variableecho
# export PYSIDE_DESIGNER_PLUGINS=/Users/petermysliwy/Desktop/pythonProject1/PyQt5-Video-Book-main/lib/python3.11/site-packages/PySide6/examples/designer/taskmenuextension:$PYSIDE_DESIGNER_PLUGINS
# echo $[variable name] -> echo $PYSIDE_DESIGNER_PLUGINS
# unset [variable_name]

# os.environ.setdefault('PYSIDE_DESIGNER_PLUGINS', '')
USER = os.getenv('PYSIDE_DESIGNER_PLUGINS')
# PASSWORD = os.environ.get('USER')

print(f'PYSIDE_DESIGNER_PLUGINS -> {USER}')
# print(os.environ)

for key in os.environ:
    print(f'key: {key} {os.environ[key]}')


