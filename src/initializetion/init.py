import configparser
import discord

# set discord token
def discord_init():
    infile = configparser.ConfigParser()
    infile.read('../config.ini')

    return infile.get('discord', 'token')
