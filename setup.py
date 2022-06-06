import setuptools

setuptools.setup(
    name="my_first_dagster_app",
    packages=setuptools.find_packages(exclude=["my_first_dagster_app_tests"]),
    install_requires=[
        "dagster==0.14.19",
        "dagit==0.14.19",
        "pytest",
    ],
)
