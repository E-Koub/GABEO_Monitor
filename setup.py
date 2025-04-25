from setuptools import setup, find_packages

setup(
    name="DataHive",
    version="0.1",
    description="Description de votre projet",
    author="Eudes-KOUB",
    packages=find_packages(include=[
        'src*', 
        'vendor*'
        'data*'
    ]),
    package_dir={
        '': '.'
    },
    python_requires='>=3.8',
    install_requires=[
        'streamlit>=1.30',
        'pandas>=2.1',
        'numpy>=1.24',
        'plotly>=5.15',
        'scikit-learn>=1.2',
        'matplotlib>=3.6',
        'seaborn>=0.12',
        'folium>=0.14',
        'psycopg2-binary>=2.9',
        'sqlalchemy>=2.0',
        'pyyaml>=6.0',
        'python-dotenv>=1.0',
        'pathlib2',
        'folium',
        'setuptools',
        'streamlit-folium>=0.15.0'
    ],
)