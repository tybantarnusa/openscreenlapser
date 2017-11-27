import ffmpeg

class CreateVideo:
    def __init__(self):
        pass

    def create(self, framerate, inputPath, outputName):
        try:
            (ffmpeg
                .input(inputPath + '/screen-%03d.png')
                .output(outputName)
                .overwrite_output()
                .run()
            )
            return True
        except:
            return False

instance = CreateVideo()