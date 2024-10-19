import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download speed in mbps ::",down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed /10**6, 2)
    print ("Upload speed in mbps ::",up_speed)

    ping = test.results.ping
    print("ping ::",ping)
Speed_Test()