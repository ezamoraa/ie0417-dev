if(EXISTS "/home/katharina/Documentos/DiseñoSoftware/ie0417-dev/labs/lab4/c/gtest_demo/build/test/unittest[1]_tests.cmake")
  include("/home/katharina/Documentos/DiseñoSoftware/ie0417-dev/labs/lab4/c/gtest_demo/build/test/unittest[1]_tests.cmake")
else()
  add_test(unittest_NOT_BUILT unittest_NOT_BUILT)
endif()
