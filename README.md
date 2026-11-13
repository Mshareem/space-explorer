# Space Explorer

Fetches NASA's Astronomy Picture of the Day (APOD), shows its title, date, image link and explanation in the terminal, and opens the HD image in your browser.

## Install
```bash
git clone https://github.com/Mshareem/space-explorer.git
cd space-explorer
python -m venv .venv
source .venv\Scripts\activate
pip install requests
```

## Run
```bash
python space_explorer.py
```

## Sample output
Title: NGC 206 and the Star Clouds of Andromeda
Date:  2026-11-13
Image: https://science.nasa.gov/image-article/apod-2026-november-13-ngc-206-and-the-star-clouds-of-andromeda/
------------------------------------------------------------
Explanation: The large stellar association cataloged as NGC 206 is nestled within the dusty arms of the neighboring Andromeda galaxy along with the galaxy's pinkish star-forming regions. Also known as M31, the spiral galaxy is a mere 2.5 million light-years away. NGC 206 is found at the center of this sharp and detailed close-up of the southwestern extent of Andromeda's disk. The bright, blue stars of NGC 206 indicate its youth. In fact, its youngest massive stars are less than 10 million years old. Much larger than the open or galactic clusters ofyoung stars in the disk of our Milky Way galaxy, NGC 206 spans about 4,000 light-years. That's comparable in size to the giant stellar nurseries NGC 604 in nearby spiral M33 and the Tarantula Nebula in the Large Magellanic Cloud.

Tomorrow's picture: pixels on the Moon

## API
NASA APOD: https://science.nasa.gov/wp-json/wp/v2/apod-basic