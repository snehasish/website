Title: Building and Testing GCC 4.7.2
Date: 2013-01-11 
Tags: gcc, build, test
Slug: building-and-testing-gcc-4.7.2
Author: Snehasish
Summary: Building and testing GCC 4.7.2 on Ubuntu 12.04

Steps to build GCC 4.7.2 from source on Ubuntu 12.04 (64 bit). GCC ( GNU Compiler Collection) contains compilers for many languages, here we will only be compiling it for C and C++.

1. Grab a tarball of the release from one of the [mirrors](http://gcc.gnu.org/mirrors.html).
		
		cd ~/Downloads
		wget http://gcc.parentingamerica.com/releases/gcc-4.7.2/gcc-4.7.2.tar.bz2

2. Extract the tarball

		tar jxvf gcc-4.7.2.tar.bz2

3. Install the prerequisite packages

		sudo apt-get install libgmp-dev  \
							 libmpfr-dev \
							 libmpc-dev  \
							 m4 \
							 libc6-dev-i386

	Add a link to the standard location for x86_64-linux-gnu
		
		sudo ln -s /usr/lib/x86_64-linux-gnu /usr/lib64

4. Create a directory to build in your home directory

		mkdir ~/gcc-4.7.2-build
		cd ~/gcc-4.7.2-build

5. Run configure with the given options. This will set the installation dir for gcc-4.7.2 to ~/gcc-4.7.2

		$HOME/Downloads/gcc-4.7.2/configure --build=x86_64-linux-gnu --prefix=$HOME/gcc-4.7.2 --enable-languages=c,c++ --disable-multilib --program-suffix=-4.7

6. Make! ( in parallel, with number of threads set to the number of processors on your system)

		grep processor /proc/cpuinfo | wc -l | xargs make -j

7. Next install dejagnu

		sudo apt-get install dejagnu autogen

8. Run the testsuite from the current directory, the k flag ensures that errors do not halt the process. Errors will occur as we only build a subset of the languages available

		make -k check # Check all the things!
		make -k check-c++ # Check only g++

9. Install the binaries into the folder specified using

		make install

10. Add the binaries to your path by adding the following lines into your .bashrc

		gedit $HOME/.bashrc
		export PATH=$HOME/gcc-4.7.2/bin:$PATH
		export LD_LIBRARY_PATH=$HOME/gcc-4.7.2/lib:$HOME/gcc-4.7.2/lib64:$LD_LIBRARY_PATH

	Source the file

		. $HOME/.bashrc

11. You can now check to see if our binaries are in the path

		g++-4.7 --version

	Expected output

		g++-4.7 (GCC) 4.7.2
		Copyright (C) 2012 Free Software Foundation, Inc.
		This is free software; see the source for copying conditions.  There is NO
		warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

We can now go ahead and use all the new features present in g++ for the new c++0x standard.






