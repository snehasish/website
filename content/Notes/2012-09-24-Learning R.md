Title: Learning R
Date: 2012-09-24 
Tags: R, programming, statistics, coursera
Slug: learning-r
Author: Snehasish
Summary: The Computing for Data Analysis course on Coursera

I've spent almost the entire time as Master's student wrestling with different plotting tools and wondering about how best to visualise the data I collect, and working in the field of *Computer Architecture* means that there is a lot of data to analyse. I've finally decided to rectify this wrong and learn *R*. "*R* is a free software environment for statistical computing and graphics" ([Homepage](http://www.r-project.org/ "The R Project")). [Coursera](https://www.coursera.org/ "Coursera Homepage") is offering a month-long course on *R* called [Computing for Data Analysis](https://www.coursera.org/course/compdata), taught by Dr. Roger D. Peng who is an Associate Professor of Biostatistics at the Johns Hopkins Bloomberg School of Public Health and a Co-Editor of the [Simply Statistics blog](http://simplystatistics.org/). The course is structured based on the Mac and Windows distributions of R. I've decided to stick to Linux (Ubuntu 12.04). I have listed the Linux equivalents of any platform specific issues I come across.

### Installing R and R-Studio on Ubuntu 12.04

To install *R* on Ubuntu using from your repository using apt-get, type the following into a terminal screen

	gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9
	gpg -a --export E084DAB9 | sudo apt-key add -

Add the mirror to your apt/sources.list file using

	echo "deb http://cran.stat.sfu.ca/bin/linux/ubuntu precise/" | sudo tee -a /etc/apt/sources.list

You can using a different mirror depending on your location/preference. Install the R packages with the following commands

	sudo apt-get update
	sudo apt-get install r-base

You can now go ahead and [download R Studio](http://rstudio.org/download/desktop). Download the corresponding debian package (.deb) file for your architecture. Try installing the package using the command

	sudo dpkg -i rstudio-0.96.331-amd64.deb 

You might get an error similar to what I saw, depending on which packages are missing ( R Studio depends on a lot of Qt packages which you may not have installed)

	Selecting previously unselected package rstudio.
	(Reading database ... 164510 files and directories currently installed.)
	Unpacking rstudio (from rstudio-0.96.331-amd64.deb) ...
	dpkg: dependency problems prevent configuration of rstudio:
	 rstudio depends on libjpeg62; however:
	  Package libjpeg62 is not installed.
	dpkg: error processing rstudio (--install):
	 dependency problems - leaving unconfigured

So I went ahead and installed the missing package

	sudo apt-get install libjpeg62

And now we have R Studio ready. If for some reason that doesn't work for you check out the Cran [Ubuntu Readme](http://cran.r-project.org/bin/linux/ubuntu/README.html). 

### R Basics

1. Bash style comments with #
2. Everything is an object and by default variables are vectors of objects.
3. Primitives are called *Atomic* objects:
	1. Numeric
	2. Char
	3. Integer 
	4. Complex
	5. Logical
4. Vectors contain only a single type of object
5. Lists are special vectors which can contain multiple types of objects
6. Assignment operator is `<-`
7. Operator `:` to create sequences (Similar to Matlab, but does not take 3 args)
8. `c(...)` - Create vector from args. Also concat vectors of same type
9. `vector(type,length)` - Create vector with default value using arguments
10. *Type coercion* when `c(...)` used with non matching types - Silent - Watchout!
11. Explicit coercion using function as.*type*. E.g. - `as.numeric("a")`
12. `class(...)` - returns type information for arg.
13. `NaN` - Not a Number , `Inf` - Infinity , `NA` - Not Available
14. `is.na()` to check for `NA` and `is.nan()` to check for `NAN`
15. `factor(c(...)[, levels=c(...)])` creates a vector which I feel best descibed as *auto enumeration*, further more levels can be explicitly enumerated, this is useful for specifying baseline levels as some functions pick up the first level as the baseline.
16. `table(...)` returns the frequency count
17. R objects can have names. E.g. `names(x) <- c("a","b","c")` 
18. `??string` in R Studio will search the documentation for `string` and return relevant results 
19. `str(...)` returns info about the object

### Matrices in R

1. `matrix(nrow,ncol)` - Creates a matrix of NA with specified dimensions
2. `dim(...)` - Returns the dimensions of the matrix
3. `attributes(...)` - Shows attributes including dimension
4. Sequence can be used to create matrix. `matrix(1:n,nrow,ncol)` creates nrowXncol matrix with the elements of the sequence in column-major order
5. Forcing a matrix dimension on a vector will create a matrix. E.g. - `dim(m) <- c(2,3)`
6. `cbind(...)` and `rbind(...)` are R equivalents of `vertcat` and `horzcat` in Matlab 
7. `nrow(...)` for number of rows and `ncol(...)` for number of columns
8. Matrix dimensions can have names. Use `dimnames(x) <- list(c(...),c(...))`

### Data Frames

1. Special data structure to deal with tabular data
2. Each column is a vector of objects. (Thus each column should have objects of same type)
3. Unlike matrices, different columns can have different types of objects
4. Create a dummy data frame using `x <- data.frame(col1=1:5,col2=c(T,F,F,F,F))`. `col1` and `col2` are the names of the columns and can be accessed by the `row.names` attribute
5. Data frames are usually created using `read.table()` or `read.csv()`

### Subsetting and Vector Operations

1. Operator `[index]` returns subset of same type, here index itself can be range or a vector
2. Operator `[["name"]]` returns object, can also be used to retrieve objects by index, cannot be used to extract multiple elements, tries an exact match for `name` by default (this behaviour can be modified by setting `exact=FALSE`)
3. Operator `$` returns object by name, also does partial matching of the name to lookup
4. Subsetting works on matrices as well, however `[,drop=FALSE]` needs to be specified in order to ensure that return is a matrix and not a vector. Indices can also be missing which would mean fetch the entire range. E.g. `mat[,2]`
5. `complete.cases(...)` returns a vector of `TRUE/FALSE` where all indices of args are not `NA`
6. Subset chaining is possible. E.g. `x[1:10][1:5]` where x is a 1-dimensional vector
7. Normal operators are applied to vector *per element*, matrix operations are performed by enclosing with %. E.g. `x %*% y`
8. `subset(x, <logical vector>)` returns the subset using the logical vector.

### Read/Writing Data

1. `read.table(...)` returns data frame, see docs for args, `read.csv(...)` is similar except the default separator is a comma
2. `read.table(...)` can get out of hand for very large data sets. Also object metadata overhead increases memory consumption to ~2X.
3. R also detects the type of each element whilst loading, if `colClasses` are specified then a noticable speedup can be attained. Here is a way of quickly picking up the correct classes:

		initial <- read.table("data.txt",nrows=100)
		classes <- sapply(initial, class)
		full    <- read.table("data.txt", colClasses=classes)

### Environment

The course describes usage on Mac and Windows. Here I will be documenting the Linux equivalents using R Studio. 

1. Set working director is found under `Tools > Set Working Directory > Choose Working Directory (Ctrl+Shift+K)` in R Studio. Alternatively use command `setwd(...)`
2. `dir()` gets contents of current working directory and `ls()` get contents of workspace (functions and objects loaded in the workspace like Matlab)
3. R scripts are saved with .R extension and functions syntax looks like this

		funtion_name <- function(args) {
			# Code
		}
4. `source`'ing the file will load the functions into the workspace