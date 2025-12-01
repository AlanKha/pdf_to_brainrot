from typing import List, TypedDict


class DialogueItem(TypedDict):
    character: str
    sentence: str
    image_search: str
    image: str


# Video Settings
VIDEO_TITLE: str = "NLP Quiz 3"
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
        "sentence": "Alright Stewie, I’m trying to log into Club Penguin to find my 'igl oo', but the computer is yelling at me. I think I broke the internet.",
        "image_search": "Peter Griffin typing on computer confused",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "You fat-fingered imbecile. You typed 'igl oo' with a space. The system needs to calculate the String Distance to figure out you meant 'igloo'.",
        "image_search": "Levenshtein distance matrix example",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "String distance? Is that how far the cat can chase the yarn? I bet I can chase it further.",
        "image_search": "Peter Griffin playing with yarn like a cat",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "No. It is the edit cost. Specifically, Levenshtein Distance. It counts insertions, deletions, or substitutions. To fix 'igl oo', we need one deletion. Distance is 1.",
        "image_search": "Levenshtein edit distance calculation diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Okay, but what if I type 'teh' instead of 'the'? That happens all the time because my fingers are like sausages.",
        "image_search": "Peter Griffin looking at his hands",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "That is a transposition. Levenshtein would charge you 2 edits for that. But Damerau-Levenshtein, the 'Typo Specialist', counts swapping adjacent characters as just 1 edit. It understands humans make mistakes.",
        "image_search": "Damerau-Levenshtein transposition example",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Neat. Hey, help me find my friend Anderson. Or was it Andersen? I only know the first part of his name matches.",
        "image_search": "Peter Griffin looking through a phone book",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Then you want Jaro-Winkler Distance. It gives a mathematical boost to strings that match at the start—the prefix. It is the 'Name Specialist' for deduplicating databases.",
        "image_search": "Jaro-Winkler prefix matching diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Got it. Now look at this text: 'I ate an apple while visiting Apple.' The computer is confused. It thinks I ate a laptop.",
        "image_search": "Peter Griffin trying to eat a laptop",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "That is a Named Entity Recognition (NER) problem. Context matters. The first 'apple' is a common noun. The second is an Organization (ORG).",
        "image_search": "Named Entity Recognition tagging example",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "Just like in the sentence 'Sherlock Holmes investigated with Dr. Watson.' Holmes and Watson are Persons (PER), not just random words.",
        "image_search": "Sherlock Holmes cartoon magnifying glass",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Okay, genius. I built a trap to catch Meg when she comes in the house. But it keeps trapping Lois instead! Lois is mad.",
        "image_search": "Peter Griffin holding a trap box",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Your Precision is terrible. Precision measures: Of the people you trapped, how many were actually Meg? You have too many False Positives.",
        "image_search": "Precision vs Recall diagram confusion matrix",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "So I should just never set the trap? Then I'll never catch Lois by mistake!",
        "image_search": "Peter Griffin tapping head smart meme",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "But then your Recall would be zero! Recall asks: Of the times Meg actually entered, how many did you catch? You need a balance, Peter. You need a good F1-Score.",
        "image_search": "F1 score harmonic mean formula visual",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "My head hurts. I'm gonna ask this cricket AI who won the match yesterday. Wait... it says the match hasn't happened yet. Is it stupid?",
        "image_search": "robot reading an old newspaper",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "It's frozen in time! The LLM only knows facts up to its training cutoff. It's hallucinating. We need RAG: Retrieval-Augmented Generation.",
        "image_search": "RAG architecture diagram retrieval augmentation generation",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "We give the AI an 'Open Book Exam'. It Retrieves live cricket scores, Augments the prompt with that data, and then Generates the answer.",
        "image_search": "open book exam cartoon",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Can I put that AI on my flip phone? The Qatar Airways app is too big and slow.",
        "image_search": "Peter Griffin holding an old flip phone",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Not the full model. You need Model Optimization. Specifically, Knowledge Distillation. We train a tiny 'Student' model to mimic the big 'Teacher' model.",
        "image_search": "Knowledge Distillation teacher student network diagram",
        "image": "stewie.png",
    },
    {
        "character": "Stewie",
        "sentence": "Or we use Quantization. We turn the brain's precise 32-bit numbers into chunky 8-bit integers. Less memory, same attitude.",
        "image_search": "quantization neural network weights diagram",
        "image": "stewie.png",
    },
    {
        "character": "Peter",
        "sentence": "Last question. I'm counting words. The word 'the' appears a million times. It must be the most important word in the world!",
        "image_search": "word cloud with THE very big",
        "image": "peter.png",
    },
    {
        "character": "Stewie",
        "sentence": "Wrong again! In TF-IDF, common words get a score of zero. Rare words that appear frequently in *this* document but nowhere else are the important ones.",
        "image_search": "TF-IDF formula explanation graphic",
        "image": "stewie.png",
    },
]
