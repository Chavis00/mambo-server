from torrentp import TorrentDownloader


class Torrent_Downloader:
    
    def __init__(self):
        pass

    def download_torrent(self, magnet, path):
        torrent_file = TorrentDownloader(magnet, path)
        torrent_file.start_download()
    
    def upload_torrent(self, update, context):
        magnet = ""
        for arg in context.args:
                magnet = magnet + arg 
        
        update.message.reply_text("Downloading...")
        try:
            self.download_torrent(magnet, "/code/Films")
            update.message.reply_text("Film was added to Plex!")
        except:
            update.message.reply_text("Something went wrong :c")

        

