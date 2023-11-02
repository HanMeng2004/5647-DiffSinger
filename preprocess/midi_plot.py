from visual_midi import Plotter
from visual_midi import Preset
from pretty_midi import PrettyMIDI

# Loading a file on disk using PrettyMidi, and show
pm = PrettyMIDI("houlai.mid")
plotter = Plotter()
plotter.show(pm, "/tmp/example-01.html")
