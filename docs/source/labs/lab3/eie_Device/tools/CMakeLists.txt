add_executable(eieDevice main.c)

target_link_libraries(eieDevice ${LIB_NAME})

install(
  TARGETS eieDevice
  RUNTIME DESTINATION bin
)
