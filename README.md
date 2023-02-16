## How to run

0. Install GCC (tested on 12.2.0) and pyvideoreader (`pip3 install pyvideoreader`)
1. Enter target terminal size to terminal_size.txt
2. Run:
```
python preprocess.py
python generate_cpp.py
```
4. Run with buffering so that animation plays with original 30fps
```sh
g++ sources/badapple_*.cpp |& python buffer.py
```
5. Or just play (this doesn't keep up speed and passes very fast)
```sh
g++ sources/badapple_*.cpp
```