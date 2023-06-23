from setuptools import find_packages, setup

setup(
    name="stable_diffusion_tf",
    version="0.1",
    description="Stable Diffusion in Tensorflow / Keras",
    author="Baris Aydin",
    author_email="dev.barisaydin@gmail.com",
    platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
    url="https://github.com/dev-baris/ai-stable-diffusion-tensorflow",
    packages=find_packages(),
)
