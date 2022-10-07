music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)