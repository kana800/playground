# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\sliderapp_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\sliderapp_autogen.dir\\ParseCache.txt"
  "sliderapp_autogen"
  )
endif()
