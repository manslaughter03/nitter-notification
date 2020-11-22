from setuptools import setup, find_packages


setup(
    name="nitter",
    version="0.0.1",
    description="Nitter notification tools",
    url="https://github.com/manslaughter03/nitter-notification",
    author="b4nks@protonmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Twitter Tools',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.5',
    packages=find_packages(),
    package_data={'nitter': ['resources/*.png']},
    install_requires=[
        "PyYAML==5.3.1",
        "lxml==4.6.1",
        "requests==2.25.0",
        "sdnotify==0.3.2"
    ]
)
