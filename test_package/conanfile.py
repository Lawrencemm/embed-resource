import os

from conans import ConanFile, CMake, tools


class EmbedresourceTestConan(ConanFile):
    settings = "os", "arch"
    generators = "cmake", 'virtualenv'

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        activate_command = (
            'activate.bat' if self.settings.os == 'Windows' else
            '. ./activate.sh'
        )
        self.run(activate_command)
        cmake.build()

    def imports(self):
        self.copy("embed-resource", src="bin")
        self.copy("embed-resource.exe*", src="bin")
        self.copy('embed-resource.cmake', dst='scripts', src='cmake')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%sexample" % os.sep)
