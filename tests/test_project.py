from PIL import Image
from backend.app.multimodal import analyze
def test_run(): assert analyze(Image.new("RGB",(10,10)),"AI research")["author"]=="Rayyan Anwar"
