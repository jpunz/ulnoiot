from ulnoiot import *
mqtt("192.168.12.1", "sensors")
rgb("rgb",d1,d2,d3)
button("reed",d4,"off","on")
button("quicksilver",d5,"off","on")
run()