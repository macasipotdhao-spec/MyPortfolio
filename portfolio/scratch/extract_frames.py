import yt_dlp
import cv2
import os

urls = {
    'sams': 'https://www.youtube.com/watch?v=fRCW6r94044',
    'smartsched': 'https://www.youtube.com/watch?v=G8wS_6iFOu4'
}

ydl_opts = {'format': 'best'}
assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

for name, url in urls.items():
    print(f"Extracting 10s frame for {name} from {url}...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']
            
            cap = cv2.VideoCapture(video_url)
            # Set position to 10 seconds (10000 ms)
            cap.set(cv2.CAP_PROP_POS_MSEC, 10000)
            success, frame = cap.read()
            
            if success:
                out_path = os.path.join(assets_dir, f"{name}_10s.jpg")
                cv2.imwrite(out_path, frame)
                print(f"Saved {out_path}")
            else:
                print(f"Failed to read frame at 10s for {name}")
            cap.release()
    except Exception as e:
        print(f"Error processing {name}: {e}")
