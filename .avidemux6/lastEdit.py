#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
if not adm.loadVideo("/Users/ymm26/Documents/Personal Projects/Python/Videos/NORMB/NORMB_VID_052.mp4"):
    raise("Cannot load /Users/ymm26/Documents/Personal Projects/Python/Videos/NORMB/NORMB_VID_052.mp4")
adm.clearSegments()
adm.addSegment(0, 0, 60133000)
adm.markerA = 0
adm.markerB = 10700000
adm.setPostProc(3, 3, 0)
adm.videoCodec("Copy")
adm.audioClearTracks()
adm.setContainer("MKV", "forceDisplayWidth=False", "displayWidth=1280", "displayAspectRatio=0")
