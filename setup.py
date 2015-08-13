from setuptools import setup, find_packages


setup(
    name="devpi-remote_user",
    description=open('README').read(),
    version='0.1',
    author="Autolib' dev team",
    author_email="autolib-dev@polyconseil.fr",
    url="https://github.com/Polyconseil/devpi-remote_user",
    license="MIT",
    keywords="devpi plugin",
    entry_points={
        'devpi_server': [
            "devpi-remote_user = devpi_remote_user.main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
)
