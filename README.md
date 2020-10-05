# YoutubeDownloader
PYTHON GUI TO DOWNLOAD VIDEOS FROM YOUTUBE WITH THE VIDEO LINK USING pytube MODULE and PLAY THE DOWNLOADED VIDEO IN THE APPLICATION WINDOW.

pytube is a very serious, lightweight, dependency-free Python library (command-line utility) for downloading YouTube Videos. It has no third party dependencies & aims to be highly reliable. pytube also makes pipelining easy, allowing to specify callback functions for different download events, such as on progress or on complete.

## The module can be installed using the command - pip install pytube

P.S - IN CASE YOU GET AN ERROR RELATED TO KeyError 'CIPHER', open the extract.py file mentioned in the Error and on line no. 301 replace 'cipher' keyword in parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats) with signatureCipher keyword parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
