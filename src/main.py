from initializetion import init
import getMessage

@init.discord_client.event
async def on_message(message):
    await getMessage.getMessage(init.discord_client, message)

if __name__ == '__main__':
    init.init()
