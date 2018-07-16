# ## Homework _9_ (not 8): Problem 2, steganography
#
# This question asks you to write two functions, likely with some helper functions, that will enable you
# to embed arbitrary text (string) messages into an image (if there is enough room!)

# For extra credit, the challenge is to be
# able to extract/embed an image into another image...

#
# You'll want to borrow from hw8pr1 for
#  + opening the file
#  + reading the pixels
#  + create some helper functions!
#  + also, check out the slides :-)
#
# Happy steganographizing, everyone!
#





# Part A: here is a signature for the decoding
# remember - you will want helper functions!

import cv2
import numpy as np
import matplotlib.pyplot as plt
from binascii import *

def int_to_bin(integer):
    """
    Input: integer - one digit integer type
    Output: final_bin - binary version of integer with leading zeros
                        such that it is 8 digits long as a string
    """
    binary = bin(integer)[2:]
    leading_zeros = (8-len(binary))*str(0)
    final_bin = leading_zeros + binary
    return final_bin

def msg_to_bin( image ):
    """
    Input: image object that needs to be decoded
    Output: String of the message encoded in the image in binary
     """

    #initializing binary string
    binary_str = ""

    #getting image dimensions
    height, width, channels = image.shape

    #below is some cursed syntax. Nested while loops with nested if statements...
    row = 0
    decoding_finished = False
    while decoding_finished == False:
        end_row = False
        print("On row ",row)
        col = 0
        while end_row == False:
            print("On column ",col)

            rb = int_to_bin(image[row,col][0])[-1:]
            binary_str += rb
            if len(binary_str)%8 == 0 and binary_str[-8:] == "0"*8:
                decoding_finished = True
                break

            gb = int_to_bin(image[row,col][1])[-1:]
            binary_str += gb
            if len(binary_str)%8 == 0 and binary_str[-8:] == "0"*8:
                decoding_finished = True
                break

            bb = int_to_bin(image[row,col][2])[-1:]
            binary_str += bb
            if len(binary_str)%8 == 0 and binary_str[-8:] == "0"*8:
                decoding_finished = True
                break

            if col == width-1:
                end_row = True
            col+=1

        row+=1

    return binary_str

def desteg_string(image):
    binary_msg = msg_to_bin(image)
    split_bin = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    decoded_msg = ""
    for encoded_ascii in split_bin[:-1]:
        integer = int(encoded_ascii,2)
        character = chr(integer)
        decoded_msg+=character

    return decoded_msg


# IMAGE_NAME = "./small_flag_with_message_bgr.png"
# image_bgr = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)
# image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
# decoded_msg = desteg_string(image)
# print(decoded_msg)




# Part B: here is a signature for the encoding/embedding
# remember - you will want helper functions!
def load_image(file_path):
    """This loads in an image"""
    image_bgr = cv2.imread(file_path,cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return image

def char_to_bin(character):
    """
    Input: character - a string consisting of a single ascii character
    Output: char_bin - a string representing this ascii character in binary
    """
    small_bin = bin(ord(character))[2:]
    num_zeros = 8 - len(small_bin)
    char_bin = num_zeros*str(0)+small_bin
    return char_bin

def string_to_bin(msg):
    """
    Input: msg - a string of ascii characters
    Output: bin_msg - a string of binary represnting these ascii characters
    """
    bin_msg = ""
    for character in msg:
        char_bin = char_to_bin(character)
        bin_msg +=char_bin
    return bin_msg

def steganographize( image, msg, new_image_name="Ooohhh, a spooky encoded image!" ):
    """
    Inputs:
    image - 3D numpy array representing an image
    msg - a string representing the message to be encoded
    Output:
    encoded_image - this is a 3D numpy array represnting the original image
                    with the encoded message
    """
    # bin_msg = ""
    # for character in msg:
    #     bin_msg += bin(ord(character))[2:]
    #
    # bin_msg += str(0)*8

    bin_msg = string_to_bin(msg)
    print(bin_msg)
    image_vec = np.reshape(image,image.shape[0]*image.shape[1]*image.shape[2])

    i = 0
    for bit in bin_msg:
        print("og",image_vec[i])
        image_vec[i] = int(bin(image_vec[i])[2:-1]+bin_msg[i],2)
        print('new',image_vec[i])

        i+=1
    image_vec[i:i+8]=str(0)*8
    new_image = np.reshape(image_vec,image.shape)
    image_to_save = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(new_image_name, image_to_save)

    return new_image

def display_image(image):
    """This displays an image"""
    plt.figure()
    plt.axis('off')
    plt.imshow(image)
    plt.show()

image_dir = 'art.png'
image = load_image(image_dir)
image_name = image_dir + "_encoded.png"
new_image = steganographize( image,"hey there buddy chum pal friend buddy pal chum bud friend fella bruther amigo pal buddy friend chummy chum chum pal i don't mean to be rude my friend pal home slice bread slice dawg but i gotta warn ya if u take one more diddly darn step right there im going to have to diddly darn snap ur neck and wowza wouldn't that be a crummy juncture, huh? do yuo want that? do wish upon yourself to come into physical experience with a crummy juncture? because friend buddy chum friend chum pally pal chum friend if you keep this up well gosh diddly darn i just might have to get not so friendly with u my friendly friend friend pal friend buddy chum pally friend chum buddy...", image_name)
print(desteg_string(new_image))
