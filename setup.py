from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aviation/__init__.py
from aviation import __version__ as version

setup(
	name="aviation",
	version=version,
	description="Aviation",
	author="Ed Harrison",
	author_email="ed@turbinetech.aero",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)