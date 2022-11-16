import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("pw/VERSION", "r") as f:
    version = f.read()

setuptools.setup(
    name="pw",
    version=version,
    author="alphabet5",
    author_email="johnburt.jab@gmail.com",
    description="Copy credentials.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alphabet5/pw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    entry_points={"console_scripts": ["c=pw.pw:c",
                                        "p=pw.pw:p",
                                        "u=pw.pw:u",
                                        "o=pw.pw:o"]},
    include_package_data=True,
    package_data={
        "pw": ["*"],
    },
    install_requires=["rich", "keyring"],
)
