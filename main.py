import pyrogram as pg
import tqdm

bot = pg.Client(
    name="userbot"
)

@bot.on_message(pg.filters.command("start", prefixes=["."]))
async def start(client: pg.Client, message: pg.types.Message):
    await client.send_message(
        chat_id=message.chat.id,
        text="Hello, World!"
    )
    
async def progress(current, total, message, action):
    with tqdm.tqdm(total=total, unit='B', unit_scale=True, desc=action) as pbar:
        pbar.update(current)

@bot.on_message(pg.filters.command("dl", prefixes=["."]))
async def download(client: pg.Client, message: pg.types.Message):
    if message.reply_to_message:
        dl_something = await client.send_message("me", "Descargando algo xd")
        await client.delete_messages(message.chat.id, message.id)
        if message.reply_to_message.document:
            file = await client.download_media(
                message.reply_to_message.document,
                progress=progress,
                progress_args=(message, "Downloading")
            )
            await client.send_message(
                chat_id="me",
                text=f"Downloaded file: {file.split('/')[-1]}"
            )
            await client.send_document(
                chat_id="me",
                document=file,
                thumb="thumb.jpg",
                progress=progress,
                progress_args=(message, "Uploading")
            )
            await dl_something.delete()
        elif message.reply_to_message.video:
            file = await client.download_media(
                message.reply_to_message.video,
                progress=progress,
                progress_args=(message, "Downloading")
            )
            await client.send_message(
                chat_id="me",
                text=f"Downloaded file: {file.split('/')[-1]}"
            )
            await client.send_document(
                chat_id="me",
                document=file,
                thumb="thumb.jpg",
                progress=progress,
                progress_args=(message, "Uploading")
            )
            await dl_something.delete()
        elif message.reply_to_message.audio:
            file = await client.download_media(
                message.reply_to_message.audio,
                progress=progress,
                progress_args=(message, "Downloading")
            )
            await client.send_message(
                chat_id="me",
                text=f"Downloaded file: {file.split('/')[-1]}"
            )
            await client.send_document(
                chat_id="me",
                document=file,
                thumb="thumb.jpg",
                progress=progress,
                progress_args=(message, "Uploading")
            )
            await dl_something.delete()
        elif message.reply_to_message.photo:
            file = await client.download_media(
                message.reply_to_message.photo,
                progress=progress,
                progress_args=(message, "Downloading")
            )
            await client.send_message(
                chat_id="me",
                text=f"Downloaded file: {file.split('/')[-1]}"
            )
            await client.send_document(
                chat_id="me",
                document=file,
                thumb="thumb.jpg",
                progress=progress,
                progress_args=(message, "Uploading")
            )
            await dl_something.delete()
        else:
            await client.send_message(
                chat_id="me",
                text="Reply to a document to download it."
            )
    else:
        await client.send_message(
            chat_id="me",
            text="Reply to a document to download it."
        )

if __name__ == "__main__":
    print("Starting Userbot...")
    bot.run()