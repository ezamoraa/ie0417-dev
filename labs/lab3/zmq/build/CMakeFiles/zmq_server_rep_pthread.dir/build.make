# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dev/ws/labs/lab3/zmq

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dev/ws/labs/lab3/zmq/build

# Include any dependencies generated for this target.
include CMakeFiles/zmq_server_rep_pthread.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/zmq_server_rep_pthread.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/zmq_server_rep_pthread.dir/flags.make

CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.o: CMakeFiles/zmq_server_rep_pthread.dir/flags.make
CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.o: ../src/zmq_server_rep_pthread.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/dev/ws/labs/lab3/zmq/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.o   -c /home/dev/ws/labs/lab3/zmq/src/zmq_server_rep_pthread.c

CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/dev/ws/labs/lab3/zmq/src/zmq_server_rep_pthread.c > CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.i

CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/dev/ws/labs/lab3/zmq/src/zmq_server_rep_pthread.c -o CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.s

# Object files for target zmq_server_rep_pthread
zmq_server_rep_pthread_OBJECTS = \
"CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.o"

# External object files for target zmq_server_rep_pthread
zmq_server_rep_pthread_EXTERNAL_OBJECTS =

zmq_server_rep_pthread: CMakeFiles/zmq_server_rep_pthread.dir/src/zmq_server_rep_pthread.c.o
zmq_server_rep_pthread: CMakeFiles/zmq_server_rep_pthread.dir/build.make
zmq_server_rep_pthread: CMakeFiles/zmq_server_rep_pthread.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/dev/ws/labs/lab3/zmq/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable zmq_server_rep_pthread"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/zmq_server_rep_pthread.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/zmq_server_rep_pthread.dir/build: zmq_server_rep_pthread

.PHONY : CMakeFiles/zmq_server_rep_pthread.dir/build

CMakeFiles/zmq_server_rep_pthread.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/zmq_server_rep_pthread.dir/cmake_clean.cmake
.PHONY : CMakeFiles/zmq_server_rep_pthread.dir/clean

CMakeFiles/zmq_server_rep_pthread.dir/depend:
	cd /home/dev/ws/labs/lab3/zmq/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dev/ws/labs/lab3/zmq /home/dev/ws/labs/lab3/zmq /home/dev/ws/labs/lab3/zmq/build /home/dev/ws/labs/lab3/zmq/build /home/dev/ws/labs/lab3/zmq/build/CMakeFiles/zmq_server_rep_pthread.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/zmq_server_rep_pthread.dir/depend

