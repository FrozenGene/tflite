# TFLite
TFLite python API package for parsing TFLite model.

The generated Python API is based on Tensorflow 1.13.

If you want to generate by yourself, you could do using the following commands:

1. Get the Tensorflow 1.13 TFLite model schema file, for example: `wget https://raw.githubusercontent.com/tensorflow/tensorflow/r1.13/tensorflow/lite/schema/schema.fbs` or you could find this `schema.fbs` file in this repo.
2. `flatc --python schema.fbs`

Then you should find one generated directory named as `tflite` in your current directory.

Finally, make your `PYTHONPATH` could find your `tflite` package. For example: `export PYTHONPATH=/home/someone/tflite`. Be careful, you should make the root directory of `tflite` package in your `PYTHONPATH`. For example, you should set `export PYTHONPATH=https://github.com/FrozenGene/tflite` not `export PYTHONPATH=https://github.com/FrozenGene/tflite/tflite`.

After these steps, you could test using this command: `python3 -c "import tflite"`

If you don't have Flatbuffers compiler(flatc), you could see more instructions about how to build / install: https://github.com/google/flatbuffers

Use `python3 setup.py sdist bdist_wheel` to build a python package.
