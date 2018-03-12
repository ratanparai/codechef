#!/bin/bash
# Bash script to build and test bazel project

# check if we wanted to clean the project
echo $1

if [ $1 = "clean" ]
then
    echo "=================================================="
    echo "=                CLEANING                        ="
    echo "=================================================="
    bazel clean
fi


echo "=================================================="
echo "=                BUILDING                        ="
echo "=================================================="

# run bazel build command
bazel build //...

echo "=================================================="
echo "=              RUNNING TESTS                     ="
echo "=================================================="
# run bazel test
bazel test //...