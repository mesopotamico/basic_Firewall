from setuptools import setup, find_packages

setup(
    name='firewall_project',  # Name of your project
    version='0.1',            # Version of your project
    packages=find_packages(where="src"),  # Automatically find all packages in src
    package_dir={"": "src"},  # Specify that packages are found in src
    install_requires=[        # Dependencies
        'scapy',
    ],
    entry_points={            # Define the entry point for the command-line tool
        'console_scripts': [
            'firewall=firewall:main',  # Format: 'command=module:function'
        ],
    },
)

