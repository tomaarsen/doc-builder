# Doc-builder package setup.
# The line above is checked by some of the utilities in this repo, do not change it.

from setuptools import find_packages, setup

install_requires = ["black", "GitPython", "tqdm", "pyyaml", "packaging", "nbformat", "huggingface_hub"]

extras = {}

extras["transformers"] = ["transformers[dev]"]
extras["testing"] = ["pytest", "pytest-xdist", "torch", "transformers", "tokenizers", "timm", "google-api-python-client", "requests"]
extras["quality"] = ["black~=22.0", "isort>=5.5.4", "flake8>=3.8.3"]

extras["all"] = extras["testing"] + extras["quality"]
extras["dev"] = extras["all"]


setup(
    name="hf-doc-builder",
    version="0.5.0.dev0",
    author="Hugging Face, Inc.",
    author_email="sylvain@huggingface.co",
    description="Doc building utility",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="doc documentation doc-builder huggingface hugging face",
    url="https://github.com/huggingface/doc-builder",
    package_dir={"": "src"},
    packages=find_packages("src"),
    extras_require=extras,
    install_requires=install_requires,
    entry_points={"console_scripts": ["doc-builder=doc_builder.commands.doc_builder_cli:main"]},
)
