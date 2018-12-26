import os

from conans import ConanFile, CMake, tools


SOURCE_FOLDER = 'src'


class EmbedresourceConan(ConanFile):
    name = "embed-resource"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "https://github.com/lawrencem99/embed-resource.git"
    description = "<Description of Embedresource here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "arch"
    generators = "cmake"
    scm = {
        "type": "git",
        "url": "https://github.com/lawrencem99/embed-resource.git",
        "revision": 'master',
        "subfolder": SOURCE_FOLDER,
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=SOURCE_FOLDER)
        cmake.build()

    def package(self):
        self.copy("Resource.h", dst="include", src=SOURCE_FOLDER)
        self.copy("embed-resource", dst="bin", keep_path=False)
        self.copy("embed-resource.exe", dst="bin", keep_path=False)
        self.copy('embed-resource.cmake', dst='cmake', src=SOURCE_FOLDER)

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, 'bin'))
