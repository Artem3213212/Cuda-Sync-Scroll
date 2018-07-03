import os
from cudatext import *
import cudatext_cmd as cmds

def CallBackUpdate():
    if VerticalScrol or HorizontalScrol:
        if GROUPS_ONE==app_proc(PROC_GET_GROUPING,''):
            app_proc(PROC_SET_EVENTS,__name__+';on_state;;')
        else:
            app_proc(PROC_SET_EVENTS,__name__+';on_scroll,on_state;;')
    else:
        app_proc(PROC_SET_EVENTS,__name__+';;;')
    

class Command:
    sync_v = False
    sync_h = False
    
    def __init__(self):
        pass

    def config(self):
        pass
        
    def toggle_vert(self):
        self.sync_v = not self.sync_v
        CallBackUpdate()

    def toggle_horz(self):
        self.sync_h = not self.sync_h
        CallBackUpdate()

    def on_scroll(self,ed_self):
        vpos=ed_self.get_prop(PROP_SCROLL_VERT)
        hpos=ed_self.get_prop(PROP_SCROLL_HORZ)
        n=ed_self.get_prop(PROP_INDEX_GROUP)
        for i in range(6):
            if i==n:
                continue
            e=ed_group(i)
            if e!=None:
                if self.sync_v:
                    e.set_prop(PROP_SCROLL_VERT,vpos)
                if self.sync_h:
                    e.set_prop(PROP_SCROLL_HORZ,hpos)
                e.cmd(cmds.cmd_RepaintEditor)
                
    def on_state(self, ed_self, state):
        if state==APPSTATE_GROUPS:
            CallBackUpdate()


"""
AAAAAAAAAAAAAAAAAAA
a 
wsv
fa
e
fa
s
ea
f
a
e

as
d
as
df
a
sd
f
as
df
as
d
fa
sd
fa
sdf
a
d
f
as
fd
as
df
a

fd
as
f
das
f
da
sf

das
fa

df
a
df
a
sdf

"""