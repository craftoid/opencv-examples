

# Getting Started with Python and OpenCV

## Installation on OSX

	# install homebrew
	brew tap homebrew/science
	brew install opencv

	# install virtualenv + co.
	pip install virtualenv
	pip install virtualenvwrapper
	echo 'export PATH=$HOME/bin:$PATH' >> $HOME/.profile
	echo 'source /usr/local/bin/virtualenvwrapper.sh' >> $HOME/.profile
	source $HOME/.profile

	# create a virtualenv for OpenCV
	mkvirtualenv computervision
	pip install numpy matplotlib
	workon computervision
	add2virtualenv /usr/local/lib/python2.7/site-packages
