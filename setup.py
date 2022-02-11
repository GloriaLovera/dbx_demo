from setuptools import find_packages, setup
from dbx_ci_cd_demo import __version__

setup(
    name="dbx_ci_cd_demo",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
