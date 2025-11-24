from typing import List, TypedDict


class DialogueItem(TypedDict):
    character: str
    sentence: str
    image_search: str
    image: str


# Video Settings
VIDEO_TITLE: str = "Chapter 7: CPU Scheduling"
TITLE_SOUND_PATH: str = "image_assests/title_sound.mp3"

# File Paths
VIDEO_TEMPLATE_PATH: str = "video_assests/minecraft_background.mp4"
safe_title = (
    VIDEO_TITLE.replace(" ", "_").replace(":", "_").replace("/", "_").replace("\\", "_")
)
OUTPUT_VIDEO_PATH: str = f"output_videos/{safe_title}.mp4"
AUDIO_ASSETS_DIR: str = "audio_assests"
IMAGE_ASSETS_DIR: str = "image_assests"
DOWNLOADED_IMAGES_DIR: str = "downloaded_images"
RUNTIME_LOGS_DIR: str = "runtime_logs"


# Dialogue Data
DIALOGUE: List[DialogueItem] = [
    {
        "character": "Peter",
        "sentence": "Okay Stewie, 'Scheduling'. I know this one. It's like when Lois tells me I have to go to the clam at 8, but I actually go at 5.",
        "image_search": "Peter Griffin looking at a calendar confused",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Not quite, you scheduling disaster. We are talking about OS Scheduling Policies. The logic used to decide which process gets the CPU next.",
        "image_search": "cpu scheduling process queue diagram",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "We start with **Workload Assumptions**. Imagine a perfect world where every job arrives at the same time and we know exactly how long they take.",
        "image_search": "perfect world utopia cartoon",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Easy. Just let the first guy in line go first. **FIFO**. First In, First Out. Like the line at the buffet.",
        "image_search": "people waiting in line buffet cartoon",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "A primitive approach. But imagine if you, a man of considerable girth, are at the front of the line and take 100 minutes to eat.",
        "image_search": "peter griffin eating slowly at buffet",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "Everyone behind you waits forever. This is the **Convoy Effect**. It ruins **Turnaround Time**, which is the metric measuring how long it takes to finish a job from when it arrives.",
        "image_search": "convoy effect scheduling diagram truck blocking cars",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Okay, so we let the skinny guys eat first? **Shortest Job First**?",
        "image_search": "small person skipping line in front of giant",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Exactly. **SJF** is optimal for Turnaround Time. But it has a flaw. It is **Non-Preemptive**.",
        "image_search": "sjf scheduling gantt chart",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "If a long job starts, and a short job arrives one second later, the short job is stuck waiting until the big one finishes.",
        "image_search": "person waiting impatiently watch",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "So we just kick the big guy off the chair! Preempt him!",
        "image_search": "peter griffin fighting chicken",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Violence is the answer! That is **STCF**: Shortest Time-to-Completion First. It adds preemption.",
        "image_search": "stcf scheduling preemption diagram",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "If a new job arrives that is shorter than what is *left* of the current job, the OS switches immediately.",
        "image_search": "context switch cpu diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "But wait, what if I'm typing on my keyboard and the computer ignores me because it's doing a 'long job'? I hate lag.",
        "image_search": "peter griffin angry at computer lag",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Ah, you are concerned with **Response Time**. STCF is bad for that. For interactivity, we need **Round Robin**.",
        "image_search": "round robin scheduling circle diagram",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "We slice time into quantum chunks. Every job gets a slice, then we switch. It feels like everything is running at once.",
        "image_search": "slicing a pie round robin analogy",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "So Round Robin is the best! Everyone gets a trophy!",
        "image_search": "participation trophy cartoon",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "No, you fool. There is a trade-off. Round Robin is great for Response Time, but terrible for Turnaround Time.",
        "image_search": "trade off scale fairness vs performance",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "It stretches every job out to the very end. You can't have your cake and eat it too.",
        "image_search": "peter griffin eating cake",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "One last thing. What about when the computer is waiting for the hard drive? That takes forever.",
        "image_search": "hard drive loading spinner",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "That is **I/O Overlap**. The Scheduler treats CPU bursts as separate jobs.",
        "image_search": "cpu io burst overlap diagram",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "When a process initiates I/O, it is Blocked. The OS immediately runs something else so the CPU isn't wasted. Efficiency, Peter, efficiency.",
        "image_search": "blocked process state diagram",
        "image": "stewie.png",
    },
]
