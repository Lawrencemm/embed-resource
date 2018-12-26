cmake_minimum_required(VERSION 3.5)
project(EmbedResource)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED YES)

add_executable(embed-resource embedresource-cpp-11.cpp Resource.h)
