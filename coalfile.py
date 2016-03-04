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
        cp('build/include', 'include')
        cp('build/*.a', 'libs/')
        cp('build/*.lib', 'libs/')
    def info(self, generator):
        generator.add_library("-lglad")
        generator.add_link_dir('libs/')
        generator.add_include_dir('include/')
