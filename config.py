from typing import List, TypedDict


class DialogueItem(TypedDict):
    character: str
    sentence: str
    image_search: str
    image: str
    id: int | None


# File Paths
VIDEO_TEMPLATE_PATH: str = "video_assests/minecraft_background.mp4"
OUTPUT_VIDEO_PATH: str = "output_final_video.mp4"
AUDIO_ASSETS_DIR: str = "audio_assests"
IMAGE_ASSETS_DIR: str = "image_assests"
DOWNLOADED_IMAGES_DIR: str = "downloaded_images"
RUNTIME_LOGS_DIR: str = "runtime_logs"

# Video Settings
VIDEO_TITLE: str = "Operating Systems 101"
TITLE_SOUND_PATH: str = "image_assests/title_sound.mp3"

# Dialogue Data
DIALOGUE: List[DialogueItem] = [
    {
        "character": "Peter",
        "sentence": "So, a 'process' is basically just a program that's actually doing something. Like me when I'm awake versus me on the couch.",
        "image_search": "process vs program diagram",
        "image": "peter.png",
        "id": None,
    },
    {
        "character": "Stewie",
        "sentence": "A crude analogy, but accurate. The program on the disk is lifeless bytes. The OS loads it into memory and gives it life. It’s the Frankenstein of computing.",
        "image_search": "operating system loading program into memory",
        "image": "stewie.png",
        "id": None,
    },
    {
        "character": "Peter",
        "sentence": "But wait, I got a browser, a game, and my email open. How does the computer run all that at once? Does it have a hundred tiny brains?",
        "image_search": "multitasking operating system processes diagram",
        "image": "peter.png",
        "id": None,
    },
    {
        "character": "Stewie",
        "sentence": "No, you simpleton. It's an illusion created by 'virtualizing' the CPU. It creates a virtual CPU for every process.",
        "image_search": "cpu virtualization illustration",
        "image": "stewie.png",
        "id": None,
    },
    {
        "character": "Peter",
        "sentence": "Virtualizing? Is that like when I pretend to listen to Lois while watching TV?",
        "image_search": "virtual cpu diagram",
        "image": "peter.png",
        "id": None,
    },
    {
        "character": "Stewie",
        "sentence": "In a way. It's called Time Sharing. The OS runs one process, stops it, runs another, and switches so fast you think they're all running at once.",
        "image_search": "time sharing operating system diagram",
        "image": "stewie.png",
        "id": None,
    },
    {
        "character": "Peter",
        "sentence": "Okay, but how does it decide who goes next? Is it a lottery? Do they fight to the death?",
        "image_search": "cpu scheduling algorithm illustration",
        "image": "peter.png",
        "id": None,
    },
    {
        "character": "Stewie",
        "sentence": "That brings us to Mechanism versus Policy. The mechanism is the 'how'—like the context switch that swaps them out.",
        "image_search": "mechanism vs policy in operating system chart",
        "image": "stewie.png",
        "id": None,
    },
    {
        "character": "Peter",
        "sentence": "And the policy is the 'which'? Like deciding whether to eat a donut or a bagel first?",
        "image_search": "cpu scheduling policy decision",
        "image": "peter.png",
        "id": None,
    },
    {
        "character": "Stewie",
        "sentence": "Precisely. The Scheduler uses policy to decide which process gets the CPU based on history or performance metrics.",
        "image_search": "scheduler algorithm process selection",
        "image": "stewie.png",
        "id": None,
    },
    {
        "character": "Peter",
        "sentence": "Now, what about the stuff inside? The text says something about a Stack and a Heap. Sounds like my laundry room.",
        "image_search": "stack vs heap memory diagram",
        "image": "peter.png",
        "id": None,
    },
    {
        "character": "Stewie",
        "sentence": "The Stack manages local variables and function calls. The Heap is for dynamic memory, like when you need extra space for your stupidity.",
        "image_search": "memory stack and heap layout",
        "image": "stewie.png",
        "id": None,
    },
    {
        "character": "Peter",
        "sentence": "And if a process finishes but the parent hasn't checked on it yet... it becomes a Zombie?",
        "image_search": "zombie process operating system diagram",
        "image": "peter.png",
        "id": None,
    },
    {
        "character": "Stewie",
        "sentence": "Yes, a Zombie state. Dead, but occupying a slot in the process table until the parent calls wait(). Much like you at a family gathering.",
        "image_search": "process table with zombie process",
        "image": "stewie.png",
        "id": None,
    },
]
