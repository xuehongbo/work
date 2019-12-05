from setuptools import setup, find_packages

setup(
    name='str_to_dict_tool',
    version='0.0.2',
    keywords='str to dict',
    description='a str to dict tool',
    license='MIT License',
    url='https://github.com/xuehongbo/work',
    author='HongBo Xue',
    author_email='505386086@qq.com',
    packages=find_packages(where="caafinder"),
    package_dir={'': 'caafinder'},
    include_package_data=True,
    platforms='any',
    install_requires=[],
)
