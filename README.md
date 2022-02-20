# ZeusDetector

- Installing:   
`pip install ZeusDetector`

- Requirements:   
`requests`

# Sample Usage

```python
from ZeusDetector import detector

sentence = "This is a sample sentence."
word, detected = detector(sentence)

if detected:
    print(f"Profanity detected.\nWord: {word}")
```   

Made with 💕 by [ZeusBotsNetwork](https://t.me/ZeusBotsNetwork).