def telegram_group_publisher(message):
    if message is None:
        raise Exception("Error message not found")
    print("Telegram group publisher: \n", message)


def telegram_channel_publisher(message):
    if message is None:
        raise Exception("Error message not found")
    print("Telegram channel publisher: \n", message)
