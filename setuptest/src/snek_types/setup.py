from setuptools import setup

setup(
    name='cute_snek',
    entry_points={
        'snek_types': [
            'cute = cute_snek:cute_snek',
            'spec = cute_snek:spec_snek'
        ],
    }
)