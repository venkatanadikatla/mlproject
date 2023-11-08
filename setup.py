from  setuptools import find_packages, setup
from typing import List
# find_packages  will automaticaly find all the (cont below)
# packages in the ml application in the directory that we have  actually  created

# Creating constant variable
HYPEN_E_DOT = '-e .'
#Below function  can be considered as a metadata information of  this entire project

def get_requirements(file_path: str)-> List[str]:
    """
    this function will return  the  list of requirements
    """
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '')for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    
    name = 'mlproject',
    version='0.0.1',
    author = 'Venkat',
    author_email ='nvenkatavijay@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
    )