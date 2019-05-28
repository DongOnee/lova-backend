from youtube_transcript_api import YouTubeTranscriptApi
import sys

if __name__ == "__main__":
    scripts = YouTubeTranscriptApi.get_transcript(sys.argv[1])
    essay = list()
    for script in scripts:
        essay.append(script['text'])
    print(''.join(essay))
