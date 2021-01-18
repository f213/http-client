from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_name }}',
    use_scm_version=True,
    description='{{ cookiecutter.project_slug }} -- fancy new client for some fancy new integration',
    keywords=[],
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    license='{{ cookiecutter.license }}',
    packages=find_packages(),
    install_requires=[
        'httpx',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    include_package_data=True,
    zip_safe=False,
)
