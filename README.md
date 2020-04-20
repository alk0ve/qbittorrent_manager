# qbittorrent_manager
A Python manager for qBitTorrent using its Web UI

# What is this
This is a manager daemon for pausing torrents and shutting down qBitTorrent once all torrents reach a certain seeding ratio (currently 2.0).
The daemon logs its last action into a file in the folder it runs from.

# Installation
1. Run 'pip install -r requirements.txt'
2. Enable qBitTorrent's Web UI (it's best to enable it *only* on 127.0.0.1) and enable "Bypass authentication for clients on localhost"
3. Set up the script to run with pythonw.exe (to hide the console screen) once every 10 minutes using Task Scheduler
4. Profit :)
