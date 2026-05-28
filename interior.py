#I will help someone choose an inspo photo to decorate their room and sure its in their budget.

import webbrowser

names= ["Grey Modern Simple Room", "Grey Complex Modern Room", "Grey Blue Room with Gaming Setup", "Grey and Purple Modern Vinerery Room"]

urls = ["https://tinyurl.com/mrjt2htb", "https://tinyurl.com/m3x33wzm", "https://tinyurl.com/2p8yt6u3", "https://tinyurl.com/2jbtvsvr"]

description = ["This image features a modern, minimalist bedroom with an upholstered grey bed that"
"appears to float due to vibrant blue LED strip lighting installed underneath. The room is illuminated with "
"additional colorful, ambient light strips, accentuating a high-tech, cyberpunk design aesthetic.", "This bedroom features a "
"minimalist, modern design characterized by high-contrast tones, including charcoal gray walls, white bedding, and light wood flooring. "
"The space emphasizes a 'less is more' aesthetic through a low-profile, upholstered platform bed, a simple "
"pedestal nightstand, and a black swing-arm wall lamp", "This modern teen boy's bedroom features a high-energy, cyberpunk aesthetic defined "
"by a dark gray and black color palette with vibrant neon blue and purple LED lighting. Key elements include a dedicated gaming station, a "
"low-profile platform bed, and extensive, atmospheric LED strip lighting on shelves and under the bed.",  "This vibrant neon sanctuary is "
"drenched in deep purple and pink lighting, creating a trendy, immersive atmosphere perfect for a modern teen. The space balances sharp "
"'gamer' aesthetics with ultra-plush textures, featuring shaggy faux-fur pillows and a glowing neon wall sign that serves as the focal point."]

prices = [2700.00 ,1000.00 ,2000.00 , 900.00]

empty = []

#Input what type of room you want to open description, picture, name, and price
def interested():

    print ("Welcome to Artificial Interior Assistance")
    interest = input("What are some ideas you are thinking of?: Grey Modern Simple Room, Grey Complex Modern Room, " \
    "Grey Blue Room with Gaming Setup, Grey and Purple Modern Vinerery Room: ")
    if interest == "Grey Modern Simple Room":
        print (names[0])
        webbrowser.open(urls [0])
        print (description[0])
        print (prices[0])
    elif interest == "Grey Complex Modern Room":
        print (names[1])
        webbrowser.open(urls [1])
        print (description[1])
        print (prices[1])
    elif interest == "Grey Blue Room with Gaming Setup":
        print (names[2])
        webbrowser.open(urls [2])
        print (description[2])
        print (prices[2])
    elif interest == "Grey and Purple Modern Vinerery Room":
        print (names[3])
        webbrowser.open(urls [3])
        print (description[3])
        print (prices[3])


#Figure out if the room inspo is in your price range
def room(budget):
    for i in range (len(names)):
        if prices[i] >= budget:
            empty.append(names[i])
            empty.append (prices[i])
    print(f"Other Options in Price Range: {empty}")
    empty.clear()




#Call your fuctions and input your budget in the parameter
interested()

room(2000)



#Picture of Grey Bedroom
#Author Name: Pheonix
#Website URL: https://www.superlightingled.com/blog/6-best-led-strip-lights-ideas-for-led-room-lights/
#Picture Desciption: LED lights for bedroom
#Title of Article: 6 Best LED Strip Lighting Ideas For Rooms
#Date: May 20, 2022

#Picture of Grey Complex Bedroom
#Author Name: Maria Sabella
#Website URL: https://www.architecturaldigest.com/gallery/timeless-boys-bedroom-ideas-that-can-grow-with-them
#Picture Desciption: Merges style and function
#Title of Article: 19 Timeless Boys Bedroom Ideas That Can Grow With Them
#Date: June 9, 2025
#Photo: Rikki Snyder

#Picture of Gaming Style Bedroom
#Author Name: Tharanga Ekanayaka
#Website URL: https://variousloft.com/20-teen-boy-bedroom-trends-that-will-wow-everyone/
#Picture Desciption:
#Title of Article: 20 Teen Boy Bedroom Trends That Will Wow Everyone!
#Date: April 11, 2025


#Picture of Purple and Grey Room
#Author Name: GE Lighting
#Website URL: https://www.gelighting.com/inspiration/bedroom-lighting-ideas
#Picture Desciption: Purple LED Room
#Title of Article: Creative Lighting Ideas for The Perfect Bedroom
#Date: May 01, 2024

