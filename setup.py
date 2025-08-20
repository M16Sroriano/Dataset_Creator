from setuptools import setup, find_packages

def leer_requisitos(ignorar=None):
    ignorar = set(ignorar or [])
    with open("requirements.txt", encoding="utf-16") as f:
        return [line for line in f.read().splitlines() if line not in ignorar]

setup(
    name="mi_proyecto",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    py_modules=[
        "main", "first_step", "second_step", "third_step",
        "fourth_step", "fifth_step", "sixth_step", "tooldata"
    ],
    install_requires=leer_requisitos(ignorar=["-e git+https://github.com/facebookresearch/sam2.git@2b90b9f5ceec907a1c18123530e92e794ad901a4#egg=SAM_2"]),

    entry_points={
        'console_scripts': [
            'segmentedcreator=segmentedcreator.main:main'
        ]
    },
    author="Miguel S. Soriano-Garcia",
    description='Herramienta CLI para procesamiento y segmentación de video',
    python_requires=">=3.8",
)
