from typing import List, TypedDict


class DialogueItem(TypedDict):
    character: str
    sentence: str
    image_search: str
    image: str

# Video Settings
VIDEO_TITLE: str = "Chapter 6: CPU mechanisms"
TITLE_SOUND_PATH: str = "image_assests/title_sound.mp3"

# File Paths
VIDEO_TEMPLATE_PATH: str = "video_assests/minecraft_background.mp4"
OUTPUT_VIDEO_PATH: str = f"output_videos/{VIDEO_TITLE.replace(' ', '_')}.mp4"
AUDIO_ASSETS_DIR: str = "audio_assests"
IMAGE_ASSETS_DIR: str = "image_assests"
DOWNLOADED_IMAGES_DIR: str = "downloaded_images"
RUNTIME_LOGS_DIR: str = "runtime_logs"


# Dialogue Data
DIALOGUE: List[DialogueItem] = [
    {
        "character": "Peter",
        "sentence": "Stewie, I'm reading this chapter on Limited Direct Execution and it sounds like a mob hit. Are we executing people directly?",
        "image_search": "Peter Griffin mobster suit holding tommy gun",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "No, you dullard. It is the strategy the OS uses to run programs efficiently. Direct Execution means the program runs directly on the CPU for speed. The Limited part is the chains the OS puts on it so it doesn't destroy the machine.",
        "image_search": "dog on a leash limitations diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Chains? You mean like User Mode and Kernel Mode? Is User Mode where I get to do whatever I want?",
        "image_search": "baby in a playpen vs office desk",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Quite the opposite. User Mode is the playpen. You are restricted. You cannot touch the hardware directly. Kernel Mode is the parent with the keys to the house.",
        "image_search": "user mode vs kernel mode privilege rings",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "So if I'm in the playpen, User Mode, and I want to write to the hard disk, what do I do? Scream until Mom comes?",
        "image_search": "screaming baby attention",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Essentially. You perform a System Call, like open or write. To do this, your code executes a special TRAP instruction.",
        "image_search": "trap instruction system call diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "It's a trap! So I jump into the Kernel, do the work, and then what? Do I stay there?",
        "image_search": "admiral ackbar its a trap meme",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "No. The OS executes a Return-from-Trap instruction. It lowers the privilege level back to User Mode and resumes your code. It uses a Trap Table set up at boot time to know exactly where to jump in the kernel code.",
        "image_search": "trap table operating system diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Okay, but what if a program is being a jerk? What if it just loops forever and never calls a Trap? Does the computer just freeze?",
        "image_search": "computer frozen blue screen of death",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "That was the flaw of the old Cooperative Approach. To fix this, we use the Timer Interrupt. It is a hardware device that punches the CPU in the face every few milliseconds to give control back to the OS.",
        "image_search": "timer interrupt hardware diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "So the OS takes control back by force. Then it switches to another process? Is that the Context Switch?",
        "image_search": "wrestler tagging partner in ring",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Precisely. A Context Switch is when the OS saves the register values of the old process onto its Kernel Stack, and restores the values of the new process. It switches the execution flow entirely.",
        "image_search": "context switch process control block diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Wait, saving and restoring... that takes time. Is it slow?",
        "image_search": "sloth moving slowly",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "It has overhead, yes. But it happens in microseconds. To you, it looks like everything is running at once. It is the magic of Time Sharing.",
        "image_search": "time sharing cpu scheduling diagram",
        "image": "stewie.png",
    },
]
