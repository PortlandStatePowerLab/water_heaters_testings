# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
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
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/water_heaters_testings/dcs

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/water_heaters_testings/dcs/build/debug

# Include any dependencies generated for this target.
include CMakeFiles/sample2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/sample2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/sample2.dir/flags.make

CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.o: CMakeFiles/sample2.dir/flags.make
CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.o: ../../sample2/sample2/UCMImpl.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/water_heaters_testings/dcs/build/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.o -c /home/pi/water_heaters_testings/dcs/sample2/sample2/UCMImpl.cpp

CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/water_heaters_testings/dcs/sample2/sample2/UCMImpl.cpp > CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.i

CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/water_heaters_testings/dcs/sample2/sample2/UCMImpl.cpp -o CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.s

CMakeFiles/sample2.dir/sample2/sample2/main.cpp.o: CMakeFiles/sample2.dir/flags.make
CMakeFiles/sample2.dir/sample2/sample2/main.cpp.o: ../../sample2/sample2/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/water_heaters_testings/dcs/build/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/sample2.dir/sample2/sample2/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/sample2.dir/sample2/sample2/main.cpp.o -c /home/pi/water_heaters_testings/dcs/sample2/sample2/main.cpp

CMakeFiles/sample2.dir/sample2/sample2/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sample2.dir/sample2/sample2/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/water_heaters_testings/dcs/sample2/sample2/main.cpp > CMakeFiles/sample2.dir/sample2/sample2/main.cpp.i

CMakeFiles/sample2.dir/sample2/sample2/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sample2.dir/sample2/sample2/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/water_heaters_testings/dcs/sample2/sample2/main.cpp -o CMakeFiles/sample2.dir/sample2/sample2/main.cpp.s

CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.o: CMakeFiles/sample2.dir/flags.make
CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.o: ../../sample2/sample2/mcp3008.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/water_heaters_testings/dcs/build/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.o -c /home/pi/water_heaters_testings/dcs/sample2/sample2/mcp3008.cpp

CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/water_heaters_testings/dcs/sample2/sample2/mcp3008.cpp > CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.i

CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/water_heaters_testings/dcs/sample2/sample2/mcp3008.cpp -o CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.s

# Object files for target sample2
sample2_OBJECTS = \
"CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.o" \
"CMakeFiles/sample2.dir/sample2/sample2/main.cpp.o" \
"CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.o"

# External object files for target sample2
sample2_EXTERNAL_OBJECTS =

sample2: CMakeFiles/sample2.dir/sample2/sample2/UCMImpl.cpp.o
sample2: CMakeFiles/sample2.dir/sample2/sample2/main.cpp.o
sample2: CMakeFiles/sample2.dir/sample2/sample2/mcp3008.cpp.o
sample2: CMakeFiles/sample2.dir/build.make
sample2: libcea2045.so
sample2: CMakeFiles/sample2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/water_heaters_testings/dcs/build/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable sample2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sample2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/sample2.dir/build: sample2

.PHONY : CMakeFiles/sample2.dir/build

CMakeFiles/sample2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/sample2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/sample2.dir/clean

CMakeFiles/sample2.dir/depend:
	cd /home/pi/water_heaters_testings/dcs/build/debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/water_heaters_testings/dcs /home/pi/water_heaters_testings/dcs /home/pi/water_heaters_testings/dcs/build/debug /home/pi/water_heaters_testings/dcs/build/debug /home/pi/water_heaters_testings/dcs/build/debug/CMakeFiles/sample2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/sample2.dir/depend

