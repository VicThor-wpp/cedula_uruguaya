from setuptools import setup, find_packages

setup(
    name='cedula_uruguaya',
    version='0.1.0',
    packages=find_packages(),
    description='Gestión de cédulas uruguayas con validación de dígitos verificadores',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='SoyVA3',
    author_email='victor.aragon@vmlyr.com',
    url='https://github.com/VicThor-wpp/cedula_uruguaya',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'random',  # Incluye aquí las dependencias necesarias
    ]
)