# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class ReducerOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsReducerOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ReducerOptions()
        x.Init(buf, n + offset)
        return x

    # ReducerOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ReducerOptions
    def KeepDims(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def ReducerOptionsStart(builder): builder.StartObject(1)
def ReducerOptionsAddKeepDims(builder, keepDims): builder.PrependBoolSlot(0, keepDims, 0)
def ReducerOptionsEnd(builder): return builder.EndObject()
