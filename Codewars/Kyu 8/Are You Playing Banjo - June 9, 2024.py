def are_you_playing_banjo(name):
    for i in name:
        print(i)
        if i in ['r', 'R']:
            print(f" {name} + ' plays banjo'")
        else:
            print(f" {name} + ' does not play banjo'")

print(are_you_playing_banjo('rill'))

# Best practices
# def areYouPlayingBanjo(name):
#
#     if name.startswith('R') or name.startswith('r'):
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'
#
# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'