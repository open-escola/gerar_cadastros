"""
Pastas
dez.22
"""


from pathlib import Path


project_path = Path('.').absolute().parent


# Data
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
