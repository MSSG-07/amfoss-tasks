cmake_minimum_required(VERSION 3.10)
project(ShaderProject)

set(CMAKE_CXX_STANDARD 17)

# Specify the location of Vulkan SDK
set(Vulkan_INCLUDE_DIR /path/to/vulkan-sdk/include)
set(Vulkan_LIBRARY /path/to/vulkan-sdk/libvulkan.so)

include_directories(${Vulkan_INCLUDE_DIR})
include_directories(${CMAKE_SOURCE_DIR}/third_party)


# Add source files
add_executable(ShaderProject src/main.cpp)

# Link Vulkan library
target_link_libraries(ShaderProject ${Vulkan_LIBRARY})
