# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='mysnek',
    version='1.1.0',
    description='my first package',
    platforms='Independant',
    zip_safe=False,
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    py_modules=['snek'],#必要,否则install 后缺少必要模块
    entry_points={'console_scripts':[
                  'snek=snek:main']}
)
