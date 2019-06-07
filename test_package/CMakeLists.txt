cmake_minimum_required(VERSION 3.8)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include(${CMAKE_BINARY_DIR}/scripts/embed-resource.cmake)

embed_resources(RESOURCES resource.txt)

add_executable(example example.cpp second_definition.cpp ${RESOURCES})
