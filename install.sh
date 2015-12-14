#!/bin/sh

#  install.sh
#  
#
#  Created by Flint Ory on 12/13/15.
#

#!/bin/bash

NODE_VERSION=4.2.3
NPM_VERSION=2.14.4

# Save script's current directory
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#cd "${DIR}"

#
# Check if Homebrew is installed
#
which -s brew
if [[ $? != 0 ]] ; then
# Install Homebrew
echo "**** Installing Homebrew ****"
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
else
echo "**** Updating Homebrew ****"
brew update
fi

#
# Check if Git is installed
#
echo "**** Checking for git and installing if necessary ****"
which -s git || brew install git

#
# Check if Node is installed and at the right version
#
echo "Checking for Node version ${NODE_VERSION}"
node --version | grep ${NODE_VERSION}
if [[ $? != 0 ]] ; then
# Install Node
cd `brew --prefix`
$(brew versions node | grep ${NODE_VERSION} | cut -c 16- -)
echo "**** Installing Node ****"
brew install node
fi

#
# Check if Node Package Manager is installed and at the right version
#
#echo "Checking for NPM version ${NPM_VERION}"
#npm --version | grep ${NPM_VERSION}
#if [[ $? != 0 ]] ; then
#echo "Downloading npm"
#git clone git://github.com/isaacs/npm.git && cd npm
#git checkout v${NPM_VERSION}
#make install
#fi

#
# Ensure NODE_PATH is set
#
#grep NODE_PATH ~/.bash_profile > /dev/null || cat "export NODE_PATH=/usr/local/lib/node_modules" >> ~/.bash_profile && . ~/.bash_profile

#
# Check if python is installed
#
echo "Checking for Python and installing if necessary"
which -s python
if [[ $? != 0 ]] ; then
# Install Python
brew install python
fi

