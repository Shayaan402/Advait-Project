# Sentiment-Analysis Assignment (Sonnet 130)

###  Description
This is a **Python program** written to analyze the **sentiment of Shakespeare’s *Sonnet 130*** (a classic poem about the poet’s realistic view of his lover). The script calculates a simple sentiment **score** based on lists of positive and negative words.

###  Approach
- The full text of *Sonnet 130* is stored as a string.
- Two dictionaries are used:
  - `POSITIVE_WORDS` — words assigned **+1 score**.
  - `NEGATIVE_WORDS` — words assigned **−1 score**.
- The program:
  - Removes punctuation.
  - Converts text to lowercase.
  - Splits text into words.
  - Adds or subtracts scores based on word lists.

###  Difficulties Faced
- Making sure **punctuation** doesn’t interfere with word matching.
- Ensuring all words are compared in **lowercase** so matches are accurate.

###  Resolution of Difficulties
- Used `str.translate()` with a punctuation table to clean text.
- Converted the text to lowercase before splitting into words.

###  Result
- The script calculates and prints the **overall sentiment score** of *Sonnet 130*.  
- A **negative score** suggests more negative words, while a **positive score** suggests more positive words.

###  What Was Learned
- How to **clean text** of punctuation in Python.
- How to **process strings and lists**.
- Using **simple dictionaries** and loops to tally sentiment.

###  Setup
1. Install **Python** on your system if not already installed.
2. Open **VS Code**.
3. Open the folder containing `sonnet_sentiment.py` in VS Code.
4. Make sure the **Python extension** is installed in VS Code.
5. Open `sonnet_sentiment.py` in the editor.
6. Run the script by:
   - Pressing `F5`, **or**
   - Right-clicking in the editor and selecting **Run Python File in Terminal**.
7. You will see the **sentiment score** printed in the terminal inside VS Code.
