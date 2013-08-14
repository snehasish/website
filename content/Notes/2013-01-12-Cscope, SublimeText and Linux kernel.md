Title: SublimeText and the Linux kernel
Date: 2013-01-12 
Tags: sublime text, linux, kernel, cscope, plugin
Slug: sublime-text-and-linux-kernel
Author: Snehasish
Summary: 

In the kernel source root directory, we will create a list of files we want cscope to index. We are going to be looking at only the i386 architecture files and leave out the rest. Assuming cscope is installed and present in the path.

1. Ensure that the source tree is clean, and then generate a list of files to be indexed

		make clean
		find  .                                                                	\
			-path "./arch/*" ! -path "./arch/i386*" -prune -o               	\
			-path "./include/asm-*" ! -path "./include/asm-i386*" -prune -o 	\
			-path "./tmp*" -prune -o                                           	\
			-path "./Documentation*" -prune -o                                 	\
			-path "./scripts*" -prune -o                                       	\
			-path "./drivers*" -prune -o                                       	\
		        -name "*.[chxsS]" -print > cscope.files

2. Create the cscope index using 

		cscope -b -q -k 

3. Invoke the interactive browser with

		cscope -d

	Or use it from the command line as ( also refer manpage )

		cscope -dL -Xpattern 
		# Where X can be one of:
		# 0 ==> C symbol
		# 1 ==> function definition
		# 2 ==> functions called by this function
		# 3 ==> functions calling this function
		# 4 ==> text string
		# 5 ==> egrep pattern
		# 6 ==> files #including this file