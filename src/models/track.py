
class Track:
    def __init__(self, data: dict):
        self.raw_data = data
        self.id = data.get('id', '')
        attributes = data.get('attributes', {})
        self.name = attributes.get('name', 'Unknown Track')
        self.artist = attributes.get('artistName', 'Unknown Artist')
        self.album = attributes.get('albumName', 'Unknown Album')
        self.duration_ms = attributes.get('durationInMillis', 0)
        self.track_number = attributes.get('trackNumber', 0)
        self.disc_number = attributes.get('discNumber', 0)
        
        self.status = "Queued"
        self.probe_result = None

    @property
    def duration_str(self) -> str:
        if self.duration_ms == 0:
            return "0:00"
        seconds = self.duration_ms // 1000
        return f"{seconds // 60}:{seconds % 60:02d}"

class Album:
    def __init__(self, data: dict):
        self.raw_data = data  
        album_data = data.get('data', [{}])[0]
        attributes = album_data.get('attributes', {})

        self.id = album_data.get('id', '')
        self.name = attributes.get('name', 'Unknown Album')
        self.artist = attributes.get('artistName', 'Unknown Artist')

        
        self.storefront = attributes.get('playParams', {}).get('storefrontId', 'us')
        
        tracks_data = album_data.get('relationships', {}).get('tracks', {}).get('data', [])
        self.tracks = [Track(t_data) for t_data in tracks_data]