from ulnoiot import *

def main():
    # connect to mqtt server mymqttgateway (can also be an IP address),
    # and report all local devices under the topic myroom/test1.
    # If not set on your mqtt server, you can skip user and password.
    from ulnoiot.shield import relay
    mqtt("192.168.12.1", "door")
    out("lock", d1, "on", "off")
    run()

    ## use some shields
    # the onboard-led is always available, will report under myroom/test1/blue
    # and can be set via sending off or on to myroom/test1/blue/test
    #from ulnoiot.shield import blue
    #blue.high() # make sure it's off

    ## add some other devices
    # add a button with a slightlyhigher debounce rate, which will report
    # in the topic myroom/test1/button1
    #button("button1",d8,threshold=2)

    # count rising signals on d2=Pin(4)
    # and report number counted at myroom/test1/shock1
    #trigger("shock1",Pin(4))

    ## start to transmit every 10 seconds (or when status changed)
    #run(10)

main()
