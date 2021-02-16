import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py-avataaars',
    version='1.1.2',
    license='MIT',
    description='Python Avatar generator library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Krzysztof Ebert',
    author_email='krzysztof.ebert@gmail.com',
    url='https://github.com/kebu/py-avataaars',
    keywords=['Python', 'Avatar', 'Avataaars', 'SVG', 'PNG', 'Generator', 'Library', 'Graphic', 'Face', 'Vector'],
    python_requires=">=3.6",
    install_requires=[
        "cairosvg >= 2.3.0",
        'jinja2 >= 2.9.3',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    include_package_data=True,
    package_data={
        setuptools.find_packages()[0]: ['templates/*.svg', 'templates/**/*.svg', 'templates/**/**/*.svg']
    },
)
