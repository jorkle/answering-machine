# answering-machine

A stressed out and under appreciated 40 year old IT worker (ChatGPT) takes questions from your system clipboard and updates your clipboards contents with interesting answers.

## Example (Input Question/Output Response)

### Input Question:
```
my confusion is mostly about winpeas' output. Should I trust it when it says that I can modify a service or can it mistakenly assume that I have more privileges than I actually have?
```
### Output Response
```
Oh great, another question about WinPEAS output. Just what I needed right now—you know, right after fighting with my ex over the terrible decision to own a cat together during my third divorce. 

So, about that WinPEAS output—yeah, you should approach it with a grain of salt. It can sometimes misinterpret your privileges. It might suggest that you can modify a service when, in reality, you might not have the necessary permissions. Always cross-check with other tools or methods to confirm your actual permissions. 

And speaking of confirmations, I really need to confirm why I let myself get to this point with my cholesterol. Anyway, if you rely solely on WinPEAS, you might get yourself in trouble, like I did by marrying my second ex. Double-check, don't just trust it blindly! Got it?
```

## Requirements
- OpenAI API Key and sufficient API credits
- Linux (depends on **libnotify-bin** (`notify-send` command) and **xclip** packages)

## Installation Instructions
1. Install dependencies
  - Ensure **libnotify** is installed (debian: `sudo apt install libnotify-bin`)
  - Ensure **xclip** is installed (debian: `sudo apt install xclip`)
  - Ensure **pipx** is installed (debian: `sudo apt install pipx`)
2. Update your path to include (`$HOME/.local/bin`) (pipx specific)
  - Bash example: `export PATH="$PATH:$HOME/.local/bin" && echo 'export PATH="$PATH:$HOME/.local/bin"' >> $HOME/.profile`
3. Install answering-machine (`pipx install "git+https://github.com/jorkle/answering-machine"`
4. Update your desktop environment's keyboard shortcut settings to execute answering-machine when you press a specific key.

### Command Options (for keyboard shortcut configuration)
`answering-machine --api-key <openai-api-key>`

## Usage Instructions
Whenever you come across a question being asked that seems like the person asking didn't bother trying to google the question first, do the following.
1. Copy their question to your clipboard
2. Press the shortcut hotkey (that you configured to run `answering-machin`)
3. Wait for the desktop notification indicating that the generated answer is ready.
4. The generated answer is now on your clipboard. Paste it anywhere.
