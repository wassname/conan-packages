from conans import ConanFile, CMake, tools
import shutil
import os
from conans.tools import download, unzip
from conans import AutoToolsBuildEnvironment


class freeglutConan(ConanFile):
    name = "freeglut"
    generators = "cmake"
    settings =  "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url = "http://github.com/Av3m/conan-repo"

    def source(self):
        self.run("git clone https://github.com/dcnieho/FreeGLUT.git")
        self.run("git checkout FG_%s" %( self.version ), cwd="FreeGLUT")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "install"
        cmake.configure(source_dir="FreeGLUT", build_dir=".")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*", dst=".", src="install")
        self.copy("*", dst="cmake", src="install/share/freeglut/cmake")

    def package_info(self):
        self.cpp_info.includedirs = [ os.path.join("include","GL") ]

