# Define band collaboration graph
bands_collabs = {
    'Pink Floyd': ['Led Zeppelin', 'The Beatles'],
    'Led Zeppelin': ['Pink Floyd', 'The Rolling Stones', 'Queen'],
    'The Rolling Stones': ['Led Zeppelin'],
    'The Beatles': ['Pink Floyd'],
    'Nirvana': ['Pink Floyd'],
    'Queen': ['Led Zeppelin']
}

print(f"Band Collaboration Graph: {bands_collabs}")
