from picamera import mmalobj as mo, mmal, PiOverlayRenderer
from skimage.draw import line_aa
from MPU_readout import read_mpu
from signal import pause
import numpy as np
import random
import time

a = np.zeros((480, 400, 4), dtype=np.uint8)
a[240, :, :] = 0xff
a[:, 200, :] = 0xff

a = np.rot90(a)
a = np.concatenate((a, a), 0)
a = np.ascontiguousarray(a)

overlay = PiOverlayRenderer(parent=None, source=memoryview(a), resolution=(480, 800),
                            format='rgba', rotation=90, layer=2, alpha=255)

camera = mo.MMALCamera()
splitter = mo.MMALSplitter()
render_l = mo.MMALRenderer()
render_r = mo.MMALRenderer()

camera.outputs[0].framesize = (480, 400)
camera.outputs[0].framerate = 40
camera.outputs[0].commit()

p = render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]
p.set = mmal.MMAL_DISPLAY_SET_FULLSCREEN | mmal.MMAL_DISPLAY_SET_DEST_RECT
p.fullscreen = False
p.dest_rect = mmal.MMAL_RECT_T(0, 0, 400, 480)
render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION] = p
render_l.inputs[0].params[mmal.MMAL_PARAMETER_ROTATION] = 270

p.dest_rect = mmal.MMAL_RECT_T(400, 0, 400, 480)
render_r.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION] = p
render_r.inputs[0].params[mmal.MMAL_PARAMETER_ROTATION] = 270

splitter.connect(camera.outputs[0])
render_l.connect(splitter.outputs[0])
render_r.connect(splitter.outputs[1])

splitter.enable()
render_l.enable()
render_r.enable()

pause()

exit()

while True:
    slope = read_mpu()

    a = np.zeros((480, 400, 4), dtype=np.uint8)

    y1 = 480 / 2 - 200 * slope
    y2 = 480 / 2 + 200 * slope

    rr, cc, val = line_aa(int(y1), 0, int(y2), 399)
    a[rr, cc, :] = 0xff

    a = np.rot90(a)
    a = np.concatenate((a, a), 0)
    a = np.ascontiguousarray(a)

    overlay.update(source=memoryview(a))
