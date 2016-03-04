from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class BulletFile(CoalFile):
    url = "https://github.com/bulletphysics/bullet3.git"
    exports = ["include", "libs"]
    def prepare(self):
        git_clone(self.url, 'master', 'src')
    def build(self):
        default_cmake_build('src/', 'build/')
    def package(self):
        cp('src/src', 'include') # TODO: just copy header files
        cp('build/lib/*', 'libs/')
        cp('build/src/Bullet3Common/*.a', 'libs/')
        cp('build/src/BulletSoftBody/*.a', 'libs/')
        cp('build/src/BulletDynamics/*.a', 'libs/')
        cp('build/src/BulletCollision/*.a', 'libs/')
        cp('build/src/LinearMath/*.a', 'libs/')
    def info(self, generator):
        generator.add_library("-lBullet3Common -lBulletSoftBody -lBulletDynamics -lBulletCollision -lLinearMath")
        generator.add_link_dir('libs/')
        generator.add_include_dir('include/')
