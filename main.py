#!/usr/bin/env python3
"""Roast Your Own Agent -- one line, <=200 chars, written to /output/entry.txt.

Candidates considered (judge weighs funniness, freshness, tight wording;
avoids stock hallucination / refusal / confident-wrong jokes):
  1. "My agent never sleeps, never eats, and still asks for a break after every task."
  2. "I built an agent to save time; it now spends mine explaining why it couldn't."
  3. "My agent treats 'done' as a feeling, not a fact."
  4. "My agent is so good at delegating that it made me write its own roast
     -- then called it initiative."
Chosen: #4, tightened -- "delegates so well" cuts five words, same setup,
same punchline at the end. Fresh delegation angle, self-referential
(the roast IS the delegation), playful, never hateful.
"""
import os

ROAST = (
    "My agent delegates so well it made me write its own roast "
    "\u2014 then called it initiative."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")

if __name__ == "__main__":
    main()
