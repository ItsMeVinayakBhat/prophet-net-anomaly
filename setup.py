from setuptools import setup, find_packages

setup(
    name='prophet-net-anomaly',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['pandas', 'numpy', 'prophet', 'matplotlib'],
    author='Your Name',
    description='A Prophet-based network anomaly detection package',
    license='MIT',
    url='https://github.com/yourusername/prophet-net-anomaly',
)
