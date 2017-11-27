import os
import ffmpeg
import capture

class CreateVideo:
    def __init__(self):
        pass

    def create(self, framerate, inputPath, outputName):
        try:
            (ffmpeg
                .input(os.path.join(inputPath, ('%s%%03d.png' % capture.instance.filename)))
                .output(outputName)
                .overwrite_output()
                .run()
            )
            return True
        except:
            return False

instance = CreateVideo()