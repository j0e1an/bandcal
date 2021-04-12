streaming_band = 10
streaming_4k_band = 25
browsing_band = 0.01
server_base_band = 0.023
gaming_band = 3
iot_band = 0.01
music_band = 0.5
computer_base_band = 1
mobile_base_band = 1
file_downloading_band = 10
video_call_band = 1.8
network_mode = ""
total_band = float()

print("Welcome to BandCal, a tool to calculate your bandwidth in your home or at work. Please answer the simple "
      "questions below to get started. ")


def mode_select():
    wired_or_wireless = input(
        "Do all your devices use wired connections, wireless connections or mix? Input \"w\" for wired only and "
        "\"wi\" for wireless only and \"m\" for both: ")
    return wired_or_wireless


def devices(device_type, base_type):
    global streaming_band
    global streaming_4k_band
    global browsing_band
    global server_base_band
    global iot_band
    global gaming_band
    global music_band
    global computer_base_band
    global mobile_base_band
    global file_downloading_band
    global video_call_band
    global total_band
    device = input("Feel free to let me know how many " + device_type + " you have: ")
    try:
        total_band += base_type * int(device)
    except ValueError:
        print("I'm sorry, but the input needs to be an integer. Please try again.")
        devices(device_type, base_type)
    if total_band > 10000:
        if_mistake = input("You got some serious business running with that many devices. If it is a typo, "
                           "enter \"typo\" here otherwise just hit enter for the next questions: ")
        if if_mistake == "typo":
            devices(device_type, base_type)


def bandcal():
    mode_selector = mode_select()
    print(mode_selector)
    global network_mode
    global total_band
    if mode_selector == "w":
        network_mode = "wired"
        devices("computers", computer_base_band)
        devices("computers are used in video conference", video_call_band)
        if_server = input("Do you have servers? Such as web server or application server, yes or no: ")
        if if_server == "yes" or if_server == "y":
            devices("views per day for the servers", server_base_band)
        devices("computers are used for browsing the internet", browsing_band)
        devices("computers are used for regular video streaming (up to 1080p)", streaming_band)
        devices("computers are used for 4k video streaming", streaming_4k_band)
        devices("gaming consoles or computers that are used for gaming", gaming_band)
        devices("computers are used for music streaming", music_band)
        devices("computers are used for p2p downloading", file_downloading_band)
    elif mode_selector == "wi":
        network_mode = "wifi"
        devices("mobile devices", mobile_base_band)
        devices("mobile devices are used in video conference", video_call_band)
        devices("mobile devices are used for browsing the internet", browsing_band)
        devices("mobile devices are used for regular video streaming (up to 1080p)", streaming_band)
        devices("mobile devices are used for 4k video streaming", streaming_4k_band)
        devices("gaming consoles", gaming_band)
        devices("mobile devices are used for music streaming", music_band)
        devices("mobile devices are used for p2p downloading", file_downloading_band)
        devices("IoT devices", iot_band)
    elif mode_selector == "m":
        network_mode = "both"
        devices("computers", computer_base_band)
        devices("mobile devices", mobile_base_band)
        if_server = input("Do you have servers? Such as web server or application server, yes or no: ")
        if if_server == "yes" or if_server == "y":
            devices("views per day for the servers", server_base_band)
        devices("devices are used in video conference", video_call_band)
        devices("devices are used for browsing the internet", browsing_band)
        devices("devices are used for regular video streaming (up to 1080p)", streaming_band)
        devices("devices are used for 4k video streaming", streaming_4k_band)
        devices("devices are used for music streaming", music_band)
        devices("gaming consoles or computers that are used for gaming", gaming_band)
        devices("devices are used for p2p downloading", file_downloading_band)
        devices("IoT devices", iot_band)
    else:
        print("Unknown input detected, please check.")
        bandcal()
    if total_band <= 1000:
        print("Your total bandwidth needed is " + str(total_band) + "Mbps")
    else:
        total_band = total_band/1000
        print("Your total bandwidth needed is " + str(total_band) + "Gbps")


# initiate the program
if __name__ == "__main__":
    bandcal()
