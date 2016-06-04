import sfml
from sfml import sf

def main():
    w = sf.RenderWindow(sf.VideoMode(640,480), "Test")
    while w.is_open:
        w.clear(sf.Color.BLUE)
        w.display()
        for event in w.events:
            if event == sf.CloseEvent:
                w.close()
        

if __name__ == "__main__":
    main()
