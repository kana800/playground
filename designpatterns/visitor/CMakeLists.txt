cmake_minimum_required(VERSION 3.0.0)
project(visitor VERSION 0.1.0)

include(CTest)
enable_testing()


add_subdirectory(card)

add_executable(${PROJECT_NAME} main.cpp)

set_target_properties(card PROPERTIES LINKER_LANGUAGE CXX)

target_include_directories(${PROJECT_NAME} PUBLIC card)
target_link_directories(${PROJECT_NAME} PRIVATE card)
target_link_libraries(${PROJECT_NAME} card)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
