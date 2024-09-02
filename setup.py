from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'sbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share' , package_name , 'description'), glob('description/*.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akshay',
    maintainer_email='aakshay1114@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sbot_bullet = sbot.sbot_bullet:main'
        ],
    },
)
