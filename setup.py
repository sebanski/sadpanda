from setuptools import setup, find_packages

setup(
		name = "sadpanda",
		version = "0.0.1",
		description = "a basic blockchain datastore and library written entirely in python",
		url = "http://github.com/sebanski/sadpanda",
		author = "Alex Balzer",
		author_email = "sebanskimiami@gmail.com",
		license = "MIT",
		packages = find_packages(include=["sadpanda", "sadpanda.*"]),
		include_package_data=True,
		zip_safe = False,
		install_requires=[
			'pycrypto',
			'python-snappy',
		],
    	setup_requires=['pytest-runner'],
    	tests_require=['pytest'],
    	classifiers=[
        'Development Status :: Alpha 0.0.1',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Datastore :: Blockchain',
        'Topic :: Software Development :: Libraries :: Python Modules'
		],
)
