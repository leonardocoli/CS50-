# Assuming CS50 library is imported (replace with your import statement)

def count_letters(text):
  """Counts the number of letters in the text."""
  return sum(char.isalpha() for char in text)

def count_words(text):
  """Counts the number of words in the text."""
  return sum(char == " " for char in text) + 1

def count_sentences(text):
  """Counts the number of sentences in the text."""
  sentence_count = 0
  end_chars = ".?!"
  for char in text:
    if char in end_chars:
      sentence_count += 1
  return sentence_count

def coleman_liau_index(text):
  """Calculates the Coleman-Liau index for the text."""
  letters = count_letters(text)
  words = count_words(text)
  sentences = count_sentences(text)
  if words == 0 or sentences == 0:
    return None
  return (0.0588 * (letters / words * 100)) - (0.296 * (sentences / words * 100)) - 15.8

def readability_score(text):
  """Calculates and interprets the readability score."""
  score = coleman_liau_index(text)
  if score is None:
    print("Error: Empty text or invalid characters.")
    return
  score = round(score)  # Round the score before interpretation
  if score < 1:
    print("Before Grade 1")
  elif score >= 16:
    print("Grade 16+")
  else:
    print(f"Grade {score}")

text = str(input("Input some text: "))
readability_score(text)
