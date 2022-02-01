from setuptools import find_packages, setup


def descriptions():
    with open('README.md') as fh:
        ret = fh.read()
        first = ret.split('\n', 1)[0].replace('#', '')
        return first, ret


def version():
    with open('{MODULE}/__init__.py') as fh:
        for line in fh:
            if line.startswith('__VERSION__'):
                return line.split("'")[1]


description, long_description = descriptions()

tests_require = (
    'pytest',
    'pytest-network',
    # TODO: other test-time requirements
)

setup(
    author='{AUTHOR}',
    author_email='{AUTHOR_EMAIL}',
    description=description,
    extras_require={
        'dev': tests_require + (
            'build>=0.7.0',
            'pycodestyle>=2.6.0',
            'pyflakes>=2.2.0',
            'readme_renderer[md]>=26.0',
            'twine>=3.4.2',
        ),
    },
    install_requires=(
        'octodns>=0.9.14',
        # TODO: other requirements
    ),
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='{MODULE_DASHED}',
    packages=find_packages(),
    python_requires='>=3.6',
    tests_require=tests_require,
    url='https://github.com/octodns/{MODULE_DASHED}',
    version=version(),
)
