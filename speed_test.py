import speedtest as st

def Speed_Test():
    test = st.Speedtest()
    #download speed
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download speed in mbps ::",down_speed)
    #upload speed
    up_speed = test.upload()
    up_speed = round(up_speed /10**6, 2)
    print ("Upload speed in mbps ::",up_speed)
    #ping test
    ping = test.results.ping
    print("ping ::",ping)


#Speed_Test()
#def speedtest(jarvis, s):
    #"""Runs a speedtest on your internet connection"""
    #try:
    #    res = st.Speedtest()
    #except st.ConfigRetrievalError:
    #    return jarvis.connection_error()

    # Create a spinner on command line to show that its running
    #jarvis.spinner_start('Running the test ')

    #res.get_best_server()
    #download_speed = res.download()
    #upload_speed = res.upload()

    #jarvis.spinner_stop('')

    # Print the results
    #jarvis.say('Speed test results:', Fore.GREEN)
    #jarvis.say('Download: ' + pretty_speed(download_speed), Fore.GREEN)
    #jarvis.say('Upload: ' + pretty_speed(upload_speed), Fore.GREEN)
