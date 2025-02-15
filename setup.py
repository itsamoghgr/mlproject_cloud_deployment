from setuptools import find_packages, setup



setup(
    name = 'mlp_cloud',
    version='0.0.1',
    author = 'Amogh Ramagiri',
    author_email = 'amoghgr64@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)
