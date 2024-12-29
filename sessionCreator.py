import pyrogram as pg

def sessionCreator(hash: str, appid: int, phone_number: str):
    client = pg.Client(
        name="userbot",
        api_hash=hash,
        api_id=appid,
        phone_number=phone_number
    )
    
    print("starting client")
    client.start()
    print("client started")
    client.stop()
    print("client stopped and created")
    
sessionCreator(
    hash="",
    appid=123456,
    # Phone number must have his prefix (country code) and without spaces, for example
    # for Cuba will be 53, so the number is 5355555555
    phone_number=""
)