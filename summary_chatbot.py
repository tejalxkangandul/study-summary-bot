from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Read text from file
with open("study_input.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

# Ask how many sentences you want in summary
try:
    count = int(input("🔢 How many sentences should the summary have? (e.g., 3): "))
except:
    print("⚠️ Using default = 3 sentences.")
    count = 3

# Summarize
parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
summarizer = LsaSummarizer()
summary = summarizer(parser.document, count)

# Output
print("\n📌 Summary:\n")
for sentence in summary:
    print("•", sentence)
