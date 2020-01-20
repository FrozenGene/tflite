# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class FakeQuantOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFakeQuantOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FakeQuantOptions()
        x.Init(buf, n + offset)
        return x

    # FakeQuantOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FakeQuantOptions
    def Min(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # FakeQuantOptions
    def Max(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # FakeQuantOptions
    def NumBits(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FakeQuantOptions
    def NarrowRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def FakeQuantOptionsStart(builder): builder.StartObject(4)
def FakeQuantOptionsAddMin(builder, min): builder.PrependFloat32Slot(0, min, 0.0)
def FakeQuantOptionsAddMax(builder, max): builder.PrependFloat32Slot(1, max, 0.0)
def FakeQuantOptionsAddNumBits(builder, numBits): builder.PrependInt32Slot(2, numBits, 0)
def FakeQuantOptionsAddNarrowRange(builder, narrowRange): builder.PrependBoolSlot(3, narrowRange, 0)
def FakeQuantOptionsEnd(builder): return builder.EndObject()
