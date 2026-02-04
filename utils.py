def audio_score(sr, bit_depth, bitrate):
    """Compute Audio Score based on metadata"""
    score = 0

    # Sample rate
    if sr >= 96000:
        score += 35
    elif sr >= 48000:
        score += 25
    elif sr >= 44100:
        score += 20
    else:
        score += 5

    # Bit depth
    if bit_depth >= 24:
        score += 35
    elif bit_depth >= 16:
        score += 25
    else:
        score += 5

    # Bitrate
    if bitrate > 2500000:
        score += 30
    elif bitrate > 1500000:
        score += 20
    else:
        score += 5

    return min(score, 100)
