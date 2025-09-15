#!/bin/bash

# Python
if [ "$1" == "py" ];then
    echo ">> Run Python <<"
    python py_src/main.py


# Cpp
elif [ "$1" == "cp" ];then
    echo ">> Build Cpp <<"
    g++ cp_src/main.cpp cp_src/lib.cpp -o cp_src/main

    echo "  >> Run Cpp <<"
    ./cp_src/main

# Rust
elif [ "$1" == "rs" ];then
    echo ">> Build and run Rust <<"
    cargo run

elif [ "$1" == "--all" ];then
    # Python
    echo ">> Run Python <<"
    python py_src/main.py

    # Cpp
    echo ">> Build Cpp <<"
    g++ cp_src/main.cpp cp_src/lib.cpp -o cp_src/main

    echo "  >> Run Cpp <<"
    ./cp_src/main

    # Rust
    echo ">> Build and run Rust <<"
    cargo run

# Exit
else
    echo "CLA not supported"
    exit 0 

fi
