from setuptools import setup, find_packages

setup(
    name='propano',  # Must be unique on PyPI
    version='0.1.0',  # Increment for new releases
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'prophet',
        'matplotlib',
        'plotly'  # Required for interactive visualization
    ],
    entry_points={
        'console_scripts': [
            'propano=propano.cli:main',  # Update CLI entry point
        ],
    },
    author='Vinayak Bhat',
    author_email='vinayak.sjcebhat@gmail.com',
    description='A Prophet-based network anomaly detection package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/yourusername/prophet-net-anomaly',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.7',
)
