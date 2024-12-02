import pygame

pygame.init()

audio1 = pygame.mixer.Sound('assets/audio/jump.mp3')
audio2 = pygame.mixer.Sound('assets/audio/music.wav')

pygame.mixer.set_num_channels(2)

channel1 = pygame.mixer.Channel(0)
channel1.set_volume(0.1)
channel1.play(audio1)
channel1.queue(audio2)


pygame.time.wait(1000)
channel1.set_volume(1)
channel1.play(audio2, loops=-1)

pygame.time.wait(1000)


pygame.quit()
