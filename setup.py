from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="azureChatGPT",
    version="0.0.1",
    description="ChatGPT is a reverse engineering of Azure ChatGPT API",
    url="https://github.com/EvAnhaodong/azureChatGPT",
    author="yehaodong",
    author_email="yehaodong@genomics.cn",
    license="GNU General Public License v2.0",
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    py_modules=["azure"],
    install_requires=[
        "pyyaml",
        "prompt-toolkit",
        "tiktoken>=0.3.0",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    extras_require={
        "WebGPT": ["duckduckgo_search"],
    },
)
