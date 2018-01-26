cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# Version Number
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# Configure header file to pass CMale settings to source
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
)

# Add binary tree to search path for include files so that we
# find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# Add executable
add_executable(Tutorial tutorial.cxx)
