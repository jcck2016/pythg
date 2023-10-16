press_release = """

Doody Calls, a nationwide leader in dog poop removal services, is growing its footprint in the pooper scooper industry with the opening of an office in Orlando, Florida. Doody Calls currently cleans up dog poop in over 57 territories across 23 states and has been named the number-one dog poop removal franchise in the United States by Entrepreneur Magazine's annual Franchise 500 list.

"""

# Remove the leading and trailing whitespace (new lines) from press_release
press_release_strip = press_release.strip()


# Replace the phrase "dog poop" with "pet waste" in the press release.  Our research shows "pet waste" tests better than "dog poop"
press_release_replaceWords = press_release_strip.replace(
    'dog poop', 'pet waste')

# We changed our company name! replace the phrase "Doody Calls" with "DoodyCalls" (no space between the words)
press_release_replaceSPACE = press_release_replaceWords.replace(
    'Doody Calls', 'DoodyCalls')

# Our research shows that it's best to shout our press releases. Make the entire press release uppercased!
press_release_replaceCAP = press_release_replaceSPACE.upper()

# Print out the updated press release with all of the above changes:
print("*******STRIP EXTRA SPACES********")
print(press_release_strip)
print("*******REPLACE WORDS*************")
print(press_release_replaceWords)
print("*******REMOVED SPACE*************")
print(press_release_replaceSPACE)
print("*******CAP ALL ******************")
print(press_release_replaceCAP)
