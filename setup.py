from setuptools import setup, find_packages

setup(
		name = "sadpanda",
		version = "0.0.1",
		description = "a basic blockchain datastore and library written entirely in python",
		url = "http://github.com/baallezx/sadpanda",
		author = "Alex Balzer",
		author_email = "zabbal22@gmail.com",
		license = "MIT",
		packages = find_packages("sadpanda"), # ["sadpanda"], # find_packages()
		package_dir={'': 'sadpanda'},
		include_package_data=True,
		zip_safe = False,
    	setup_requires=['pytest-runner'],
    	tests_require=['pytest'],
)
