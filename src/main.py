from lib import lib

delay = float(input("Delay between screenshots(Seconds): "))
interval = float(input("Interval between frames shown on video(Seconds): "))

start_index = 0

capture = lib(delay=delay, start_index=start_index, dir="../imgs/", interval=interval)

capture.run()
