#! /usr/bin/env python3
#
# SMD Resistor, Capacitor, Inductor discrete parts
#

from pcbflow import *

class Discrete2(PCBPart):
    def assign_pads(self, pad1=None, pad2=None):
        layer = "GTL" if self.side == "top" else "GBL"
        if pad1 is not None:
            self.pads[0].set_name(pad1)
        if pad2 is not None:
            self.pads[1].set_name(pad2)
        return self

class wb_pad_12(Discrete2):
    def __init__(self, *args, family="C", **kwargs):
        self.family = family
        super().__init__(*args, **kwargs)

    def place(self, dc):
        n = 12 
        w = 1.5 # mm
        h = 0.5 # mm
        pitch = 1 ## mm 
        for idx in range(n):
            if n>0:
                dc.forward(pitch)
            dc.rect(w, h)
            self.smd_pad(dc)
            self.id = [idx]
            dc.silk(side=self.side)

        # self.label(dc)
        # dc.pop()

    def escape_2layer(self):
        # escape for 2-layer board (VCC on GTL, GND on GBL)
        self.pads[0].set_name("VCC").w("o f 0.5").wire()
        self.pads[1].w("o -")

class TE35(Discrete2):
    def __init__(self, *args, family="C", **kwargs):
        self.family = family
        super().__init__(*args, **kwargs)

    def place(self, dc):
        # Pads on either side
        l = 3.15 
        w = 0.9 
        n = 12
        pitch = 3.5 
        
        for idx in range(n):
            if idx > 0:
                dc.forward(pitch)
            dc.rect(l, w)
            self.smd_pad(dc)
            dc.rect(l+.01, w+.01)
            dc.silk(side=self.side)   
            self.id = [idx]

    def escape_2layer(self):
        # escape for 2-layer board (VCC on GTL, GND on GBL)
        self.pads[0].set_name("VCC").w("o f 0.5").wire()
        self.pads[1].w("o -")

class rf_pad_x(Discrete2):
    def __init__(self, *args, family="C", **kwargs):
        self.family = family
        super().__init__(*args, **kwargs)

    def place(self, dc):
        h = MILS(38)
        w = 1.5*MILS(50)
        
        dc.rect(w, h)
        self.smd_pad(dc, ignore_paste = False)
        self.id = [0]
        # dc.silk(side=self.side)

        # self.label(dc)
        # dc.pop()

    def escape_2layer(self):
        # escape for 2-layer board (VCC on GTL, GND on GBL)
        self.pads[0].set_name("VCC").w("o f 0.5").wire()
        self.pads[1].w("o -")


class rf_pad_y(Discrete2):
    def __init__(self, *args, family="C", **kwargs):
        self.family = family
        super().__init__(*args, **kwargs)

    def place(self, dc):
        w = MILS(38)
        h = 1.5*MILS(50)
        
        dc.rect(w, h)
        self.smd_pad(dc, ignore_paste = False)
        self.id = [0]
        # dc.silk(side=self.side)

        # self.label(dc)
        # dc.pop()

    def escape_2layer(self):
        # escape for 2-layer board (VCC on GTL, GND on GBL)
        self.pads[0].set_name("VCC").w("o f 0.5").wire()
        self.pads[1].w("o -")