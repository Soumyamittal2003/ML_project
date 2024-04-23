from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnet
    '''

    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        [req.replace("\n","")for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
            
    return requirement


setup(
name='mlproject',
version='0.0.1',
author='soumya mittal',
author_email='soumyamittalrgh@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirement.txt')

)