import setuptools

setuptools.setup(
    name="RealTimeApp",
    version="1.0.0",
    packages=setuptools.find_packages(),
    description="RealTimeApi",
    entry_points={'console_scripts-hotfix': ['api-util = src.__main__:api_call']}
)
print(setuptools.find_packages())
