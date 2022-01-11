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

setup(
    author='{AUTHOR}',
    author_email='{AUTHOR_EMAIL}',
    description=description,
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='{MODULE_DASHED}',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=('octodns>=0.9.14', 'TODO: other requirements'),
    url='https://github.com/octodns/{MODULE_DASHED}',
    version=version(),
    tests_require=[
        'mock>=4.0.3',
        'nose',
        'nose-no-network',
        'TODO: other test-time requirements'
    ],
)
