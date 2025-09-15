!#/bin/bash
# Python
echo ">> Run Python"
python py_src/main.py

# Rust
echo ">> Build and run Rust"
cargo run

# Cpp
echo ">> Build Cpp"
g++ cp_src/main.cpp cp_src/lib.cpp -o cp_src/main

echo "  >> Run Cpp"
./cp_src/main
