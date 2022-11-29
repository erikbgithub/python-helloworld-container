from setuptools import setup

setup(
  name="pyhellocont",
  version="1.0",
  description="just to test podman desktop",
  author="Erik Bernoth",
  author_email="erik.bernoth@gmail.com",
  url="https://github.com/erikbgithub/python-helloworld-container",
  py_modules=["app"],
  install_requires=[
    "fastapi>=0.88.0",
    "uvicorn>=0.20.0",
  ],
  provides=[
    "pyhellocont (1.0)",
  ],
)

