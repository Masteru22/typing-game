import random

word_list = [
    "apple", "banana", "cherry", "dog", "elephant", "flower", "grape", "house", "island", "jungle",
    "kite", "lemon", "monkey", "night", "orange", "pencil", "queen", "river", "sun", "tree",
    "umbrella", "violet", "water", "xray", "yellow", "zebra", "air", "boat", "cat", "door",
    "egg", "fish", "game", "hat", "ice", "jam", "key", "lamp", "moon", "nest",
    "ocean", "pool", "quiz", "road", "star", "toy", "unit", "van", "wall", "yard",
    "zoo", "about", "after", "again", "always", "animal", "answer", "around", "back", "because",
    "before", "begin", "being", "below", "between", "bird", "black", "blue", "both", "bring",
    "build", "bus", "call", "car", "carry", "clean", "climb", "cold", "come", "cut",
    "dance", "day", "deep", "do", "draw", "drink", "dry", "eat", "eight", "end",
    "even", "fall", "far", "fast", "find", "five", "fly", "full", "fun", "get",
    "give", "go", "green", "grow", "hand", "happy", "hard", "help", "high", "hot",
    "jump", "keep", "kind", "laugh", "light", "like", "long", "look", "love", "low",
    "make", "many", "move", "much", "name", "new", "now", "off", "old", "open",
    "out", "over", "own", "part", "place", "play", "push", "rain", "read", "red",
    "rest", "ride", "run", "say", "see", "send", "set", "shape", "show", "sing",
    "sit", "six", "sleep", "slow", "small", "smile", "snow", "some", "soon", "start",
    "stop", "swim", "take", "tell", "ten", "think", "three", "today", "top", "train",
    "try", "turn", "two", "under", "use", "walk", "want", "warm", "wash", "watch",
    "way", "well", "white", "who", "why", "wish", "work", "write", "yes", "young"
]

def add_sentence():
    return ' '.join(random.choices(word_list, k=6))
