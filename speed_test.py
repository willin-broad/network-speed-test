import speedtest as st
import time

def pretty_speed(speed_bps):
    """Converts speed from bits per second to megabits per second and formats it."""
    speed_mbps = speed_bps / 10**6  # Convert to Mbps
    return f"{speed_mbps:.2f} Mbps"

def Speed_Test():
    try:
        print("Finding the best server for speed test...")
        test = st.Speedtest()
        
        for _ in range(5):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")
        
        test.get_best_server()  # Finds the best server for the test
        print("Running speed test...\n")
        
        # Download speed
        down_speed = test.download()
        print(f"Download speed: {pretty_speed(down_speed)}")
        
        # Upload speed
        up_speed = test.upload()
        print(f"Upload speed: {pretty_speed(up_speed)}")
        
        # Ping test
        ping = test.results.ping
        print(f"Ping: {ping:.2f} ms")
        
    except st.ConfigRetrievalError:
        print("Error: Could not retrieve configuration for the speed test. Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the speed test
Speed_Test()



# import speedtest as st

# def Speed_Test():
#     test = st.Speedtest()
#     #download speed
#     down_speed = test.download()
#     down_speed = round(down_speed / 10**6, 2)
#     print("Download speed in mbps ::",down_speed)
#     #upload speed
#     up_speed = test.upload()
#     up_speed = round(up_speed /10**6, 2)
#     print ("Upload speed in mbps ::",up_speed)
#     #ping test
#     ping = test.results.ping
#     print("ping ::",ping)


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
