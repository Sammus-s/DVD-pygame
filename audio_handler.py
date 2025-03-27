class AudioHandler:
    pygame.mixer.init()
    back_ground_music = pygame.mixer.music
    back_ground_music.load("Alarm01.wav")
    back_ground_music.play(-1)

    sound_effect = pygame.mixer.Sound("walkieTalkieStart.mp3")